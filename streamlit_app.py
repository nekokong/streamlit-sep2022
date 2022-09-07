import streamlit as st
import pandas as pd

st.title('🎈 App Name')

st.header('Sandbox')
genre = st.radio(
     "Select your Class value",
     ('Mumu', 'Neko', 'Ping'))

if genre == 'Ping':
    st.write('You are NarMaw.')
else:
    st.write("You select again na.")

# df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/iris.csv')
# st.write(df)

st.sidebar.subheader('Input')
url_input = st.sidebar.text_input('URL', '')

# st.subheader('Output')
# st.info(f'The GitHub URL of your data is: {url_input}')
# st.warning

if url_input:
    st.subheader('Output')
    st.info(f'The GitHub URL of your data is: {url_input}')
    df = pd.read_csv(url_input)
    st.write(df)

    column_names = df.columns[-1]

    st.write(column_names)
    df2 = df.groupby(column_names).mean()
    st.write(df2)
    st.bar_chart(df2)

else:
    st.subheader('Enter your input')
    st.error('Awaiting your input')
