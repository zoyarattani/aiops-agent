import pandas as pd
from sklearn.ensemble import IsolationForest

FEATURES = ["cpu_pct", "mem_pct", "latency_ms", "error_rate"]

def load_metrics(path="data/metrics.csv"):
    return pd.read_csv(path)

def train_model(df):
    model = IsolationForest(
        n_estimators=200,
        contamination=0.08,
        random_state=42
    )
    model.fit(df[FEATURES])
    return model

def detect_anomalies(model, df):
    result = df.copy()
    result["is_anomaly"] = model.predict(df[FEATURES]) == -1
    result["anomaly_score"] = model.decision_function(df[FEATURES])
    return result
