# import easyocr as ocr
# import streamlit as st
# from PIL import Image
# import numpy as np

# # Title
# st.title("Easy OCR - Extract Text from Images")

# # Subtitle
# st.markdown("## Optical Character Recognition - Using `easyocr`, `streamlit`")

# st.markdown("")

# # Image uploader
# image = st.file_uploader(label="Upload your image here", type=['png', 'jpg', 'jpeg'])

# @st.cache_data
# def load_model():
#     reader = ocr.Reader(['en'], model_storage_directory='.')
#     return reader

# reader = load_model()  # Load model

# if image is not None:
#     input_image = Image.open(image)  # Read image
#     st.image(input_image)  # Display image

#     with st.spinner("🤖 AI is at Work! "):
#         result = reader.readtext(np.array(input_image))
        
#         # Join all the text results into a single string
#         result_text = ' '.join([text[1] for text in result])
        
#         st.write(result_text)
#         st.balloons()
# else:
#     st.write("Upload an Image")

# import easyocr as ocr
# import streamlit as st
# from PIL import Image
# import numpy as np

# # Importing for logging
# import logging

# # Configure logging
# logging.basicConfig(filename='ocr_app.log', level=logging.INFO)

# # Title
# st.title("Easy OCR - Extract Text from Images")

# # Subtitle
# st.markdown("## Optical Character Recognition - Using `easyocr`, `streamlit`")

# st.markdown("")

# # Image uploader
# image = st.file_uploader(label="Upload your image here", type=['png', 'jpg', 'jpeg'])

# # Track the number of image uploads
# if image is not None:
#     logging.info('Image uploaded')

# @st.cache_data
# def load_model():
#     reader = ocr.Reader(['en'], model_storage_directory='.')
#     return reader

# reader = load_model()  # Load model

# if image is not None:
#     input_image = Image.open(image)  # Read image
#     st.image(input_image)  # Display image

#     with st.spinner("🤖 AI is at Work! "):
#         result = reader.readtext(np.array(input_image))
        
#         # Join all the text results into a single string
#         result_text = ' '.join([text[1] for text in result])
        
#         st.write(result_text)
#         st.balloons()

#         # Track OCR requests made
#         logging.info('OCR request made')

# else:
#     st.write("Upload an Image")

# import easyocr as ocr
# import streamlit as st
# from PIL import Image
# import numpy as np

# # Importing for logging
# import logging

# # Configure logging
# logging.basicConfig(filename='ocr_app.log', level=logging.INFO)

# # Counter for successful OCR requests
# successful_requests = 0

# # Title
# st.title("Easy OCR - Extract Text from Images")

# # Subtitle
# st.markdown("## Optical Character Recognition - Using `easyocr`, `streamlit`")

# st.markdown("")

# # Image uploader
# image = st.file_uploader(label="Upload your image here", type=['png', 'jpg', 'jpeg'])

# # Track the number of image uploads
# if image is not None:
#     logging.info('Image uploaded')

# @st.cache_data
# def load_model():
#     reader = ocr.Reader(['en'], model_storage_directory='.')
#     return reader

# reader = load_model()  # Load model

# if image is not None:
#     input_image = Image.open(image)  # Read image
#     st.image(input_image)  # Display image

#     with st.spinner("🤖 AI is at Work! "):
#         result = reader.readtext(np.array(input_image))
        
#         # Increment the counter for successful OCR requests
#         successful_requests += 1
        
#         # Join all the text results into a single string
#         result_text = ' '.join([text[1] for text in result])
        
#         st.write(result_text)
#         st.balloons()

#         # Track OCR requests made
#         logging.info('OCR request made')

#         # Track successful OCR requests fulfilled
#         logging.info('Successful OCR request')

# else:
#     st.write("Upload an Image")

# # Display the number of successful OCR requests fulfilled
# st.write(f"Successful OCR requests fulfilled: {successful_requests}")


# import easyocr as ocr
# import streamlit as st
# from PIL import Image
# import numpy as np

# # Importing for logging
# import logging

# # Configure logging
# logging.basicConfig(filename='ocr_app.log', level=logging.INFO)

# # Title
# st.title("Easy OCR - Extract Text from Images")

# # Subtitle
# st.markdown("## Optical Character Recognition - Using `easyocr`, `streamlit`")

# st.markdown("")

# # Image uploader
# image = st.file_uploader(label="Upload your image here", type=['png', 'jpg', 'jpeg'])

# # Track the number of image uploads
# if image is not None:
#     logging.info('Image uploaded')

