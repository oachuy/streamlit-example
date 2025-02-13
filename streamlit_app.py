import streamlit as st
# Importing libraries
import nltk
import re
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pandas as pd
import matplotlib.pyplot as plt

# Preprocessing
def remove_string_special_characters(s):
    print('Hola')
    # removes special characters with ' '
    stripped = re.sub('[^a-zA-z\s]', '', s)
    stripped = re.sub('_', '', stripped)

    # Change any white space to one space
    stripped = re.sub('\s+', ' ', stripped)

    # Remove start and end white spaces
    stripped = stripped.strip()
    if stripped != '':
        return stripped.lower()
        
def plot_graph(x, y):
    fig, ax = plt.subplots()
    ax.barh(x, y)
    ax.set_xlabel('TF-IDF Score')
    ax.set_ylabel('Term')
    ax.set_title('TF-IDF Scores')
    st.pyplot(fig)
    
def main():
    st.title("TF-IDF Visualization")
    nltk.download('punkt')
    # Input the file
    txt1 = []
    with open('output_tf_idf_file.txt') as file:
        txt1 = file.readlines()

    nltk.download('stopwords')
    stop_words = set(stopwords.words('english'))
    your_list = []     
    for i, line in enumerate(txt1):
        txt1[i] = ' '.join([x for
            x in nltk.word_tokenize(line) if
            ( x not in stop_words ) and ( x not in your_list )])
    # Getting bigrams
    vectorizer = CountVectorizer(ngram_range =(2, 2))
    X1 = vectorizer.fit_transform(txt1)
    features = (vectorizer.get_feature_names_out())
    # print("\n\nX1 : \n", X1.toarray())
        
    # Applying TFIDF
    # You can still get n-grams here
    vectorizer = TfidfVectorizer(ngram_range = (2, 2))
    X2 = vectorizer.fit_transform(txt1)
    scores = (X2.toarray())
    # print("\n\nScores : \n", scores)
        
    # Getting top ranking features
    sums = X2.sum(axis = 0)
    data1 = []
    for col, term in enumerate(features):
        data1.append( (term, sums[0, col] ))
         
    ranking = pd.DataFrame(data1, columns = ['term', 'rank'])
    words = (ranking.sort_values('rank', ascending = False))
    words= words.head(7)
        
    # Display the raw data
    #st.subheader("Raw Data")
    #st.dataframe(words)
        
    # Plot the graph
    plot_graph(words[0],words[1])

if __name__ == '__main__':
    main()

