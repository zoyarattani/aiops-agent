from anomaly_detector import load_metrics, train_model, detect_anomalies
from decision_engine import decide
from remediation import perform

def main():
    df = load_metrics("data/metrics.csv")

    model = train_model(df)
    scored = detect_anomalies(model, df)

    anomalies = scored[scored["is_anomaly"]].copy()
    print("\n=== AIOps Agent Run ===")
    print("Total rows:", len(scored))
    print("Anomalies detected:", len(anomalies), "\n")

    # Show the most anomalous points (lowest score)
    anomalies = anomalies.sort_values("anomaly_score").head(12)

    for _, row in anomalies.iterrows():
        t = int(row["t"])
        cpu = float(row["cpu_pct"])
        mem = float(row["mem_pct"])
        lat = float(row["latency_ms"])
        err = float(row["error_rate"])

        d = decide(cpu, mem, lat, err)

        print(f"t={t} | cpu={cpu:.1f}% mem={mem:.1f}% latency={lat:.1f}ms errors={err:.1f}")
        print(f"  -> incident_type: {d.incident_type}")
        print(f"  -> likely_cause : {d.likely_cause}")
        print(f"  -> action       : {d.action}")
        print(f"  -> confidence   : {d.confidence}")

        # Autonomous behavior: perform action for medium/high confidence cases
        if d.confidence in ("High", "Medium") and d.incident_type != "UNKNOWN":
            perform(d.action)

        print("")

    scored.to_csv("aiops_report.csv", index=False)
    print("Wrote aiops_report.csv")

if __name__ == "__main__":
    main()
