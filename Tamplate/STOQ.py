def run_formula(dv):
    pre=dv.add_formula('PRE','Ts_Sum(turnover,21)',
                       is_quarterly=False,add_data=True)
    STOQ=dv.add_formula('STOQ','Log((PRE+Delay(PRE,21)+Delay(PRE,42))/3)',
                        is_quarterly=False,add_data=True)
    return STOQ
