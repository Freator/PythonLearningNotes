#import 导入标准模块 sys
import sys
print("命令行参数：")
print(sys.argv)
for i in sys.argv:
	print(i)