# @st.cache_data
# def load_model():
#     reader = ocr.Reader(['en'], model_storage_directory='.')
#     return reader

# reader = load_model()  # Load model

# if image is not None:
#     input_image = Image.open(image)  # Read image
#     st.image(input_image)  # Display image

#     with st.spinner("🤖 AI is at Work! "):
#         result = reader.readtext(np.array(input_image))
        
#         # Join all the text results into a single string
#         result_text = ' '.join([text[1] for text in result])
        
#         st.write(result_text)
#         st.balloons()

#         # Track successful OCR requests fulfilled
#         logging.info('Successful OCR request fulfilled')

#         # Get the number of successful OCR requests from the log file
#         with open('ocr_app.log', 'r') as file:
#             lines = file.readlines()
#             successful_requests = sum('Successful OCR request fulfilled' in line for line in lines)

#         # Display the number of successful OCR requests in a styled circle
#         st.markdown(f'<div style="background-color: goldenrod; color: white; padding: 10px; border-radius: 50%; text-align: center; width: 50px; height: 50px; font-size: 20px;">{successful_requests}</div>', unsafe_allow_html=True)

# else:
#     st.write("Upload an Image")

# import easyocr as ocr
# import streamlit as st
# from PIL import Image
# import numpy as np

# # Importing for logging
# import logging

# # Configure logging
# logging.basicConfig(filename='ocr_app.log', level=logging.INFO)

# # Title
# st.title("Easy OCR - Extract Text from Images")

# # Subtitle
# st.markdown("## Optical Character Recognition - Using `easyocr`, `streamlit`")

# st.markdown("")

# # Image uploader
# image = st.file_uploader(label="Upload your image here", type=['png', 'jpg', 'jpeg'])

# # Track the number of image uploads
# if image is not None:
#     logging.info('Image uploaded')

# @st.cache_data
# def load_model():
#     reader = ocr.Reader(['en'], model_storage_directory='.')
#     return reader

# reader = load_model()  # Load model

# if image is not None:
#     input_image = Image.open(image)  # Read image
#     st.image(input_image)  # Display image

#     with st.spinner("🤖 AI is at Work! "):
#         result = reader.readtext(np.array(input_image))
        
#         # Join all the text results into a single string
#         result_text = ' '.join([text[1] for text in result])
        
#         st.write(result_text)
#         st.balloons()

#         # Track successful OCR requests fulfilled
#         logging.info('Successful OCR request fulfilled')

#         # Ask user satisfaction and record their answer
#         satisfaction = st.radio("Are you satisfied with the OCR results?", ("Yes", "No"))

#         # Calculate accuracy percentage based on user satisfaction
#         if satisfaction == "Yes":
#             accuracy_percentage = 95  # Example accuracy percentage
#         else:
#             accuracy_percentage = 75  # Example accuracy percentage

#         # Display accuracy percentage to the user
#         st.write(f"We offer {accuracy_percentage}% accuracy.")

# else:
#     st.write("Upload an Image")

# import easyocr as ocr
# import streamlit as st
# from PIL import Image
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt

# # Importing for logging
# import logging

# # Configure logging
# logging.basicConfig(filename='ocr_app.log', level=logging.INFO)

# # Title
# st.title("Easy OCR - Extract Text from Images")

# # Subtitle
# st.markdown("## Optical Character Recognition - Using `easyocr`, `streamlit`")

# st.markdown("")

# # Image uploader
# image = st.file_uploader(label="Upload your image here", type=['png', 'jpg', 'jpeg'])

# # Track the number of image uploads
# if image is not None:
#     logging.info('Image uploaded')

# @st.cache_data
# def load_model():
#     reader = ocr.Reader(['en'], model_storage_directory='.')
#     return reader

# reader = load_model()  # Load model

# # Data for storing ratings
# ratings_data = []

# if image is not None:
#     input_image = Image.open(image)  # Read image
#     st.image(input_image)  # Display image

#     with st.spinner("🤖 AI is at Work! "):
#         result = reader.readtext(np.array(input_image))
        
#         # Join all the text results into a single string
#         result_text = ' '.join([text[1] for text in result])
        
#         st.write(result_text)
#         st.balloons()

#         # Track successful OCR requests fulfilled
#         logging.info('Successful OCR request fulfilled')

#         # Ask user to rate on a scale of 5 stars
#         st.write("Please rate us on a scale of 5 stars:")
#         rating = st.slider("", 1, 5)
#         ratings_data.append(rating)

