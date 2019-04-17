
Project Title
-------------

OMDBAPI

Getting Started
----------------

clone the repository from github "https://github.com/chinniprashanth/omdb" 

This repo will get you a copy of the project up and running on your local machine for testing purposes.

Prerequisites
-------------

Unix based operating system must be present

Docker must be installed in it.


Usage
------

use Dockerfile to build the image

Built With
-----------

    docker build -t imagename .
                               


This command will build the image and will get the image by using the image we can create a container

To create and run the container 

Running the tests
------------------

     docker run -it --name containername/id  imagename/id 
                                                           

It will automatically execute the python file and it will ask you the movie name 


when we given the movie name it will display the movie name and "Rotten Tomatoes rating"


Else there is no Rotten Tomatoes rating in the movie list it will display no Rotten Tomatoes ratings 



Authors
--------

Chinniprashanth


