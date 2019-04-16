This repository contains Dockerfile and pythonscript 

-> Base Ubuntu image
-> Dockerfile
-> main.py(python)

Git Repo

To test the project 
-> clone the repository from github "https://github.com/chinniprashanth/omdb" 

Usage

->use the both pythonscript(mail.py) and Dockerfile to build the image 
->Build the image by using command

 docker build -t tagname .

->To create and run the container command 

 docker run -it --name containername/id  imageid/name

->It will automatically execute the python file and it will ask you the movie name 

->when we given the movie name it will display the movie name and "Rotten Tomatoes rating"

->Else there is no Rotten Tomatoes rating in the movie it will shows no Rotten Tomatoes ratings 
