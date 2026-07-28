# 🛡️ Network Intrusion Detection System (NIDS) using Machine Learning

An advanced, machine learning-driven Network Intrusion Detection System (NIDS) designed to classify malicious network traffic and prevent cyberattacks in real time. This project evaluates, optimizes, and deploys high-performance ensemble models—including **XGBoost**, **CatBoost**, and **Stacking Classifiers**—to achieve high detection accuracy while minimizing false alarm rates.

---

## 📌 Features

- **Multi-Class & Binary Classification:** Detects both binary threats (Normal vs. Attack) and multi-class intrusion types (e.g., DoS, Probe, R2L, U2R).
- **Data Preprocessing & Downsampling:** Implements structured feature engineering, categorical encoding, feature scaling, and class-imbalance downsampling/SMOTE techniques.
- **Advanced Ensemble Architectures:** Evaluates single gradient boosted models against Meta-Stacking Classifiers to boost precision and recall metrics.
- **Model Interpretability:** Analyzes feature importance to identify key network packet indicators driving threat classifications.

---

## 🛠️ Tech Stack & Dependencies

- **Language:** Python 3.8+
- **Machine Learning & Analytics:** Scikit-learn, XGBoost, CatBoost, Pandas, NumPy
- **Data Visualization:** Matplotlib, Seaborn
- **Model Serialization:** Joblib / Pickle

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone [https://github.com/Wajeehabutt614/Network-Intrusion-Detection-System.git](https://github.com/Wajeehabutt614/Network-Intrusion-Detection-System.git)
cd Network-Intrusion-Detection-System
