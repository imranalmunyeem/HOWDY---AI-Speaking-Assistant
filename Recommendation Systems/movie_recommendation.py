import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Embedding, Flatten, Dot, Concatenate

# Load MovieLens dataset (download it from https://grouplens.org/datasets/movielens/)
data = pd.read_csv("D:\Python Projects\Python-AI-Projects\HOWDY - AI Speaking Assistant\Recommendation Systems\movies.dat")  # Replace with your actual path
ratings = pd.read_csv("D:\Python Projects\Python-AI-Projects\HOWDY - AI Speaking Assistant\Recommendation Systems\ratings.dat")  # Replace with your actual path

# Merge movie and ratings data
df = pd.merge(ratings, data, on='movieId')

# Create user and movie indices
df['userId'] = df['userId'].astype("category").cat.codes.values
df['movieId'] = df['movieId'].astype("category").cat.codes.values

# Split the dataset
train, test = train_test_split(df, test_size=0.2, random_state=42)

# Build the neural network model
num_users = len(df['userId'].unique())
num_movies = len(df['movieId'].unique())
embedding_size = 50

# User input
user_input = Input(shape=(1,), name='user_input')
user_embedding = Embedding(input_dim=num_users, output_dim=embedding_size)(user_input)
user_embedding = Flatten()(user_embedding)

# Movie input
movie_input = Input(shape=(1,), name='movie_input')
movie_embedding = Embedding(input_dim=num_movies, output_dim=embedding_size)(movie_input)
movie_embedding = Flatten()(movie_embedding)

# Concatenate user and movie embeddings
merged = Concatenate()([user_embedding, movie_embedding])

# Dense layers
dense1 = tf.keras.layers.Dense(128, activation='relu')(merged)
dense2 = tf.keras.layers.Dense(64, activation='relu')(dense1)

# Output layer
output = tf.keras.layers.Dense(1)(dense2)

# Build and compile the model
model = Model(inputs=[user_input, movie_input], outputs=output)
model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
model.fit([train['userId'], train['movieId']], train['rating'], epochs=5, verbose=1)

# Evaluate the model
test_loss = model.evaluate([test['userId'], test['movieId']], test['rating'])
print(f'Test Loss: {test_loss}')

# Make predictions for a specific user
user_id = 0  # Replace with the user ID you want recommendations for
movies_not_rated_by_user = df.loc[df['userId'] == user_id, 'movieId'].unique()

user_movie_input = np.array([user_id] * len(movies_not_rated_by_user))
predictions = model.predict([user_movie_input, movies_not_rated_by_user])

# Get recommended movies
recommendations = pd.DataFrame({'movieId': movies_not_rated_by_user, 'prediction': predictions.flatten()})
recommendations = recommendations.sort_values(by='prediction', ascending=False)

# Display top N recommendations
top_n = 5
top_recommendations = recommendations.head(top_n)
top_recommendations = pd.merge(top_recommendations, data[['movieId', 'title']], on='movieId')

print(f"\nTop {top_n} movie recommendations for User {user_id}:\n")
print(top_recommendations[['title', 'prediction']])
