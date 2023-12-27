import imdb
import pyttsx3
import speech_recognition as sr

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_user_input(question):
    speak(question)
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        user_input = recognizer.recognize_google(audio)
        print("You said:", user_input)
        return user_input.lower()
    except sr.UnknownValueError:
        speak("Sorry, I could not understand your speech. Please try again.")
        return get_user_input(question)
    except sr.RequestError as e:
        speak(f"Error accessing Google Speech Recognition service: {e}")
        return get_user_input(question)

def movie_recommendation_program():

    genre_movie = get_user_input("Please state your favorite movie genre:")

    ia = imdb.IMDb()

    # Search for best-rated movies based on user genre preferences
    best_movies = ia.search_movie(genre_movie)[:5]

    speak("Here are the 5 best movies in your favorite genre:")
    for movie in best_movies:
        title = movie.get('title')
        year = movie.get('year')
        rating = movie.data.get('rating')
        speak(f"{title}, released in {year}")

    response_export = get_user_input("Do you want to export the list of best movies to a notepad file?")
    if response_export.startswith(('yes', 'yea', 'yeah', 'yup')):
        with open('best_movies_list.txt', 'w') as file:
            file.write("Best Movies:\n")
            for movie in best_movies:
                title = movie.get('title')
                year = movie.get('year')
                rating = movie.data.get('rating')
                file.write(f"{title}, released in {year}\n")
        speak("The list of best movies has been exported to 'best_movies_list.txt'.")
    else:
        speak("Thank you for using the Movie Recommendation Program!")
        return

if __name__ == "__main__":
    movie_recommendation_program()
