# 005 — Machine Learning Results

## Dataset

- Dataset: Fitbit Fitness Tracker
- Target: `target_calories_next_day`
- Temporal split: 80/20
- Split date: 2016-05-07
- Train: 555 rows
- Test: 125 rows

## Complete Experiment Comparison

| Model                            |     MAE |    RMSE |      R2 |
|:---------------------------------|--------:|--------:|--------:|
| Decision Tree — Base             | 496.213 | 719.382 |  0.2924 |
| Linear Regression — Base         | 496.038 | 738.598 |  0.2541 |
| Random Forest — All Features     | 481.733 | 740.433 |  0.2504 |
| User Mean                        | 486.791 | 753.181 |  0.2244 |
| Linear Regression — All Features | 485.049 | 754.326 |  0.222  |
| 7-Day Mean                       | 479.967 | 757.968 |  0.2145 |
| Linear Regression — Rolling      | 492.457 | 758.82  |  0.2127 |
| Linear Regression — Lag          | 503.125 | 760.236 |  0.2098 |
| Decision Tree — Lag              | 566.133 | 784.008 |  0.1596 |
| Decision Tree — Rolling          | 517.99  | 787.838 |  0.1513 |
| Decision Tree — All Features     | 533.494 | 789.161 |  0.1485 |
| Previous Day                     | 542.432 | 803.879 |  0.1164 |
| Global Mean                      | 732.112 | 898.733 | -0.1044 |

## Main observations

- Best R²: Decision Tree — Base (0.2924)
- Best RMSE: Decision Tree — Base (719.38)
- Best MAE: 7-Day Mean (479.97)
- Random Forest — All Features: MAE 481.73, R² 0.2504
- Temporal lag/rolling features did not improve the main models.
- User Mean was a strong baseline (R² 0.2244).
