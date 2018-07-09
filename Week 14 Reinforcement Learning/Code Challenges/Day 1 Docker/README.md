# Reinforcement Learning - Coding Challenge 1

In this challenge you'll work on setting up a local environment suitable for
reinforcement learning. We'll use a tool called Docker to facilitate building
and running containers with our code and dependencies. Because this challenge
is "operational" there will be a range of goals - if you're familiar with Docker
you should jump ahead to the stretch goals, but if this is your first time using
it then just getting through the first one or two is reasonable.

## Goal 0 - Understanding "What is Docker?"

This goal does not involve turning anything in, but it is good before you get
started to take a moment and understand what this tool does. Normally when you
install and run software, you are downloading packages and drivers and running
them directly on your local operating system (which in turn mediates the
resources from your physical machine) - this is a sensible approach for most
things, but when you're dealing with complicated projects things can get ugly:

- Inconsistencies deploying across different operating systems - Windows, Mac,
  and Linux can have obscure disagreements about everything from case
  sensitivity to network operations
- Conflicting dependencies across projects - project 1 wants Python 2, project 2
  wants Python 3
- Hidden assumptions - a project works in one environment because it happens to
  have the correct global installation or other dependency, but breaks elsewhere

And even when things do work, they often get "entangled" and it's hard to
reproduce why they're working, and dangerous to remove things or start over.

One possible but absurd solution - just buy a different computer for everything.
If you have a complete dedicated piece of hardware set up for each significant
project/task, then it can be consistent and functional and avoid conflicts.

A slight improvement - instead of actual computers, use virtual machines. These
function the same as separate computers, but with the different hardware
emulated (so you could buy less hardware overall).

A better way - containers. This is what Docker does, and they are similar to
virtual machines in that they function as independent computers and keep things
separate, but they are lighter weight because they share the system kernel. This
means you can run more of them with less hardware, and they're much cheaper to
start and stop (or even destroy and recreate).

Docker is a major player in the container space, and provides a fast workflow
for quickly building, running, and deploying images (operating systems *and*
running software). A `Dockerfile` gives you a standard reproducible formula for
the software you're running, and it works the same across platforms. There is a
learning curve - brushing up on your command line skills is advisable - but the
benefits are significant, and it is a widely used tool in industry. For example,
Colab and similar services are able to provide varied environments to many users
by creating and destroying containers on demand.

## Goal 1 - Hello Docker!

Your first task is to install Docker and verify your success by running a basic
container. Docker containers are portable, but Docker itself is still
platform-specific software, so installation will vary. In general, you want the
free community edition, and you don't need to make a Docker ID unless you intend
to publish your own Docker containers.

- Download links: https://www.docker.com/community-edition#/download
- Mac instructions: https://docs.docker.com/docker-for-mac/install/
- Windows instructions: https://docs.docker.com/docker-for-windows/install/

If you use a command line package management tool there is probably a `docker`
package available, e.g. `brew cask install docker` on MacOS and similar 
(distribution-dependent) on Linux.

Once you've installed Docker, you can test by running:
`docker run hello-world`

You should see and message that says your installation is working, and gives
instructions and links to take things further. For more details see:
https://docs.docker.com/samples/library/hello-world/

You should explore the suggested resources, but for now once you've got
`hello-world` working you should move to the text task.

## Goal 2 - Docker Compose and OpenAI Gym

You've got Docker, now it's time to run something useful - the OpenAI Gym, a
toolkit for reinforcement learning. You can see a bit about what it does here:
https://gym.openai.com/docs/

Those documents instruct on how to install locally via `pip`, but a full working
setup can be quite complicated (Gym also needs a library to do the actual
numerical computation, e.g. TensorFlow, and often other dependencies). To get
started more efficiently we'll use a Docker container prepared for this purpose:
https://github.com/ageron/handson-ml/tree/master/docker

To use this container do the following steps (in a terminal):

1. Get to an appropriate working directory (look up `mkdir` and `cd` if you're
  unfamiliar, or see: https://hellowebbooks.com/learn-command-line/)
2. `git clone https://github.com/ageron/handson-ml` - get the repo locally
3. `cd handson-ml/docker/` - get to the Docker subdirectory
4. Follow the instructions in the `docker/README.md`
5. Once `make run` succeeds, you should have a URL to access Jupyter in Docker

Note that you may have to replace the host in the URL with `0.0.0.0`, depending
on your Docker networking settings. For other troubleshooting, refer to the
documentation and chat for help.

Once you've got it working, verify by opening `16_reinforcement_learning.ipynb`
in Jupyter and rerunning cell by cell, reading as you go. This notebook will
give a working example of reinforcement learning using OpenAI Gym.

## Goal 3 - To Jupyter and Beyond!

*Optional/stretch!*

Now that you've gotten this far, you can take Docker further by using it to run
any of several flavors of Jupyter, each tuned to give you a quick start in a
different subtopic of data science: https://github.com/jupyter/docker-stacks

Pick whichever notebook(s) interest you and try to run them. To turn in, commit
an example notebook file that runs in the image you used.

At this point, you are using Docker as a consumer, and it's fair to stop here
and just take advantage of the many great existing Docker images. But if you
want to go further, you can learn how to use Docker to deploy tools for multiple
users, and to make your own custom Docker images.

- https://github.com/jupyterhub/jupyterhub - a multi-user notebook server
- https://docs.docker.com/get-started/part2/ - learn how to make your own
  `Dockerfile`, which lets you build an image with dependencies you choose
  
If you go deep in Docker, you may be interested in orchestration tools such as
[Kubernetes](https://kubernetes.io/), which enables managing and running large
numbers of containers. This is how things like compute clusters for big data are
actually set up and run, and while that's not a skill everyone needs to develop,
it's certainly a cool topic for people who want to learn it.
