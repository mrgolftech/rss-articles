# Refinement without Specification

**来源:** https://buttondown.com/hillelwayne
**链接:** https://buttondown.com/hillelwayne/archive/refinement-without-specification/
**日期:** Tue, 20 Jan 2026 17:49:07 +0000

---

Imagine we have a SQL database with a `user` table, and users have a non-nullable `is_activated` boolean column. Having read [That Boolean Should Probably Be Something else](https://ntietz.com/blog/that-boolean-should-probably-be-something-else/), you decide to migrate it to a nullable `activated_at` column. You can change any of the SQL queries that read/update the `user` table but not any of the code that uses the results of these queries. Can we make this change in a way that preserves all external properties? 

Yes. If an update would set `is_activated` to true, instead set it to the current date. Now define the **refinement mapping** that takes a `new_user` and returns an `old_user`. All columns will be unchanged _except_ `is_activated`, which will be
    
    
    f(new_user).is_activated = 
        if new_user.activated_at == NULL 
        then FALSE
        else TRUE
    

Now new code can use `new_user` directly while legacy code can use `f(new_user)` instead, which will behave indistinguishably from the `old_user`. 

A little more time passes and you decide to switch to an [event sourcing](https://martinfowler.com/eaaDev/EventSourcing.html)-like model. So instead of an `activated_at` column, you have a `user_events` table, where every record is `(user_id, timestamp, event)`. So adding an `activate` event will activate the user, adding a `deactivate` event will deactivate the user. Once again, we can update the queries but not any of the code that uses the results of these queries. Can we make a change that preserves all external properties?

Yes. If an update would change `is_activated`, instead have it add an appropriate record to the event table. Now, define the refinement mapping that takes `newer_user` and returns `new_user`. The `activated_at` field will be computed like this:
    
    
    g(newer_user).activated_at =
            # last_activated_event
        let lae = 
                newer_user.events
                          .filter(event = "activate" | "deactivate")
                          .last,
        in
            if lae.event == "activate" 
            then lae.timestamp
            else NULL
    

Now new code can use `newer_user` directly while old code can use `g(newer_user)` and the really old code can use `f(g(newer_user))`.

### Mutability constraints

I said "these preserve all external properties" and that was a lie. It depends on the properties we explicitly have, and I didn't list any. The real interesting properties for me are mutability constraints on how the system can evolve. So let's go back in time and add a constraint to `user`:
    
    
    C1(u) = u.is_activated => u.is_activated'
    

This constraint means that if a user is activated, any change will preserve its activated-ness. This means a user can go from deactivated to activated but not the other way. It's not a particular good constraint but it's good enough for teaching purposes. Such a SQL constraint can be enforced with [triggers](https://www.postgresql.org/docs/current/sql-createeventtrigger.html). 

Now we can throw a constraint on `new_user`:
    
    
    C2(nu) = nu.activated_at != NULL => nu.activated_at' != NULL
    

If `nu` satisfies `C2`, then `f(nu)` satisfies `C1`. So the refinement still holds.

With `newer_u`, we _cannot_ guarantee that `g(newer_u)` satisfies `C2` because we can go from "activated" to "deactivated" just by appending a new event. So it's not a refinement. This is fixable by removing deactivation events, that would work too.

So a more interesting case is `bad_user`, a refinement of `user` that has both `activated_at` and `activated_until`. We propose the refinement mapping `b`:
    
    
    b(bad_user).activated =
        if bad_user.activated_at == NULL && activated_until == NULL
        then FALSE
        else bad_user.activated_at <= now() < bad_user.activated_until
    

But now if enough time passes, `b(bad_user).activated' = false`, so this is not a refinement either.

### The punchline

Refinement is one of the most powerful techniques in formal specification, but also one of the hardest for people to understand. I'm starting to think that the reason it's so hard is because they learn refinement while they're _also_ learning formal methods, so are faced with an unfamiliar topic in an unfamiliar context. If that's the case, then maybe it's easier introducing refinement in a more common context like databases.

I've written a bit about refinement in the normal context [here](https://hillelwayne.com/post/refinement/) (showing one specification is an implementation of another). I kinda want to work this explanation into the book but it might be too late for big content additions like this.

(Food for thought: how do refinement mappings relate to database views?)
