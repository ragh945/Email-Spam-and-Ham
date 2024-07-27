# Email Spam and Ham Classifier
This project is an email spam and ham classifier built using Streamlit and a Naive Bayes algorithm. The application allows users to input an email, which is then classified as either spam or ham (non-spam). Below are the details of how the application works:

Deployment Link : https://email-spam-and-ham-jxhhbnlexywv4blm3fwuov.streamlit.app/

## Technologies Used
- Streamlit: A web application framework used to build the interactive user interface.
- Naive Bayes Algorithm: A probabilistic classifier based on applying Bayes' theorem, used here for spam detection.
- Scikit-learn: A machine learning library used for building the Naive Bayes model and TF-IDF vectorizer.
- Pickle: A module for serializing and de-serializing Python objects, used to save and load the trained model and vectorizer.
- PIL (Python Imaging Library): Used to display images in the Streamlit app.

## How It Works
- User Interface: The application starts with displaying images and titles to give a visual appeal. Users can enter the content of an email into a text input box.
- Model Loading: The pre-trained Naive Bayes model and the TF-IDF vectorizer are loaded from serialized files (Email_spam_ham.pkl and tfidf_vectorization.pkl respectively).

## Email Input and Processing:
- The user inputs an email into the provided text box.
- Upon clicking the "Submit" button, the input email is transformed using the loaded TF-IDF vectorizer into a format suitable for model prediction.

## Prediction:
- The transformed email data is fed into the Naive Bayes model to predict whether the email is spam or ham.
- Based on the prediction, a message is displayed indicating whether the email is classified as spam or ham.
- 
## Visual Feedback:
- Depending on the classification result, corresponding images (spam or ham) are displayed to enhance user understanding.

  ![image](https://github.com/user-attachments/assets/4feec628-c160-4eda-92c6-249995fef4a6)



## Conclusion
This Streamlit application provides a simple and intuitive interface for classifying emails as spam or ham using a Naive Bayes algorithm and TF-IDF vectorization.
It demonstrates the power of combining machine learning with web-based interfaces to create useful and interactive tools.

