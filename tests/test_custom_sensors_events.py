# -*- coding: utf-8 -*-

from garbevents.custom_sensors_events import GetData

from garbevents.settings import Settings as ST

import pandas as pd

'mitmdump -p 8889 -s test_custom_sensors_events.py'

ST.report_path = 'report'

#  国内版本
ST.url = 'https://sc.jiliguala.com/sa?project=default'
#  ST.url = 'https://sc.jiliguala.com/sa?project=production'

ST.report_path = 'report'


#  从excel表格中读取埋点事件名
# def excel_one_line_to_list():
#     df = pd.read_excel('/Users/jlglqa/Downloads/叽里呱啦核心埋点.xlsx', sheet_name='Sheet1', header=1, usecols='B',
#                        keep_default_na=False)
#
#     df_li = df.values.tolist()
#     ST.all_events = []
#     for s_li in df_li:
#         ST.all_events.append(s_li[0])
#
#     print(ST.all_events)


#  海外版本
#  ST.url = 'https://sc.jiligaga.com/sa?project=default'
#  ST.url = 'https://sc.jiligaga.com/sa?project=production'


# def excel_one_line_to_list_intl():
#     df = pd.read_excel('/Users/jlglqa/Downloads/cocos埋点大全.xlsx', sheet_name='埋点汇总', header=0, usecols='A',
#                        keep_default_na=False)
#
#     df_li = df.values.tolist()
#     ST.all_events = []
#     for s_li in df_li:
#         ST.all_events.append(s_li[0])
#
#     print(ST.all_events)

ST.all_events = ['home_view']

ST.events_properties = {
    'home_view': ['vesion'],
}

addons = [
    GetData(),
    #  excel_one_line_to_list(),
    #  excel_one_line_to_list_intl(),
]
