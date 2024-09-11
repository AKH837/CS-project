import streamlit as st
from streamlit_option_menu import option_menu
import random

# Custom CSS for the sidebar with a darker background
sidebar_css = """
<style>
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
    .subheading {
        color: #ffffff;
        text-align: center;
        font-size: 24px;
        margin-top: 20px;
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
            "container": {"padding": "0!important", "background-color": "#0f0f0f"},
            "icon": {"color": "#ffffff", "font-size": "18px"},
            "nav-link": {
                "font-size": "16px",
                "text-align": "left",
                "margin": "0px",
                "padding": "20px",
                "background-color": "#1a1a1a",  # Match with sidebar background
                "color": "#f0f0f0",  # Text color
                "--hover-color": "#333333"  # Hover effect color
            },
            "nav-link-selected": {
                "background-color": "#333333",  # Darker background for the selected item
                "color": "#ffffff",  # Text color for selected item
            },
        },
    )

# Initialize session state


if selected == "Home":
    if not st.session_state.show_upload:
        # Custom huge title for "Welcome Student"
        st.markdown("<h1 class='huge-heading'>Welcome Student</h1>", unsafe_allow_html=True)

        # Custom title for "Select Your Class"
        st.markdown("<h2 class='custom-heading'>Select Your Class</h2>", unsafe_allow_html=True)

        # Class Selection
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            if st.button("Class 9"):
                st.session_state.selected_class = "Class 9"
        with col2:
            if st.button("Class 10"):
                st.session_state.selected_class = "Class 10"
        with col3:
            if st.button("Class 11"):
                st.session_state.selected_class = "Class 11"
        with col4:
            if st.button("Class 12"):
                st.session_state.selected_class = "Class 12"

        # Subject Selection
        st.markdown("<h2 class='custom-heading'>Select Your Subject</h2>", unsafe_allow_html=True)

        classes_subjects = {
            "Class 9": ["French", "Hindi", "Regional Language"],
            "Class 10": ["French", "Hindi", "Regional Language"],
            "Class 11": ["Science", "Commerce", "Arts", "English"],
            "Class 12": ["Science", "Commerce", "Arts", "English"]
        }

        selected_class = st.selectbox(
            "Choose the class:",
            options=["Class 9", "Class 10", "Class 11", "Class 12"],
            index=["Class 9", "Class 10", "Class 11", "Class 12"].index(
                st.session_state.selected_class) if st.session_state.selected_class else 0,
            disabled=True
        )

        subjects = classes_subjects.get(selected_class, [])
        selected_subject = st.selectbox("Choose the subject:", options=subjects)

        # School Selection Dropdown
        st.markdown("<h2 class='custom-heading'>Select Your School</h2>", unsafe_allow_html=True)

        schools = ["GIIS School", "XYZ School", "ABC School"]
        selected_school = st.selectbox("Choose your school:", options=schools)

        # Centered OK button
        st.markdown("<div class='centered-container'><div>", unsafe_allow_html=True)
        if st.button("OK"):
            # Simulate saving to the database and proceeding
            """
            try:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="yourusername",
                    password="yourpassword",
                    database="yourdatabase"
                )
                mycursor = mydb.cursor()
                sql = "INSERT INTO students (class, subject, school) VALUES (%s, %s, %s)"
                val = (st.session_state.selected_class, selected_subject, selected_school)
                mycursor.execute(sql, val)
                mydb.commit()
                st.success("Data saved successfully!")
            except mysql.connector.Error as err:
                st.error(f"Error: {err}")
            finally:
                mydb.close()
            """

            st.session_state.show_upload = True
            st.session_state.data_saved = True
        st.markdown("</div></div>", unsafe_allow_html=True)

    if st.session_state.data_saved and st.session_state.show_upload:
        # Display the new page
        st.markdown("<h1 class='huge-heading'>Welcome Student</h1>", unsafe_allow_html=True)
        st.markdown("<h2 class='subheading'>Check out your lectures and more in the sidebar!</h2>",
                    unsafe_allow_html=True)

        # Display a random education image
        #education_images = [
            #"https://imgur.com/w3tiPuU.jpg",
            #"https://imgur.com/a/S7jpWWF.jpg",
            #"https://imgur.com/kOvRNwW.jpg"
        #]
        st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)
        #random_image_url = random.choice(education_images)
        img_url = "https://i.imgur.com/w3tiPuU.jpg"

        st.markdown(f"<div style='text-align: center;'><img src='{img_url}' width='700'></div>",
                    unsafe_allow_html=True)

if selected == "Profile":
    st.markdown("<h1 class='huge-heading'>Your Profile</h1>", unsafe_allow_html=True)

#Fetch user details from the database (Replace with actual query logic)
#sql = "SELECT class, school, username, email FROM sgn1 WHERE username=%s"
#cursor.execute(sql, (st.session_state.username,))
#profile_data = cursor.fetchone()

    # For demonstration, we'll use mock data
    profile_pic_url="https://imgur.com/VuwdK9G.jpg"
    st.markdown(f"<img src='{profile_pic_url}' width='220' height='200' class='profile-pic'>",
                unsafe_allow_html=True)
    profile_data = {
        "username": "john_doe",
        "email": "john@example.com",
        "class": "Class 10",
        "school": "XYZ School"
    }

    # Display the profile information
    st.markdown(
        f"""
        <div class="profile-info">
            <p>Username: {profile_data['username']}</p>
            <p>Email ID: {profile_data['email']}</p>
            <p>Class: {profile_data['class']}</p>
            <p>School: {profile_data['school']}</p>
        </div>
        """, unsafe_allow_html=True
    )