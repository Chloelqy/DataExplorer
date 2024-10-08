
#Create a list of movie titles, ratings, and genres:
#Example: movies = ['Inception', 'The Dark Knight', 'Interstellar']
#Example: ratings = [9, 8.5, 9.5]
#Example: genres = ['Sci-Fi', 'Action', 'Drama']
movies = ['Spiderman', 'Iron Man', 'Godzilla x Kong', 'Minions']
ratings = [4.7, 4.7, 4.4, 4.3]
genres = ['Comedy', 'Action', 'Action', 'Comedy']

#Access and modify items in the list:
#Print the first movie in the list: print(movies[0])
print(movies[0]) 

#Change the rating of 'Inception' to 9.2: ratings[0] = 9.2 
ratings[0] = 4.6 

#Add new movies to the list:
#Use the append() function to add a new movie to the list:

movies.append('Tenet')
ratings.append(3.75)
genres.append('Thriller')

print(movies)
print(ratings)
print(genres)