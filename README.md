To test the project 
1) clone the repository "omdb" and use the both pythonscript(mail.py) and Dockerfile to build the image 
2)build the image by using docker build -t tagname . (The you will get the image)
3)To create and run the container command docker run -it --name containername/id  imageid/name
# It will automatically execute the python file and it will ask you the movie name 
#when we given the movie name it will display the movie name and "rotten Tomatoes rating"
#Else the is no Rotten Tomatoes rating in the movie it will shows no Rotten Tomatoes ratings 
