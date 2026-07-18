<<<<<<< HEAD
# 🔍 Insider Threat Detection — AI & Machine Learning

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python&logoColor=white)
![ML](https://img.shields.io/badge/ML-Isolation%20Forest-orange?style=flat)
![Status](https://img.shields.io/badge/Status-Ongoing-yellow?style=flat)
![Focus](https://img.shields.io/badge/Focus-Anomaly%20Detection%20%7C%20User%20Behavior-purple?style=flat)

> A machine learning pipeline that detects anomalous user behavior and flags potential insider threats by analyzing authentication logs and file access activity using Isolation Forest anomaly detection.
=======
# 🎣 Phishing Detection — NLP & Machine Learning

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python&logoColor=white)
![ML](https://img.shields.io/badge/ML-Logistic%20Regression-orange?style=flat)
![NLP](https://img.shields.io/badge/NLP-TF--IDF%20%7C%20NLTK-green?style=flat)
![Status](https://img.shields.io/badge/Status-Paused-brightgreen?style=flat)

> A machine learning system that detects phishing messages using Natural Language Processing — classifying text as spam or legitimate using TF-IDF vectorization and Logistic Regression.
>>>>>>> 955ded2a1e9fc43da3db7e4cd4ba8e405348ef56

---

## 📌 Objective

<<<<<<< HEAD
Build an AI-powered insider threat detection system that monitors user behavior patterns across authentication and file access logs, identifies statistical anomalies, and flags suspicious activity that deviates from normal baselines — helping SOC analysts detect malicious insiders early.
=======
Build a phishing detection pipeline that preprocesses raw text messages, extracts meaningful features using NLP techniques, and classifies them as phishing or legitimate using a trained machine learning model.
>>>>>>> 955ded2a1e9fc43da3db7e4cd4ba8e405348ef56

---

## 🧠 How It Works

```
<<<<<<< HEAD
Raw Logs (Auth + File Access)
          │
          ▼
Data Preprocessing
 - Normalize timestamps
 - Encode categorical fields
 - Engineer behavioral features
          │
          ▼
Feature Engineering
 - Login frequency per user
 - After-hours activity score
 - Failed login count
 - Sensitive file access count
 - Unique systems accessed
          │
          ▼
Isolation Forest Model
 - Unsupervised anomaly detection
 - No labeled data needed
 - Assigns anomaly score per user
          │
          ▼
Threat Flagging
 - Anomaly score threshold
 - High-risk users flagged
 - Report generated
```

---

## 🏗️ Project Structure

```
Insider-Threat-Detection-AI/
│
├── README.md
├── insider_threat_detector.py    ← main detection script
├── preprocess.py                 ← data preprocessing
├── requirements.txt              ← dependencies
│
├── data/
│   ├── synthetic_auth_logs.csv   ← synthetic authentication logs
│   └── synthetic_file_logs.csv   ← synthetic file access logs
│
├── model/
│   └── model_notes.md            ← model details
│
└── results/
    └── flagged_users.csv         ← detection output
```

---

## ⚙️ Installation & Usage

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/Insider-Threat-Detection-AI.git
cd Insider-Threat-Detection-AI
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the detector
```bash
python insider_threat_detector.py
=======
Raw Text Message
      │
      ▼
Text Preprocessing (NLTK)
 - Lowercase conversion
 - Remove punctuation & stopwords
 - Tokenization & stemming
      │
      ▼
Feature Extraction (TF-IDF)
 - Converts text to numerical vectors
 - Weights rare but important words higher
      │
      ▼
Rule-Based Keyword Filter
 - Flags known phishing keywords
 - (e.g. "verify account", "click here", "urgent")
      │
      ▼
Logistic Regression Model (scikit-learn)
 - Trained on labeled spam/ham dataset
 - Predicts: Phishing ⚠️ or Legitimate ✅
      │
      ▼
Classification Result
>>>>>>> 955ded2a1e9fc43da3db7e4cd4ba8e405348ef56
```

---

## 🛠️ Tech Stack

| Component | Tool / Library |
|---|---|
| Language | Python 3.x |
<<<<<<< HEAD
| ML Model | Isolation Forest (scikit-learn) |
| Data Handling | Pandas, NumPy |
| Visualization | Matplotlib |
| Log Sources | Authentication logs, File access logs |

---

## 🔍 Features Analyzed

| Feature | Description |
|---|---|
| `login_count` | Total logins per user per day |
| `failed_logins` | Number of failed authentication attempts |
| `after_hours_logins` | Logins outside 9AM–6PM window |
| `sensitive_file_access` | Access to restricted/sensitive files |
| `unique_systems` | Number of unique systems accessed |
| `avg_session_duration` | Average session length in minutes |

---

## 🗺️ MITRE ATT&CK Mapping

| Behavior Detected | Tactic | Technique |
|---|---|---|
| Excessive failed logins | Credential Access | T1110 — Brute Force |
| After-hours access | Discovery | T1083 — File & Directory Discovery |
| Mass file access | Exfiltration | T1005 — Data from Local System |
| Lateral movement | Lateral Movement | T1021 — Remote Services |
=======
| Text Preprocessing | NLTK |
| Data Handling | Pandas |
| Feature Extraction | TF-IDF (scikit-learn) |
| ML Model | Logistic Regression (scikit-learn) |
| Keyword Analysis | Rule-based (custom) |

---

## 📁 Project Structure

```
Phishing-Detection-NLP/
│
├── README.md
├── phishing_detector.py       ← main detection script
├── train_model.py             ← model training script
├── requirements.txt           ← dependencies
│
├── data/
│   └── dataset.csv            ← labeled spam/ham dataset
│
├── model/
│   └── model_notes.md         ← model details & observations
│
└── results/
    └── results_notes.md       ← sample outputs & findings
```

---

## ⚙️ Installation & Usage

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/Phishing-Detection-NLP.git
cd Phishing-Detection-NLP
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the detector
```bash
python phishing_detector.py
```

---

## 🔍 Key Features

- Text cleaned and normalized using NLTK pipelines
- TF-IDF vectorization to capture word importance across messages
- Rule-based keyword filter as a first-pass detection layer
- Logistic Regression model trained on real spam/ham dataset
- Easy to extend with new keywords or swap in a different ML model

---

## 🗺️ MITRE ATT&CK Relevance

| Technique | ID |
|---|---|
| Phishing | T1566 |
| Phishing via email attachment | T1566.001 |
| Phishing via spearphishing link | T1566.002 |
>>>>>>> 955ded2a1e9fc43da3db7e4cd4ba8e405348ef56

---

## 📚 Key Learnings

<<<<<<< HEAD
- Understood how Isolation Forest detects outliers without labeled training data
- Learned how to engineer behavioral features from raw log data
- Gained experience building an end-to-end ML pipeline for security use cases
- Practiced generating and working with synthetic security datasets
=======
- Understood how TF-IDF captures meaningful patterns in text vs simple word counts
- Learned how stopword removal and stemming improve model accuracy
- Gained experience combining rule-based and ML approaches for better detection
- Practiced evaluating model performance using precision, recall, and F1-score
>>>>>>> 955ded2a1e9fc43da3db7e4cd4ba8e405348ef56

---

## 🔮 Future Improvements

<<<<<<< HEAD
- [ ] Add UEBA (User and Entity Behavior Analytics) scoring
- [ ] Integrate with Splunk for real-time detection
- [ ] Add email alerting for flagged users
- [ ] Train on CERT Insider Threat Dataset
- [ ] Build a simple dashboard for visualizing anomalies
=======
- [ ] Upgrade to a transformer-based model (BERT / RoBERTa)
- [ ] Add URL analysis for embedded phishing links
- [ ] Build a simple web interface for real-time detection
- [ ] Train on a larger, more diverse dataset
- [ ] Add multilingual phishing detection
>>>>>>> 955ded2a1e9fc43da3db7e4cd4ba8e405348ef56

---

## 🛠️ Tools & Technologies

<<<<<<< HEAD
`Python` `scikit-learn` `Isolation Forest` `Pandas` `NumPy` `Matplotlib` `UEBA`
=======
`Python` `NLTK` `Pandas` `scikit-learn` `TF-IDF` `Logistic Regression` `NLP`
>>>>>>> 955ded2a1e9fc43da3db7e4cd4ba8e405348ef56

---

## 👤 Author

<<<<<<< HEAD
**Shyam Ravi**
=======
**AK**
>>>>>>> 955ded2a1e9fc43da3db7e4cd4ba8e405348ef56
CEH | SOC Aspirant | Splunk SIEM
[LinkedIn](https://linkedin.com/in/) • [GitHub](https://github.com/)

---

<<<<<<< HEAD
> ⚠️ This project uses synthetic data generated for educational purposes. No real user data is used.
=======
> ⚠️ This project is built for educational and research purposes in cybersecurity threat detection.
>>>>>>> 955ded2a1e9fc43da3db7e4cd4ba8e405348ef56
