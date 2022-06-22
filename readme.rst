Intro
-----

For an overview on the importance of managing your computational environment and
the benefits of containers, see Chapter 4 (and especially 4.2) of the Neuroimaging
and Data Science book. (http://neuroimaging-data-science.org/content/002-datasci-toolbox/003-docker.html)

Overview
--------

When we make a container, we are going to roughly follow these steps:

1. Write a piece of code and/or pipeline that you want to containerize
2. Create a wrapper script to make that code play nice with the command line
3. Create a Dockerfile that will describe how to run your code along with any dependencies
4. Use the Dockerfile to build your container
5. Export the container as a tar file, and convert it to a Singularity container so
   people can run the container without administrative privelages

