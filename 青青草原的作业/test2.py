import tkinter as tk
from tkinter import simpledialog

window = tk.Tk()
window.title('自助点餐')
window.geometry('300x400')

allPrice = 0
selectedItems = []


def countPrice(type):
    global allPrice, selectedItems
    if type == 1:
        allPrice += 12
        selectedItems.append('红糖盖饭')
    if type == 2:
        allPrice += 7
        selectedItems.append('芝士奶油饭')
    if type == 3:
        allPrice += 10
        selectedItems.append('奶油芝士稀饭')
    if type == 4:
        allPrice += 5
        selectedItems.append('白糖饭')


def showTotal():
    global allPrice, selectedItems
    tem_text = ''
    if selectedItems:
        tem_text = '您点了' + '和'.join(selectedItems) + \
            '，一共' + '{:.2f}'.format(allPrice) + '元'
    else:
        tem_text = '您还没有选择任何物品'
    tem.config(text=tem_text)


def payBack():
    tempt = int(pay.get())
    payB = tempt - allPrice
    l2.config(text='收您' + pay.get() + '元' +
              ', 找零' + '{:.1f}'.format(payB) + '元')


def memberPayment():
    member_code = simpledialog.askstring('会员付款', '请输入会员码')
    if member_code == '想跟瑞丰出去玩！！！':
        global allPrice, selectedItems
        tem_text = ''
        allPrice *= 0.8
        if selectedItems:
            tem_text = '您点了' + '和'.join(selectedItems) + \
                '，一共' + '{:.1f}'.format(allPrice) + '元'
        else:
            tem_text = '您还没有选择任何物品'
        tem.config(text=tem_text)
    else:
        showTotal()


l = tk.Label(window, text='您好，请问需要什么？')
l.pack()

c1 = tk.Checkbutton(window, text='红糖饭: 12元', command=lambda: countPrice(1))
c2 = tk.Checkbutton(window, text='芝士奶油饭: 7元', command=lambda: countPrice(2))
c3 = tk.Checkbutton(window, text='芝士奶油稀饭: 10元', command=lambda: countPrice(3))
c4 = tk.Checkbutton(window, text='白糖饭: 5元', command=lambda: countPrice(4))
c1.pack()
c2.pack()
c3.pack()
c4.pack()

tem = tk.Label(window)
tem.pack()

buttonOK = tk.Button(text='OK', command=memberPayment)
buttonOK.pack()

pay = tk.Entry(window, relief='ridge')
pay.pack()

buttonPay = tk.Button(text='付款', command=payBack)
buttonPay.pack()

l2 = tk.Label(window)
l2.pack()

window.mainloop()
