from dataclasses import dataclass

@dataclass
class Decision:
    incident_type: str
    likely_cause: str
    action: str
    confidence: str

def decide(cpu_pct: float, mem_pct: float, latency_ms: float, error_rate: float) -> Decision:
    # Explainable rules (easy to defend in your video)

    if error_rate >= 10 and latency_ms >= 200:
        return Decision(
            incident_type="ERROR_BURST",
            likely_cause="Downstream dependency failure or misconfiguration causing elevated errors and retries.",
            action="Rollback recent config (simulated); restart service; notify on-call.",
            confidence="High"
        )

    if cpu_pct >= 85 and latency_ms >= 250:
        return Decision(
            incident_type="CPU_SATURATION",
            likely_cause="CPU saturation leading to request queuing and increased response latency.",
            action="Scale up replicas by +1 (simulated) and restart the hottest process.",
            confidence="High"
        )

    if mem_pct >= 88 and latency_ms >= 220:
        return Decision(
            incident_type="MEMORY_PRESSURE",
            likely_cause="Memory pressure/leak causing GC thrash or swapping, increasing latency.",
            action="Restart service to clear memory; schedule memory profiling follow-up.",
            confidence="Medium"
        )

    if latency_ms >= 300 and error_rate <= 2:
        return Decision(
            incident_type="LATENCY_SPIKE",
            likely_cause="Performance regression or noisy neighbor; latency high but errors low.",
            action="Run health check; shift traffic to healthy instance (simulated).",
            confidence="Medium"
        )

    return Decision(
        incident_type="UNKNOWN",
        likely_cause="No clear single-cause signal from current metrics.",
        action="Collect more telemetry; notify on-call with snapshot.",
        confidence="Low"
    )
