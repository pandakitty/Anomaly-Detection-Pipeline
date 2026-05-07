import numpy as np

class SurgicalAnomalyDetector:
    """
    Surgical removal of noise using Z-Score logic.
    Categorized by 'System Role': This engine defines entity capacity vs efficiency.
    """
    def __init__(self, threshold=3.0):
        self.threshold = threshold

    def detect(self, data):
        # Calculate State Data (Point-in-Time Snapshot)
        mean = np.mean(data)
        std = np.std(data)
        
        # Identify Activity Data (Deviations from the mean)
        z_scores = [(x - mean) / std for x in data]
        
        # Filter anomalies (The Logical Gate)
        anomalies = [data[i] for i, z in enumerate(z_scores) if np.abs(z) > self.threshold]
        clean_data = [data[i] for i, z in enumerate(z_scores) if np.abs(z) <= self.threshold]
        
        return clean_data, anomalies

# # Professional Thought Process:
# # Logic for 'Noise' vs 'Signal':
# # Anomaly = Liability (future cost). Clean Data = Asset (future value).
