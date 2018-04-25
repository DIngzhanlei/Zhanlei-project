def run_formula(dv):
    PLRC12=dv.add_formula('PLRC12_simu',"((Delay(close,12)-Ts_Mean(close,12))*1+(Delay(close,11)-Ts_Mean(close,12))*2+(Delay(close,10)-Ts_Mean(close,12))*3+(Delay(close,10)-Ts_Mean(close,12))*3+(Delay(close,9)-Ts_Mean(close,12))*4+(Delay(close,8)-Ts_Mean(close,12))*5+(Delay(close,7)-Ts_Mean(close,12))*6+(Delay(close,6)-Ts_Mean(close,12))*7+(Delay(close,5)-Ts_Mean(close,12))*8+(Delay(close,4)-Ts_Mean(close,12))*9+(Delay(close,3)-Ts_Mean(close,12))*10+(Delay(close,2)-Ts_Mean(close,12))*11+(Delay(close,1)-Ts_Mean(close,12))*12)/13"
              ,is_quarterly=False,add_data=True)
    return PLRC12
    
