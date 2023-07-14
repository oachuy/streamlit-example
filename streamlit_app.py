import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
#
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

def main():
    st.title("TF-IDF Visualization")

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
     # print ("\n\nWords : \n", words.head(7))
        
     # Display the raw data
     #st.subheader("Raw Data")
     #st.dataframe(df)
        
     # Plot the graph
     #plot_graph(df)

if __name__ == '__main__':
    main()
