def run_formula(dv,param=None):
    defult_param = 5
    if not param:
        param = defult_param
        
    t = param

    factor4=dv.add_formula('factor4','-1*Ts_Mean(close-Ts_Mean(close,%s),%s)'%(t,t)
                           ,is_quarterly=False,add_data=True)


    return factor4
