# -*- coding:utf-8 -*-

# ##对原始数据进行分割 
import requests
def city_name():
	# 构造请求头
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36', 
				'Referer': 'https://kyfw.12306.cn/otn/login/init' }
	url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9091'
	city_code = requests.get(url, headers=headers, verify=False)
	# 数据使用字符串操作处理
	city_code_list = city_code.text.split("|")
	city_dict = {}
	for k, i in enumerate(city_code_list):
		if '@' in i:		# 城市作为字典的键，城市编号作为字典的值
			city_dict[city_code_list[k + 1]] = city_code_list[k + 2].replace(' ', '')#这里的replace函数是将字符串中的空格符号换掉（或者说去掉空格符），比如 '北 京'变成'北京'。
	return (city_dict)
	
# 输出处理后的值
print(city_name())