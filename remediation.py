from datetime import datetime

def perform(action: str) -> None:
    ts = datetime.now().isoformat(timespec="seconds")
    print(f"[{ts}] REMEDIATION: {action}")
