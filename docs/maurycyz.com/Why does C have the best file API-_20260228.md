# Why does C have the best file API?

**来源:** [maurycyz.com](https://maurycyz.com)
**发布时间:** Sat, 28 Feb 2026 00:00:00 +0000
**链接:** https://maurycyz.com/misc/c_files/

---

<!-- mksite: start of content -->
<p>

There are a lot of nice programming languages, but files always seem like an afterthought. 
You usually only get read(), write() and some kind of serialization library.
</p><p>
In C, you can access files exactly the same as data in memory:
<!-- snip -->
</p>
<p>
</p>

<pre>
#include &lt;sys/mman.h&gt;
#include &lt;stdio.h&gt;
#include &lt;stdint.h&gt;
#include &lt;fcntl.h&gt;
#include &lt;unistd.h&gt;

void main() {
	// Create/open a file containing 1000 unsigned integers
	// Initialized to all zeros.
	int len = 1000 * sizeof(uint32_t);
	int file = open("numbers.u32", O_RDWR | O_CREAT, 0600);
	ftruncate(file, len);

	// Map it into memory.
	uint32_t* numbers = mmap(NULL, len, 
		PROT_READ | PROT_WRITE, MAP_SHARED,
		file, 0);

	// Do something:
	printf("%d\n", numbers[42]);
	numbers[42] = numbers[42] + 1;

	// Clean up
	munmap(numbers, len);
	close(file);
}
</pre>
<p>
Memory mapping isn't the same as loading a file into memory:
It still works if the file doesn't fit in RAM.
Data is loaded as needed, so it won't take all day to open a terabyte file.
</p><p>
It works with all datatypes and is automatically cached.
This cache is cleared automatically if the system needs memory for something else.
</p><p>
<em>However, in other most languages</em>,
you have to read() in tiny chunks, parse, process, serialize and finally write() it back to the disk.
This works, but is slow and needlessly limited to sequential access:
Computers haven't used tape for decades.
</p><p>
<em>If you're lucky enough to have memory mapping</em>, it will be limited to byte arrays,
which still require explicit parsing/serialization.
It ends up as just a nicer way to call read() and write()
</p><p>
Considering that most languages already support custom allocators, adding a better way to access files seems very doable...
but, as far as I'm aware, C is the only language that lets you specify a binary format and just use it.
</p><p>
C's implemenation isn't even very good:
Memory mapping comes some overhead (page faults, TLB flushes) and C does nothing to handle endianness &mdash;
but it doesn't take much to beat nothing. 
</p><p>
<em>Sure, you might want to do some parsing and validation</em>, but this shouldn't be required every time data leaves the disk. 
When working with larger data, it's very common to run out of memory, making it impossible to just parse everything into RAM.
Being able to just offload data without complicating the code is very useful.
</p><p>
Just look at Python's pickle:
it's a completely insecure serialization format.
Loading a file can cause code execution even if you just wanted some numbers...
but still very widely used because it fits with the mix-code-and-data model of python.
</p><p>
A lot of files are not untrusted. 
</p><p>
<em>File manipulation</em> is similarly neglected. 
The filesystem is the original NoSQL database, but you seldom get more then a wrapper around C's readdir().
</p><p>
This usually results in people running another database, such as SQLite, on top of the filesystem,
but relational databases never quite fit your program. 
</p><p>
... and SQL integrates even worse than files:
On top of having to serialize all your data, you have to write code in a whole separate language just to access it!
</p><p>
Most programmers just use it as a key-value store, and implement their own metadata handling:
creating a bizarre triple nested database.
</p><p>
<em>So to answer the title,</em>
I think it's a result of a bad assumption:
That data being read from a file is coming from somewhere else and needs to be parsed...
and that data being written to disk is being sent somewhere and needs to be serialized into a standard format. 
</p><p>
This simply isn't true on memory constrained systems &mdash;
and with 100 GB files &mdash; 
every system is memory constrained.
</p>
<!-- mksite: end of content -->

---

*抓取时间: 2026-03-01 12:06:12*
