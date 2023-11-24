import streamlit as st
import mysql.connector

def execute_query(query):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Ma@131216ash@4832",
        database="DBMS_miniproject",
        auth_plugin="mysql_native_password",
    )
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    connection.close()
    return result

def custom_query():
    st.title('Custom Query Tab')

    query = st.text_area('Enter your SQL query:', height=100)
    if st.button('Run Query'):
        if query.strip() != '':
            result = execute_query(query)
            st.write('Query Result:')
            if result:
                st.write(result)
            else:
                st.write('No results found for the query.')
