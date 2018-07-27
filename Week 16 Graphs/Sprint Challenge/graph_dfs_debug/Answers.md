Describe the fixes/improvements you made to the Graph implementation here.

1. The edges aren't showing up because `add_edge` method is connecting `start` to `start` and `end` to `end`, instead of `start` to `end` and `end` to `start`.

Fix: 

```
def add_edge(self, start, end, bidirectional=True):
        self.vertices[start].add(end)		# <--
        if bidirectional:
            self.vertices[end].add(start)	# <--
```

2. In the `find_components` method, a vertex should be explored if it is not already in the `visited` set. Currently the logic is backwards.
 

Fix: 
```
def find_components(self):
    visited = set()
    current_component = 0

    for vertex in self.vertices:
        if vertex not in visited:								# <--
            reachable = self.dfs(vertex)
            for other_vertex in reachable:
                other_vertex.component = current_component
            current_component += 1
            visited.update(reachable)
    self.components = current_component
```

Also, depth-first search is not updating the set tracking visiting vertices inside the loop.

3. This has to do with the recursion based depth-first search not being implemented totally correctly. In addition to needing to update the set, the stack needs to be updated with only vertices that have not already been visited, so that the search does not loop infinitely. (I have also renamed the variables to reflect their purposes.)

4. In order to find a target, it is the current vertex that must be compared, not the entire stack.

Fix:
```
def dfs(self, start, target=None):
    frontier = []
    frontier.append(start)
    visited = set()

    while frontier:
        current = frontier.pop()
        if current == target:								# <-- 4
            break
        visited.add(current)								# <-- 2
        frontier.extend(self.vertices[current] - visited)	# <-- 3

    return visited
```

5. Lint is a tool to help keep consistent style in the code. You can simply make the changes it requests (adding more blank lines, removing unused imports, etc.).

6. I renamed quite a few variables. In general, try to name variables so that you can tell what their purpose is just by reading them, without needing to look at their surrounding context too much.

__Recursion__: 

First of all, I have renamed all the variables. Next, to check for a target, I implemented a base-case where `start == target`. In order for the recursion to do something, each recursive call has to add to some collection. Right now all the returns from the recursive calls are going nowhere. I've solved this by having an empty default value for the `visited` set, and updating it within the recursion.

Fix:
"""
def graph_rec(self, start, target=None, visited=set()):		# <--
    visited.add(start)
    for vertex in self.vertices[start]:
        if vertex not in visited:							# <--
            visited.update(self.graph_rec(vertex, visited))	# <--
    return visited
"""