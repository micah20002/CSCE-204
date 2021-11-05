def getMovies():
    movies = []
    try:
            with open("excercises/nov-02/movies.txt") as file:
                for line in file:
                    movie = line.replace("\n", "")
                    movies.append("movie")
    except FileNotFoundError:
        print("file could not be located.")

print("*** Awesome movie program ***")
movies = getMovies()

for movie in movies:
    print(movie)