#         # Convert ratings data to DataFrame
#         ratings_df = pd.DataFrame(ratings_data, columns=['Rating'])

#         # Generate bar chart for ratings distribution
#         rating_counts = ratings_df['Rating'].value_counts().sort_index()
#         plt.bar(rating_counts.index, rating_counts.values)
#         plt.xlabel('Rating')
#         plt.ylabel('No. of Users')
#         plt.title('Rating Distribution')
#         st.pyplot()

#         # Calculate accuracy percentage based on user satisfaction
#         if rating >= 4:
#             accuracy_percentage = 95  # Example accuracy percentage
#         else:
#             accuracy_percentage = 75  # Example accuracy percentage

#         # Display accuracy percentage to the user
#         st.write(f"We offer {accuracy_percentage}% accuracy.")

#         # Generate pie chart for OCR accuracy
#         accuracy_labels = ['Accurate', 'Ineffective']
#         accuracy_values = [accuracy_percentage, 100 - accuracy_percentage]
#         colors = ['green', 'red']
#         plt.pie(accuracy_values, labels=accuracy_labels, colors=colors, autopct='%1.1f%%', startangle=140)
#         plt.title('OCR Accuracy')
#         st.pyplot()

# else:
#     st.write("Upload an Image")

# import easyocr as ocr
# import streamlit as st
# from PIL import Image
# import numpy as np

# # Importing for logging
# import logging

# # Configure logging
# logging.basicConfig(filename='ocr_app.log', level=logging.INFO)

# # Title
# st.title("Easy OCR - Extract Text from Images")

# # Subtitle
# st.markdown("## Optical Character Recognition - Using `easyocr`, `streamlit`")

# st.markdown("")

# # Image uploader
# image = st.file_uploader(label="Upload your image here", type=['png', 'jpg', 'jpeg'])

# # Track the number of image uploads
# if image is not None:
#     logging.info('Image uploaded')

# @st.cache_data
# def load_model():
#     reader = ocr.Reader(['en'], model_storage_directory='.')
#     return reader

# reader = load_model()  # Load model

# if image is not None:
#     input_image = Image.open(image)  # Read image
#     st.image(input_image)  # Display image

#     with st.spinner("🤖 AI is at Work! "):
#         result = reader.readtext(np.array(input_image))
        
#         # Join all the text results into a single string
#         result_text = ' '.join([text[1] for text in result])
        
#         st.write(result_text)
#         st.balloons()

#         # Track successful OCR requests fulfilled
#         logging.info('Successful OCR request fulfilled')

#         # Ask user to rate on a scale of 5 stars or "Not now"
#         rating = st.select_slider("Please rate us on a scale of 5 stars:", options=[1, 2, 3, 4, 5, "Not now"])
        
#         # Log the user's rating
#         if rating != "Not now":
#             logging.info(f"User rating: {rating}")

#             # Display feedback message based on rating
#             if rating >= 4:
#                 st.success("Thank you for your positive feedback!")
#             elif rating >= 3:
#                 st.info("We appreciate your feedback. We will strive to improve.")
#             else:
#                 st.error("We're sorry to hear that. Please let us know how we can improve.")
#         else:
#             st.info("You chose not to rate us at this time. Feel free to rate us later.")

# else:
#     st.write("Upload an Image")


# import easyocr as ocr
# import streamlit as st
# from PIL import Image
# import numpy as np

# # Importing for logging
# import logging

# # Configure logging
# logging.basicConfig(filename='ocr_app.log', level=logging.INFO)

# # Title
# st.title("Easy OCR - Extract Text from Images")

# # Subtitle
# st.markdown("## Optical Character Recognition - Using `easyocr`, `streamlit`")

# st.markdown("")

# # Image uploader
# image = st.file_uploader(label="Upload your image here", type=['png', 'jpg', 'jpeg'])

# # Track the number of image uploads
# if image is not None:
#     logging.info('Image uploaded')

# @st.cache_data
# def load_model():
#     reader = ocr.Reader(['en'], model_storage_directory='.')
#     return reader

# reader = load_model()  # Load model

# if image is not None:
#     input_image = Image.open(image)  # Read image
#     st.image(input_image)  # Display image

#     with st.spinner("🤖 AI is at Work! "):
#         result = reader.readtext(np.array(input_image))
        
#         # Join all the text results into a single string
#         result_text = ' '.join([text[1] for text in result])
        
#         st.write(result_text)
#         st.balloons()

