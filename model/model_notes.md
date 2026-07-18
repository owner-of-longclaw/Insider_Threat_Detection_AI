# Model Notes

## Algorithm
Isolation Forest (scikit-learn)

## Why Isolation Forest?
- Unsupervised — no labeled insider threat data needed
- Works well on tabular behavioral data
- Fast and lightweight
- Industry-used for anomaly detection in UEBA systems

## Features Used
- avg_login_count — average daily logins
- avg_failed_logins — average failed authentication attempts
- avg_after_hours_logins — logins outside business hours
- avg_sensitive_access — average sensitive file access count
- avg_unique_systems — number of unique systems accessed
- avg_session_duration — average session length in minutes
- max_failed_logins — peak failed logins in a single day
- max_sensitive_access — peak sensitive file access in a day

## Hyperparameters
- n_estimators: 100
- contamination: 0.05 (expects ~5% anomalies)
- random_state: 42

## Dataset
Synthetic data generated using NumPy random distributions
- 50 users, 30 days each = 1500 records
- ~5% simulated insider threats with abnormal behavior patterns

## Future Improvements
- Train on CERT Insider Threat Dataset (real-world)
- Add LSTM for time-series behavior modeling
- Integrate with Splunk for real-time scoring