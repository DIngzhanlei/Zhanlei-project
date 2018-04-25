def run_formula(dv):

    factor1=dv.add_formula('factor1','total_oper_rev/10^(9)',
                           is_quarterly=True,add_data=True)

    return factor1
