import streamlit as st
import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download()


st.set_page_config(page_title='The Keyword Extraction App',
    layout='wide')


st.write("""
# 
Hi there!
This Web Application helps you to Extract Keywords from Questions into CSV files.
""")

with st.sidebar.header('1. Upload your CSV data'):
    uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])


st.subheader('1. Dataset')
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.markdown('**1.1. Glimpse of dataset**')
    st.write(df)
    
  
else:
    st.info('Awaiting for CSV file to be uploaded.')
    

st.subheader('2. Keywords')

stop_words = stopwords.words('english')

def get_keywords(row):
    Question = row['Question']
    lowered = Question.lower()
    tokens = nltk.tokenize.word_tokenize(lowered)
    keywords = [keyword for keyword in tokens if keyword.isalpha() and not keyword in stop_words]
    keywords_string = ','.join(keywords)
    return keywords_string

df['Keywords'] = df.apply(get_keywords, axis=1)

df


st.download_button(label="Download the Extracted Keywords",data=df.to_csv(),mime='text/csv')
