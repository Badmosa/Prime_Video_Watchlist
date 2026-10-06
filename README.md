# 🎬 Prime Video Watchlist App

This is a small Python app that keeps track of movies you want to watch and movies you've already seen. Built to practice **classes and objects** (OOP) in Python.

## What it does

- Add movies to your watchlist
- Block duplicates (not case-sensitive, so "Ike" and "ike" count as the same movie)
- Mark a movie as watched by its title
- See what you haven't watched yet
- See what you've already watched

## How it works

The app has two classes.

**`Movie`** represents one movie.

| Part | What it does |
|---|---|
| `title` | The name of the movie |
| `watched` | `False` by default, becomes `True` once you've seen it |
| `mark_watched()` | Sets `watched` to `True` |
| `__str__()` | Prints the movie like `[✓] Ike` or `[ ] Spider-Man` |

**`Watchlist`** holds all your movies.

| Method | What it does |
|---|---|
| `add_movie(movie)` | Adds a movie (skips it if it's already there) |
| `mark_watched(title)` | Finds a movie by title and marks it watched |
| `get_unwatched()` | Returns the movies you haven't watched |
| `get_watched()` | Returns the movies you've watched |

## Tool

- Python

## Skills
- Critical Thinking
- Clean Code Practice
- Object-Oriented Programming
- Well-Structured Encapsulation Practices

## How to run

1. Save the code as `watchlist.py`
2. Open your terminal in the same folder
3. Run:

```bash
python watchlist.py
```

## Code

```python
watchlist = Watchlist()

watchlist.add_movie(Movie("Data Movie by Baraa"))
watchlist.add_movie(Movie("Fast and Furious"))
watchlist.add_movie(Movie("Spider-Man"))
watchlist.add_movie(Movie("Ike"))
watchlist.add_movie(Movie("Fundamentals of Data Engineering"))

watchlist.mark_watched("Fast and Furious")
watchlist.mark_watched("Ike")

print("Not Yet Watched:")
for movie in watchlist.get_unwatched():
    print(movie)

print("\nWatched:")
for movie in watchlist.get_watched():
    print(movie)
```

**Output:**

```
Not Yet Watched:
[ ] Data Movie by Baraa
[ ] Spider-Man
[ ] Fundamentals of Data Engineering

Watched:
[✓] Fast and Furious
[✓] Ike
```

## What I learned

- Creating classes and objects
- Using `__init__` to set up an object's starting values
- Using `__str__` to control how an object prints
- Keeping data in one class (`Movie`) and managing it in another (`Watchlist`)
- Returning data from methods instead of printing inside them

## Author

**Badmos Adesola Ayomide**
**Data Engineer**
[LinkedIn](https://linkedin.com/in/badmosayomide) · [Portfolio](https://datascienceportfol.io/badmosayomide02)
