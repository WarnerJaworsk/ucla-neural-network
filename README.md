# UCLA_Admission_Chance_application

This app has been built using Streamlit and deployed with Streamlit community cloud

[Visit the app here](https://w13admissionchance.streamlit.app/)

password - streamlit

This application predicts a student's chance of admission into UCLA. The model aims to help users assess probablity of admission to UCLA by leveraging machine learning predictions.

## Features

- User-friendly interface powered by Streamlit.
- Input form to enter details such as GRE Score, TOEFL Score, income, and other relevant factors.
- Real-time prediction of admission chance based on the trained model.
- Accessible via Streamlit Community Cloud.

## Dataset

The application is trained on the **Admission.csv dataset**, a dataset collecting students scores and characteristics. It includes features like:

- GRE_Score: (out of 340)
- TOEFL_Score: (out of 120)
- University_Rating: Out of 5
- SOP: Statement of Purpose Strength (out of 5)
- LOR: Letter of Recommendation Strength (out of 5)
- CGPA: Student's Undergraduate CGPA(out of 10)
- Research: Whether student has Research Experience (0 or 1)
- Admit_Chance: either Yes or NO (0 or 1)

## Technologies Used

- **Streamlit**: For building the web application.
- **Scikit-learn**: For model training and evaluation.
- **Pandas** and **NumPy**: For data preprocessing and manipulation.
- **Matplotlib** and **Seaborn**: For exploratory data analysis and visualization (if applicable).

## Model

The predictive model is trained using the Admission.csv dataset. It applies preprocessing steps like encoding categorical variables and scaling numerical features. The neural network model used includes the MLP Classifier algorithm.

## Future Enhancements

- Adding support for multiple datasets.
- Incorporating explainability tools like SHAP to provide insights into predictions.
- Adding visualizations to better represent user input and model predictions.

## Installation (for local deployment)

If you want to run the application locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/WarnerJaworsk/ucla-neural-network/upload/main
   cd credit_eligibility_application

   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows, use `env\\Scripts\\activate`

   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt

   ```

4. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

#### Thank you for using the Credit Eligibility Application! Feel free to share your feedback.
