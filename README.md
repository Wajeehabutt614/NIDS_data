# Sentinel AI: Network Threat Detection System with Adaptive Learning

A comparative study of ensemble machine learning models for network intrusion detection, evaluated across six systematically designed experimental cases on the CICIDS-2017 and CICIDS-2018 benchmark datasets.

## Overview

Sentinel AI investigates a core methodological problem in ML-based network intrusion detection (NIDS): **class imbalance handling matters more than the choice of classification algorithm.** Standard models can exceed 99% accuracy while completely failing to detect rare, high-impact attack classes — a phenomenon known as the accuracy paradox.

This project systematically classifies 12+ zero-day network attacks using ensemble learning, benchmarking stacking, boosting, and bagging architectures under multiple imbalance-handling strategies, and evaluates generalization across two distinct network environments (2017 and 2018 traffic).

## Problem Statement

Three issues limit the real-world efficacy of deployed ML-based NIDS:

1. **Class imbalance** — a classifier predicting "benign" for every sample can be 83%+ accurate while detecting zero attacks. This accuracy paradox is well known but underrepresented in comparative studies.
2. **Lack of cross-dataset testing** — most IDS research trains and tests on the same dataset, offering no insight into generalization across different network environments or attack patterns.
3. **Under-studied feature selection in ensembles** — techniques like variance thresholding, correlation filtering, mutual information, Random Forest importance, and SHAP values select very different feature subsets, with under-explored impacts on ensemble performance.

## Datasets

- **CICIDS-2017** and **CICIDS-2018** — benchmark network intrusion detection datasets, pooled and evaluated both independently and jointly to test cross-dataset generalization.
- Preprocessed dataset size: 756,208 instances.
- Feature reduction: Variance Threshold removed 12 near-zero-variance columns (from 79 to 66 features) before further SHAP-based selection.

## Methodology

A quantitative, controlled experimental design across **six cases**, each isolating one variable (imbalance handling method, ensemble architecture, feature selection, or dataset composition) while holding all others constant — enabling direct causal attribution of performance changes.

Metrics tracked across all cases: **F1-Macro, F1-Weighted, Accuracy, Precision, Recall, and MCC** (Matthews Correlation Coefficient), evaluated with 5-fold cross-validation.

Tools: Python 3.x, scikit-learn, imbalanced-learn, XGBoost, LightGBM, CatBoost, SHAP. All experiments use a fixed random seed (42) for reproducibility.

### Experimental Cases

| Case | Focus | Key Result |
|------|-------|------------|
| 1 | Baseline (no imbalance handling) | Decision Tree best baseline at 81.94% F1-Macro; all models showed the accuracy paradox (99%+ accuracy, F1-Macro as low as 10.19%) |
| 2 | Cross-dataset generalization | F1-Macro dropped from 26–82% (single dataset) to 7–26% (pooled 2017+2018) — exposing distribution shift vulnerability |
| 3 | Gradient boosting pipeline (native imbalance handling) | HistGradientBoosting, LightGBM, XGBoost, CatBoost achieved 91.95–93.61% F1-Macro |
| 4 | Stacking ensemble architectures | Best: RF + XGBoost + LightGBM base learners with Logistic Regression meta-learner — 93.35% F1-Macro |
| 5 | Bagging methods | Tuned Bagging Classifier (Decision Tree base learners) outperformed aggressive undersampling (EasyEnsemble, RUSBoost) — 82.16% F1-Macro, MCC 0.9958 |
| 6 | SHAP-based feature selection | Top-30 features improved F1-Macro by 22 points and cut dimensionality by 45%, with zero performance loss |

## Key Findings

- **Class imbalance handling has more impact on performance than the choice of classification algorithm.**
- **Cross-dataset testing is essential** — same-distribution test splits significantly overestimate real-world performance.
- **SMOTE-based synthetic oversampling is incompatible with gradient boosting dynamics** — native imbalance handling (e.g. `is_unbalance=True`, class weighting) outperforms generative oversampling for boosting models.
- **Strict anti-leakage cross-validation is critical** — applying SMOTE within folds (rather than before splitting) prevents inflated, unrealistic performance estimates. A naive approach scored 93.35% F1-Macro; the leak-proof version dropped to 67.12%, revealing the true, honest performance.
- **SHAP-based feature selection at 30 features** is the optimal preprocessing configuration across all model types tested.

## Best Model Recommendation

The recommended configuration for operational NIDS on CICIDS-family datasets:

**SHAP feature selection (30 features) → Gradient boosting with native imbalance handling (HistGradientBoosting or LightGBM with `is_unbalance=True`)**

This achieved a Macro F1 score above **93.5%** on the pooled 2017+2018 dataset — the strongest result across all six cases, and the most practical to implement in production.

| Configuration | F1-Macro |
|---|---|
| Baseline — Decision Tree (no imbalance handling) | 81.94% |
| Best stacking ensemble (RF + XGBoost + LightGBM → LogReg) | 93.35% |
| **Recommended — Gradient boosting pipeline (SHAP + native imbalance handling)** | **93.61%** |

## Repository Structure

```
├── CASE_1.ipynb                       # Baseline (no imbalance handling)
├── CASE_2.ipynb                       # Cross-dataset generalization
├── CASE_3_Boosting_Pipeline.ipynb     # Gradient boosting with native imbalance handling
├── CASE_4_Stacking_Ensemble.ipynb     # Stacking architecture comparison
├── CASE_5_Bagging.ipynb               # Bagging vs. undersampling methods
├── CASE_6_Feature_Selection.ipynb     # SHAP-based feature selection
├── requirements.txt                   # Python dependencies
└── README.md
```

*(Note: rename notebook files to match the descriptive names above for clarity.)*

## Tech Stack

Python · scikit-learn · imbalanced-learn · XGBoost · LightGBM · CatBoost · SHAP · pandas · numpy

## Getting Started

```bash
git clone https://github.com/Wajeehabutt614/NIDS_data.git
cd NIDS_data
pip install -r requirements.txt
```

Datasets: Download CICIDS-2017 and CICIDS-2018 from the [Canadian Institute for Cybersecurity](https://www.unb.ca/cic/datasets/index.html) and place them in a `/data` directory before running the notebooks.

## Authors

- Wajeeha Ghazal Tasneem
- Umama Fatima
- Miral Sajid

## Acknowledgments

With gratitude to our supervisor, **Dr. Syed Ali Raza**, for his invaluable guidance and mentorship throughout this research.

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
