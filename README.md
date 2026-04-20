# Does AI Exposure Cause Workers to Transition to Self-Employment?

**ECON 5200 Applied Data Analytics in Economics — Final Project (Spring 2026)**

## Research Question

Does higher occupational AI exposure cause higher probability of self-employment? We use Double Machine Learning (DML) to isolate the causal effect of AI exposure from occupation-level confounding.

## Key Finding (Preliminary)

DML estimates a causal effect of **θ = +0.010 (p < 0.0001, 95% CI: [0.006, 0.014])** — a 1-unit increase in AIOE raises self-employment probability by ~1 percentage point. Notably, this **reverses the sign** of the naive OLS estimate (-0.002), which is confounded by the fact that high-AIOE occupations tend to be corporate white-collar jobs with inherently low self-employment rates.

## Identification Strategy

- **Method:** Double Machine Learning — Chernozhukov et al. (2018), manual cross-fitted residualization
- **Treatment:** AIOE score (Felten et al., 2021), aggregated to SOC 2-digit major group
- **Outcome:** Self-employed (binary, from CPS CLASSWKR)
- **Controls:** Age, sex, education years, log income, marital status, number of children
- **Robustness (planned):** Pre-ChatGPT placebo test (2021–2022 vs 2023–2024)

## Data Sources

| Source | Description | Link |
|--------|-------------|------|
| IPUMS CPS ASEC 2021–2024 | Individual-level microdata, N ≈ 274,000 employed workers aged 18–65 | https://cps.ipums.org |
| Felten et al. (2021) AIOE | AI Occupational Exposure scores for 774 occupations | https://github.com/AIOE-Data/AIOE |
| O*NET Work Context | Occupation characteristics (autonomy, automation, etc.) | https://www.onetcenter.org/database.html |

## Citation

Felten, E., Raj, M., & Seamans, R. (2021). Occupational, industry, and geographic exposure to artificial intelligence: A novel dataset and its potential uses. *Strategic Management Journal*, 42(12), 2195–2217.

## Repository Structure

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
