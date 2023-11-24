import mysql.connector


def create_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Ma@131216ash@4832",
        database="DBMS_miniproject",
        auth_plugin="mysql_native_password",
    )
    return connection


def feedback_recieved(Counsellor_ID):
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)

    query = """SELECT Comments,Ratings FROM Feedback WHERE Counsellor_ID=%s"""
    cursor.execute(query, (Counsellor_ID,))
    payments = cursor.fetchall()

    cursor.close()
    connection.close()

    return payments
