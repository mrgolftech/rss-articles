# Minimal GitHub Workflow

**来源:** https://susam.net
**链接:** https://susam.net/minimal-github-workflow.html
**日期:** Thu, 15 Jan 2026 00:00:00 +0000

---

# Minimal GitHub Workflow

By **Susam Pal** on 15 Jan 2026

This is a note where I capture the various errors we receive when we create GitHub workflows that are smaller than the smallest possible workflow. I do not know why anyone would ever need this information and I doubt it will serve any purpose for me either but sometimes you just want to know things, no matter how useless they might be. This is one of the useless things I wanted to know today. 

## Contents

  * Empty Workflow
  * On
  * On Push
  * Jobs
  * Job ID
  * Steps
  * Runs On
  * Runs On Ubuntu Latest
  * Empty Steps
  * Run
  * Run Echo
  * Hello, World



## Empty Workflow

For the first experiment we just create a zero byte file and push it to GitHub as follows, say, like this: 
    
    
    mkdir -p .github/workflows/
    touch .github/workflows/hello.yml
    git add .github/
    git commit -m 'Empty workflow'
    git push -u origin main

Under the GitHub repo's **Actions** tab, we find this error: 
    
    
    Error
    No event triggers defined in `on`

## On

Then we update the workflow as follows: 
    
    
    on:

Now we get this error: 
    
    
    Invalid workflow file: .github/workflows/hello.yml#L1
    (Line: 1, Col: 4): Unexpected value '', (Line: 1, Col: 1): Required property is missing: jobs

## On Push

Next update: 
    
    
    on: push

Corresponding error: 
    
    
    Invalid workflow file: .github/workflows/hello.yml#L1
    (Line: 1, Col: 1): Required property is missing: jobs

## Jobs

Workflow: 
    
    
    on: push
    jobs:

Error: 
    
    
    Invalid workflow file: .github/workflows/hello.yml#L1
    (Line: 2, Col: 6): Unexpected value ''

## Job ID

Workflow: 
    
    
    on: push
    jobs:
      world:

Error: 
    
    
    Invalid workflow file: .github/workflows/hello.yml#L1
    (Line: 3, Col: 9): Unexpected value ''

## Steps

Workflow: 
    
    
    on: push
    jobs:
      world:
        steps:

Error: 
    
    
    Invalid workflow file: .github/workflows/hello.yml#L1
    (Line: 4, Col: 11): Unexpected value '', (Line: 4, Col: 5): Required property is missing: runs-on

## Runs On

Workflow: 
    
    
    on: push
    jobs:
      world:
        runs-on:
        steps:

Error: 
    
    
    Invalid workflow file: .github/workflows/hello.yml#L1
    (Line: 4, Col: 13): Unexpected value '', (Line: 5, Col: 11): Unexpected value ''

## Runs On Ubuntu Latest

Workflow: 
    
    
    on: push
    jobs:
      world:
        runs-on: ubuntu-latest
        steps:

Error: 
    
    
    Invalid workflow file: .github/workflows/hello.yml#L1
    (Line: 5, Col: 11): Unexpected value ''

## Empty Steps

Workflow: 
    
    
    on: push
    jobs:
      world:
        runs-on: ubuntu-latest
        steps: []

Error: 
    
    
    Invalid workflow file: .github/workflows/hello.yml#L1
    No steps defined in `steps` and no workflow called in `uses` for the following jobs: world

## Run

Workflow: 
    
    
    on: push
    jobs:
      world:
        runs-on: ubuntu-latest
        steps:
          - run:

Success: 
    
    
    ▼ Run
    
      shell: /usr/bin/bash -e {0}

## Run Echo

Workflow: 
    
    
    on: push
    jobs:
      world:
        runs-on: ubuntu-latest
        steps:
          - run: echo

Success: 
    
    
    ▼ Run
      echo
      shell: /usr/bin/bash -e {0}
    

## Hello, World

Workflow: 
    
    
    on: push
    jobs:
      world:
        runs-on: ubuntu-latest
        steps:
          - run: echo hello, world

Success: 
    
    
    ▼ Run echo hello, world
      echo hello, world
      shell: /usr/bin/bash -e {0}
    hello, world

The experiments are preserved in the commit history of [github.com/spxy/minighwf](https://github.com/spxy/minighwf). 

[Comments](./comments/minimal-github-workflow.html) | [#technology](./tag/technology.html)

* * *

[Home](./) [Maze](./maze.html) [Links](./links.html) [Feed](./feed.xml) [Subscribe](./form/subscribe/) [About](./about.html) [GitHub](https://github.com/susam) [Mastodon](https://mastodon.social/@susam)

(C) 2001-2026 Susam Pal
