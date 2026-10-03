import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# تنظیمات صفحه
st.set_page_config(
    page_title="BESS Degradation & Health Monitor",
    page_icon="🔋",
    layout="wide"
)

st.title("🔋 BESS Degradation & Health Monitor")
st.markdown("Industrial Battery Energy Storage System (BESS) Asset Health & Degradation Risk Platform.")

# سایدبار برای تنظیمات سناریو توسط کاربر
st.sidebar.header("⚙️ Operating Parameters")
c_rate = st.sidebar.slider("C-Rate (Charging/Discharging Intensity)", 0.5, 2.0, 1.0)
avg_temp = st.sidebar.slider("Average Cell Temperature (°C)", 20.0, 45.0, 25.0)
cycles_per_day = st.sidebar.slider("Daily Equivalent Cycles", 1, 4, 2)

# تولید دیتای تحلیلی بر اساس پارامترهای سایدبار
hours = np.arange(24 * 7)
power = c_rate * 2.0 * np.sin(2 * np.pi * hours / 24)
temp = avg_temp + 3 * np.sin(2 * np.pi * hours / 48)

df = pd.DataFrame({
    'hour': hours,
    'power_mw': power,
    'temperature_c': temp
})

# محاسبات تخریب
nominal_capacity = 2.0 # MWh
replacement_cost = 150000 # EUR
energy_throughput = np.abs(df['power_mw']) * 1.0
temp_stress = np.exp(0.06 * (df['temperature_c'] - 25).clip(lower=0))
df['degradation_cost'] = (energy_throughput / (nominal_capacity * 3000)) * temp_stress * replacement_cost
df['cumulative_cost'] = df['degradation_cost'].cumsum()

# بخش نمایش متریک‌های کلیدی بالا
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Total Degradation Cost (7 Days)", value=f"€ {df['cumulative_cost'].iloc[-1]:,.2f}")
with col2:
    st.metric(label="Max Cell Temperature", value=f"{df['temperature_c'].max():.1f} °C")
with col3:
    st.metric(label="Total Energy Throughput", value=f"{energy_throughput.sum():,.1f} MWh")

st.markdown("---")

# نمودارها با Plotly
st.subheader("📈 Asset Health & Degradation Trajectory")

fig = px.line(df, x='hour', y='cumulative_cost', title="Cumulative Degradation Cost Over Time (€)",
              labels={'hour': 'Hours', 'cumulative_cost': 'Cost [€]'})
fig.update_traces(line_color='#FF4B4B', line_width=3)
st.plotly_chart(fig, use_container_width=True)

# نمودار دما و توان
col_a, col_b = st.columns(2)
with col_a:
    fig_power = px.line(df, x='hour', y='power_mw', title="BESS Operating Power Profile (MW)")
    st.plotly_chart(fig_power, use_container_width=True)
with col_b:
    fig_temp = px.line(df, x='hour', y='temperature_c', title="Cell Temperature Profile (°C)", color_discrete_sequence=['orange'])
    st.plotly_chart(fig_temp, use_container_width=True)

with st.expander("📋 View Raw Simulation Data"):
    st.dataframe(df)
