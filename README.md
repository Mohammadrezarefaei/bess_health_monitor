# 🔋 BESS Degradation & Health Monitor

An industrial-grade asset health, degradation risk modeling, and operational optimization platform tailored for Battery Energy Storage Systems (BESS) in European power markets (such as Germany's day-ahead and aFRR ancillary services).

[![BESS CI Pipeline](https://github.com/Mohammadrezarefaei/bess_health_monitor/actions/workflows/pipeline.yml/badge.svg)](https://github.com/Mohammadrezarefaei/bess_health_monitor/actions)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://besshealthmonitor-ik9lk8vav8pagvtsqgmm8x.streamlit.app/)
[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 🎯 Overview

As the European energy transition accelerates, utility-scale Battery Energy Storage Systems (BESS) are critical for grid stabilization and arbitrage. However, aggressive cycling (e.g., participating in high-frequency ancillary markets like **aFRR**) accelerates cell degradation, impacting the total cost of ownership (TCO).

**BESS Degradation & Health Monitor** bridges the gap between **economic revenue optimization** and **physical asset longevity** by quantifying real-time degradation costs, thermal stress, and capacity fade.

---

## 🚀 Key Features

* **Physics-Informed Degradation Modeling:** Calculates real-time capacity fade and aging costs based on depth of discharge (DoD), energy throughput, and Arrhenius-based cell temperature stress factors.
* **Machine Learning Integration (XGBoost):** Predicts degradation risk and degradation cost profiles under variable load and thermal regimes.
* **Interactive Streamlit Dashboard:** Allows grid operators and analysts to simulate custom C-rates, ambient thermal profiles, and daily cycling intensity to evaluate asset lifetime impacts.
* **Rigorous CI/CD Pipeline:** Fully automated unit tests using `pytest` and GitHub Actions ensuring code reliability and enterprise-grade software standards.

---

## 📊 Live Dashboard Preview

Access the live application deployed on Streamlit Cloud:  
👉 **[BESS Degradation & Health Monitor Live App](https://besshealthmonitor-ik9lk8vav8pagvtsqgmm8x.streamlit.app/)**

---

## 🏗️ Repository Structure

```text
bess_health_monitor/
├── .github/
│   └── workflows/
│       └── pipeline.yml       # CI/CD automated testing pipeline
├── models/
│   └── degradation_xgb_model.json # Trained XGBoost configuration & metadata
├── tests/
│   ├── __init__.py
│   └── test_degradation.py    # Unit tests for core degradation logic
├── app.py                     # Interactive Streamlit dashboard UI
├── pipeline.py                # Core mathematical & ML processing pipeline
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
