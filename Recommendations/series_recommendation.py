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

def series_recommendation_program():

    genre_series = get_user_input("Please state your favorite series genre:")

    ia = imdb.IMDb()

    # Search for top-rated series based on user genre preferences
    top_series = ia.search_movie(genre_series)[:5]

    speak("Here are the 5 top-rated series in your favorite genre:")
    for series in top_series:
        title = series.get('title')
        year = series.get('year')
        rating = series.data.get('rating')
        speak(f"{title}, released in {year}")

    response_export = get_user_input("Do you want to export the list of top-rated series to a notepad file?")
    if response_export.startswith(('yes', 'yea', 'yeah', 'yup')):
        with open('top_series_list.txt', 'w') as file:
            file.write("Top-rated Series:\n")
            for series in top_series:
                title = series.get('title')
                year = series.get('year')
                rating = series.data.get('rating')
                file.write(f"{title}, released in {year}\n")
        speak("The list of top-rated series has been exported to 'top_series_list.txt'.")
    else:
        speak("Thank you for using the Series Recommendation Program!")

if __name__ == "__main__":
    series_recommendation_program()
