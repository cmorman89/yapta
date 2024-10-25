# Yet Another Python To-Do App (YAPTA)

## Intro
Welcome to the To-Do List of To-Do Lists, affectionately dubbed **"Yet Another Python To-Do App" (YAPTA).**

***Wait! "Not another Python to-do app!"*** 😱😱😱

Yes, I'm aware—just like you are—that there are more to-do list apps out there than *actual tasks on those lists*. I can already hear the collective dismay of recruiters. Trust me, the irony isn't lost on me. In fact, building a to-do app is practically the `Hello, World!` of full-stack development—it's the avocado toast of coding projects. 🥑

Let me assure you: this isn't just any list. This is my **grand entry into the public coding arena**, a veritable rite of passage that proves I can do more than just churn out `print(😵)` statements for debugging (though let's be honest, old habits die hard). **YAPTA** is a project that will evolve into a full-stack application with a *responsive React front end*, complete with *RESTful API calls* that would make even the most stoic JSON objects smile.

*And because we're living in the **future**, why not sprinkle in some **Natural Language Processing**?* 🤖

Sure, it might start as a flaky noun classifier, but every skyscraper starts with a single brick—or in this case, a ~~*poorly-disguised attempt to make this project flashy*~~ dubiously-organized part of speech. 🦾

On the technical side, I'm embracing the tools that keep real-world projects afloat. The code is sailing smoothly on *GitHub* waters, avoiding the treacherous reefs of lost versions—no more `final_final_v2_actualfinal_use_this_one.py` lurking on my desktop. *Continuous Integration and Deployment* are handled with pytest and tight IDE integration, ensuring that each new feature or line of code doesn't also introduce a new bug 🐞. And yes, I've traded in my freestyle coding ways for the strict rhythms and clean code of *PEP 8* (enforced with `black`).

So, before you dismiss this as just another "Example Task 1" generator 📒, take a closer look. It's my proof that I have at least a tenuous grasp of Python—or, at the very least, that I can make a list of things to do and then cross off "build another to-do app" from it:

> **To Do:**
>
> - [X] ~~Build another to-do app~~
> - [ ] Impress recruiters
> - [ ] ***[Get a job](mailto:recruiters@cmorman.com"recruiters@cmorman.com")***

*It's not just another Python to-do app, it's...*

### ***Yet Another Python To Do App***

##### (But really, recruiters—[call me 📞](mailto:recruiters@cmorman.com"recruiters@cmorman.com"))

---

## Features

- **Task Creation:** Each task is defined by the `Task` class, which holds task-related attributes (ie. `task_id`, `task_name`, `due_date`, etc.)
- **Task Updating:** The `Task` class has methods to set and update its attributes. `task_id` is immutable.
- **CRUD Operations:** The `TaskList` class performs `add_task()`, `get_task()`, `remove_task()`, etc. to tasks in list in a `task_queue`
- **UUID Management:** The `UniqueId` class ensures a standardized UUID is accessible to any object requiring a unique identifer (such as `Task`, `TaskList`).
- **Robust Testing:** Includes unit and integration tests covering core functionality, data integrity, and interactions between `Task` and `TaskList`.

---

## Project Roadmap

- **Frontend Development:**
  - React, TypeScript, JavaScript, tailwindcss, HTML5 for responsive web frontend
  - Dynamic task/element theming
  - Brand standards: logo, colors, typeface, etc
  - 
- **Backend Development:**
  - Recurring tasks
  - Multiple task lists
  - Save and load tasks
  - Investigate database use (SQLite?)

---

## Techncical Stack

- **`Python`:** Core language for backend development.
- **`pytest`:** Testing framework for unit and integration tests.
- **`black`:** Code formatter ensuring PEP 8 compliance.
- **`uuid`:** Library used for generating unique task and list IDs.
  
---

## Setup Instructions

Coming Soon! 