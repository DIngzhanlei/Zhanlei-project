def run_formula(dv,param=None):

    defult_param = 5
    if not param:
        param = defult_param
        
    t = param
    


    factor8=dv.add_formula('factor8','-1*((close-Delay(close,1))*volume/(Delay(close,1)*10^6)/StdDev((close-Delay(close,1))*volume/(Delay(close,1)*10^6),%s))'%(t)
                           ,is_quarterly=False,add_data=True)


    return factor8
