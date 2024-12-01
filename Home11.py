#Home page for students grade 11!
import pandas as pd
import random
import streamlit as st
from streamlit_option_menu import option_menu
import mysql.connector
import base64

# Custom CSS for the sidebar with a darker background
sidebar_css = """
<style>
    .stApp {
        background: linear-gradient(to right, #004fee, #00081a); /* Gradient background */
    }
    .css-1d391kg {
        color: #ffffff;  /* Header color */
        background-color: #1a1a1a;  /* Darker background color */
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
        margin-top: 20px;
    }
    .css-1d391kg {
        background-color: #1a1a1a;  /* Darker background color */
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
        margin-top: 20px;
    }
    .css-1d391kg:hover {
        background-color: #333333;
    }
    .css-1d391kg div {
        color: #ffffff !important;
    }
    .css-1v3fvcr {
        color: #f0f0f0 !important;
    }
    .css-1v3fvcr:hover {
        color: #ffffff !important;
    }
    .css-1oe6wy4 {
        margin-top: 50px;
    }
    /* Style for headings */
    .custom-heading {
        color: #ffffff !important;
        text-align: center;
        font-weight: bold;
        font-size: 24px;  /* Size for section headings */
        margin-top: 20px;
        margin-bottom: 20px;
    }
    .huge-heading {
        color: #ffffff !important;
        text-align: center;
        font-weight: bold;
        font-size: 48px;  /* Increased size for the welcome heading */
        margin-top: 50px;
        margin-bottom: 30px; /* Gap between headings */
    }
    .stButton > button {
        background-color: #4caf50;
        color: #ffffff;
        font-weight: bold;
        border-radius: 20px;
        padding: 15px 25px;  /* Larger button size */
        transition: background-color 0.3s ease;
        font-size: 20px;  /* Larger text size */
        display: block;  /* Ensure block display for centering */
        margin: 0 auto;  /* Center button */
    }
    .stButton > button:hover {
        background-color: #388e3c;
    }
    .tabular-layout {
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        gap: 20px;
        margin-top: 30px;
    }
    .tabular-layout div {
        flex: 1 1 45%;  /* 2x2 layout with equal spacing */
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .centered-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 30px;
    }
    .centered-container div {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        margin-top: 20px;
    }
    .upload-container {
        text-align: center;
        margin-top: 50px;
    }
    .upload-container img {
        width: auto;  /* Adjust width as needed */
        height: 300px;  /* Set height to reduce the image size */
        max-width: 100%;  /* Ensure it doesn't exceed container width */
    }
    .upload-container button {
        margin: 20px 10px;  /* Space between buttons */
        padding: 15px 25px;  /* Button size */
    }
    .profile-title {
        text-align: center;
        font-size: 48px;
        font-weight: bold;
        color: #ffffff;
        margin-bottom: 30px;
    }
    .profile-pic {
        display: block;
        margin-left: auto;
        margin-right: auto;
        border-radius: 50%;
        margin-bottom: 30px;
    }
    .profile-info {
        text-align: center;
        font-size: 30px;
        color: #ffffff;
        margin-bottom: 20px;
        margin-top: 10px
    }
</style>
"""







# Apply the custom CSS
st.markdown(sidebar_css, unsafe_allow_html=True)
if 'selected_class' not in st.session_state:
    st.session_state.selected_class = None
if 'show_upload' not in st.session_state:
    st.session_state.show_upload = False
if 'data_saved' not in st.session_state:
    st.session_state.data_saved = False


# Sidebar menu with dark theme and increased spacing
with st.sidebar:
    selected = option_menu(
        menu_title="Main menu",
        options=["Home",  "Classes", "Profile"],
        icons=["house",  "camera-video", "person"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "5!important", "background-color": "#1a1a1a"},
            "icon": {"color": "white", "font-size": "20px"},
            "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#004fee"}
        }
    )
    st.sidebar.markdown(
        '<strong><p style="font-size:14px;">LearnVid is a very useful tool for students as it allows them to clear backlogs and understand a missed concept. Missed a class? we got you covered, Log-in to LearnVid today and boost your learning. Happy Learning!</p></strong>',
        unsafe_allow_html=True)
    st.sidebar.markdown('<strong><p style="font-size:18px;">DID YOU KNOW?</p></strong>', unsafe_allow_html=True)
    st.sidebar.markdown(
        '<strong><p style="font-size:14px;"> LearnVid is a website created by two students from Grade 12 as a Computer Science Project!</p><strong>',
        unsafe_allow_html=True)
    st.sidebar.markdown(
        '<strong><p style="font-size:14px;">Who knew it would be a game changer for thousands of students!</p></strong>',
        unsafe_allow_html=True)
    #st.sidebar.image("A:\Python\pythonProject\LearnVid Logo.png", caption="LearnVid", use_column_width=True)

