def run_formula(dv):
    PLRC12=dv.add_formula('PLRC12_simu',"Ta('LINEARREG_SLOPE',0,open,high,low,close,volume,12)"
              ,is_quarterly=False,add_data=True)
    return PLRC12
    
