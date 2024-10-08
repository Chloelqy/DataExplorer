#Session 2: Loops
#Task: 
# Write a loop to print each movie title from the list:
#Use a for loop:
#for movie in movies: 
#print(movie)
movies = ['Spiderman', 'Iron Man', 'Godzilla x Kong', 'Minions']
for movie in movies:
    print(movie)
#2.Write a loop to calculate the sum of all movie ratings in the list:
#Use a loop to add all ratings together:
ratings = [4.7, 4.7, 4.4, 4.3]
total_rating = 0    
for rating in ratings:
    total_rating += rating 
print('Total Rating:', total_rating)

#Task1: Create a loop that prints both the movie title and its rating.
#Example:
for i in range(len(movies)):
    print(movies[i], 'has a rating of', ratings[i])



#Task 2: Write a loop to find the highest-rated movie in the list.
#Hint: You can use a loop to compare each rating.
highest_rating = max(ratings)
index = ratings.index(highest_rating)
print('The highest-rated movie is:', movies[index])

#Task 3:
#Create a loop that filters the movies by genre and stores them in a new list.
#Example: Filter for 'Sci-Fi' movies.
genres = ['Comedy', 'Action', 'Action', 'Comedy']

filtered_movies = []
for i in range(len(movies)):
    if genres[i] == 'Action':
        filtered_movies.append(movies[i])
print('Sci-Fi Movies:', filtered_movies)


