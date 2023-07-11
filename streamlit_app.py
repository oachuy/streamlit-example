import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.pyplot as plt

# Load the data from a file
@st.cache  # Cache the data to avoid reloading on every run
def load_data(filename):
    df = pd.read_csv(filename)
    return df

# Calculate TF-IDF scores
def calculate_tfidf(data):
    vectorizer = TfidfVectorizer()
    tfidf_scores = vectorizer.fit_transform(data)
    return tfidf_scores

# Plot the graph
def plot_graph(x, y):
    fig, ax = plt.subplots()
    ax.barh(x, y)
    ax.set_xlabel('TF-IDF Score')
    ax.set_ylabel('Term')
    ax.set_title('TF-IDF Scores')
    st.pyplot(fig)

# Main function
def main():
    st.title("TF-IDF Visualization")

    # Load data
    filename = 'output_tf_idf_file.txt'
    df = load_data(filename)

    # Display the raw data
    st.subheader("Raw Data")
    st.dataframe(df)

    # Preprocess the data
    preprocessed_data = df['text_column'].tolist()

    # Calculate TF-IDF scores
    tfidf_scores = calculate_tfidf(preprocessed_data)

    # Extract terms and scores
    feature_names = vectorizer.get_feature_names()
    scores = tfidf_scores.toarray()[0]

    # Create a dataframe for visualization
    plot_graph(df_scores['Term'], df_scores['TF-IDF Score'])

if __name__ == '__main__':
    main()
