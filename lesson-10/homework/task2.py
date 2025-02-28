import requests
import os
import random

api_key = os.getenv("TMDB_API_KEY")

# Function to fetch available genres
def get_genres():
    url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}&language=en-US"
    response = requests.get(url)
    if response.status_code == 200:
        genres = response.json()["genres"]
        return {genre["name"].lower(): genre["id"] for genre in genres}
    else:
        print("Error fetching genres:", response.status_code)
        return {}

# Function to fetch movies by genre ID
def get_movies_by_genre(genre_id):
    url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&with_genres={genre_id}"
    response = requests.get(url)
    if response.status_code == 200:
        movies = response.json()["results"]
        return movies
    else:
        print("Error fetching movies:", response.status_code)
        return []

# Main function
def recommend_movie():
    genres = get_genres()
    
    if not genres:
        print("Could not fetch genres. Exiting...")
        return

    print("Available genres:")
    for genre in genres.keys():
        print(f"- {genre.capitalize()}")

    user_genre = input("\nEnter a genre: ").strip().lower()

    if user_genre in genres:
        genre_id = genres[user_genre]
        movies = get_movies_by_genre(genre_id)

        if movies:
            movie = random.choice(movies)  # Pick a random movie
            print(f"\n🎬 Recommended Movie: {movie['title']}")
            print(f"⭐ Rating: {movie['vote_average']}/10")
            print(f"📅 Release Date: {movie['release_date']}")
            print(f"📖 Overview: {movie['overview']}")
        else:
            print("No movies found in this genre.")
    else:
        print("Invalid genre. Please try again.")

if __name__ == "__main__":
    recommend_movie()