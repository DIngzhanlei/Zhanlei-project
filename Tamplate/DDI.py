def run_formula(dv):
    DMZ=dv.add_formula('DMZ','If((low+high)<=(Delay(low,1)+Delay(high,1)),0,Max(Abs(high-Delay(high,1)),Abs(low-Delay(low,1))))'
               ,is_quarterly=False,add_data=True)
    DMF=dv.add_formula('DMF','If(low+high>=Delay(low,1)+Delay(high,1),0,Max(Abs(high-Delay(high,1)),Abs(low-Delay(low,1))))'
               ,is_quarterly=False,add_data=True)
    DIZ=dv.add_formula('DIZ_simu','Ts_Sum(DMZ,13)/(Ts_Sum(DMZ,13)+Ts_Sum(DMF,13))'
               ,is_quarterly=False,add_data=True)
    DIF=dv.add_formula('DIF_simu','Ts_Sum(DMF,13)/(Ts_Sum(DMZ,13)+Ts_Sum(DMF,13))'
               ,is_quarterly=False,add_data=True)
    DDI=dv.add_formula('DDI_simu','DIZ_simu-DIF_simu'
               ,is_quarterly=False,add_data=True)
    return DDI
