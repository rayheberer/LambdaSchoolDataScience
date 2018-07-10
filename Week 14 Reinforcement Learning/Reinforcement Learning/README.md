# Reinforcement Learning - Assignment

*Work in progress - please check back for updates.*

## Part 1 - Improve Cart-Pole

If you've not already, complete through goal 2 of [Coding Challenge 1](../cc1/).
The first part of the assignment is to improve the policy for the agent that is
trying to keep the pole upright on the cart in the notebook
[16_reinforcement_learning.ipynb](https://github.com/ageron/handson-ml/blob/master/16_reinforcement_learning.ipynb).
Read the notebook through `A simple hard-coded policy`, and then add your own
code (in your local Docker-powered environment) to try to do better.

As noted, the main problem with the simple approach is that it ends up moving
the cart too abruptly and losing stability. You can refer to the later sections
of the notebook for some hints on ways to improve with various techniques, but
your goal here is to write your own code leveraging knowledge from the various
resources you have available.

Please turn in an updated notebook with your strategy, as well as text in the
notebook describing it and its performance.


## Part 2 - Play Pong

Implement an agent to play Pong - the OpenAI Gym
[integrates an Atari environment](https://github.com/openai/gym#atari), and you
can start by trying
[example agents](https://github.com/openai/gym/tree/master/examples/agents). The
random agent is a simple initial example, and the keyboard agent can allow you
to actually play the game yourself (and potentially use that data to train
some other agent). The example notebook from the first coding challenge has
useful snippets of code for visualizing what is going on.

After getting set up and playing with a few agents, check out
[this article](http://karpathy.github.io/2016/05/31/rl/) on using policy
gradients to train a model to play Pong. Code your own agent based on this
technique - [this video](https://youtu.be/YOW8m2YGtRg) illustrates the end
result of such an agent.


## Part 3 - An environment of your choice

OpenAI supports
[many interesting environments](https://github.com/openai/gym#environments) -
pick one, and start by trying to run existing agents and find prior work (as
with Pong). Then take a shot at writing your own - this is open-ended, so have
fun and explore something that interests you, but also chat and share what
you're doing so people can collaborate and learn from one another.
