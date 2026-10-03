import pandas as pd
import numpy as np
import xgboost as xgb

def generate_simulation_data(c_rate=1.0, avg_temp=25.0, days=7):
    hours = np.arange(24 * days)
    power = c_rate * 2.0 * np.sin(2 * np.pi * hours / 24)
    temp = avg_temp + 3 * np.sin(2 * np.pi * hours / 48)
    
    df = pd.DataFrame({
        'hour': hours,
        'power_mw': power,
        'temperature_c': temp
    })
    
    # محاسبه هزینه تخریب
    nominal_capacity = 2.0
    replacement_cost = 150000
    energy_throughput = np.abs(df['power_mw']) * 1.0
    temp_stress = np.exp(0.06 * (df['temperature_c'] - 25).clip(lower=0))
    df['degradation_cost'] = (energy_throughput / (nominal_capacity * 3000)) * temp_stress * replacement_cost
    df['cumulative_cost'] = df['degradation_cost'].cumsum()
    
    return df
