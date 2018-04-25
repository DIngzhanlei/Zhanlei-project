def run_formula(dv):
    factor3=dv.add_formula('factor3','(total_oper_rev)^2/((capital_stk)*10^10)'
                           ,is_quarterly=True,add_data=True)


    return factor3
