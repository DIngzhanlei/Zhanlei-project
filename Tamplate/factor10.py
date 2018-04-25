def run_formula(dv,param1=9,param2=26,param3=12):


    TYP=dv.add_formula('TYP','(close+high+low)/3',is_quarterly=False,add_data=True)
    


    factor10=dv.add_formula('factor10','-1*((Ts_Mean(TYP,%s)-Ts_Mean(TYP,%s))/Ts_Mean(volume,%s)*100)'%(param1,param2,param3)
                            ,is_quarterly=False,add_data=True)


    return factor10
