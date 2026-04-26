# Does Occupational AI Exposure Cause Self-Employment?
### Causal Inference via Double Machine Learning | CPS ASEC 2021–2024

> **Objective:** Estimate the causal effect of occupational AI exposure on individual self-employment probability using Double Machine Learning, and deliver an industry-style consulting recommendation backed by causal evidence.

---

## Causal Question

**Does higher occupational AI exposure (AIOE) cause a higher probability of self-employment?**

- **Treatment (T):** AIOE score (continuous, range: −1.34 to +1.31) — Felten et al. (2021) occupation-level index aggregated to SOC 2-digit major group
- **Outcome (Y):** Self-employed (binary) — derived from CPS CLASSWKR (incorporated + unincorporated self-employment)
- **Identification strategy:** Double Machine Learning (DML) with GradientBoosting nuisance models and 5-fold cross-fitting
- **Key assumption:** Conditional Independence — after controlling for individual demographics, residual AIOE variation is uncorrelated with unobserved self-employment determinants

---

## Why Causal Inference, Not Prediction?

A naive OLS regression yields a **negative** coefficient (θ = −0.00239), suggesting AI exposure *reduces* self-employment. This is a textbook case of selection bias: high-AIOE occupations (programmers, lawyers, analysts) are predominantly high-income corporate roles with structurally low self-employment rates. A predictive model (Random Forest, R² = 0.016) cannot resolve this — it can identify *who* self-employs, but cannot determine *whether AI caused it*. DML isolates the causal channel by residualizing both outcome and treatment against the same demographic controls before estimating the effect.

---

## Methodology

- **Data:** IPUMS CPS ASEC 2021–2024 merged with Felten et al. (2021) AIOE scores and O\*NET Work Context variables (N = 273,919 employed workers with valid occupation codes)
- **Treatment construction:** OCC2010 → SOC major group crosswalk (22 groups); AIOE scores aggregated to 2-digit SOC level
- **Controls:** Age, sex, education years, log income, marital status, number of children
- **DML nuisance models:** GradientBoostingRegressor (n\_estimators=200, max\_depth=5, learning\_rate=0.1) with 5-fold cross-fitting for both Y and T models
- **Final stage:** OLS regression of Y residuals on T residuals with HC1 heteroskedasticity-robust standard errors
- **Robustness Check 1:** Ridge nuisance model (RidgeCV) as alternative specification — chosen because Ridge imposes linearity on the nuisance models, providing a conservative lower bound and confirming the result is not an artifact of GradientBoosting's nonlinear flexibility
- **Robustness Check 2:** Pre/Post-ChatGPT placebo test (2021–2022 vs. 2023–2024 subsamples)
- **Dashboard:** Interactive Streamlit app with what-if sliders, uncertainty bands, and counterfactual scenario

---

## Key Results

| Estimator | θ (Effect) | 95% CI | Interpretation |
|---|---|---|---|
| Naive OLS | −0.00239 | [−0.00388, −0.00090] | Biased — selection suppresses true effect |
| **DML — Full Sample** | **+0.00836** | **[0.00661, 0.01012]** | **Causal estimate (preferred)** |
| DML — Ridge (Robustness) | +0.00491 | [0.00323, 0.00660] | Consistent sign and significance |
| DML — Pre-ChatGPT (2021–22) | +0.01175 | [0.00929, 0.01420] | Inflated by COVID-era displacement |
| DML — Post-ChatGPT (2023–24) | +0.00427 | [0.00176, 0.00678] | Conservative lower bound |

**Headline finding:** A one-unit increase in AIOE raises self-employment probability by **0.836 percentage points** (p < 0.0001). The sign reversal from Naive OLS to DML confirms that negative confounding from high-skill occupational selection was masking a genuine positive causal effect. Scaled to the U.S. labor force, this implies approximately **1.3 million additional self-employed workers** attributable to occupational AI exposure.

> ⚠️ **Interpretation note:** AIOE is assigned at the 22-group SOC major level. The estimated θ = 0.00836 should be treated as an **upper bound** on the true causal effect, as occupation-level amenability to self-employment may remain in the residual AIOE variation even after DML residualization.

---

## Data Sources

| Dataset | Source | Usage |
|---|---|---|
| CPS ASEC 2021–2024 | [IPUMS CPS](https://cps.ipums.org/) | Outcome, treatment mapping, individual controls |
| AIOE Scores | [Felten et al. (2021)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3955403) | Treatment variable (occupational AI exposure) |
| Language Modeling AIOE | Felten et al. (2021) Appendix | ChatGPT-specific exposure index |
| O\*NET Work Context | [O\*NET Online](https://www.onetonline.org/) | Occupation amenability controls |

---

## Repository Structure

```
DA-final-project/
├── data/
│   ├── raw/                          # Source data files
│   │   ├── cps_00001.csv.gz          # IPUMS CPS ASEC 2021-2024
│   │   ├── AIOE_DataAppendix.xlsx    # Felten et al. AIOE scores
│   │   ├── Language Modeling AIOE and AIIE.xlsx
│   │   └── Work Context.xlsx         # O*NET work context variables
│   └── processed/                    # Cleaned/merged outputs
├── deliverables/
│   └── app.py                        # Streamlit dashboard
├── notebooks/
│   └── 5200-final-project.ipynb      # Main analysis notebook (Parts 0-7)
├── src/
│   ├── Correlation Heatmap.png
│   ├── Self-Employment Rate by AIOE.png
│   └── Self-Employment Trends - High vs Low AIOE.png
├── README.md
└── requirements.txt
```

---

## References

- Felten, E., Raj, M., & Seamans, R. (2021). *Occupational, Industry, and Geographic Exposure to Artificial Intelligence.* SSRN Working Paper.
- Chernozhukov, V., et al. (2018). Double/debiased machine learning for treatment and structural parameters. *The Econometrics Journal*, 21(1), C1–C68.
- Goldsmith-Pinkham, P., Sorkin, I., & Swift, H. (2020). Bartik instruments: What, when, why, and how. *American Economic Review*, 110(8), 2586–2624.
- Cajner, T., et al. (2020). *The U.S. Labor Market during the Beginning of the Pandemic Recession.* NBER Working Paper 27159.

---

*Analysis conducted for ECON 5200: Data Analytics, Northeastern University, Spring 2026.*
