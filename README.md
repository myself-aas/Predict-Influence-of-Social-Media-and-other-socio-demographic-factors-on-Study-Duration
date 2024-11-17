
# Project Title

Influence of Social Media and other socio-demographic factors on Study Duration Prediction Web App


## Overview

This web application leverages machine learning to predict the study duration based on several personal and lifestyle factors. The app takes input such as **GPA scores**, **social media engagement**, **Residence**, **Family Education**, **relationship status**, and more, and provides a prediction for the **study duration** (ranging from 2 to 8 hours).

The goal of this project is to give students an insight into how their personal and social habits affect their study time, helping them manage their time better.

## Features

- **User Input**: Allows users to input key factors such as GPA scores, relationship status, and social media engagement.
- **Study Duration Prediction**: Predicts the amount of time a student should ideally spend studying based on the input data.
- **Machine Learning Model**: Trained using real-world data to predict study duration effectively.
- **Flask Backend**: Used to build the RESTful API that handles predictions.
- **Elegant UI**: A responsive and user-friendly frontend for ease of interaction.


## Tech Stack

- **Frontend**: HTML, CSS, js
- **Backend**: Flask (Python-based web framework)
- **Machine Learning**: scikit-learn, pandas, numpy
- **Deployment**: Render (or any cloud hosting platform like Heroku or AWS)
## Installation and Setup

To run this project locally:

### Prerequisites
- Python 3.x
- pip (Python package manager)

### Steps:
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/Study-Duration-Prediction.git
   cd Study-Duration-Prediction

2. **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt

3. **Run the Flask app:**
    ```bash
    python app.py
    
## Model Details

The model is trained to predict the study duration based on the following input features:

- **SSC GPA:** Secondary school GPA *(between 1.00 to 5.00)*
- **HSC GPA:** Higher secondary school GPA *(between 1.00 to 5.00)*
- **Social Media Engagement:** Hours spent on social media *(between 1 to 5 hours)*
- **Relationship:** Whether the student is in a relationship *(0 = No, 1 = Yes)*
- **Bad Habits:** Whether the student has any bad habits *(0 = No, 1 = Yes)*
- **External Factors:** Influence of external factors *(0 = No, 1 = Yes)*
- **Residence with Family:** Whether the student lives with their family *(0 = No, 1 = Yes)*
- **Family Education:** Whether the family is educated *(0 = No, 1 = Yes)*
- **Politics:** Whether the student is involved in politics *(0 = No, 1 = Yes)*
## Screenshots

![App Screenshot](https://github.com/myself-aas/Predict-Influence-of-Social-Media-and-other-socio-demographic-factors-on-Study-Duration/blob/main/screencapture-192-168-184-132-5000-2024-11-17-15_26_43.png)


## Example Input

- **SSC GPA:** 5.00
- **HSC GPA:** 5.00
- **Residence with Family:** 0
- **Family Education:** 1
- **Social Media Engagement:** 3
- **Relationship:** 1
- **Bad Habits:** 0
- **Politics:** 0
- **External Factors:** 1
## Example Output

- **Predicted Study Duration:** 7.86 hours
## Usage

1/ Open the web app in your browser ``(http://127.0.0.1:5000/).``

2/ Fill in the form with the required data points.

3/ Click **Predict** to receive the study duration prediction.

4/ The result will display below the form with an estimated study duration.


## Deployment

You can deploy this app on platforms such as [Render](https://render.com/) or [Heroku](https://www.heroku.com/). Follow their respective documentation to deploy the Flask app online.
## Future Enhancements

- **Model Improvement:** Integrate more features and improve the model's accuracy using advanced algorithms.
- **User Accounts:** Allow users to sign in and track their study patterns over time.
- **Visualization:** Include visual graphs showing trends and correlations between social media use and study duration.
## License

This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License.


## Acknowledgements

- **Flask Documentation:** https://flask.palletsprojects.com/
- **scikit-learn Documentation:** https://scikit-learn.org/


## Authors

- [@myself-aas](https://github.com/myself-aas)


## Support

For support and queries, [email](shuvoasifahmed@gmail.com) me.
