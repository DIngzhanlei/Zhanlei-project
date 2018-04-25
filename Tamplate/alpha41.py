def run_formula(dv):
    
    alpha41=dv.add_formula('alpha41','(Rank(Max(Delta((vwap), 3), 5))* -1)',is_quarterly=False,add_data=True)

    return alpha41        

