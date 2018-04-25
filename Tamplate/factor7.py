def run_formula(dv,param1=None,param2=None):
    defult_param1 = 2
    defult_param2 =4
    if not param1:
        param1 = defult_param1
    if not param2:
        param2 = defult_param2
        
    u = param1
    v = param2

    
    factor7=dv.add_formula('factor7','((close/Delay(close,%s))-(close/Delay(close,%s)))*100'%(u,v)
                           ,is_quarterly=False,add_data=True)


    return factor7
 
