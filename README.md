# AI-Driven AIOps Agent (Anomaly Detection + Auto-Remediation)

## Overview
This project is a lightweight AI-driven AIOps agent prototype that monitors operational telemetry (system metrics), detects anomalous behavior using machine learning, diagnoses likely incident causes using explainable decision logic, and triggers automated remediation actions (simulated).

The goal is to demonstrate AI-driven thinking in IT operations through a simple “observe → decide → act” loop.

## What it does
- Ingests telemetry from `data/metrics.csv` (CPU, memory, latency, error rate)
- Detects anomalies using an unsupervised ML model (Isolation Forest)
- Classifies incidents (CPU saturation, memory pressure, error bursts, latency spikes)
- Produces an action recommendation and automatically executes it (simulated)
- Generates `aiops_report.csv` as a run artifact

## Architecture
**Telemetry → ML anomaly detection → diagnosis → remediation**

1. Ingestion: load metrics from CSV
2. Detection (AI/ML): Isolation Forest flags anomalous states using multivariate patterns
3. Decision logic: rules map metric snapshots to an incident type + likely cause + action
4. Automation: remediation actions are executed (simulated) and logged

## AI techniques used
- Isolation Forest (unsupervised anomaly detection):
  - Learns “normal” operational patterns without labeled incident data
  - Flags unusual combinations of CPU/memory/latency/error rate
- **Explainable decision engine**:
  - Human-readable rules translate anomalies into incident types
  - Produces a clear rationale + action (easy to audit/explain)

## How the agent makes decisions
1. The model flags a telemetry point as anomalous.
2. The decision engine evaluates that point:
   - High CPU + high latency → CPU saturation → scale up + restart
   - High memory + elevated latency → memory pressure/leak → restart + profile
   - High error rate + high latency → dependency/config issue → rollback + restart + notify
3. The remediation module logs the action taken (simulated autonomous behavior).

## Setup / Run
### Requirements
- Python 3.x
- Packages in `requirements.txt`

### Install
```bash
py -m pip install -r requirements.txt

## Outputs
- Console output showing detected anomalies, diagnoses, and remediation steps
- aiops_report.csv containing anomaly flags and scores

## Assumptions
- Telemetry is simulated for demonstration (no real cloud/Kubernetes integration)
- Remediation actions are simulated (printed) rather than calling real APIs
- Single-service view without dependency topology graph

## Future improvements
- Real-time ingestion (Prometheus/log pipeline) instead of CSV
- Multi-service dependency graph for better localization/root cause analysis
- Feedback loop: incorporate incident confirmations to tune thresholds or train supervised models
- Integrate real actions (Kubernetes scaling, service restart, config rollback APIs)

Demo Video
Video walkthrough of the AIOps agent: https://share.vidyard.com/watch/hA1FSFFZp5uzwMbuaCCzw1

