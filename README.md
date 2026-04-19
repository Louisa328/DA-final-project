AI Exposure and Labor Market Transitions: A Causal Analysis of Self-Employment
This project serves as a data-driven recommendation for labor market policy, analyzing whether technological shocks from generative AI drive workers toward self-employment.

1. Project Overview
Causal Question: Does higher occupational AI exposure (T) cause a higher probability of transitioning into self-employment (Y)?
Consulting Context: Beyond mere prediction, this project identifies whether AI tools lower the barrier to solo-work or if observed trends are merely correlations driven by inherent occupational characteristics
.
2. Identification Strategy: Double Machine Learning (DML)
A pure predictive model is insufficient because it cannot distinguish between (a) inherent occupation amenability and (b) AI tools lowering the self-employment barrier
.
Method: We use Double Machine Learning (DML) to flexibly control for high-dimensional confounders, isolating the "pure" causal effect of AI exposure (channel b)
.
Placebo Test: To validate the causal claim, we re-run the model on a pre-ChatGPT subsample (2021–2022). A significantly smaller or zero coefficient in the pre-period supports a causal interpretation of the recent AI shock
.
3. Dataset & Variables
Sources: IPUMS CPS ASEC (2021–2024), Felten AIOE scores, and O*NET occupational characteristics
.
Sample Size: N>10,000 (well exceeding the 1,000+ observation requirement)
.
Treatment (T): AIOE score (continuous, 0–5)
.
Outcome (Y): Self-employed (binary)
.
Controls (X): Individual demographics (Age, Sex, Race, Education) and O*NET features (Autonomy, Independence, Computer use)
.
4. Repository Structure
Following the DA Final clean repo standards
:
├── README.md               # Project overview and instructions
├── requirements.txt        # Python dependencies for reproducibility
├── streamlit_app.py        # Streamlit dashboard with what-if scenarios
├── src/                    # .py modules for core logic
│   ├── data_cleaning.py    # Merging CPS and AIOE via SOC crosswalk
│   └── dml_engine.py       # DML implementation and estimation
├── notebooks/
│   └── checkpoint_proposal.ipynb  # Preliminary EDA and Naive estimation
└── deliverables/           # Final PDF reports
    ├── executive_summary.pdf
    ├── technical_report.pdf
    └── ai_methodology_appendix.pdf
5. Streamlit "What-If" Dashboard
The deployed dashboard allows for real-time counterfactual analysis
:
Parameter Sliders: Modify AI exposure intensity to see predicted shifts in self-employment rates.
Uncertainty Visualization: Displays dynamic confidence bands (95% CI)
.
Counterfactual Scenario: "If AI exposure in white-collar sectors increased by X%, the estimated change to self-employment is Y [CI:a,b]"
.
6. Reproducibility
To replicate the results:
Clone this repository.
Install requirements: pip install -r requirements.txt.
Run the dashboard: streamlit run streamlit_app.py.
7. AI Methodology (P.R.I.M.E.)
This project utilizes an AI-augmented methodology. All significant interactions with LLMs (Code Generation, Analysis Assistance, Writing) are documented using the P.R.I.M.E. framework and human-verified for accuracy
. Detailed logs are found in the AI_Methodology_Appendix.pdf.
