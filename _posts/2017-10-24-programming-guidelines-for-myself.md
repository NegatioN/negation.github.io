---
layout: post
title: Programming Guidelines
excerpt: We can’t really improve upon things we haven't defined what are, so I’ve decided to note down some of my current convictions/guidelines when it comes to programming.
---
(for myself)

We can’t really improve upon things we haven't defined what are, 
so I’ve decided to note down some of my current convictions/guidelines when it comes to programming. 
This can hopefully be an evolving guide I look back on, and modify throughout the years.

1. Write as many pure functions as you can.
    * It simplifies testing, as you can send in all the variables to easily test for edge cases.
    * A good way to write pure functions easily, is to pass functions as parameters to them. 
This can let us more easily mock out the state-dependent part of it
2. Test core functionality, but don’t go overboard and test useless stuff.
3. Don’t optimize prematurely.
    * Optimization often means we have to make functions impure, or makes code 
harder to read or change in the future. Make sure this is a trade-off you need to do before you spend time on it.
4. Write procedural code. Keep the flow of the program easily observable.
    * This means, shy away from using injection frameworks that magically joins together 
your code to form a program, unless it simplifies something else to a ridiculous degree.
5. Strive for simplicity in your code.
    * Only be satisfied with the code being complex if it has to. Otherwise, refactor and simplify.
    * This makes it easier to work with the code next time you need to make a 
change. And easier for others who share that code-base with you.
    * What is simple code?
        * Self-contained code.
        * Short/Readable code.
        * Code implemented in the most “normal” way. No esoteric stuff.
6. Try to keep the state of the program somewhat contained. Don’t follow the 
OO model of spreading it all around and encapsulating it, because this means 
we need to have a complete hierarchy to know with certainty how our program will act.
7. Write a readme in a parent directory that documents rudimentary usage of the project.
8. Writing code that’s idiomatic to the language it’s written in. 
9. Be conscious of the APIs you expose to consumers.... As you're stuck with them.
 (Or they will be painfully hard to change)

2023 Addendum:
1. There should ideally only be one way of doing a given thing in the code-base.
    * This means it's easier to maintain, and easier to change later.
2. There shouldn't be more complexity in the solution, than there is in the problem you're solving.
3. Make use of higher-order functions as ways to make your program testable and modular.
    * I.e. instead of having a deeply nested if-statement in a function, rather pass that function another function it can execute so that the complexity of it is isolated closer to where you called the procedure.
