from tkinter import *
from tkinter import messagebox
import MailSystem
import Stock
import json

data = []

def Writeinjson(x):
    d = {
        x[0]:{
            'Name':x[1],
            'Country':x[2]
        }
    }
    try:
        with open('data.json','r') as file:
            data_json = json.load(file)
            if x[0] in data_json:
                messagebox.showwarning(title='Error', message='Already Subscried')
    except FileNotFoundError:
        with open('data.json','w') as file:
            json.dump(d,file,indent=4)
    else:
        with open('data.json', 'w') as file:
            data_json.update(d)
            json.dump(data_json,file,indent=4)

def selected_item():
    for i in stock_list_box.curselection():
        s = stock_list_box.get(i)
        x = s.split('\t  ')
        for m in range(0,len(data)):
            if x[0] in data[m]['1. symbol']:
                messagebox.showinfo(title='Selected', message=f'Subscribe to {x[1]} is successful')
                break

        Writeinjson(x)

def getAllStocks():
    global data
    stock_list_box.delete(0,END)
    if not stock_entry_box.get():
        messagebox.showwarning(title='Error', message='Please Input A Valid Stock Name')
        return
    data = Stock.FindParticularStock(search_stock=stock_entry_box.get())
    if not data:
        messagebox.showwarning(title='Error',message='Please Enter A Valid Stock Name')
    k = 0
    for i in data:
        stock_symbol = i['1. symbol']
        stock_name = i['2. name']
        stock_region = i['4. region']
        s = f'{stock_symbol}\t   {stock_name}\t   {stock_region}'
        stock_list_box.insert(k,s)
        k += 1

window = Tk()
window.title("Stock App")
window.config(bg='white')

stock_label = Label(text='Stock Name:', font=("Arial", 18))
stock_label.grid(row=0, column=0, padx=0, pady=10)

stock_entry_box = Entry(width=20)
stock_entry_box.grid(row=0, column=1,padx=0,pady=10)
stock_entry_box.focus_set()

stock_list_box = Listbox(width=50,selectmode='SINGLE')
stock_list_box.grid(row=1,column=0,columnspan=3,padx=50,pady=30)
stock_list_box.yview()
stock_list_box.xview()

search_button = Button(text='Search',command=getAllStocks,font=("Arial", 15, 'bold'))
search_button.grid(row=0,column=2,padx=50,pady=10,columnspan=2)

subscribe_button = Button(text='Subscribe',command=selected_item,font=("Arial", 15, 'bold'))
subscribe_button.grid(row=2,column=0,padx=50,pady=20,columnspan=3)

try:
    with open('data.json', 'r') as file:
        messagebox.showinfo(title='Subscried',message='It seems like you have subscribed..Sending Mail..Please Wait')
        MailSystem.sendMail()
        messagebox.showinfo(title='Done', message='Please Check your Mail and Spam Box')
except FileNotFoundError:
    messagebox.showwarning(title='Error', message='You have not subscried to any stock')


window.mainloop()