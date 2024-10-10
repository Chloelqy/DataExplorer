# Session 2: Functions

def greet(name):
    print("Hello, " + name + "!")
    
greet('Alice')

#Exercise 1:
# Calculate the average rating of the movies.
def calculate_average_rating(ratings):
    total = sum(ratings)
    return total / len(ratings)

ratings = [4.7, 4.7, 4.4, 4.3]

average = calculate_average_rating(ratings)
print('Average Rating:', average)

#Exercise 2:
#Write a function find_highest_rated(movies, ratings) that uses a loop to find the highest-rated movie.
def find_highest_rated(movies, ratings):
    highest_rating = max(ratings)
    index = ratings.index(highest_rating)
    return movies[index]

movies = ['Spiderman', 'Iron Man', 'Godzilla x Kong', 'Minions']

top_movie = find_highest_rated(movies, ratings)
print('Top Rated Movie:', top_movie)

genres = ['Comedy', 'Action', 'Action', 'Comedy']


#Session 3: Read & Write to CSV File
#Task:
#Example: Reading from a file:
#with open('movies.txt', 'r') as file:
    #data = file.readlines()

#Example: Writing to a file:
	#with open('output.txt', 'w') as file:
   	 #file.write('Analysis Results')


#Exercise: Practice with File Handling Task 1:

#Write a function load_movies(filename) to read movie data from a file.
def load_movies(filename):
    with open(filename, 'r') as file:
        movies = file.readlines()
    return [movie.strip() for movie in movies]
