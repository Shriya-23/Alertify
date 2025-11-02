💳 ALERTIFY : REAL-TIME CREDIT CARD FRAUD DETECTION

[Detecting financial frauds before they cause damage.]

🔷 About the Project

-As a Computer Science engineering student, my curiosity for Machine Learning and data-driven systems has always been strong,especially when it comes to how Python can turn raw data into meaningful insights.

-One day, while exploring real-world datasets, I stumbled upon the Credit Card Fraud Detection dataset,a huge collection of anonymized banking transactions.

-Can I teach a machine to identify and detect fraudulent transactions just by learning patterns from this data?

-That curiosity led to Alertify:A machine learning-powered fraud detection system that analyzes transaction patterns in real time.

-It’s more than a dataset project: It’s a practical glimpse into how FinTech companies protect users and banks from millions in daily losses.

💡What is Alertify?

-Alertify is an intelligent fraud detection system that uses machine learning models to classify transactions as legitimate or fraudulent.

-It’s designed to help banks, payment gateways, and financial services detect anomalies in real time.

🏦 Why I Built It

-Financial fraud has become one of the biggest challenges for banks today,especially with the rise of digital payments.

-As a student diving into Python and machine learning algorithms, I wanted to understand how machine learning can safeguard trust in such a critical domain.

So, I built Alertify:

-To learn and implement ML algorithms that work with real-world data.

-To simulate real-time fraud detection like in modern banking systems.

-To bridge the gap between academic learning and real FinTech challenges.

⚙️ Tech Stack

🔷Machine Learning & Backend:

-Python – Core programming language

-scikit-learn – For model training and evaluation (Random Forest Classifier)

-joblib – To save and load trained ML models efficiently

-Pandas & NumPy – For data preprocessing and feature manipulation

-FastAPI – Lightweight, fast backend framework for serving predictions via REST API

🔷Frontend:

-React.js – For building the interactive and real-time dashboard

-Chart.js (react-chartjs-2) – To visualize fraud probability as a live chart

-Tailwind CSS – For clean, responsive UI styling

🔷 Model Training Environment:

Dataset used

Credit Card Fraud Detection Dataset (Kaggle)

-Contains ~284,807 transactions and 492 fraud cases

-Features are PCA-transformed for confidentiality

-Highly imbalanced dataset requiring preprocessing and sampling

-Balanced it & trained Random Forest model saved as rf_model_balanced.pkl

✅Technical Working

Step 1 - Data Preprocessing:

-The dataset (creditcard.csv) was loaded and cleaned using Pandas.

-Columns V1 to V28 are anonymized numerical features generated through PCA (Principal Component Analysis).

-The dataset was imbalanced (fraud cases were <0.2%), so it was balanced using resampling techniques before model training.

Step 2 - Model Training:

-A Random Forest Classifier was trained to predict the Class label (0 = Legit, 1 = Fraud).

-The model learns subtle relationships between features like transaction amount, time, and PCA components.

-Performance metrics like precision, recall, and F1-score were analyzed to ensure reliability.

Step 3 - Model Deployment (Backend):

-The trained model (rf_model_balanced.pkl) is loaded into a FastAPI backend.

-A /predict endpoint accepts JSON input — Time, Amount, and V1–V28 features.

-The backend preprocesses the input, passes it to the model, and returns:

{
  "is_fraud": true,
  "fraud_probability": 0.87
}


Step 3 - Frontend Visualization:

-The React.js frontend calls the FastAPI endpoint.

It displays:

-A Doughnut Chart showing Fraud vs Legit probability.

-A dynamic summary (verdict, model confidence, and suggested actions).

-Users only need to input Time and Amount — synthetic V1–V28 features are auto-generated for demo purposes.

🔷 How to Run Locally

🔷 Clone the Repository

git clone https://github.com/Shriya-23/Alertify.git

cd Alertify


🔷 Setup Backend

cd backend

python -m venv venv

venv\Scripts\activate   # On Windows

pip install -r requirements.txt

python app.py


🔷Setup Frontend

cd frontend

npm install

🔷 Conclusion

Alertify isn’t just another project,As a learner, I wanted to explore how algorithms can make financial systems smarter and safer, and this project became the perfect playground to connect data, logic, and impact.

his is just the beginning of my journey into machine learning and financial analytics, and I’m always open to learning, improving, and collaborating with others who share the same curiosity.

Got feedback or ideas? I’d love to hear them!
shriya.sharma1923@gmail.com

💼 About Author

Hi! I’m Shriya Sharma-A Computer Science student passionate about building practical, data-driven, and impactful tech solutions.

I love transforming ideas into simple, meaningful tools that bridge the gap between technology and real-world problems.
