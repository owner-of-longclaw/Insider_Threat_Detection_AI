# 🔍 Insider Threat Detection — AI & Machine Learning

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python&logoColor=white)
![ML](https://img.shields.io/badge/ML-Isolation%20Forest-orange?style=flat)
![Status](https://img.shields.io/badge/Status-Ongoing-yellow?style=flat)
![Focus](https://img.shields.io/badge/Focus-Anomaly%20Detection%20%7C%20User%20Behavior-purple?style=flat)

> A machine learning pipeline that detects anomalous user behavior and flags potential insider threats by analyzing authentication logs and file access activity using Isolation Forest anomaly detection.

---

## 📌 Objective

Build an AI-powered insider threat detection system that monitors user behavior patterns across authentication and file access logs, identifies statistical anomalies, and flags suspicious activity that deviates from normal baselines — helping SOC analysts detect malicious insiders early.

---

## 🧠 How It Works

```
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
```

---

## 🛠️ Tech Stack

| Component | Tool / Library |
|---|---|
| Language | Python 3.x |
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

---

## 📚 Key Learnings

- Understood how Isolation Forest detects outliers without labeled training data
- Learned how to engineer behavioral features from raw log data
- Gained experience building an end-to-end ML pipeline for security use cases
- Practiced generating and working with synthetic security datasets

---

## 🔮 Future Improvements

- [ ] Add UEBA (User and Entity Behavior Analytics) scoring
- [ ] Integrate with Splunk for real-time detection
- [ ] Add email alerting for flagged users
- [ ] Train on CERT Insider Threat Dataset
- [ ] Build a simple dashboard for visualizing anomalies

---

## 🛠️ Tools & Technologies

`Python` `scikit-learn` `Isolation Forest` `Pandas` `NumPy` `Matplotlib` `UEBA`

---

## 👤 Author

**Shyam Ravi**
CEH | SOC Aspirant | Splunk SIEM
[LinkedIn](https://linkedin.com/in/) • [GitHub](https://github.com/)

---

> ⚠️ This project uses synthetic data generated for educational purposes. No real user data is used.