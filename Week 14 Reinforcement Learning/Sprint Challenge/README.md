# Reinforcement Learning Sprint Challenge - play Taxi

For the sprint challenge, we will apply the techniques we have learned to play
[Taxi](https://gym.openai.com/envs/Taxi-v2/), an environment in the OpenAI Gym.
In this task the agent controls a taxi that can navigate between four locations.
The goal is to pick up a passenger from one location and drop them off to
another. You get 20 points for each successful drop off, but lose 1 point for
each step you take, and additionally there is a 10 point penalty for illegal
pick-up/drop-off actions.

You can create the environment and watch a random agent play with this code:

```python
import gym

env = gym.make('Taxi-v2')
state = env.reset()
env.render()

total_reward = 0
done = False
while not done:
    state, reward, done, info = env.step(env.action_space.sample())
    total_reward += reward
    env.render()

print('Total reward:', total_reward)
```

You'll see that a random agent doesn't do very well - in a trial run the score
reached -713 before the environment terminated.


## Instructions

Make a Python notebook where you work on the below goals. You can use whatever
environment you wish to develop, but for turning in you should add the file to
the `ML-Reinforcement-Learning` repository in the `sprintchallenge/` directory.
Add, commit, push, and it will appear in your already open pull request.

The goals involve trying to beat a score in Taxi - be sure to measure the score
of your approach after it is trained, and not during the training. This snippet
measures performance (run a simulation repeatedly and average total rewards):

```python
episodes = 1000
rewards = []
max_steps = 99

for episode in range(episodes):
    state = env.reset()  # Assuming you already have env created as above
    total_rewards = 0
    
    for step in range(max_steps):
        action = env.action_space.sample()  # TODO your policy here!
        state, reward, done, info = env.step(env.action_space.sample())
        total_rewards += reward
        if done:
            break
    rewards.append(total_rewards)        

print('Average score over time:', sum(rewards) / episodes)
```


## Goal 1 - Beat Random

As an initial goal, come up with an agent/policy that does better than random.
And more specifically, try to at least have a positive score (>0) average.

This game is discrete, and so you can use the Q-learning approach and build a
matrix of states by actions populated with expected rewards. This approach
should work well and it is suggested you start with it.


## Goal 2 - Beat Basic Q-learning

Once you've got an initial Q-learning approach working, you should try to
improve it via hyperparameter optimization. A score (average performance across
many games) generated without optimizing hyperparameters that you should try to
beat: `8.467`

You should be able to do better without having to use different techniques (i.e.
just with hyperparameter optimization).


## Goal 3 - Beat Optimized Q-learning (stretch)

Now the sky's the limit - or rather, the best possible performance in Taxi. With
the default environment, optimized Q-learning has achieved an average score of
`9.423`. See if you can get in that range, or possibly even beat it, by
employing alternative techniques.

What is an alternative technique? It's anything that maps from environment state
to action - Q-learning achieves this by populating a Q-table, but any model that
can take the environment state and possible action as input and give predicted
reward as output can serve the same purpose. And the Gym environment object
gives us a simulator perfect for generating arbitrary amounts of training data
to train such a model.

The true optimal performance in Taxi is probably not much more than the
optimized Q-learning score - the score certainly has to be less than 20 as the
taxi must always take at least some steps to achieve the task.

If you get this far, feel free to share the best score you get, and see how your
classmates are doing. Good luck!
