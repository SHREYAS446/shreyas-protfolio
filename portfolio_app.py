
import streamlit as st

st.set_page_config(page_title="Mudhalkar Shreyas | Data Science Portfolio", layout="wide")

st.title("👨‍💻 Mudhalkar Shreyas")
st.subheader("Aspiring Data Scientist | Python Enthusiast | Machine Learning Learner")

st.write("📍 Velpur, Nizamabad, Telangana | 📞 9640826818 | ✉️ 238r1a6745@cmrec.ac.in")

# ---- About Me ----
st.header("About Me")
st.write("""
I'm an aspiring Data Scientist with a strong foundation in Python, Machine Learning, and Data Analytics.
I enjoy exploring datasets, uncovering insights, and building ML models to solve real-world problems.
""")

# ---- Skills ----
st.header("Skills")
st.markdown("""
- **Languages**: Python, SQL  
- **Libraries**: NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn  
- **Tools**: Streamlit, Jupyter, VS Code, Git  
- **Concepts**: Data Cleaning, EDA, Machine Learning, Model Evaluation, SMOTE, NLP  
""")

# ---- Projects ----
st.header("Projects")

st.subheader("📰 Fake News Detection Using NLP")
st.write("""
- Built a classification model to detect real vs fake news articles.
- Used TF-IDF, Logistic Regression, SVM.
- Achieved 95% accuracy and deployed a prototype.
""")

st.subheader("📉 Customer Churn Prediction")
st.write("""
- Predicted churn using classification models like Logistic Regression and Random Forest.
- Used SMOTE to handle class imbalance.
- Deployed using Streamlit.
""")

st.subheader("📊 Restaurant Ratings Analysis")
st.write("""
- Analyzed Zomato dataset to find insights on rating patterns.
- Visualized online delivery, table booking vs ratings.
""")

# ---- Education ----
st.header("Education")
st.write("""
**B.Tech - CMR Engineering College, Hyderabad**  
(Year: [Add your graduation year])  
""")

# ---- Contact ----
st.header("Connect With Me")
st.markdown("""
- [GitHub](https://github.com/yourgithub)  
- [LinkedIn](https://linkedin.com/in/yourlinkedin)  
- Email: 238r1a6745@cmrec.ac.in  
""")

