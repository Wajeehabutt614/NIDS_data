# Comprehensive Implementation Plan: NIDS Machine Learning Cases

This document serves as a unified implementation blueprint summarizing all the experimental cases and pipeline architectures developed thus far for the Network Intrusion Detection System (NIDS) project. It spans from initial data ingestion and high-velocity baseline modeling to advanced ensemble stacking architectures.

---

## 1. Case 1: High-Velocity Analytical Engine Architecture
**Target:** Establish a baseline analytical engine on the CIC-IDS-2017 dataset.
*   **Data Nebula:** 2.8 Million data points.
*   **Preprocessing Pipeline:** 
    *   K-Means based imputation for missing values.
    *   Feature Distillation: Reducing dimensionality from 79 to 66 features across 12 behavioral archetypes.
    *   Target Imbalance Neutralization.
*   **Algorithmic Propulsion (Dual-Vector):**
    *   **Support Vector Machine (RBF Kernel):** Deep non-linear boundary extraction.
    *   **LinearSVC:** High-speed linear projection for extreme execution efficiency.
*   **Output:** Correlation maps, terminal synthesis, and baseline detection results.

---

## 2. Preprocessing & Data Harmonization (Cases 2 & 3 equivalent)
**Target:** Construct a robust, memory-efficient Python preprocessing pipeline for the massive CIC-IDS-2018 dataset.
*   **Minority Hunter Strategy:** Aggressively prioritize the retention of minority attack samples while proportionally subsampling overwhelming Benign traffic to prevent memory overflow and model bias.
*   **Data Cleansing:** 
    *   Rigorous string/numeric type conversions.
    *   Median-based Imputation for robustness against outliers.
    *   Variance-based Feature Selection with safety fallbacks.
    *   Multi-stage Data Normalization.
*   **Output Synthesis:** Generation of `Global_Pool_Subsampled_Train.csv`, `Balanced`, and `Unbalanced` tracking variants.

---

## 3. Case 4: Global Pool Evaluation & Ensemble Architecture
**Target:** Global Pool Evaluation, Ensemble Architecture & ADASYN Harmonization.
*   **Focus:** Evaluating the harmonized global training pool and leveraging ADASYN for synthetic oversampling. 
*   **Objective:** Setting up the baseline ensemble structures and validating the global pool's integrity before feeding it into advanced boosting and stacking architectures.

---

## 4. Case 5: Single-Node Boosting Pipeline Architecture
**Target:** A comparative stress test of five distinct gradient boosting methodologies against a Naive Baseline.
*   **Ingestion:** Unified 70/30 train/test split on the downsampled global pool. All boosting algorithms measure against an identical cross-section.
*   **Algorithm Implementations:**
    1.  **Baseline Naive LightGBM:** Null-hypothesis validation (unmodified parameters).
    2.  **XGBoost:** Dynamic `scale_pos_weight` and class weight matrices.
    3.  **LightGBM:** Native `is_unbalance=True` mapping and tight child sampling to catch minority attacks.
    4.  **CatBoost:** Algorithmic `auto_class_weights='Balanced'` optimization.
    5.  **AdaBoost via SMOTE:** Generative Synthesis modifying the physical matrix shape.
    6.  **HistGradientBoosting:** High-velocity explicit target weight matrices.
*   **Evaluation:** Strict benchmarking comparing Accuracy, Precision, Recall, Weighted F1, Macro F1, and MCC. Special focus on extracting recall rates for critical minority infiltrations (e.g., Infiltration, Heartbleed).

---

## 5. Case 6: Advanced Stacking Architectures
**Target:** Rigorous evaluation of six highly distinct hierarchical classification architectures using 5-Fold Stratified Validation to maximize attack surface detection while preventing overfitting.
*   **Architectural Configurations:**
    *   **6a (Paper Original):** Decision Tree, KNN, Random Forest -> Logistic Regression Meta-Learner.
    *   **6b (Modern Boosting Baseline):** Random Forest, XGBoost, LightGBM -> Logistic Regression Meta-Learner.
    *   **6c (Non-linear Meta-learning):** RF, XGB, LGBM -> Multi-Layer Perceptron (MLP) for extracting obscure non-linear bounds.
    *   **6d (High-Diversity Ensemble):** RF, XGB, CatBoost, LinearSVC -> LightGBM Meta-Learner.
    *   **6e (Boosting on Boosting):** RF, XGB, LGBM, AdaBoost -> XGBoost Meta-Learner.
    *   **6f (Anti-Leakage Fold Strategy):** Wrapping Base Learners inside `imblearn` Pipelines. Forces the internal StackingClassifier to apply SMOTE *strictly* within the internal $k-1$ folds during Out-Of-Fold (OOF) predictions, entirely neutralizing mathematical target leakage.
*   **Evaluation:** Comparative analysis of Fold Yields (MCC vs. Macro F1) and architectural stability testing.
