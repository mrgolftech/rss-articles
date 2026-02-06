# A Fast, Growable Array With Stable Pointers in C

**来源:** https://danielchasehooper.com
**链接:** https://danielchasehooper.com/posts/segment_array/
**日期:** Tue, 05 Aug 2025 00:00:00 +0000

---

[Daniel Hooper](https://danielchasehooper.com/)

[Home](https://danielchasehooper.com/) ・ [Articles](https://danielchasehooper.com/posts) ・ [Projects](https://danielchasehooper.com/#projects) ・ [About](https://danielchasehooper.com/about) ・ [X.com ](https://x.com/danielchooper)[Bluesky ](https://bsky.app/profile/danielchooper.bsky.social)[Mastodon](https://mastodon.gamedev.place/@danielchooper) [RSS](https://danielchasehooper.com/feed.xml)

# A Fast, Growable Array With Stable Pointers in C

August 5, 2025・7 minute read

My last article about [generic data structures in C](/posts/typechecked-generic-c-data-structures/) was written to set the stage for today's topic: A data structure with constant time indexing, stable pointers, and works well with [arena allocators](https://www.rfleury.com/p/untangling-lifetimes-the-arena-allocator). Its been independently discovered by multiple programmers over the years and so goes by different names. A [2001 paper](https://duckduckgo.com/?q=%22Experiences+with+the+design+and+implementation+of+space-efficient+deques%22) called it a "levelwise-allocated pile" (bleh). Zig calls it a "[Segmented List](https://github.com/ziglang/zig/blob/e17a050bc695f7d117b89adb1d258813593ca111/lib/std/segmented_list.zig)". Then there's C++ with `std::deque`, which is only superficially similar. I like the name that [Per Vognsen](https://mastodon.social/@pervognsen) uses: "[Segment Array](https://gist.github.com/pervognsen/c9d18e8012ce497e7a92d3f86c112337)". Code linked at end.

The idea is straight forward: the structure contains a fixed sized array of pointers to segments. Each segment is twice the size of its predecessor. New segments are allocated as needed. Here's how that looks:

NULLNULLsegments arraysegment 0segment 1segment 2  
  


Unlike standard arrays, pointers to a segment array's items are always valid because items are never moved. Leaving items in place also means it never leaves "holes" of abandoned memory in arena allocators. The layout also allows us to access any index in constant time.

## The Implementation

You could implement a Segment Array just from the description above, but there are a few details worth discussing further. Here's the above diagram as a C struct:
    
    
    typedef struct {
        u32 count;
        int used_segments;
        u8 *segments[26];
    } SegmentArrayInternal;
    

The `segments` array being a fixed size is actually important because it means it's right next to the rest of the struct in memory and likely wont get a cache miss when we index into it. If the segments didn't double in size then we'd need _way_ more of them to store a lot of items, and the segments array would have to be a separate allocation.

So how did I arrive at 26 segments? The size doubling of segments means only 48 of them can hold `2^48 - 1` items, more than 256 _tebibytes_ of memory. Most 64 bit computers can only use 48 bits of a pointer, so its not sensible to use more than 48 segments. I reduce the segment count further to 32 because I like to use `uint32_t` to index the array1. Finally, I get rid of the the 6 smallest segments (with sizes 1, 2, 4, 8, 16, 32) because they aren't worth their overhead. 26 segments can hold 4,294,967,232 items (just under `UINT32_MAX`).

You may have noticed I'm using segment sizes that are a power of two. It's not strictly necessary, but it makes the math nice and allows us to use fast bit shift operations for calculating indices:
    
    
    #define SMALL_SEGMENTS_TO_SKIP 6
    
    #define log2i(X) ((u32) (8*sizeof(unsigned long long) \
        - __builtin_clzll((X)) - 1))
    
    u32 capacity_for_segment_count(int segment_count) {
        return ((1 << SMALL_SEGMENTS_TO_SKIP) << segment_count) 
            - (1 << SMALL_SEGMENTS_TO_SKIP);
    }
    
    void *_sa_get(SegmentArrayInternal *sa, u32 index, size_t item_size) {
        int segment = log2i((index >> SMALL_SEGMENTS_TO_SKIP) + 1);
        u32 slot = index - capacity_for_segment_count(segment);
        return sa->segments[segment] + item_size*slot;
    }
    

`log2i` (base 2 logarithm for integers) is implemented with the compiler intrinsic `__builtin_clzll` (count leading zeros of unsigned long long). It's just an efficient way to calculate which segment a given index falls within.

Clang optimizes `_sa_get` to just 10 x86-64 instructions (with `-O3`):
    
    
    _sa_get:
        mov     eax, esi
        shr     eax, 5
        inc     eax
        bsr     ecx, eax
        mov     eax, -32
        shl     eax, cl
        add     eax, esi
        add     eax, 32
        imul    rax, rdx
        add     rax, qword ptr [rdi + 8*rcx + 8]
        ret
    

When accessing one item, it will take longer to load the item from memory than for these instructions to calculate its address. That's true of standard arrays too. If you're iterating items in order, you don't need `sa_get` at all. You can loop over the segments and their items directly. I have a macro to make that easy in segment_array.h.

Here's the code to allocate a new item. It also creates a new segment if needed:
    
    
    void *_sa_alloc(SegmentArrayInternal *sa, size_t item_size) {
        if (sa->count >= capacity_for_segment_count(sa->used_segments)) {
            size_t slots_in_segment = (1 << SMALL_SEGMENTS_TO_SKIP) << sa->used_segments;
            size_t segment_size = item_size * slots_in_segment;
            sa->segments[sa->used_segments] = malloc(segment_size);
            sa->used_segments++;
        }
    
        sa->count++;
        return _sa_get(sa, sa->count-1, item_size);
    }
    

One final implementation note: You can ensure the segment array's capacity is always a power-of-two by making the first two segments the same size. It makes the code less nice, but it's useful when using it as the backing array for a power-of-two-sized hash table2 and you don't want it to waste ~50% of its memory.

## Generics

I use the techniques from my [last article](/posts/typechecked-generic-c-data-structures/) to allow the Segment Array to store any type while also being type checked. This macro associates type information with the generic struct:
    
    
    #define SegmentArray(type) \
        union { \
            SegmentArrayInternal internal; \
            type *payload; \
        }
    

And these macros use the payload member to pass the item size to the generic functions:
    
    
    #define sa_get(sa, index) \
        ((typeof((sa)->payload))_sa_get(&(sa)->internal, \
                                        index,  \
                                        sizeof(*(sa)->payload)))
        
    #define sa_alloc(sa) \
        (typeof((sa)->payload))_sa_alloc(&(sa)->internal, \
                                         sizeof(*(sa)->payload))
    

Feel free to not do this if you don't want to use `typeof()`, or don't like macros like this. It's not critical to the data structure.

## In Use

All together we get this nice API:
    
    
    #define SEGMENT_ARRAY_IMPL
    #include "segment_array.h"
    #include <stdio.h>
    
    int main(void) {
        typedef struct {int a,b; } Entity;
    
        SegmentArray(Entity) entities = {0};
        sa_add(&entities, (Entity){ 1,0 });
        sa_add(&entities, (Entity){ 2,0 });
    
        // getting one item
        printf("entities[0].a = %i\n", sa_get(&entities, 0)->a);
    
        // iterating all items
        sa_for(&entities) {
             printf("entities[%i].a = %i\n", it_index, it.a);
        }
    
        // only needed when not using an arena
        sa_free(&entities);
    
        return 0;
    }
    

## Comparison

There is no data structure that is the best in all situations. The Segment Array is no exception. There are several other options worth considering when storing a list of items:

  * Fixed Size Array - An array that doesn't grow. Either calculate how many items you'll need ahead of time, or calculate an upper limit.
  * Dynamic Array - standard array that grows by some multiple of its size (usually 1.5), and moves its items.
  * Chunked Linked List - a linked list that stores one or more items per link.
  * Hybrid Approach - when creating an unknown number of items all at once (such as when parsing a file) you create the items in a chunked linked list. Once you have all items, you copy them into a fixed sized array and free the linked list.
  * Virtual Memory Array - Use mmap (macOS, Linux) or VirtualAlloc (Windows) to reserve a huge amount of virtual address space and commit to physical memory as the array grows. This can't be used on platforms without virtual memory like webassembly and embedded systems.



Now let me compare them on these criteria:

  1. Growable - can you add more items over time?
  2. Stable - does it have stable pointers (leave items in place), and not leave holes in arena allocators?
  3. Random access - can you access a random index in constant time, or do you have to iterate in order?
  4. Contiguous - Are all items stored in a single range of memory with no gaps? Useful when interfacing with API that accept a pointer and length, like `write()`.



* * *

| Growable| Stable| Random Access| Contiguous  
---|---|---|---|---  
Fixed Size Array| ❌| ✅| ✅| ✅  
Dynamic Array| ✅| ❌| ✅| ✅  
Chunked Linked List| ✅| ✅| ❌| ❌  
Hybrid Approach| ✅ (at creation)| ✅| ✅ (after creation)| ✅ (after creation)  
Virtual Memory Array| ✅ (up to reservation)| ✅| ✅| ✅  
Segment Array| ✅| ✅| ✅| ❌  
  
* * *

Average memory efficiency:

  * Fixed Size Array: 100%
  * Dynamic Array: 83% with a 1.5x growth factor
  * Chunked Linked List: nearly 100%. Depends on chunk size and item count.
  * Hybrid approach: 100%
  * Virtual Memory Array: 100% (give or take one page's worth of memory)
  * Segment Array: 75%



Personally, I most often reach for the fixed sized array, or the hybrid approach. I've found the segment array useful in situations where I'm generating an unknown number of items over time and can't use a Virtual Memory Array - like in the [build profiler](/posts/syscall-build-snooping/) I'm working on.

## Conclusion

The segment array is probably most helpful if you already use arena allocators heavily. Otherwise another option may work better.

It is large-ish at 216 bytes (vs 24 for a dynamic array: pointer + count + capacity), so they work best for big central arrays that store all of the program's Entities, or Samples, or whatever.

Whether or not you use this interesting data structure, there's a lot to learn in its diminutive 120 lines. My single-header library implementation can be downloaded by joining my newsletter at the bottom of this page. You'll get sent to the download page after confirming your email.

* * *

  1. Useful for [handles](https://floooh.github.io/2018/06/17/handles-vs-pointers.html) ↩︎

  2. Thanks to Andrew Reece for the power-of-two-size technique ↩︎




❖

Get notified about my next article:

Join Newsletter

[More articles by Daniel](https://danielchasehooper.com/)
