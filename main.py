import urllib,ast

movieTitle = raw_input("Enter the MovieName : ")

f =urllib.urlopen("http://www.omdbapi.com/?&apikey=42040d6&t="+str(movieTitle)+"")
data = f.readline()
result =ast.literal_eval(data)

if result.has_key('Error'):
    print result['Error']
    
else:
    print "Movie Title :",result['Title']
    for value in result['Ratings']:
        if value.has_key('Source'):
            if value['Source'] == 'Rotten Tomatoes':
               
                print "Rotten Tomatoes : ",value['Value']
                break
                
        else:
            print "There is no reviewer for this movie .."
    else:
        print "There is no review from Rotten Tomatoes for this movie... "
        
    #print "Actors : ",result['Actors']
   # print "Year : ",result['Year']
