from dotenv import load_dotenv
load_dotenv() ## load all the environemnt variables

import streamlit as st
import os
import sqlite3

import google.generativeai as genai
## Configure Genai Key

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function To Load Google Gemini Model and provide queries as response

def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text

## Fucntion To retrieve query from the database

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

## Define Your Prompt
prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name OIL and has the following columns - NAME, TYPE, 
    PRICE and STOCK \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM OIL ;
    \nExample 2 - Tell me all the names fo sunflower type?, 
    the SQL command will be something like this SELECT * FROM OIL 
    where TYPE="Sunflower"; 
    \nExample 3 - Tell me how much stock is there in palm oil, 
    the SQL command will be something like this SELECT STOCK FROM OIL WHERE TYPE = 'Palm';


    also the sql code should not have ``` in beginning or end and sql word in output

    """


]

## Streamlit App

st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Oil Information")

question=st.text_input("What do you want to ask: ",key="input")

submit=st.button("Ask the question")

# if submit is clicked
if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    response=read_sql_query(response,"oil.db")
    st.subheader("Your Response is ")
    for row in response:
        print(row)
        st.header(row)
