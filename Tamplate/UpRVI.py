def run_formula(dv):
    USD = dv.add_formula('USD', 
               "If(Return(close,1)>0,StdDev(close,10),0)"
               , is_quarterly=False, add_data=True)

    DSD = dv.add_formula('DSD', 
               "If(Return(close,1)<0,StdDev(close,10),0)"
               , is_quarterly=False, add_data=True)

    UpRVI = dv.add_formula('UpRVI_simu', 
               "Ta('EMA',0,USD,USD,USD,USD,USD,14)"
               , is_quarterly=False, add_data=True)
    return UpRVI
