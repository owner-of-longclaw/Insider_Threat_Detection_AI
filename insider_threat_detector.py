# ============================================================
#  Insider Threat Detection — AI & Machine Learning
#  Author : Shyam Ravi
#  Model  : Isolation Forest (Unsupervised Anomaly Detection)
#  Description: Detects anomalous user behavior from
#               authentication and file access logs
# ============================================================

import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')


# ─────────────────────────────────────
#  STEP 1 — GENERATE SYNTHETIC DATA
# ─────────────────────────────────────
def generate_synthetic_logs(n_users=50, n_days=30):
    """Generate synthetic auth and file access logs for testing."""
    np.random.seed(42)
    users = [f"user_{i:03d}" for i in range(1, n_users + 1)]
    records = []

    for user in users:
        # 5% of users are simulated insider threats
        is_threat = np.random.random() < 0.05

        for day in range(n_days):
            if is_threat:
                # Insider threat behavior — abnormal patterns
                login_count         = np.random.randint(15, 40)
                failed_logins       = np.random.randint(5, 20)
                after_hours_logins  = np.random.randint(5, 15)
                sensitive_file_access = np.random.randint(20, 60)
                unique_systems      = np.random.randint(8, 20)
                avg_session_duration = np.random.uniform(180, 480)
            else:
                # Normal user behavior
                login_count         = np.random.randint(1, 10)
                failed_logins       = np.random.randint(0, 2)
                after_hours_logins  = np.random.randint(0, 2)
                sensitive_file_access = np.random.randint(0, 5)
                unique_systems      = np.random.randint(1, 4)
                avg_session_duration = np.random.uniform(20, 120)

            records.append({
                'user': user,
                'day': day,
                'login_count': login_count,
                'failed_logins': failed_logins,
                'after_hours_logins': after_hours_logins,
                'sensitive_file_access': sensitive_file_access,
                'unique_systems': unique_systems,
                'avg_session_duration': round(avg_session_duration, 2),
                'is_actual_threat': is_threat
            })

    df = pd.DataFrame(records)
    df.to_csv('data/synthetic_auth_logs.csv', index=False)
    print(f"[+] Generated {len(df)} log records for {n_users} users")
    return df


# ─────────────────────────────────────
#  STEP 2 — FEATURE ENGINEERING
# ─────────────────────────────────────
def engineer_features(df):
    """Aggregate per-user behavioral features for model input."""
    print("[*] Engineering behavioral features...")
    features = df.groupby('user').agg(
        avg_login_count         = ('login_count', 'mean'),
        avg_failed_logins       = ('failed_logins', 'mean'),
        avg_after_hours_logins  = ('after_hours_logins', 'mean'),
        avg_sensitive_access    = ('sensitive_file_access', 'mean'),
        avg_unique_systems      = ('unique_systems', 'mean'),
        avg_session_duration    = ('avg_session_duration', 'mean'),
        max_failed_logins       = ('failed_logins', 'max'),
        max_sensitive_access    = ('sensitive_file_access', 'max'),
    ).reset_index()
    return features


# ─────────────────────────────────────
#  STEP 3 — TRAIN ISOLATION FOREST
# ─────────────────────────────────────
def train_model(features_df):
    """Train Isolation Forest on behavioral features."""
    print("[*] Training Isolation Forest model...")

    feature_cols = [
        'avg_login_count', 'avg_failed_logins', 'avg_after_hours_logins',
        'avg_sensitive_access', 'avg_unique_systems', 'avg_session_duration',
        'max_failed_logins', 'max_sensitive_access'
    ]

    X = features_df[feature_cols]

    # Normalize features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Isolation Forest — contamination = expected % of anomalies
    model = IsolationForest(
        n_estimators=100,
        contamination=0.05,
        random_state=42
    )
    model.fit(X_scaled)

    # Predict: -1 = anomaly (threat), 1 = normal
    features_df['anomaly_score'] = model.decision_function(X_scaled)
    features_df['prediction'] = model.predict(X_scaled)
    features_df['is_threat'] = features_df['prediction'] == -1

    return features_df, model, scaler


# ─────────────────────────────────────
#  STEP 4 — RESULTS & REPORT
# ─────────────────────────────────────
def generate_report(features_df):
    """Print flagged users and save results."""
    flagged = features_df[features_df['is_threat']].sort_values('anomaly_score')

    print("\n" + "=" * 60)
    print("   INSIDER THREAT DETECTION REPORT — BY LONG CLAW")
    print("=" * 60)
    print(f"\n[+] Total users analyzed : {len(features_df)}")
    print(f"[+] Flagged as threats   : {len(flagged)}")
    print(f"[+] Detection rate       : {len(flagged)/len(features_df)*100:.1f}%")

    print("\n⚠️  FLAGGED USERS:")
    print("-" * 60)
    for _, row in flagged.iterrows():
        print(f"\n  User    : {row['user']}")
        print(f"  Score   : {row['anomaly_score']:.4f} (lower = more suspicious)")
        print(f"  Avg failed logins    : {row['avg_failed_logins']:.1f}")
        print(f"  Avg after-hours      : {row['avg_after_hours_logins']:.1f}")
        print(f"  Avg sensitive access : {row['avg_sensitive_access']:.1f}")
        print(f"  Avg unique systems   : {row['avg_unique_systems']:.1f}")

    flagged.to_csv('results/flagged_users.csv', index=False)
    print("\n[+] Full results saved to results/flagged_users.csv")
    return flagged


# ─────────────────────────────────────
#  STEP 5 — VISUALIZE
# ─────────────────────────────────────
def visualize(features_df):
    """Plot anomaly scores for all users."""
    plt.figure(figsize=(12, 5))
    colors = ['red' if t else 'steelblue' for t in features_df['is_threat']]
    plt.bar(range(len(features_df)), features_df['anomaly_score'], color=colors)
    plt.axhline(y=0, color='black', linestyle='--', linewidth=0.8, label='Threshold')
    plt.xlabel('Users')
    plt.ylabel('Anomaly Score (lower = more suspicious)')
    plt.title('Insider Threat Detection — Anomaly Scores per User')
    plt.legend(['Threshold', 'Normal user', 'Flagged threat'])
    plt.tight_layout()
    plt.savefig('results/anomaly_scores.png', dpi=150)
    print("[+] Chart saved to results/anomaly_scores.png")


# ─────────────────────────────────────
#  MAIN
# ─────────────────────────────────────
if __name__ == "__main__":
    import os
    os.makedirs('data', exist_ok=True)
    os.makedirs('results', exist_ok=True)

    print("=" * 60)
    print("   Insider Threat Detection System — By LONG CLAW")
    print("=" * 60 + "\n")

    df          = generate_synthetic_logs()
    features_df = engineer_features(df)
    results, model, scaler = train_model(features_df)
    flagged     = generate_report(results)
    visualize(results)