# AI Exposure and the Shift to Self-Employment: A Causal Analysis

This repository contains a data-driven consulting project that investigates whether technological shocks from generative AI drive workers toward self-employment. This project is built to meet the requirements of the Spring 2026 Causal Inference Final, featuring a Double Machine Learning (DML) identification strategy and a Streamlit "What-If" dashboard.

## 1. Project Overview
*   **Causal Question:** Does higher occupational AI exposure ($T$) cause a higher probability of self-employment ($Y$)? 
*   **The Business Case:** We aim to distinguish whether "AI-ready" occupations simply have a higher baseline for solo work, or if AI tools are actively lowering the barrier to entry for self-employment.

## 2. Identification Strategy: Double Machine Learning (DML)
A pure predictive approach is insufficient because it conflates inherent occupation amenability with the causal effect of AI tools. 
*   **Methodology:** We use ML nuisance models to flexibly control for high-dimensional confounders, followed by a final linear stage to estimate the causal effect with cross-fitting.
*   **Key Assumption:** **Conditional Independence.** We assume that after controlling for demographics and O*NET occupational characteristics (autonomy, independence, computer use), the residual AI exposure variation is uncorrelated with unobserved determinants of self-employment 
*   **Robustness Check:** A **Placebo Test** is conducted using a pre-ChatGPT subsample (2021–2022) to validate the causal interpretation of the recent AI shock 

## 3. Dataset & Variables
*   **Sources:** IPUMS CPS ASEC (2021–2024) integrated with Felten AIOE scores and O*NET occupational data.
*   **Sample Size:** $N > 10,000$ observations.
*   **Treatment (T):** AIOE score (continuous, 0–5.
*   **Outcome (Y):** Self-employed (binary status).
*   **Controls (X):** Age, sex, race, education, income, state, industry, and O*NET-specific job characteristics.

## 4. Repository Structure
Following the "Clean Repo" standard, the project is organized as follows:
```text
├── README.md               # Project overview and reproduction instructions
├── requirements.txt        # Python dependencies
├── streamlit_app.py        # Streamlit dashboard code
├── src/                    # .py modules for core logic
│   ├── data_cleaning.py    # SOC crosswalk and data merging
│   └── dml_engine.py       # DML implementation
├── notebooks/
│   └── checkpoint.ipynb    # Proposal, EDA, and preliminary analysis
└── deliverables/           # Final reports
    ├── executive_summary.pdf
    ├── technical_report.pdf
    └── ai_methodology.pdf