#         # Track successful OCR requests fulfilled
#         logging.info('Successful OCR request fulfilled')

#         # Ask user to rate on a scale of 5 stars
#         st.write("Please rate us on a scale of 1 to 5 stars:")
#         rating = st.slider("", 0, 5)
        
#         # Log the user's rating if it's not zero
#         if rating != 0:
#             logging.info(f"User rating: {rating}")

#         # Display feedback message based on rating
#         if rating >= 4:
#             st.success("Thank you for your positive feedback!")
#         elif rating >= 3:
#             st.info("We appreciate your feedback. We will strive to improve.")
#         elif rating == 0:
#             st.success("Waiting for your feedback!")
#         else:
#             st.error("We're sorry to hear that. Please let us know how we can improve.")

# else:
#     st.write("Upload an Image")



# import easyocr as ocr
# import streamlit as st
# from PIL import Image
# import numpy as np

# # Importing for logging
# import logging

# # Configure logging
# logging.basicConfig(filename='ocr_app.log', level=logging.INFO)

# # Title
# st.title("Easy OCR - Extract Text from Images")

# # Subtitle
# st.markdown("## Optical Character Recognition - Using `easyocr`, `streamlit`")

# st.markdown("")

# # Image uploader
# image = st.file_uploader(label="Upload your image here", type=['png', 'jpg', 'jpeg'])

# # Track the number of image uploads
# if image is not None:
#     logging.info('Image uploaded')

#     # Reset rating to 0 for every new image upload
#     rating = 0

# @st.cache_data
# def load_model():
#     reader = ocr.Reader(['en'], model_storage_directory='.')
#     return reader

# reader = load_model()  # Load model

# if image is not None:
#     input_image = Image.open(image)  # Read image
#     st.image(input_image)  # Display image

#     with st.spinner("🤖 AI is at Work! "):
#         result = reader.readtext(np.array(input_image))
        
#         # Join all the text results into a single string
#         result_text = ' '.join([text[1] for text in result])
        
#         st.write(result_text)
#         st.balloons()

#         # Track successful OCR requests fulfilled
#         logging.info('Successful OCR request fulfilled')

#         # Ask user to rate on a scale of 0 to 5 stars (0 for no rating)
#         st.write("Please rate us on a scale of 0 to 5 stars (0 for no rating):")
#         rating = st.slider("", 0, 5, value=rating)
        
#         # Log the user's rating if it's not zero
#         if rating != 0:
#             logging.info(f"User rating: {rating}")

#         # Display feedback message based on rating
#         if rating >= 4:
#             st.success("Thank you for your positive feedback!")
#         elif rating >= 3:
#             st.info("We appreciate your feedback. We will strive to improve.")
#         elif rating == 0:
#             pass  # If no rating provided, do nothing
#         else:
#             st.error("We're sorry to hear that. Please let us know how we can improve.")

# else:
#     st.write("Upload an Image")


# import easyocr as ocr
# import streamlit as st
# from PIL import Image
# import numpy as np

# # Importing for logging
# import logging

# # Configure logging
# logging.basicConfig(filename='ocr_app.log', level=logging.INFO)

# # Title
# st.title("Easy OCR - Extract Text from Images")

# # Subtitle
# st.markdown("## Optical Character Recognition - Using `easyocr`, `streamlit`")

# st.markdown("")

# # Image uploader
# image = st.file_uploader(label="Upload your image here", type=['png', 'jpg', 'jpeg'])

# # Track the number of image uploads
# if image is not None:
#     logging.info('Image uploaded')

#     # Reset rating to 0 for every new image upload
#     rating = 0
#     if rating == 0:
#         pass 
    

#     @st.cache_data
#     def load_model():
#         reader = ocr.Reader(['en'], model_storage_directory='.')
#         return reader

#     reader = load_model()  # Load model

#     input_image = Image.open(image)  # Read image
#     st.image(input_image)  # Display image

#     with st.spinner("🤖 AI is at Work! "):
#         result = reader.readtext(np.array(input_image))
        
#         # Join all the text results into a single string
#         result_text = ' '.join([text[1] for text in result])
        
#         st.write(result_text)
#         st.balloons()

#         # Track successful OCR requests fulfilled
#         logging.info('Successful OCR request fulfilled')

#         # Ask user to rate on a scale of 0 to 5 stars (0 for no rating)
#         st.write("Please rate us on a scale of 0 to 5 stars (0 for no rating):")
#         rating = st.slider("", 0, 5)
        
