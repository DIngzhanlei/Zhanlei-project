def run_formula(dv, param = None):
    
    alpha161=dv.add_formula('Alpha161','Ts_Mean(Max(Max((high-low),Abs(Delay(close,1)-high)),Abs(Delay(close,1)-low)),12)',is_quarterly=False,add_data=True)
    return alpha161  
