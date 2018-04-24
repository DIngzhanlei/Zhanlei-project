import os
import numpy as np
import pandas as pd
import jaqs_fxdayu
jaqs_fxdayu.patch_all()
from jaqs.data import DataView
from jaqs_fxdayu.data.dataservice import LocalDataService

import warnings
warnings.filterwarnings("ignore")


#--define
start = 20170101
end = 20180101
factor_list  = ['BBI','RVI','Elder','ChaikinVolatility','EPS','PE','PS','ACCA','CTOP','MA10RegressCoeff12','AR','BR','ARBR','np_parent_comp_ttm','total_share','bps']
check_factor = ','.join(factor_list)

dataview_folder = r'../../data'
ds = LocalDataService(fp = dataview_folder)

SH_id = ds.query_index_member("000001.SH", start, end)
SZ_id = ds.query_index_member("399106.SZ", start, end)
stock_symbol = list(set(SH_id)|set(SZ_id))

dv_props = {'start_date': start, 'end_date': end, 'symbol':','.join(stock_symbol),
         'fields': check_factor,
         'freq': 1,
         "prepare_fields": True}

dv = DataView()
dv.init_from_config(dv_props, data_api=ds)
dv.prepare_data()
#----

def ALPHA41():
    ALPHA41=dv.add_formula('alpha41','(Rank(Max(Delta(vwap, 4), 3))* -1)',
                   is_quarterly=False)
    return ALPHA41

def ALPHA161():
    ALPHA161=dv.add_formula('Alpha141','Ts_Mean(Max(Max((high-low),Abs(Delay(close,1)-high)),Abs(Delay(close,1)-low)),12)',
                   is_quarterly=False)
    return ALPHA161


def OperatingRevenuePSLatest():
    df1=dv.get_ts('oper_rev')
    df2=dv.get_ts('capital_stk')
    df=df1/df2
    for row in df:
        row=df.iloc[-1]
    OperatingRevenuePSLatest=dv.append_df(df,field_name='OperatingRevenuePSLatest')
    return OperatingRevenuePSLatest


def DDI():
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


def BIAS5():
    BIAS5=dv.add_formula('bias5_pro','(close-Ts_Mean(close,5))*100/Ts_Mean(close,5)',is_quarterly=False)
    return BIAS5

def UpRVI():
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

def STOQ():
    pre=dv.add_formula('PRE','Ts_Sum(turnover,21)',is_quarterly=False,add_data=True)
    STOQ=dv.add_formula('STOQ','Log((PRE+Delay(PRE,21)+Delay(PRE,42))/3)',is_quarterly=False,add_data=True)
    return STOQ



def PLRC12():
    PLRC12=dv.add_formula('PLRC12_simu',"((Delay(close,12)-Ts_Mean(close,12))*1+(Delay(close,11)-Ts_Mean(close,12))*2+(Delay(close,10)-Ts_Mean(close,12))*3+(Delay(close,10)-Ts_Mean(close,12))*3+(Delay(close,9)-Ts_Mean(close,12))*4+(Delay(close,8)-Ts_Mean(close,12))*5+(Delay(close,7)-Ts_Mean(close,12))*6+(Delay(close,6)-Ts_Mean(close,12))*7+(Delay(close,5)-Ts_Mean(close,12))*8+(Delay(close,4)-Ts_Mean(close,12))*9+(Delay(close,3)-Ts_Mean(close,12))*10+(Delay(close,2)-Ts_Mean(close,12))*11+(Delay(close,1)-Ts_Mean(close,12))*12)/13"
              ,is_quarterly=False,add_data=True)
    return PLRC12

#test output
def test(factor,data):
    if not isinstance(data, pd.core.frame.DataFrame):
        raise TypeError('On factor {} ,output must be a pandas.DataFrame!'.format(factor))
    else:
        try:
            index_name = data.index.names[0]
            columns_name = data.index.names[0]
        except:
            if not (index_name in ['trade_date','report_date'] and columns_name == 'symbol'):
                raise NameError('''Error index name,index name must in ["trade_date","report_date"],columns name must be "symbol" ''')
                
        index_dtype = data.index.dtype_str
        columns_dtype = data.columns.dtype_str
        
        if columns_dtype not in ['object','str']:
            raise TypeError('error columns type')
            
        if index_dtype not in ['int32','int64','int']:
            raise TypeError('error index type')


test_factor = False

if test_factor:   
    for factor in factor_list[5:]:
        data = globals()[factor]()
        test(factor,data)




