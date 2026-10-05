# Netflix: Build a Netflix Watchlist App with Classes & Objects

class Movie:
    def __init__(self, title):
        self.title = title
        self.watched = False

    def mark_watched(self):
        self.watched = True


class Watchlist:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)


    def show_unwatched(self):
        for movie in self.movies:
            if not movie.watched:
                print(movie.title)

class Movie:
    def __init__(self, title: str):
        self.title = title
        self.watched = False

    def mark_watched(self):
        self.watched = True

    def __str__(self):
        status = "✓" if self.watched else " "
        return f"[{status}] {self.title}"


class Watchlist:
    def __init__(self):
        self.movies: list[Movie] = []

    def add_movie(self, movie: Movie):
        if any(m.title.lower() == movie.title.lower() for m in self.movies):
            print(f"'{movie.title}' is already in your watchlist.")
            return
        self.movies.append(movie)

    def mark_watched(self, title: str):
        for movie in self.movies:
            if movie.title.lower() == title.lower():
                movie.mark_watched()
                return
        print(f"'{title}' not found.")

    def get_unwatched(self) -> list[Movie]:
        return [m for m in self.movies if not m.watched]

    def get_watched(self) -> list[Movie]:
        return [m for m in self.movies if m.watched]


if __name__ == "__main__":
    watchlist = Watchlist()
    watchlist.add_movie(Movie("Data Movie by Baraa"))
    watchlist.add_movie(Movie("Fast and Furious"))
    watchlist.add_movie(Movie("Spider-Man"))  # duplicate, rejected | Add more movies to the watchlist

    watchlist.mark_watched("Fast and Furious")

    print("To watch:")
    for movie in watchlist.get_unwatched():
        print(movie)

    print("\nWatched:")
    for movie in watchlist.get_watched():
        print(movie)
movie = Movie("Data Movie by Baraa")
watchlist = Watchlist()

watchlist.add_movie(movie)
watchlist.get_unwatched()