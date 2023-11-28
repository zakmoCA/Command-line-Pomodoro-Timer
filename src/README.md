# Refactor

Will mainly be refactoring to keep with the principles and design patterns I have observed from the developers at work and our code base.

As one of my first projects, this reads like spaghetti now. It will still read like spagetti after the refactor (to my future self), with the goal being for it simply being to read a little *less* like spaghetti. In that process we will learn a thing or two. 

## Refactor Objectives

- no global variables, it's still bad practice even for my small personal projects. I should write my personal projects the way I would write in a production codebase, especially since I am yet to learn all the best practices and design patterns (you must first [learn the rules before you can disregard them](https://thoughtbot.com/blog/chestertons-fence#:~:text=Chesterton's%20Fence%20is%20a%20principle,why%20it%20was%20put%20up.)). Keep things [simple](https://grugbrain.dev/).
- modularisation and single responsibility
- more robust error handling
- DRY
- more efficient data handling (opportunity to begin data structures and algorithms journey)
