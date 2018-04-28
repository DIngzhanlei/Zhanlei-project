def run_formula(dv,param=None):
    defult_param = 2
    if not param:
        param = defult_param
        
    t = param

    factor2=dv.add_formula('factor2','tot_cur_assets*10^11/%s*tot_cur_liab^2'%(t),
                           is_quarterly=True,add_data=True)


    return factor2
