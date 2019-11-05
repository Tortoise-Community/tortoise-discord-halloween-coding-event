<p align="center">
    <img src="https://github.com/albertopoljak/tortoise-discord-halloween-coding-event/blob/master/logo.png?raw=true">
</p>

# Tortoise Discord Haloween Event

Welcome!

This repo serves as a guide/ruleset for the event.

Do not push to this repo but instead read and follow [#Code submissions](#code-submissions)

Link to join Tortoise Discord: [![Tortoise Discord server](https://img.shields.io/discord/577192344529404154?color=%237289DA&label=Tortoise%20Server&logo=discord)](https://discord.gg/f6VcZC2)

Use this Discord for any additional questions. Good luck :)

## Short info

> **Duration:** Event starts at **October 31, 00:00h GMT+0** and will last until the end of the month aka **November 30, 23:59h GMT+0**!

> **Even difficulty:** Above average - hard for newbies (you got whole month tho).

> **Participants**: Anyone can participate as long as you follow #Code submissions, only exclusion is me :)

* Yes that means that even admins and mods from Tortoise Discord can participate - transparency is guaranteed by me 
(Discord user **BrainDead#6105**) since I solely wrote this event.

> **Language**: Only Python is accepted (testing environment has v3.8). It would be cool to see solutions in different
languages but it wouldn't be fair as the end result would mostly depend on the language of choice and not on your algorithm quality.

## Current leaderboard

Just for reference - only times are showed, authors are and will remain anonymous.

1. 0.039579914999999986s
2. 0.059650647999999966s
3. 0.06111201500000009s
4. 0.08065712699999997s
5. 0.14842655299999977s
6. 0.20886057300000016s

## Code submissions

Join Tortoise server if you haven't already (link at top of this file).

Use the command `t.submit` while in DM with the bot `Tortoise#3078` and it will guide trough the process.

You can submit multiple times - only your last submission counts!

If you'd like to make your submission public add a comment at the top of the submitted code.

Submissions marked as public will be, after the event ends, pushed to this repo so that everybody can see all the different
approaches.
Default stance is "not public" so you need to specify you want it public.

The bot sends your code directly to my DMs (Discord user **BrainDead#6105**) - no one else can see it.

## Prizes

First place gets 1 month of `Discord Nitro` + [Amnesia collection Steam key](https://store.steampowered.com/sub/36631/)

Runner up gets 1 month  of `Discord Nitro classic`

If you don't need those (already have etc) you can gift it to someone else.

# Task:

Create a script that will, based on input, return `True` if that input is a vampire number or `False` otherwise.

Quote (taken from Google, you can Google more for more info):
> "In mathematics, a vampire number (or true vampire number) is a composite natural number V,
with an even number of digits N, that can be factored into two integers X and Y each with N/2 digits
and not both with trailing zeroes, where v contains precisely all the digits from X and from Y, in any order,
counting multiplicity. X and Y are called the fangs."

### Condition for a number to be Vampire Number:

- Has a pair number of digits. Lets call the number of digits : N
    
- You can obtain the number by **multiplying two integers**, X and Y, **each with N/2 digits**. X and Y are called **fangs**.
    
- The number can be made **with all digits from X and Y**, in any order and only using each digit once (see [Examples 1250](#examples))

- Both fangs cannot end simultaneously in 0.

### Examples:

- 1260 is a vampire number.

  It's first fang is 60 and second fang is 21.
  
  It's possible fangs are `12, 16, 10, 21, 26, 20, 61, 62, 60`
  
  It is a valid vampire number because `60 * 21 = 1260` and it breaks no conditions.

- 1250 is **NOT** a vampire number!
   
  It's possible fangs are `12, 15, 10, 21, 25, 20, 51, 52, 50`
   
  You could get 1250 by multiplying it's two fangs `50 * 25 = 1250` BUT we can't write 1250 with numbers 0,2,5 (any order)

- 2500 is **NOT** a vampire number!

  It's possible fangs are `25, 20, 20, 52, 50, 50`
 
  You could get 2500 by multiplying it's two fangs `50 * 50 = 2500` BUT ,aside from breaking the previous point, 
  we're also also breaking condition where `Both fangs cannot end simultaneously in 0.`

#### First 25 vampire numbers are:
> 1260, 1395, 1435, 1530, 1827, 2187, 6880, 102510, 104260, 105210, 105264, 105750, 108135, 110758, 115672, 116725,
117067, 118440, 120600, 123354, 124483, 125248, 125433, 125460, 125500, ...

## Requirements:

- **You** are allowed to use only pure Python - no C!
  
  You can use any standard library that you wish including non-standard libraries.

- Code standards (PEP, organization, OOP etc) are **NOT counted** - only execution time is counted.

- Your script **HAS** to have a function/method named `is_vampire_number` that takes one integer as a argument - this is for easier testing.

  - Example for function:
   ```
   def is_vampire_number(number: int) -> bool:
       # code
       # return True or False based on if number is a vampire number or not
   ```

  - This function returns either `True` or `False`! No need to print anything! And no need to know/print fangs!

  - If the number has multiple distinct sets of fangs the outcome is the same (`True`).
    For example 125460 has 2 possible sets of fangs (204, 615) and (246, 510) and will still return `True`.

- Your `is_vampire_number` has to return the correct answer (True/False)
  - It has to either throw **`ValueError`** or return `False` if invalid argument is passed to it.
  - Valid argument is a natural number starting from 1 example 1,2,3....

- You will be disqualified if you don't follow any of the above rules including:
  - **Your execution time takes more than 10s** (see [#Testing environment](#testing-environment) for specs)
  - **You hardcoded the answers** - imagine your function as dumb, it doesn't know when will the first vampire number
  occur nor how many there are and which numbers are they. It **ONLY** knows the rules and algorithm on how to find one.
  So you **CANNOT** do this:
    ```
     def vampire_num(n):
       if n < 1260: return False
       ... # rest of code
    ```
    However, since your function knows the conditions from [#Condition for a number to be Vampire Number](#condition-for-a-number-to-be-vampire-number)
    you could do something similar - look at the first condition.
  - **You copy-pasted code from net that does the entire job for you** - you can copy-paste code snippets, that's normal for a dev :)
   but you cannot copy-paste the entire solution that finds vampire numbers out of the box. What I mean by snippets is for 
   example copy-pasting the source code for `from itertools import permutations` and editing it or finding a similar
   permutation algorithm with better performance for you needs and copy-pasting that.


## Testing environment

Testing will be done on a PC with the following specs:
 - CPU: Intel i5-6600 3.3GHz
 - RAM: 8GB
 - PyCharm Community 2019.1.4
 - Python 3.8
 - Background process minimized with small utility program (JetBoost)

## Testing process:

You have a file called [tests.run](https://github.com/albertopoljak/tortoise-discord-halloween-coding-event/blob/master/testing/tests_run.py) in this repository with which you can test your script.

#### Elimination tests - fail these and you are disqualified:

**elimination_test_1**

Your script **HAS** to have a function named exactly `is_vampire_number`

**elimination_test_2**

Numbers from -3 to 0 including are passed to your `is_vampire_number` function.

Each of them has to raise **`ValueError`** **OR** your `is_vampire_number` needs to return `False`.

Any other error other than **`ValueError`** is not allowed.

**elimination_test_3**

Your `is_vampire_number` function has to return True for all of these valid vampire numbers:

`146137, 150300, 536539, 10025010, 13078260, 46847920, 1000174288`

And it has to return `False` for all those numbers decremented by 1:

`146136, 150299, 536538...`

**elimination_test_4**

Your `is_vampire_number` function is ran in a loop from `1, 7000` and it has to finish in less or equal than 10 seconds.

### Timed test - this test is counted for the win, lower time = better:

Your `is_vampire_number` function is called in a for loop in range (1, 7000).

It has to return the correct True/False answer for each number.

If it takes more than 10s you are disqualified (this is for single iteration).

Your code will be ran in 100 iterations and the final score is your average time during those 100 iterations.