#-------------Page Selection----------------#
#-------------Home Page--------------#

# Home Page Section
if selected == "Home":
    # Centered titles with improved styling
    st.markdown("""
    <div style="text-align: center; margin-bottom: 50px;">
        <h1 style="color: #ffffff; font-size: 48px; margin-bottom: 20px;">Hello Student!</h1>
        <h2 style="color: #ffffff; font-size: 36px; margin-bottom: 30px;">What Our Clients Say</h2>
    </div>
    """, unsafe_allow_html=True)

    reviews = [
        {
            "name": "John Doe",
            "photo": "https://via.placeholder.com/80",
            "rating": "⭐⭐⭐⭐⭐",
            "comment": "This service is amazing! It has changed my life for the better. Highly recommend it to everyone!"
        },
        {
            "name": "Jane Smith",
            "photo": "https://via.placeholder.com/80",
            "rating": "⭐⭐⭐⭐",
            "comment": "Great experience overall. The team was professional, and the results exceeded my expectations."
        },
        {
            "name": "Sam Wilson",
            "photo": "https://via.placeholder.com/80",
            "rating": "⭐⭐⭐⭐⭐",
            "comment": "Outstanding! I've tried many services, but this one stands out."
        },
        {
            "name": "Alice Johnson",
            "photo": "https://via.placeholder.com/80",
            "rating": "⭐⭐⭐⭐",
            "comment": "A great platform for learning. I highly recommend it!"
        },
        {
            "name": "Bob Brown",
            "photo": "https://via.placeholder.com/80",
            "rating": "⭐⭐⭐⭐⭐",
            "comment": "The best experience I've ever had!"
        },
        {
            "name": "Emily Green",
            "photo": "https://via.placeholder.com/80",
            "rating": "⭐⭐⭐⭐⭐",
            "comment": "A transformative learning experience that exceeded all my expectations!"
        }
    ]


    # Function to create a review card with improved styling
    def display_review_card(review):
        return f"""
        <div style="
            background-color: rgba(255, 255, 255, 0.1); 
            border-radius: 15px; 
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); 
            padding: 25px; 
            width: 100%; 
            height: 350px;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            transition: transform 0.3s ease;
            margin: 10px; /* Added small margin between cards */
        " onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
            <img src="{review['photo']}" style="
                border-radius: 50%; 
                width: 100px; 
                height: 100px; 
                margin-bottom: 15px; 
                border: 3px solid #ffffff;
            ">
            <h3 style="
                margin: 10px 0; 
                font-size: 1.3em; 
                color: #ffffff; 
                font-weight: bold;
            ">{review['name']}</h3>
            <div style="
                color: #FFD700; 
                font-size: 1.5em; 
                margin-bottom: 10px;
            ">{review['rating']}</div>
            <p style="
                font-size: 0.9em; 
                color: #f0f0f0; 
                text-align: center;
                line-height: 1.6;
                padding: 0 10px;
            ">"{review['comment']}"</p>
        </div>
        """


    # Create a container for the review cards with precise 3x2 grid layout and gaps
    st.markdown("""
    <div style="
        display: grid; 
        grid-template-columns: repeat(3, 1fr); 
        grid-template-rows: repeat(2, 1fr);
        gap: 30px; /* Increased gap between grid items */
        padding: 20px;
        max-width: 1200px;
        margin: 0 auto;
    ">
    """, unsafe_allow_html=True)

    # Display each review card
    for review in reviews:
        st.markdown(display_review_card(review), unsafe_allow_html=True)

    # Close the container
    st.markdown("</div>", unsafe_allow_html=True)
