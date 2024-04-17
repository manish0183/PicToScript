import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Function to authenticate admin
def authenticate(username, password):
    # Predefined authorized credentials
    authorized_username = "admin"
    authorized_password = "admin123"

    # Check if provided credentials match authorized credentials
    if username == authorized_username and password == authorized_password:
        return True
    else:
        return False

# Admin authentication page
def admin_authentication():
    st.title("Admin Login")
    st.write("Please enter your credentials to log in.")

    # Input fields for username and password
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # Button to submit credentials
    if st.button("Login"):
        if authenticate(username, password):
            st.success("Login successful!")
            st.session_state.is_authenticated = True  # Set session variable to indicate authentication
        else:
            st.error("Invalid username or password. Please try again.")

# Admin dashboard
def admin_dashboard():
    st.title("Admin Dashboard")

    # Read log file
    try:
        log_data = pd.read_csv('ocr_app.log', header=None, names=['Log'])
    except FileNotFoundError:
        st.error("Log file not found.")
        return

    # Count number of successful OCR requests fulfilled
    successful_requests = log_data['Log'].str.contains('Successful OCR request fulfilled').sum()

    # Count number of positive and negative feedbacks
    positive_feedbacks = log_data['Log'].str.contains('User feedback: Yes').sum()
    negative_feedbacks = log_data['Log'].str.contains('User feedback: No').sum()

    # Display statistics
    st.subheader("Statistics")
    st.write(f"Number of successful OCR requests fulfilled: {successful_requests}")
    st.write(f"Number of positive feedbacks: {positive_feedbacks}")
    st.write(f"Number of negative feedbacks: {negative_feedbacks}")

    # Plot bar chart for feedbacks
    feedback_data = pd.DataFrame({'Feedback': ['Positive', 'Negative'], 'Count': [positive_feedbacks, negative_feedbacks]})
    st.bar_chart(feedback_data.set_index('Feedback'))

# Main function
def main():
    st.sidebar.title("Admin Panel")
    
    # Check if admin is authenticated
    if 'is_authenticated' not in st.session_state:
        st.session_state.is_authenticated = False
    
    # Show admin authentication page if not authenticated
    if not st.session_state.is_authenticated:
        admin_authentication()
    else:
        # Show admin dashboard if authenticated
        admin_dashboard()

if __name__ == "__main__":
    main()