#         # Log the user's rating if it's not zero
#         if rating != 0:
#             logging.info(f"User rating: {rating}")

#         # Display feedback message based on rating
#         if rating >= 4:
#             st.success("Thank you for your positive feedback!")
#         elif rating >= 3:
#             st.info("We appreciate your feedback. We will strive to improve.")
#         elif rating == 0:
#             pass  # If no rating provided, do nothing
#         else:
#             st.error("We're sorry to hear that. Please let us know how we can improve.")

# else:
#     st.write("Upload an Image")


# import easyocr as ocr
# import streamlit as st
# from PIL import Image
# import numpy as np

# # Importing for logging
# import logging

# # Configure logging
# logging.basicConfig(filename='ocr_app.log', level=logging.INFO)

# # Title
# st.title("Easy OCR - Extract Text from Images")

# # Subtitle
# st.markdown("## Optical Character Recognition - Using `easyocr`, `streamlit`")

# st.markdown("")

# # Image uploader
# image = st.file_uploader(label="Upload your image here", type=['png', 'jpg', 'jpeg'])

# # Admin login button
# if st.button("Admin Login"):
#     st.write("Redirecting to Admin Login page...")
#     # Redirect to the admin login page
#     st.experimental_rerun()

# # Track the number of image uploads
# if image is not None:
#     logging.info('Image uploaded')

#     @st.cache_data
#     def load_model():
#         reader = ocr.Reader(['en'], model_storage_directory='.')
#         return reader

#     reader = load_model()  # Load model

#     input_image = Image.open(image)  # Read image
#     st.image(input_image)  # Display image

#     with st.spinner("🤖 AI is at Work! "):
#         result = reader.readtext(np.array(input_image))
        
#         # Join all the text results into a single string
#         result_text = ' '.join([text[1] for text in result])
        
#         st.write(result_text)
#         st.balloons()

#         # Track successful OCR requests fulfilled
#         logging.info('Successful OCR request fulfilled')

#         # Ask user for feedback
#         st.write("Do you like our service?")
#         feedback = st.radio("Select your feedback:", ("Yes", "No", "Reply Later"), index=2)

#         # Log the user's feedback if it's not "Reply Later"
#         if feedback != "Reply Later":
#             logging.info(f"User feedback: {feedback}")

#         # Display feedback message based on user's feedback
#         if feedback == "Yes":
#             st.success("Thank you for your feedback!")
#         elif feedback == "No":
#             st.error("We're sorry to hear that. We will improve.")
#         else:
#             pass  # If "Reply Later" selected, do nothing

# else:
#     st.write("Upload an Image")

# import easyocr as ocr
# import streamlit as st
# from PIL import Image
# import numpy as np

# # Importing for logging
# import logging

# # Configure logging
# logging.basicConfig(filename='ocr_app.log', level=logging.INFO)

# # Title
# st.title("Easy OCR - Extract Text from Images")

# # Subtitle
# st.markdown("## Optical Character Recognition - Using `easyocr`, `streamlit`")

# st.markdown("")

# # # Admin login button
# # if st.button("Admin Login"):
# #     st.write("Redirecting to Admin Login page...")
# #     # Redirect to the admin login page by displaying a link
# #     st.markdown("[Admin Login Page](http://localhost:8501/?login=true)")



# # Admin login button
# if st.button("Admin Login"):
#     st.write("Redirecting to Admin Login page...")
#     # Redirect to the admin login page using query parameters
#     st.query_params(login=True)

# # Image uploader
# image = st.file_uploader(label="Upload your image here", type=['png', 'jpg', 'jpeg'])

# # Track the number of image uploads
# if image is not None:
#     logging.info('Image uploaded')

#     @st.cache_data
#     def load_model():
#         reader = ocr.Reader(['en'], model_storage_directory='.')
#         return reader

#     reader = load_model()  # Load model

#     input_image = Image.open(image)  # Read image
#     st.image(input_image)  # Display image

#     with st.spinner("🤖 AI is at Work! "):
#         result = reader.readtext(np.array(input_image))
        
#         # Join all the text results into a single string
#         result_text = ' '.join([text[1] for text in result])
        
#         st.write(result_text)
#         st.balloons()

#         # Track successful OCR requests fulfilled
#         logging.info('Successful OCR request fulfilled')

#         # Ask user for feedback
#         st.write("Do you like our service?")
#         feedback = st.radio("Select your feedback:", ("Yes", "No", "Reply Later"), index=2)

