# Task Management in Roam Research

**来源:** https://danielwirtz.com
**链接:** https://danielwirtz.com/blog/roam-research-task-management
**日期:** Tue, 26 Jan 2021 22:00:00 GMT

---

DW

BlogAboutLists

Books

Bookmarks

Tools

# Better Task Management in Roam Research

Daniel Wirtz

5 years ago • 

Copy link

Status

Slug

Desciption

Featured

Cover Video

Cover Image

Social Image

Publish date

Last edited time

Created time

URL

1000 tasks. That’s the number of finished tasks that I [recently celebrated](https://twitter.com/wirtzdan/status/1352994551934431233?s=20) in Roam Research. In this article, I would like to give you a step-by-step walkthrough of my “Magic List” system.

It has been my daily companion for almost a year and helped me to weather times of intense project management.

In a nutshell, the system helps you to prioritise daily tasks, that you can focus on throughout the day.

The system rests on three pillars:

1\. Understanding the Magic List 2\. Setting up the right queries in Roam Research 3\. Following a 3-step process

And don’t worry: This is not rocket science. It’s actually quite simple and you can implement it quickly in your own graph.

### 

What the heck is a Magic List?

The name makes it sound bigger, then it actually is. The Magic List is simply a set of to-dos that can check off two requirements:

1\. If achieved, they make the day successful 2\. Are achievable with the time and energy I have available

![notion image](https://www.notion.so/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2Fc60cb9d6-ff5a-4eb2-823a-c07963f46657%2F9dd30825-4585-4b56-8fa3-9b4e94d3a4ff%2FM5yVz7gis2XAJ3Jyv33e9xe-avvuvOn-SpUQ9PSTIOQ.jpeg%3FspaceId%3Dc60cb9d6-ff5a-4eb2-823a-c07963f46657?table=block&id=b35405a6-1c20-47fa-85b6-38e5ee7d499b&cache=v2)

I work this list out in the morning, by going through the process I describe later. As a result, all exhausting thinking and prioritising of tasks fall into a single point of the day. This is usually also the time, where I check all open mails, messages and sweep through my projects.

Throughout the day, there isn’t much extra work needed. It’s crystal clear to me what I still need to get done. That protects me from decision-fatigue because I don’t need to recalibrate every two hours. And more time for executing.

It also provides me with a clear definition of success that focuses on output, rather than time. If I’m able to check off all my tasks early, then it’s still a productive day.

### 

Setting up the queries

Okay, let’s get the heavy stuff out of the way first. On my **TODO** page, I have a setup of four queries. I use those queries to filter and visualise all my tasks. The tasks themselves live in different daily notes or pages throughout my graph.

Here are the queries for you to copy:

Magic List Template

Copy
    
    
    **Recently assigned**
    
    - {{[[query]]: {and: [[TODO]] {not: {or: [[Today]] [[Upcoming]] [[Later]] [[Template]] [[query]]]}}}}}
    
    - **Today**
    
    - {{[[query]]: {and: [[TODO]] [[Today]] {not: {or: [[Template]] [[query]]]}}}}}
    
    - **Upcoming**
    
    - {{[[query]]: {and: [[TODO]] [[Upcoming]] {not: {or: [[Template]] [[query]]]}}}}}
    
    - **Later**
    
    - {{[[query]]: {and: [[TODO]] [[Later]] {not: {or: [[Template]] [[query]]]}}}}}

Let’s walk through it quickly. The different priority levels are very much inspired by the [daily task view in Asana](https://stackedit.io/%5Bhttps://asana.com/guide/help/fundamentals/my-tasks%5D\(https://asana.com/guide/help/fundamentals/my-tasks\)).

Recently assigned consists of all blank tasks, that I haven’t processed yet. If you think about [GTD](https://stackedit.io/%5Bhttps://gettingthingsdone.com%5D\(https://gettingthingsdone.com/\)), then you can see this as the task inbox. Everything that I tagged with `#Today` is my Magic List. I leave this section always open throughout the day to see what I still need to work on. Tasks that I tagged with `#Upcoming` are my next priority. And at last, tasks tagged with `#Later` are not important right now but are still good to keep on the radar.

### 

The process: Collect, Prioritise, Execute

#### 

**Collect**

Every day at work starts with the same ritual. In the morning I breeze through all my open inboxes (e.g Gmail) and mentally walk through my projects. Then I also take a quick glance at my calendar to look out for upcoming meetings, that I need to prepare.

While I’m doing that I write down all tasks that I encounter. This can be quick emails to write or parts of projects that I want to work on. At this stage, I’m just collecting and don’t care about priorities or deadlines. This follows in the next step.

#### 

**Prioritise**

When I covered all my open projects and inboxes I put my attention on the queries. I open them all up to get a visual overview of what tasks are on the table.

From here I put my attention first on the Upcoming and Later tasks. I’m asking myself, what tasks I should move to `#Today` and thereby put on my Magic List. I’m not scientific about this process. I very much really on my gut-feeling to tell me what is important.

Afterwards, I go through all the blank tasks that I find in Recently Assigned. From here I can put them into three buckets: Today, Upcoming or Later.

From my experience, it’s good to start in this order. It’s always exciting to work on new tasks, but the stuff in Upcoming or Later is often more important. If you first tackle those tasks, then you give them the opportunity to take the pole position in your task list.

#### 

**Execute**

The last and most difficult step in the process: Execution. Many self-help books dived deep into this topic, so I will spare you with my advice. But I can tell you about my experience.

My own Magic List is generally a mix of between 5-10 small and big tasks. I try to focus on the big and important tasks first thing in the morning. At that time I’m still high energy and can lift some heavy tasks.

After lunch, I naturally progress towards smaller tasks that I can fit between meetings. Those are often tasks that need less energy. (e.g making a round of phone calls)

While I go through my day, I always have the sidebar in Roam Research open with my Magic List. I see this as my lighthouse to guide me through the jungle of all my projects.

That’s it already! At least for me this is more than enough to get a good grip on my tasks. Let me know if you have problems to set it up, or would love to chat about additional improvements.

Subscribe to my blog

Helpful tools, thoughtful articles and other findings from the web. From my desk to yours.

Subscribe

Subscribe

Blog

Menu

Dark Mode

Contact

[](https://twitter.com/wirtzdan/)[](https://www.linkedin.com/in/wirtzdan/)[](https://github.com/wirtzdan)[](https://www.youtube.com/channel/UCje_bQMr6F45x0Auii7IOvA)

Privacy
