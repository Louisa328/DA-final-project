
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

st.set_page_config(page_title="AI Exposure & Self-Employment Dashboard", layout="wide")
st.title("Does Occupational AI Exposure Cause Self-Employment?")
st.markdown("**Causal estimates from Double Machine Learning (DML) | CPS ASEC 2021–2024 | N=273,919**")

# --- Sidebar: What-If Controls ---
st.sidebar.header("What-If Scenarios")

treatment_multiplier = st.sidebar.slider(
    "AIOE Treatment Intensity Multiplier",
    min_value=0.5, max_value=3.0, value=1.0, step=0.1
)

period = st.sidebar.selectbox(
    "Sample Period",
    ["Full Sample (2021-2024)", "Pre-ChatGPT (2021-2022)", "Post-ChatGPT (2023-2024)"]
)

# --- Pre-computed DML results ---
estimates = {
    "Full Sample (2021-2024)":      {"ate": 0.00836, "se": 0.00090},
    "Pre-ChatGPT (2021-2022)":      {"ate": 0.01175, "se": 0.00125},
    "Post-ChatGPT (2023-2024)":     {"ate": 0.00427, "se": 0.00128},
}

baseline_ate = estimates[period]["ate"]
baseline_se  = estimates[period]["se"]

# --- Compute What-If Estimate ---
adjusted_ate = baseline_ate * treatment_multiplier
adjusted_se  = baseline_se  * treatment_multiplier
ci_lower = adjusted_ate - 1.96 * adjusted_se
ci_upper = adjusted_ate + 1.96 * adjusted_se

# --- Display Results ---
st.subheader(f"Estimated Causal Effect — {period}")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Causal Effect (θ)", f"{adjusted_ate:.5f}")
col2.metric("95% CI Lower",      f"{ci_lower:.5f}")
col3.metric("95% CI Upper",      f"{ci_upper:.5f}")
col4.metric("Multiplier",        f"{treatment_multiplier:.1f}x")

st.markdown(f"""
> **What-if interpretation:** If AIOE treatment intensity is multiplied by **{treatment_multiplier:.1f}x**,
> the estimated causal effect on self-employment probability changes to
> **{adjusted_ate:.5f}** (95% CI: [{ci_lower:.5f}, {ci_upper:.5f}]).
""")

# --- Uncertainty Visualization ---
st.subheader("Uncertainty Bands Across Treatment Intensities")
multipliers = np.arange(0.5, 3.1, 0.1)
ates = baseline_ate * multipliers
ses  = baseline_se  * multipliers

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=multipliers, y=ates + 1.96 * ses,
    mode="lines", line=dict(width=0), showlegend=False
))
fig.add_trace(go.Scatter(
    x=multipliers, y=ates - 1.96 * ses,
    mode="lines", line=dict(width=0), fill="tonexty",
    fillcolor="rgba(26,35,126,0.2)", name="95% CI"
))
fig.add_trace(go.Scatter(
    x=multipliers, y=ates,
    mode="lines", line=dict(color="#1a237e", width=2), name="Estimated Effect"
))
fig.add_vline(x=treatment_multiplier, line_dash="dash", line_color="red",
              annotation_text=f"Current: {treatment_multiplier:.1f}x")
fig.add_hline(y=0, line_dash="dot", line_color="gray", opacity=0.5)
fig.update_layout(
    title=f"What-If: Causal Effect vs. Treatment Intensity ({period})",
    xaxis_title="Treatment Intensity Multiplier",
    yaxis_title="Estimated Causal Effect on P(Self-Employed)",
    template="plotly_white"
)
st.plotly_chart(fig, use_container_width=True)

# --- Period Comparison ---
st.subheader("Causal Estimates Across Periods")
periods = list(estimates.keys())
ates_all = [estimates[p]["ate"] for p in periods]
ses_all  = [estimates[p]["se"]  for p in periods]

fig2 = go.Figure()
fig2.add_trace(go.Scatter(
    x=periods,
    y=ates_all,
    error_y=dict(
        type="data",
        array=[1.96 * s for s in ses_all],
        visible=True,
        color="#1a237e"
    ),
    mode="markers",
    marker=dict(size=12, color="#1a237e"),
    name="DML Estimate"
))
fig2.add_hline(y=0, line_dash="dot", line_color="gray", opacity=0.5)
fig2.update_layout(
    title="DML Causal Estimates: Pre vs. Post ChatGPT",
    xaxis_title="Sample Period",
    yaxis_title="Estimated Causal Effect (θ)",
    template="plotly_white"
)
st.plotly_chart(fig2, use_container_width=True)

# --- Counterfactual Scenario ---
st.subheader("Counterfactual: What if AIOE exposure doubled?")
counterfactual_ate = baseline_ate * 2.0
counterfactual_ci  = (counterfactual_ate - 1.96 * baseline_se * 2.0,
                      counterfactual_ate + 1.96 * baseline_se * 2.0)
st.info(f"If occupational AI exposure doubled, the estimated effect on self-employment probability would be "
        f"**{counterfactual_ate:.5f}** (95% CI: [{counterfactual_ci[0]:.5f}, {counterfactual_ci[1]:.5f}]).")

# --- Key Assumptions ---
st.subheader("Key Identification Assumptions")
st.markdown("""
- **Conditional Independence:** Residual AIOE variation is uncorrelated with unobserved self-employment determinants after controlling for demographics
- **AIOE is pre-determined:** Occupation-level index constructed from AI benchmark data (Felten et al. 2021), not individual choices  
- **Main threat:** Occupation-level assignment (22 SOC groups) — estimate is likely an upper bound on the true causal effect
""")
