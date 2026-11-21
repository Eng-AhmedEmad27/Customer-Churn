## 1. Data Source

- **Dataset:** Cell2Cell Telecom Churn
- **Link:** https://www.kaggle.com/datasets/jpacse/datasets-for-churn-telecom
- **File used:** `cell2celltrain.csv` (51,047 rows × 58 columns)
- **File NOT used:** `cell2cellholdout.csv`. Its `Churn` column is empty (no labels), so it cannot be used for training or evaluation. It must not be concatenated with the train file.
- **Task:** Binary classification. Predict whether a customer will churn (1) or stay (0).

## 2. Data Cleaning (Stage 1)

Script: `cleandata.py` | Output: `cleaned_data.csv` (51,047 rows × 56 columns)

| # | What we did | Why |
|---|---|---|
| 1 | Dropped `CustomerID` | It is only an identifier, not a useful feature |
| 2 | Converted `Churn` from Yes/No to 1/0 | Models need a numeric target |
| 3 | Checked for duplicate rows | Found 0 duplicates, so nothing was removed |
| 4 | Converted negative values in `MonthlyRevenue` and `TotalRecurringCharge` to NaN | Money amounts cannot be negative, so these are data errors |
| 5 | Converted zeros in `AgeHH1` and `AgeHH2` to NaN | A household age of 0 is impossible. Zero means "unknown" (13,917 zeros in AgeHH1 and 26,087 in AgeHH2). After this, about 29% of AgeHH1 and 53% of AgeHH2 are missing |
| 6 | Converted `HandsetPrice` from text to number, with "Unknown" as NaN | The column was stored as text, so it could not be used numerically |
| 7 | Converted `CreditRating` to a number from 1 to 7 | Values like "1-Highest" and "7-Lowest" are ordered, so the leading digit keeps the order |
| 8 | Kept "Unknown" as its own category in `Homeownership` and `MaritalStatus` | They are categorical, and "unknown" may itself carry information |
| 9 | **Dropped `ServiceArea`** | It has 747 unique values. One-hot encoding would create 747 new columns, which would slow every model and GridSearchCV heavily |

## 3. State of the Data After Stage 1

- **Shape:** 51,047 rows × 56 columns (55 features + the `Churn` target)
- **Class balance:** about 71.2% stayed (0) and 28.8% churned (1), so the classes are imbalanced
- **Still missing on purpose:** missing values, outliers, text columns, and different scales are still in the data

## 4. What Is NOT Done Yet (Stage 2)

These steps are intentionally left for after the train/test split. If they were applied to the whole dataset first, information from the test set would leak into training (data leakage):

1. Train/test split (with `stratify=y`)
2. Imputation of missing values
3. Outlier handling
4. Encoding of categorical columns
5. Scaling
6. Balancing the classes with SMOTE (on the train set only)