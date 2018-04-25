def run_formula(dv,param=None):
    defult_param = 0.01
    if not param:
        param = defult_param
        
    t = param



    factor6=dv.add_formula('factor6','-1*(Log(close/Delay(close,1))*100-%s)^2'%(t)
                           ,is_quarterly=False,add_data=True)


    return factor6
