import numpy as np
from detector import SurgicalAnomalyDetector

# 1. Generate 'Normal' signal (The Baseline Asset)
normal_data = np.random.normal(50, 5, 100).tolist()

# 2. Inject 'Noise' (The Liabilities/Anomalies)
anomalies = [150, -20, 300, 12]
messy_data = normal_data + anomalies

# 3. Run the Surgical Cleanup
detector = SurgicalAnomalyDetector(threshold=2.5)
clean, found = detector.detect(messy_data)

print(f"\n--- DATA REMEDIATION REPORT ---")
print(f"Total Points Processed: {len(messy_data)}")
print(f"Anomalies Surgically Removed: {found}")
print(f"Cleanup Status: [COMPLETE]\n")
