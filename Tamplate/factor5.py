def run_formula(dv,param=None):
    defult_param = 5
    if not param:
        param = defult_param
        
    t = param


    factor5=dv.add_formula('factor5','Ts_Mean(close,%s)/StdDev(close,%s)'%(t,t)
                           ,is_quarterly=False,add_data=True)


    return factor5
