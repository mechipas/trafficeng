
# Traffic Engineering
This repository contains all of our notebooks for exercise sessions in traffic modelling taken in the Traffic Engineering course. It introduces the 4-stage model and guides the students through each of the steps interactively. It also provides some first insights into the differences between deterministic and stochastic route choice and congested versus uncongested traffic models (DUN, DUE, SUN, SUE).
## Structure
In what follows this 4-stage model is put into practice for a simple case that serves as a good first introduction about the design of a transport model. The material of these exercise sessions is structured as follows:

1. the initialization of the transport network, i.e. the transport infrastructure
2. the traffic demand model for this simple network, i.e. productions and attractions
3. the distribution of trips over origins and destinations, i.e. OD-matrix
4. the assignment of the OD-pairs to the network, i.e. routing and flow volumes
5. (a more complex example for a real study area, i.e. leuven study area)

## Software
The different steps specified above are each put into a Jupyter Notebook and are used to run blocks of python code that makes it possible to interactively show the different steps of the transport model. Of course this is not a programming course and it is thus not expected to be proficient in python, although some knowledge about pythonic coding is helpful to better understand all of the presented material and will also help you in the future, since python is also used in other courses of this masters:
- ITS
- Supply Chain Engineering
- Integrated Practicum 2

Documentation about python is plentiful, it is definitely worthwhile to check:

- [python guide](https://wiki.python.org/moin/BeginnersGuide/Programmers)

Knowing the most important types used to easily store data should already be sufficient to get started, the most important ones are:

- dictionaries
- lists
- tuples
- numpy arrays
- pandas dataframes

# Getting Started
*Some first thoughts here: It seems useful to utilize some plattform that allows running of notebooks in the cloud for students to use our code without having the hassle of setting up an environment. After a bit of digging and comparisons https://mybinder.org/ seems like the best solution here, it's open source and very neatly interfaces with repositories that are kept within gitlab/hub. The functionality is straight forward: provide a github/gitlab repository filled with your notebooks and some dependency specification either in the form of a requirements.txt (pip) or .yml file (conda). Binder will then build an environment for you and provide the corresponding kernel together with computational resources so that you can run the notebooks straight from the browser. The perfect setup for our exercise (or at least so it seems!).*
In order to prevent you from going through a whole installation procedure to get everything working well we use *Binder*, this will setup the needed environment to run all of the code in the notebooks. 

**One very important note is that all the changes you make when working in Binder will be lost if the server stops. It is therefore VERY IMPORTANT that you save the edited files locally, SAVE THE NOTEBOOKS AS HTML FILES!**


You can check out the current state here: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/git/https%3A%2F%2Fgitlab.kuleuven.be%2FITSCreaLab%2Feducation%2Ftraffic-engineering/Joachim)