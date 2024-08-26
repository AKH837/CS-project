import streamlit as st
from streamlit_option_menu import option_menu

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
</style>
"""

# Apply the custom CSS
st.markdown(sidebar_css, unsafe_allow_html=True)

# Sidebar menu with dark theme and increased spacing
with st.sidebar:
    selected = option_menu(
        menu_title="Main menu",
        options=["Home", "Contact", "Classes", "Profile"],
        icons=["house", "envelope", "camera-video", "person"],
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
if 'selected_class' not in st.session_state:
    st.session_state.selected_class = None
if 'show_upload' not in st.session_state:
    st.session_state.show_upload = False

# Handle the content display based on the selected menu option
if selected == "Home":
    if not st.session_state.show_upload:
        # Custom huge title for "Welcome Teacher"
        st.markdown("<h1 class='huge-heading'>Welcome Student</h1>", unsafe_allow_html=True)

        # Custom title for "Select Your Class"
        st.markdown("<h2 class='custom-heading'>Select Your Class</h2>", unsafe_allow_html=True)

        with st.container():
            st.markdown("<div class='tabular-layout'>", unsafe_allow_html=True)

            # 2x2 grid of buttons
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

            st.markdown("</div>", unsafe_allow_html=True)

        st.write("\n\n")

        # Custom title for "Select Your Subject"
        st.markdown("<h2 class='custom-heading'>Select Your Subject</h2>", unsafe_allow_html=True)

        # Dropdown for subjects based on selected class
        classes_subjects = {
            "Class 9": ["English", "Math", "Science", "Social Science", "Hindi", "French"],
            "Class 10": ["English", "Math", "Science", "Social Science", "Hindi", "French"],
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
        selected_subject = st.selectbox("Choose the subject you teach:", options=subjects)

        # Centered OK button
        st.markdown("<div class='centered-container'><div>", unsafe_allow_html=True)
        if st.button("OK"):
            st.session_state.show_upload = True
        st.markdown("</div></div>", unsafe_allow_html=True)

    else:

        # Upload screen
        '''st.markdown("<h1 class='huge-heading'>Upload Your Lectures Here</h1>", unsafe_allow_html=True)

        st.write("<div class='upload-container'>", unsafe_allow_html=True)

        st.image("https://via.placeholder.com/600x300", caption="Lecture Video",
                 use_column_width=True)  # Adjusted image height

        uploaded_file = st.file_uploader("Choose a video file", type=["mp4", "avi", "mov"])

        st.write("<br>", unsafe_allow_html=True)
        col1, col2 = st.columns([1, 1])  # Create columns for buttons
        with col1:
            if st.button("Upload"):
                if uploaded_file:
                    st.session_state.uploaded_file = uploaded_file
                    st.write("File uploaded. Ready to submit!")
                else:
                    st.write("Please upload a file.")
        with col2:
            if st.button("Submit"):
                if 'uploaded_file' in st.session_state:
                    # Uncomment and add your SQL code here to save the file to the database
                    # mydb = mysql.connector.connect(
                    #     host="localhost",
                    #     user="yourusername",
                    #     password="yourpassword",
                    #     database="yourdatabase"
                    # )
                    # mycursor = mydb.cursor()
                    # sql = "INSERT INTO lectures (class, subject, video) VALUES (%s, %s, %s)"
                    # val = (st.session_state.selected_class, selected_subject, st.session_state.uploaded_file)
                    # mycursor.execute(sql, val)
                    # mydb.commit()
                    st.write("File submitted successfully!")
                    st.rerun()
                else:
                    st.write("No file to submit.")

        st.write("</div>", unsafe_allow_html=True)'''

if selected == "About Us":
    st.title(f"You have selected {selected}")
if selected == "Contact Us":
    st.title(f"You have selected {selected}")
