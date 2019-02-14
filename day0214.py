import requests
import json
import csv
# 定义全局变量，用于判断数据是否已经记录
global auctions_distinct
auctions_distinct = []

def get_auctions_info(response_auctions_info, file_name):
    with open(file_name, 'a', newline='') as csvfile:
        # 生成csv对象，用于写入CSV文件
        writer = csv.writer(csvfile)
        for i in response_auctions_info:
            # 判断是否数据已经记录
            if str(i['raw_title']) not in auctions_distinct:
                # 写入数据
                writer.writerow([i['raw_title'], i['view_price'],
                                 i['view_sales'], i['nick'], i['item_loc']])
                auctions_distinct.append(str(i['raw_title']))
        csvfile.close()

if __name__ == '__main__':
    for k in ['四件套', '手机壳']:
        # 新建csv文件，每循环一个关键字会生成其对应的CSV文件
        file_name = k + '.csv'
        with open(file_name, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            # 写入表头信息
            writer.writerow(['标题', '价格', '销量', '店铺', '区域'])
            csvfile.close()
        # 循环次数可以根据实际自行设定
        for p in range(88):
            url = 'https://s.taobao.com/api?callback=jsonp804&m=customized&q=%s&s=%s' % (k, p)
            r = requests.get(url)
            response = r.text
            response = response.split('(')[1].split(')')[0]
            response_dict = json.loads(response)
            response_auctions_info = response_dict['API.CustomizedApi']['itemlist']['auctions']
            # 调用函数get_auctions_info写入商品信息
            get_auctions_info(response_auctions_info, file_name)
    print('获取数据量为：' + len(auctions_distinct))
