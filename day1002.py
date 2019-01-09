# -*- coding:utf-8 -*-
import tkinter
import time
top = tkinter.Tk()
'''
label1 = tkinter.Label(top,text = 'Hello Python')
label1.pack()
time.sleep(5)
top.geometry('400x300+150+200')
top.mainloop()
'''
'''
top.geometry('400x300+150+200')
label1 = tkinter.Label(top,text = 'Beijing')
label2 = tkinter.Label(top,text = 'Shanghai')
label3 = tkinter.Label(top,text = 'Guangzhou')
label4 = tkinter.Label(top,text = 'Shenzhen')
label1.pack(side = 'left',fill = 'both')
label2.pack(side = 'right',fill = 'both',padx = 5,pady = 3)
label3.pack(side = 'top',fill = 'both',expand = 'yes',anchor = 'n')
label4.pack(side = 'bottom',fill = 'both',expand = 'yes',anchor = 's')
top.mainloop()
'''
top.geometry('300x100+0+0')
top.wm_title('Label Example')
label = tkinter.Label(top,text = 'Advanced Language\n Program Design\n--Python',\
						height = 4,width = 20,relief = 'ridge',\
						background = '#00ccaa',foreground = '#ff0000',\
						anchor = 'center',font = '黑体',cursor = 'man')
label.grid(row = 0,column = 1,padx = 60)
top.mainloop()	