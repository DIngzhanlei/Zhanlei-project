def run_formula(dv):
    df1=dv.get_ts('oper_rev')
    df2=dv.get_ts('capital_stk')
    df=df1/df2
    for row in df:
        row=df.iloc[-1]
    OperatingRevenuePSLatest=df
    return OperatingRevenuePSLatest