db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'askuha2659',
        'database': 'eleven'
    }
    # -------------Classes Page------------------
if selected == "Classes":

    st.markdown(
        "<h1 style='text-align: center;'>Select a Subject to access it's lectures!</h1>",
        unsafe_allow_html=True)
    #subject selection
    option = st.selectbox(
        'Select Subject',
        ('Physics', 'Chemistry', 'Math', 'Computer Science'), index=None)


    # Function to connect to the MySQL database
    def get_mysql_connection():
        return mysql.connector.connect(**db_config)


    if option == 'Physics':
        def show_vid(x):
            # Function to fetch video data from MySQL
            def fetch_video(Chapter_no):
                conn = get_mysql_connection()
                cursor = conn.cursor()
                # Assuming there's a column 'chapter_number' in your 'videos' table
                query = "SELECT video_data FROM PHYSICS WHERE Chapter_no = %s"
                cursor.execute(query, (Chapter_no,))
                result = cursor.fetchone()
                cursor.close()
                conn.close()
                return result[0] if result else None

            # Streamlit app
            st.title(f"Chapter {x} Video Lecture")

            # Fetch and display video
            try:
                video_data = fetch_video(x)  # Fetch video based on chapter number (or x)

                if video_data:
                    # Convert binary data to a base64-encoded string
                    video_base64 = base64.b64encode(video_data).decode('utf-8')
                    video_url = f"data:video/mp4;base64,{video_base64}"

                    st.video(video_url)
                else:
                    st.warning(f"No video found for Chapter {x}.")
            except Exception as e:
                st.error(f"An error occurred: {e}")
        option_in = st.selectbox(
            'Select Chapter Number',
            ('Chapter 1', 'Chapter 2', 'Chapter 3', 'Chapter 4', 'Chapter 5', 'Chapter 6', 'Chapter 7', 'Chapter 8',
             'Chapter 9', 'Chapter 10', 'Chapter 11', 'Chapter 12', 'Chapter 13', 'Chapter 14', 'Chapter 15'),
            index=None)

        # Select Chapter number!
        if option_in == None:
            st.write("Select a Chapter to continue")
        if option_in == 'Chapter 1':
            show_vid(1)
        if option_in == 'Chapter 2':
            show_vid(2)
        if option_in == 'Chapter 3':
            show_vid(3)
        if option_in == 'Chapter 4':
            show_vid(4)
        if option_in == 'Chapter 5':
            show_vid(5)
        if option_in == 'Chapter 6':
            show_vid(6)
        if option_in == 'Chapter 7':
            show_vid(7)
        if option_in == 'Chapter 8':
            show_vid(8)
        if option_in == 'Chapter 9':
            show_vid(9)
        if option_in == 'Chapter 10':
            show_vid(10)
        if option_in == 'Chapter 11':
            show_vid(11)
        if option_in == 'Chapter 12':
            show_vid(12)
        if option_in == 'Chapter 13':
            show_vid(13)
        if option_in == 'Chapter 14':
            show_vid(14)
        if option_in == 'Chapter 15':
            show_vid(15)



    if option == 'Chemistry':
        def show_vid(x):
            # Function to fetch video data from MySQL
            def fetch_video(Chapter_no):
                conn = get_mysql_connection()
                cursor = conn.cursor()
                # Assuming there's a column 'chapter_number' in your 'videos' table
                query = "SELECT video_data FROM CHEM WHERE Chapter_no = %s"
                cursor.execute(query, (Chapter_no,))
                result = cursor.fetchone()
                cursor.close()
                conn.close()
                return result[0] if result else None

            # Streamlit app
            st.title(f"Chapter {x} Video Lecture")

            # Fetch and display video
            try:
                video_data = fetch_video(x)  # Fetch video based on chapter number (or x)

                if video_data:
                    # Convert binary data to a base64-encoded string
                    video_base64 = base64.b64encode(video_data).decode('utf-8')
                    video_url = f"data:video/mp4;base64,{video_base64}"

                    st.video(video_url)
                else:
                    st.warning(f"No video found for Chapter {x}.")
            except Exception as e:
                st.error(f"An error occurred: {e}")
        option_in = st.selectbox(
            'Select Chapter Number',
            ('Chapter 1', 'Chapter 2', 'Chapter 3', 'Chapter 4', 'Chapter 5', 'Chapter 6', 'Chapter 7', 'Chapter 8',
             'Chapter 9', 'Chapter 10', 'Chapter 11', 'Chapter 12', 'Chapter 13', 'Chapter 14', 'Chapter 15'),
            index=None)

        # Select Chapter number!
        if option_in == None:
            st.write("Select a Chapter to continue")
        if option_in == 'Chapter 1':
            show_vid(1)
        if option_in == 'Chapter 2':
            show_vid(2)
        if option_in == 'Chapter 3':
            show_vid(3)
        if option_in == 'Chapter 4':
            show_vid(4)
        if option_in == 'Chapter 5':
            show_vid(5)
        if option_in == 'Chapter 6':
            show_vid(6)
        if option_in == 'Chapter 7':
            show_vid(7)
        if option_in == 'Chapter 8':
            show_vid(8)
        if option_in == 'Chapter 9':
            show_vid(9)
        if option_in == 'Chapter 10':
            show_vid(10)
        if option_in == 'Chapter 11':
            show_vid(11)
        if option_in == 'Chapter 12':
            show_vid(12)
        if option_in == 'Chapter 13':
            show_vid(13)
        if option_in == 'Chapter 14':
            show_vid(14)
        if option_in == 'Chapter 15':
            show_vid(15)



    if option == 'Math':
        def show_vid(x):
            # Function to fetch video data from MySQL
            def fetch_video(Chapter_no):
                conn = get_mysql_connection()
                cursor = conn.cursor()
                # Assuming there's a column 'chapter_number' in your 'videos' table
                query = "SELECT video_data FROM MATH WHERE Chapter_no = %s"
                cursor.execute(query, (Chapter_no,))
                result = cursor.fetchone()
                cursor.close()
                conn.close()
                return result[0] if result else None

            # Streamlit app
            st.title(f"Chapter {x} Video Lecture")

            # Fetch and display video
            try:
                video_data = fetch_video(x)  # Fetch video based on chapter number (or x)

                if video_data:
                    # Convert binary data to a base64-encoded string
                    video_base64 = base64.b64encode(video_data).decode('utf-8')
                    video_url = f"data:video/mp4;base64,{video_base64}"

                    st.video(video_url)
                else:
                    st.warning(f"No video found for Chapter {x}.")
            except Exception as e:
                st.error(f"An error occurred: {e}")
        option_in = st.selectbox(
            'Select Chapter Number',
            ('Chapter 1', 'Chapter 2', 'Chapter 3', 'Chapter 4', 'Chapter 5', 'Chapter 6', 'Chapter 7', 'Chapter 8',
             'Chapter 9', 'Chapter 10', 'Chapter 11', 'Chapter 12', 'Chapter 13', 'Chapter 14', 'Chapter 15'),
            index=None)

        # Select Chapter number!
        if option_in == None:
            st.write("Select a Chapter to continue")
        if option_in == 'Chapter 1':
            show_vid(1)
        if option_in == 'Chapter 2':
            show_vid(2)
        if option_in == 'Chapter 3':
            show_vid(3)
        if option_in == 'Chapter 4':
            show_vid(4)
        if option_in == 'Chapter 5':
            show_vid(5)
        if option_in == 'Chapter 6':
            show_vid(6)
        if option_in == 'Chapter 7':
            show_vid(7)
        if option_in == 'Chapter 8':
            show_vid(8)
        if option_in == 'Chapter 9':
            show_vid(9)
        if option_in == 'Chapter 10':
            show_vid(10)
        if option_in == 'Chapter 11':
            show_vid(11)
        if option_in == 'Chapter 12':
            show_vid(12)
        if option_in == 'Chapter 13':
            show_vid(13)
        if option_in == 'Chapter 14':
            show_vid(14)
        if option_in == 'Chapter 15':
            show_vid(15)



    if option == 'Computer Science':
        def show_vid(x):
            # Function to fetch video data from MySQL
            def fetch_video(Chapter_no):
                conn = get_mysql_connection()
                cursor = conn.cursor()
                # Assuming there's a column 'chapter_number' in your 'videos' table
                query = "SELECT video_data FROM CS WHERE Chapter_no = %s"
                cursor.execute(query, (Chapter_no,))
                result = cursor.fetchone()
                cursor.close()
                conn.close()
                return result[0] if result else None

            # Streamlit app
            st.title(f"Chapter {x} Video Lecture")

            # Fetch and display video
            try:
                video_data = fetch_video(x)  # Fetch video based on chapter number (or x)

                if video_data:
                    # Convert binary data to a base64-encoded string
                    video_base64 = base64.b64encode(video_data).decode('utf-8')
                    video_url = f"data:video/mp4;base64,{video_base64}"

                    st.video(video_url)
                else:
                    st.warning(f"No video found for Chapter {x}.")
            except Exception as e:
                st.error(f"An error occurred: {e}")
        option_in = st.selectbox(
            'Select Chapter Number',
            ('Chapter 1', 'Chapter 2', 'Chapter 3', 'Chapter 4', 'Chapter 5', 'Chapter 6', 'Chapter 7', 'Chapter 8',
             'Chapter 9', 'Chapter 10', 'Chapter 11', 'Chapter 12', 'Chapter 13', 'Chapter 14', 'Chapter 15'),
            index=None)

        # Select Chapter number!
        if option_in == None:
            st.write("Select a Chapter to continue")
        if option_in == 'Chapter 1':
            show_vid(1)
        if option_in == 'Chapter 2':
            show_vid(2)
        if option_in == 'Chapter 3':
            show_vid(3)
        if option_in == 'Chapter 4':
            show_vid(4)
        if option_in == 'Chapter 5':
            show_vid(5)
        if option_in == 'Chapter 6':
            show_vid(6)
        if option_in == 'Chapter 7':
            show_vid(7)
        if option_in == 'Chapter 8':
            show_vid(8)
        if option_in == 'Chapter 9':
            show_vid(9)
        if option_in == 'Chapter 10':
            show_vid(10)
        if option_in == 'Chapter 11':
            show_vid(11)
        if option_in == 'Chapter 12':
            show_vid(12)
        if option_in == 'Chapter 13':
            show_vid(13)
        if option_in == 'Chapter 14':
            show_vid(14)
        if option_in == 'Chapter 15':
            show_vid(15)
