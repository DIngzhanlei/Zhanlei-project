def run_formula(dv):
    bias5=dv.add_formula('bias5_simu','(close-Ts_Mean(close,5))*100/Ts_Mean(close,5)'
                   ,is_quarterly=False,add_data=True)
    return bias5
