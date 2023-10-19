# Lyft Backend Engineering Job Simulation

This repo contains all the code and commits that I made completing the simulation that Lyft created with [Forage](https://www.forage.com/).

## Initial task

I was tasked with continuing and finishing the development of a project by Lyft's rental team after a previous engineer had to leave the project.

## My approach to the task

The initial codebase focus on the servicing of the rental cars, and when car with specific batteries and engines needs servicing based on their schedules. The code was a bit mess and involved having a class for every type of car combo depending on the engine and the battery. This was a method to work with but it already showed signs of causing issues for maintainability and changes.

So first I worked through building a more object-oriented UML that would allow there to be reusability in the code and allow and changes to be made in typically only one place. After designing the new classes, I refactored the code that we had. Adding a Car Factory, removing the specific combo classes and making a Car, Engine and Battery class. This allowed to make classes that handled the servicing logic for specific engines and batteries the made focus of the servicing logic, and allowed the flexibility of adding a new engine by adding a new interface, and allowing cars combos to be easily changed as the fleet changes. I was also able to add and change the unit test based on the new refactor code to confirm that the refactor still allowed the logic to work.

After refactoring the final task was to add tires to the possible parts of the car, and do it with Test-Driven Development, based on specific wear data and it's format. I started by creating the tests for the tires based on the specs and previous tests done on the engines and batteries. Then built the Tire class and specific interfaces confirming if they passed the tests or not. Once they passed those tests, I added new tests to the car factory to confirm that the creation of a car with a tire was working and passing the proper information.

## Thoughts after completing virtual experience

Over all this was really good and valuable look into what it is like to work at Lyft as a back-end engineer. It allowed me some experience with things that are new to me like UML design, but also allowed me to continue to use and grow skills I have chose to work on like unit testing, refactoring, object-oriented programming.
