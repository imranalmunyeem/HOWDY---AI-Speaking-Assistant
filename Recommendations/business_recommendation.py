import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import pyttsx3

def business_recommendation():
    # Sample data (user_id, business_id, category)
    data = [
        ('user1', 'business1', 'food'),
        ('user1', 'business2', 'clothing'),
        ('user2', 'business1', 'food'),
        ('user2', 'business3', 'electronics'),
        ('user3', 'business2', 'clothing'),
        ('user3', 'business3', 'electronics'),
        # Add more data as needed
    ]

    # Convert data to a pandas DataFrame
    df = pd.DataFrame(data, columns=['user_id', 'business_id', 'category'])

    # Function to preprocess user input and recommend businesses
    def recommend_business(profession, age, gender, interest, financial_condition):
        # Suggest businesses based on user profile and interest
        suggestions = []

        tech_keywords = ['software', 'tech', 'science', 'technology', 'web', 'web development']
        fashion_keywords = ['fashion', 'clothing', 'outfit', 'clothes']

        if age >= 20 and age <= 40 and any(keyword in interest.lower() for keyword in tech_keywords):
            suggestions.append(('Software Company', 'Software Services'))
            suggestions.append(('IT Field', 'Information Technology'))
            suggestions.append(('Software Services', 'Software Development'))
        elif any(keyword in interest.lower() for keyword in fashion_keywords):
            suggestions.append(('Fashion Store', 'Fashion'))
            suggestions.append(('Clothing Shop', 'Clothing'))
            suggestions.append(('Design Services', 'Fashion Design'))
            suggestions.append(('Handmade Shop', 'Handmade Goods'))
        else:
            suggestions.append(('Not Available', 'I am not yet programmed for that data. Please check again in future.'))

        return suggestions

    # Function to speak the text
    def speak(text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

    # Get user input with speaking prompts
    speak("Please enter your current profession:")
    profession_input = input("Enter your current profession: ")

    speak("Please enter your age:")
    age_input = int(input("Enter your age: "))

    speak("Please enter your gender:")
    gender_input = input("Enter your gender: ")

    speak("Please enter your interest:")
    interest_input = input("Enter your interest: ")

    speak("Please enter your financial condition:")
    financial_condition_input = input("Enter your financial condition: ")

    # Example: Recommend businesses for the user based on input
    recommended_businesses = recommend_business(profession_input, age_input, gender_input, interest_input, financial_condition_input)

    # Display the recommendations
    speak("Top business recommendation:")
    for business, category in recommended_businesses:
        print(f"{business} ({category})")
        speak(f"{business}. {category}")

# Call the function to run the recommendation
# business_recommendation()
