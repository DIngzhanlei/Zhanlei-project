# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 11:08:10 2018

@author: xinger
"""

#--------------------------------------------------------
#import

import os
import numpy as np
import pandas as pd
import jaqs_fxdayu
jaqs_fxdayu.patch_all()
from jaqs.data import DataView
from jaqs_fxdayu.data.dataservice import LocalDataService

import warnings
warnings.filterwarnings("ignore")

#--------------------------------------------------------
#define

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



#--------------------------------------------------------
"""
define factor caculation functions

input  :  dict
parameter of factor
-------
output :  pd.DataFrame
    factor_values , Index is trade_date, columns are symbols.

"""
#------------------------------------------------------------------------------    
def factor1():
    factor1=dv.add_formula('factor1','total_oper_rev/10^(9)',is_quarterly=True,add_data=True)
    return factor1
def factor2():
    factor2=dv.add_formula('factor2','tot_cur_assets/2*tot_cur_liab',is_quarterly=True,add_data=True)
    return factor2
def factor3():
    factor3=dv.add_formula('factor3','(total_oper_rev)^2/((capital_stk)*10^10)',is_quarterly=True,add_data=True)
    return factor3
def factor4():
    factor4=dv.add_formula('factor4','-1*Ts_Mean(close-Ts_Mean(close,5),5)',is_quarterly=False,add_data=True)
    return factor4
def factor5():
    factor5=dv.add_formula('factor5','Ts_Mean(close,5)/StdDev(close,5)',is_quarterly=False,add_data=True)
    return factor5
def factor6():
    factor6=dv.add_formula('factor6','-1*(Log(close/Delay(close,1))*100-0.01)^2',is_quarterly=False,add_data=True)
    return factor6
def factor7():
    factor7=dv.add_formula('factor7','((close/Delay(close,2))-(close/Delay(close,4)))*100',is_quarterly=False,add_data=True)
    return factor7
def factor8():
    factor8=dv.add_formula('factor8','-1*((close-Delay(close,1))*volume/(Delay(close,1)*10^6)/StdDev((close-Delay(close,1))*volume/(Delay(close,1)*10^6),5))',is_quarterly=False,add_data=True)
    return factor8
def factor9():
    TYP=dv.add_formula('TYP','(close+high+low)/3',is_quarterly=False,add_data=True)
    factor9=dv.add_formula('factor9','Ts_Mean(TYP,12)/TYP',is_quarterly=False,add_data=True)
    return factor9
def factor10():
    TYP=dv.add_formula('TYP','(close+high+low)/3',is_quarterly=False,add_data=True)
    factor10=dv.add_formula('factor10','-1*((Ts_Mean(TYP,9)-Ts_Mean(TYP,26))/Ts_Mean(volume,12)*100)',is_quarterly=False,add_data=True)
    return factor10









#--------------------------------------------------------- 
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
