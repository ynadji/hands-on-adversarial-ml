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
company's [website](https://docs.docker.com/install/). If you're on OS X,
you'll want to install [Docker Desktop for
Mac](https://docs.docker.com/desktop/install/mac-install/) first. If you're on
Linux, `$ sudo apt-get|yum|whatever install docker|docker-ce` is probably
enough to get you going. I have not tested this with Windows, but I suspect
installing [Docker Desktop on
Windows](https://docs.docker.com/desktop/install/windows-install/) will work.

1. `$ git clone https://github.com/ynadji/hands-on-adversarial-ml.git`
1. `$ cd hands-on-adversarial-ml`
1. `$ docker build -t advml .`
1. `$ docker run -p 8888:8888 advml`
1. Open your browser to the [Jupyter Notebook](http://localhost:8888) you just
built.
1. Let's SMASH some models!
