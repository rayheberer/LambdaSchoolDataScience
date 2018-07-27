# Help!

Hi Friend,

After learning about breadth-first-search, I decided to give depth-first-search
a try.  I'm pretty sure I've almost got it working, but I can't figure out the
last few bugs.  Can you help?  I've got the following issues.  I'm not sure if
the order here matters, you might have to fix them in a different order than
they are listed. I think these are all problems with `graph.py`.

1. Nothing seems to connect, my edges aren't showing up.
2. All the vertexes are the same color.  They're supposed to be different colors
if they're not connected, and right now none of them are.
3. Sometimes I do something and when I run `python graph_demo.py` it just takes
forever, even though my `draw.py` and `graph_demo.py` are totally just the same
as from class.
4. I wanted to let it find a target vertex, but even back when it did kinda run
this part didn't really work.
5. My editor sure is complaining a lot about something called "lint."
6. I keep losing track of my variables, I guess I should name them better?

I also tried to do it with recursion instead of a stack, in `graph_rec`, but I
got even more stuck. It was running forever so I tried adding a thing to keep
track of vertices, and now I just get an error message. Please try to fix this
too if you can, or at least give me some pointers on what I should be doing.

I'm still trying to learn this stuff, so please don't just fix the code for me.
Let me know in the `Answers.md` file where my bugs are and what you did to fix
them, so I can have an easier time watching out for them next time. Oh and don't
forget to `pipenv install` and `pipenv shell`!

If you get all this figured out, it'd be great if you could also help try to
improve the `randomize()` in `BokehGraph` so I can draw vertices that don't
overlap (*i.e. stretch goal*).

Thanks!
