import numpy as np
import pandas as pd

def main():
    rng = np.random.default_rng(42)
    n = 400

    cpu = rng.normal(35, 8, n).clip(0, 100)
    memory = rng.normal(45, 10, n).clip(0, 100)
    latency_ms = rng.normal(120, 25, n).clip(1, None)
    error_rate = rng.poisson(1, n).astype(float)

    cpu[120:150] = rng.normal(92, 4, 30).clip(0, 100)
    latency_ms[120:150] = rng.normal(420, 60, 30).clip(1, None)
    error_rate[120:150] = rng.poisson(6, 30)

    memory[250:280] = rng.normal(93, 3, 30).clip(0, 100)
    latency_ms[250:280] = rng.normal(300, 50, 30).clip(1, None)
    error_rate[250:280] = rng.poisson(3, 30)

    error_rate[330:350] = rng.poisson(15, 20)
    latency_ms[330:350] = rng.normal(260, 40, 20).clip(1, None)

    df = pd.DataFrame({
        "t": np.arange(n),
        "cpu_pct": cpu.round(2),
        "mem_pct": memory.round(2),
        "latency_ms": latency_ms.round(2),
        "error_rate": error_rate.round(2),
    })

    df.to_csv("data/metrics.csv", index=False)
    print("Wrote data/metrics.csv")

if __name__ == "__main__":
    main()
