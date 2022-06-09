# -*- coding: utf-8 -*-

from garbevents.sensors_events import GetData

from garbevents.settings import Settings as ST

import pandas as pd

'mitmdump -p 8889 -s test_sensors_events.py'
#  ST.url = 'https://sc.jiligaga.com/sa?project=default'
ST.url = 'https://sc.jiligaga.com/sa?project=production'
ST.report_path = 'report'


def excel_one_line_to_list():
    df = pd.read_excel('/Users/jasonwu/Downloads/cocos埋点大全.xlsx', sheet_name='埋点汇总', header=0, usecols='A',
                       keep_default_na=False)

    df_li = df.values.tolist()
    result = []
    for s_li in df_li:
        result.append(s_li[0])


addons = [
    GetData(),
    excel_one_line_to_list()
]
