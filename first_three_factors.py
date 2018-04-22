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

def BIAS5():
    BIAS5=dv.add_formula('bias5_pro','(close-Ts_Mean(close,5))*100/Ts_Mean(close,5)',is_quarterly=False)
    return BIAS5
    

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