#         # Log the user's feedback if it's not "Reply Later"
#         if feedback != "Reply Later":
#             logging.info(f"User feedback: {feedback}")

#         # Display feedback message based on user's feedback
#         if feedback == "Yes":
#             st.success("Thank you for your feedback!")
#         elif feedback == "No":
#             st.error("We're sorry to hear that. We will improve.")
#         else:
#             pass  # If "Reply Later" selected, do nothing

# else:
#     st.write("Upload an Image")


# import easyocr as ocr
# import streamlit as st
# from PIL import Image
# import numpy as np
# import logging

# # Configure logging
# logging.basicConfig(filename='ocr_app.log', level=logging.INFO)

# # Title
# st.title("Easy OCR - Extract Text from Images")

# # Subtitle
# st.markdown("## Optical Character Recognition - Using `easyocr`, `streamlit`")

# st.markdown("")

# # Admin login button
# if st.button("Admin Login"):
#     st.write("Redirecting to Admin Login page...")
#     # Redirect to the admin login page using query parameters
#     st.experimental_set_query_params(login=True)

# # Image uploader
# image = st.file_uploader(label="Upload your image here", type=['png', 'jpg', 'jpeg'])

# # Track the number of image uploads
# if image is not None:
#     logging.info('Image uploaded')

#     @st.cache_data
#     def load_model():
#         reader = ocr.Reader(['en'], model_storage_directory='.')
#         return reader

#     reader = load_model()  # Load model

#     input_image = Image.open(image)  # Read image
#     st.image(input_image)  # Display image

#     with st.spinner("🤖 AI is at Work! "):
#         result = reader.readtext(np.array(input_image))
        
#         # Join all the text results into a single string
#         result_text = ' '.join([text[1] for text in result])
        
#         st.write(result_text)
#         st.balloons()

#         # Track successful OCR requests fulfilled
#         logging.info('Successful OCR request fulfilled')

#         # Ask user for feedback
#         st.write("Do you like our service?")
#         feedback = st.radio("Select your feedback:", ("Yes", "No", "Reply Later"), index=2)

#         # Log the user's feedback if it's not "Reply Later"
#         if feedback != "Reply Later":
#             logging.info(f"User feedback: {feedback}")

#         # Display feedback message based on user's feedback
#         if feedback == "Yes":
#             st.success("Thank you for your feedback!")
#         elif feedback == "No":
#             st.error("We're sorry to hear that. We will improve.")
#         else:
#             pass  # If "Reply Later" selected, do nothing

# else:
#     st.write("Upload an Image")


import easyocr as ocr
import streamlit as st
from PIL import Image
import numpy as np
import logging

st.set_page_config(
    page_title="PicToScript",
)

st.sidebar.success("Admin login")

# Configure logging
logging.basicConfig(filename='ocr_app.log', level=logging.INFO)

# Title
st.title("PicToScript")

# Subtitle
# st.markdown("## Optical Character Recognition - Using `easyocr`, `streamlit`")

st.markdown("")

# # Admin login button
# if st.button("Admin Login"):
#     st.write("Redirecting to Admin Login page...")
#     # Redirect to the admin login page using query parameters
#     st.query_params(login=True)

# Image uploader
image = st.file_uploader(label="Upload your image here", type=['png', 'jpg', 'jpeg'])

# Track the number of image uploads
if image is not None:
    logging.info('Image uploaded')

    @st.cache_data
    def load_model():
        reader = ocr.Reader(['en'], model_storage_directory='.')
        return reader

    reader = load_model()  # Load model

    input_image = Image.open(image)  # Read image
    st.image(input_image)  # Display image

    with st.spinner("🤖 AI is at Work! "):
        result = reader.readtext(np.array(input_image))
        
        # Join all the text results into a single string
        result_text = ' '.join([text[1] for text in result])
        
        st.write(result_text)
        st.balloons()

        # Track successful OCR requests fulfilled
        logging.info('Successful OCR request fulfilled')

        # Ask user for feedback
        st.write("Do you like our service?")
        feedback = st.radio("Select your feedback:", ("Yes", "No", "Reply Later"), index=2)

        # Log the user's feedback if it's not "Reply Later"
        if feedback != "Reply Later":
            logging.info(f"User feedback: {feedback}")

        # Display feedback message based on user's feedback
        if feedback == "Yes":
            st.success("Thank you for your feedback!")
        elif feedback == "No":
            st.error("We're sorry to hear that. We will improve.")
        else:
            pass  # If "Reply Later" selected, do nothing

else:
    st.write("Upload an Image")
