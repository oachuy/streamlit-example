import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def plot_graph(data):
    fig, ax = plt.subplots()
    ax.barh(data['Term'], data['TF-IDF Score'])
    ax.set_xlabel('TF-IDF Score')
    ax.set_ylabel('Term')
    ax.set_title('TF-IDF Scores')
    st.pyplot(fig)

def main():
    st.title("TF-IDF Visualization")

    # Load data
    filename = 'your_data_file.csv'
    df = pd.read_csv(filename)

    # Display the raw data
    st.subheader("Raw Data")
    st.dataframe(df)

    # Plot the graph
    plot_graph(df)

if __name__ == '__main__':
    main()
