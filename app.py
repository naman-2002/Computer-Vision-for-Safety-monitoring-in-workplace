# import pickle

# # Specify the file path if it's in the same directory
# model_path = 'model.pkl'

# # Load the model
# with open(model_path, 'rb') as file:
#     model = pickle.load(file)

# sample_input = [[5.1, 3.5, 1.4, 0.2]]  # Example input
# prediction = model.predict(sample_input)
# print(f"Prediction: {prediction}")

import streamlit as st
import pickle

# Load the model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# App title
st.title("Machine Learning Model Deployment")

# Input features
st.header("Enter Input Features")

feature1 = st.number_input("Title")
feature2 = st.number_input("Type")
feature3 = st.number_input("Genre")
feature4 = st.number_input("Release Year")
feature5 = st.number_input("Rating")
feature6 = st.number_input("Duration")
feature7 = st.number_input("Country")

# Add as many inputs as needed for your model
# ['Title', 'Type', 'Genre', 'Release Year', 'Rating', 'Duration', 'Country']

#Make the Dataframe out of the given data
input_data = pd.DataFrame([[feature1, feature2, feature3, feature4, feature5, feature6, feature7]], columns=['Title', 'Type', 'Genre', 'Release Year', 'Rating', 'Duration', 'Country'])

# Predict

if st.button("Predict"):
    prediction = model.predict(input_data)  # Adjust input shape as needed
    st.success(f"Prediction: {prediction[0]}")
