import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import pyttsx3

def recipe_recommendation_system():
    # Sample data (you can replace this with your own dataset)
    recipes_data = {
        'RecipeID': [1, 2, 3, 4],
        'RecipeName': ['Spaghetti Bolognese', 'Chicken Curry', 'Vegetarian Pizza', 'Chocolate Cake'],
        'Ingredients': ['pasta, meat, tomatoes', 'chicken, curry sauce, rice', 'dough, tomato sauce, cheese', 'flour, sugar, chocolate']
    }

    # Create a DataFrame from the sample data
    recipes_df = pd.DataFrame(recipes_data)

    # Combine the text data from relevant columns
    recipes_df['RecipeContent'] = recipes_df['RecipeName'] + ' ' + recipes_df['Ingredients']

    # Map user choices to ingredients
    preference_mapping = {
        '1': ['fast', 'pizza', 'burger'],
        '2': ['curry', 'spices', 'rice'],
        '3': ['healthy', 'vegetables', 'salad'],
        '4': ['vegetarian', 'vegetables'],
        '5': ['non-vegetarian', 'meat', 'fish']
    }

    # Function to get recipe recommendations based on user preferences
    def get_recommendations(user_preferences):
        # TF-IDF Vectorization
        vectorizer = TfidfVectorizer(stop_words='english')
        tfidf_matrix = vectorizer.fit_transform(recipes_df['RecipeContent'])

        # Create a vector for the user's preferences
        user_vector = [user_preferences.get(word, 0) for word in vectorizer.get_feature_names_out()]

        # Compute the cosine similarity between user preferences and recipes
        cosine_sim = linear_kernel([user_vector], tfidf_matrix).flatten()

        # Get the indices of recipes sorted by similarity
        recipe_indices = cosine_sim.argsort()[::-1]

        # Filter out recipes the user has already tried
        recommended_recipes = [recipe for recipe in recipe_indices if recipes_df.iloc[recipe]['RecipeID'] not in user_preferences]

        return recommended_recipes

    # Function to speak the text
    def speak(text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

    # Get user preferences
    speak("Choose your preferences:")
    for i in range(1, 6):
        preference_text = f"{i}. {preference_mapping[str(i)]}"
        speak(preference_text)
        print(preference_text)

    speak("Enter the numbers of your preferences")
    user_choices = input("Enter the numbers of your preferences separated by commas (1,2,3,4,5): ")

    # Get user preferences based on their choices
    user_preferences = {word: 1 for choice in user_choices.split(',') for word in preference_mapping.get(choice, [])}

    # Get recipe recommendations for the user
    recommendations = get_recommendations(user_preferences)

    # Speak the recommendations
    speak("\nRecommended Recipes:")
    print("\nRecommended Recipes:")
    for index in recommendations[:3]:  # Speak top 3 recommendations
        recipe_text = f"{recipes_df.iloc[index]['RecipeName']} with Ingredients: {recipes_df.iloc[index]['Ingredients']}"
        speak(recipe_text)
        print(recipe_text)  # Also print the recommendations to the console

# Call the function to run the recipe recommendation system
# recipe_recommendation_system()
