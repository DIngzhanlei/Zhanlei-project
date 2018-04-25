def run_formula(dv,param=None):
    defult_param = 12
    if not param:
        param = defult_param
        
    t = param
    
    TYP=dv.add_formula('TYP','(close+high+low)/3'
                       ,is_quarterly=False,add_data=True)
    factor9=dv.add_formula('factor9','Ts_Mean(TYP,%s)/TYP'%(t)
                       ,is_quarterly=False,add_data=True)


    return factor9
