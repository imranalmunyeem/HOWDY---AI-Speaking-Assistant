import imdb

def get_user_input():
    age = int(input("Enter your age: "))
    genre_movie = input("Enter your favorite movie genre: ")
    genre_series = input("Enter your favorite series genre: ")
    return age, genre_movie, genre_series

def get_recommendations(age, genre_movie, genre_series):
    ia = imdb.IMDb()

    # Search for top-rated movies and series
    top_movies = ia.get_top250_movies()[:5]
    top_series = ia.get_top250_tv()[:5]

    # Search for best-rated movies and series based on user genre preferences
    best_movies = ia.search_movie(genre_movie)[:5]
    best_series = ia.search_movie(genre_series)[:5]

    # Search for good-rated movies and series based on user genre preferences
    good_movies = ia.search_movie(genre_movie)[:5]
    good_series = ia.search_movie(genre_series)[:5]

    return {
        "Top Movies": top_movies,
        "Top Series": top_series,
        "Best Movies": best_movies,
        "Best Series": best_series,
        "Good Movies": good_movies,
        "Good Series": good_series,
    }

def display_recommendations(recommendations):
    print("\nRecommendations:")
    for category, items in recommendations.items():
        print(f"\n{category}:")
        for item in items:
            title = item.get('title', 'N/A')
            year = item.get('year', 'N/A')
            rating = item.data.get('rating', 'N/A')
            print(f"- {title} ({year}) - IMDb Rating: {rating}")

def main():
    print("Welcome to the Movie and Series Recommendation Program!")
    age, genre_movie, genre_series = get_user_input()
    recommendations = get_recommendations(age, genre_movie, genre_series)
    display_recommendations(recommendations)

if __name__ == "__main__":
    main()
