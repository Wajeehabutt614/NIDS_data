# CASE 5 Output Log

Here are the recorded outputs for each cell executed within the **Single-Node Boosting Pipeline Architecture**:

### --- Cell 1: Imports ---
```text
Imports processed successfully.
```

### --- Cell 2: Ingestion ---
```text
Data Loaded. Global Train Base Matrix Dimensions: (214694, 55)
Global Test Validation Base Matrix Dimensions: (92012, 55)
```

### --- Cell 3: Baseline Naive LightGBM ---
```text
Evaluating unmodified Naive LightGBM Baseline...
Baseline Naive LightGBM MCC Yield: 0.8932
```

### --- Cell 4: XGBoost ---
```text
1. BEFORE XGBOOST INTERVENTION - Training Shape: (214694, 55) | Training Targets: (214694,)
2. AFTER XGBOOST INTERVENTION - The physical matrix retains its shape: (214694, 55), however, sample_weights of dimension (214694,) mapped mathematical densities over it!
-> Exported predictions to 'results_xgboost.csv'
```

### --- Cell 5: LightGBM ---
```text
1. BEFORE LIGHTGBM INTERVENTION - Training Shape: (214694, 55) | Training Targets: (214694,)
2. AFTER LIGHTGBM INTERVENTION - The engine altered gradient derivation rules inherently rather than restructuring the (214694, 55) frame.
-> Exported predictions to 'results_lightgbm.csv'
```

### --- Cell 6: CatBoost ---
```text
1. BEFORE CATBOOST INTERVENTION - Training Shape: (214694, 55) | Training Targets: (214694,)
2. AFTER CATBOOST INTERVENTION - Trees were grown treating minority categories effectively as if they occupied equally sized slices of (214694, 55).
-> Exported predictions to 'results_catboost.csv'
```

### --- Cell 7: AdaBoost + SMOTE ---
```text
1. BEFORE SMOTE + ADABOOST - Physical Training Shape: (214694, 55) | Training Targets: (214694,)
2. AFTER SMOTE + ADABOOST - The physical data matrix HAS GROWN! New Trained Shape: (438202, 66) | Targeting Dimensions: (438202,)
-> Exported predictions to 'results_adaboost.csv'
```

### --- Cell 8: HistGradientBoosting ---
```text
1. BEFORE HISTGRADIENT INTERVENTION - Training Shape: (214694, 55) | Training Targets: (214694,)
2. AFTER HISTGRADIENT INTERVENTION - Physical shape remained (214694, 55). Binning heuristics prioritized gradient pathways linked to minority indexes via strict vector manipulation.
-> Exported predictions to 'results_histgradient.csv'
```

### --- Cell 9: Master Evaluation ---
```text
================ COMPARATIVE METRICS ================

            Model  Accuracy  Precision    Recall  Weighted F1  Macro F1       MCC  Infiltration Recall  Heartbleed Recall
0         XGBoost  0.948518   0.960772  0.948518     0.945042  0.933564  0.945885                    0                  0
1        LightGBM  0.948409   0.960753  0.948409     0.944917  0.935503  0.945775                    0                  0
2        CatBoost  0.946442   0.959200  0.946442     0.942999  0.919469  0.943661                    0                  0
3  AdaBoost_SMOTE  0.505592   0.656707  0.505592     0.492075  0.422493  0.478346                    0                  0
4    HistGradient  0.948464   0.953370  0.948464     0.946910  0.936111  0.944850                    0                  0

🏆 WINNING TOP PERFORMER -> XGBoost
   Max MCC: 0.9459
   Infiltration Capture Rate: 0.00%
```
