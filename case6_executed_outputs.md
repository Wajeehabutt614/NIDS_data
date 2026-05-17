# CASE 6 Output Log (Optimized Fast Run)

Here are the recorded outputs for the execution of the **Advanced Stacking Architectures & Pipeline Manipulation**. Due to the infinite hang loop from unscaled vectors, this run was optimized using a 25,000-row stratified subset and `StandardScaler` to force immediate mathematical convergence.

### --- Cell 1: Imports ---
```text
Imports processed natively.
```

### --- Cell 2: Subsampled Global Pool Ingestion ---
```text
Loading heavily imbalanced Subsampled Global Pool...
[OPTIMIZATION]: Sampling 25,000 rows stratified to prevent kernel crash and bypass the 952-minute hang...
```

### --- Cell 3: Dynamic Dictionary Mapping ---
```text
[VERBOSE] We cleanly array the parameters requested for 6a through 6f.
```

### --- Cell 4: Architecture Evaluation ---
```text
[VERBOSE] Launching Stacked Evaluations...
==================================================

Processing -> 6a: Baseline (Paper Original)
   --> Yield MCC: 0.9361 | Macro F1: 0.8760 (Evaluated in 5.29 seconds)

Processing -> 6b: Modern Boosting Baseline
   --> Yield MCC: 0.9390 | Macro F1: 0.8820 (Evaluated in 5.62 seconds)

Processing -> 6c: Non-linear Meta-learning
   --> Yield MCC: 0.9275 | Macro F1: 0.8696 (Evaluated in 8.19 seconds)

Processing -> 6d: High-diversity ensemble
   --> Yield MCC: 0.5453 | Macro F1: 0.5160 (Evaluated in 101.60 seconds)

Processing -> 6e: Boosting on Boosting
   --> Yield MCC: 0.9391 | Macro F1: 0.8783 (Evaluated in 9.65 seconds)

Processing -> 6f: Internal SMOTE inside Folds
   --> Yield MCC: 0.5130 | Macro F1: 0.4788 (Evaluated in 10.41 seconds)
```

### --- Cell 5: Master Evaluation Metrics ---
```text
================ STACKING RESULTS METRICS =================

  Case                 Architecture  Macro F1  Weighted F1       MCC    Recall  Accuracy
0   6a    Baseline (Paper Original)  0.876018     0.938752  0.936064  0.940400  0.940400
1   6b     Modern Boosting Baseline  0.881959     0.941642  0.939035  0.943200  0.943200
2   6c     Non-linear Meta-learning  0.869648     0.927442  0.927495  0.931333  0.931333
3   6d      High-diversity ensemble  0.515956     0.585259  0.545259  0.570800  0.570800
4   6e         Boosting on Boosting  0.878339     0.938084  0.939101  0.942133  0.942133
5   6f  Internal SMOTE inside Folds  0.478792     0.548356  0.513024  0.539733  0.539733
```
