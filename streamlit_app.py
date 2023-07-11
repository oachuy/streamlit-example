import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def plot_graph(data):
    # Select the top 10 rows based on TF-IDF score
    data_top10 = data.nlargest(10, 'Score')

    fig, ax = plt.subplots()
    ax.barh(data_top10['Term'], data_top10['Score'])
    ax.set_xlabel('Score')
    ax.set_ylabel('Term')
    ax.set_title('Top 10 Scores')
    st.pyplot(fig)

def main():
    st.title("TF-IDF Visualization")

    # Load data
    filename = 'output_tf_idf_file.txt'
    df = pd.read_csv(filename,sep=":")

    # Display the raw data
    st.subheader("Raw Data")
    st.dataframe(df)

    # Plot the graph
    plot_graph(df)

if __name__ == '__main__':
    main()
