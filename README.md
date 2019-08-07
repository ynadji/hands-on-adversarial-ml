# Hands on Adversarial Machine Learning

![Powered by Jupyter
 Logo](https://cdn.oreillystatic.com/images/icons/powered_by_jupyter.png)

This project contains the Jupyter Notebooks and the associated Dockerfile for
Yacin Nadji's _Hands On Adversarial Machine Learning_ workshop/course. It
contains both the exercises (/notebooks) and the solutions (/solutions), as well
as any data or files needed (/data).

## Running Jupyter Locally via Docker

The included `Dockerfile` will help you build an image for Jupyter, a fancy
schmancy way of distributing interactive code.

You will need to have Docker installed on your system to create images and run
containers. You can find the installation steps for all platforms on the
company's [website](https://docs.docker.com/install/). If you're on OS X, you'll
likely need to get `docker-machine` up and running so jump to that section
first. If you're on Linux, `$ sudo apt-get|yum|whatever install
docker|docker-ce` is probably enough to get you going.

TODO: Replace with public URL
1. `$ git clone git@github.com:ynadji/hands-on-adversarial-ml.git`
1. `$ cd hands-on-adversarial-ml`
1. `$ docker build -t advml .`
1. `$ docker run -p 8888:8888 advml`
1. Open your browser to the [http://localhost:8888](Jupyter Notebook) you just
built. If you're using `docker-machine`, `$ echo "http://$(docker-machine
ip):8888"` will give you the correct URI.
1. Let's SMASH some models!

### `docker-machine`/Mac OS X Specific Instructions

If you use `docker-machine`, or you don't know what that is and you're on OS X,
follow the instructions below. `docker-machine` runs Linux in VirtualBox so you
too can enjoy the smug misplaced sense of process isolation and smugly neglect
continuous integration and JUST SHIP IT DINGUS.

1. Install [Homebrew](link to homebrew shtuff)
1. `$ brew install docker-machine`
1. `$ brew install docker`
1. `$ docker-machine start default`
1. `$ eval $(docker-machine env)` # This configures your shell with some
environment variables `docker` needs to chooch.
1. `$ echo "http://$(docker-machine ip):8888"` # This will be the URI for
Jupyter once you've built the notebook

After completed the above steps, you should be ready to clone and build the
Docker image. Happy hacking!
