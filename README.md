# Anomaly Detection Pipeline: Surgical Signal Remediation
**Architect:** [Ashley Love](https://github.com/pandakitty)

A high-fidelity Python pipeline for identifying and purging noise from institutional datasets. This project demonstrates the application of Z-Score statistical thresholds to separate "State Data" (Assets) from "Activity Anomalies" (Liabilities).

## 🛠 Features
- **Surgical Logic:** Uses standard deviation-based gates to isolate outliers with 99.7% statistical precision.
- **Remediation Strategy:** Automatically classifies and removes data points that threaten model integrity, consistent with the [Diabetes Clinical Remediation Pipeline](https://github.com/pandakitty/Diabetes_Clinical_Remediation_Pipeline) standards.
- **Lean Architecture:** Built with NumPy for high-performance processing of large-scale time-series data.

## 🚀 Usage
1. `pip install numpy`
2. `python3 generator.py`# Anomaly-Detection-Pipeline