#-------------End of Classes-----------#


#------------Profile Page---------------#
st.markdown(
    """
    <style>
    .transparent-table-container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 80vh; /* Adjust height as needed */
        margin: 0 auto;
    }
    .transparent-table {
        background: linear-gradient(to right, #004fee , ##d4e6f1  ); /* Fully transparent background */
        color: #FFFFFF; /* Text color */
        font-size: 40px; /* Bigger font size */
        padding: 10px;
        width: 80%; /* Adjust width as needed */
        max-width: 900px; /* Maximum width of the table */
        border-collapse: collapse;
    }
    th, td {
        padding: 15px; 
        text-align: center;
        border: 10px solid #ddd; /* Light border */
        width: 30%; /* Equal width for all columns */
    }
    th {
        background-color: rgba(0, 0, 0, 0.1); /* Light background for headers */
        color: #FFFFFF; /* Text color for headers */
    }
    </style>
    """,
    unsafe_allow_html=True
)
mydb = mysql.connector.connect(
     host="localhost",
    user="root",
     password="askuha2659",
     database="Learnvid"
 )

#Create a cursor object
cursor = mydb.cursor()


if selected == "Profile":
    username = st.text_input("Enter Your username")

    if username:
        sql = "SELECT * FROM test1 WHERE username = %s"
        values = (username,)

        try:
            cursor.execute(sql, values)
            result = cursor.fetchone()  # Fetch only one row (user profile)

            if result:
                # Fetch column names to display in the table
                columns = [i[0] for i in cursor.description]

                # Convert the result to a pandas DataFrame
                df = pd.DataFrame([result], columns=columns)  # Wrap result in a list

                # Convert the DataFrame to HTML with headers
                table_html = df.to_html(index=False, classes='transparent-table')

                # Display as a transparent and bigger table, centered
                st.markdown(
                    f'<div class="transparent-table-container">{table_html}</div>',
                    unsafe_allow_html=True
                )

            else:
                st.write("User not found")

        except mysql.connector.Error as err:
            st.error(f"Error: {err}")
