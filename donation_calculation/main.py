# coding=utf-8
from tkinter import *
from tkinter import ttk, messagebox
import json

import PyInstaller.__main__
import os

vat = 1.17
product_dct_path = os.path.dirname(os.path.abspath(__file__))+ '/test.txt'
product_dct = dict(eval(open(product_dct_path, 'r').read()))




def calculate(last_root, product_name, print_type, num_of_products, suggested_price):
    constant_cost = product_dct.get('products').get(product_name).get('prices').get('prints').get(print_type).get('Base') * vat
    differential_cost = product_dct.get('products').get(product_name).get('prices').get('prints').get(print_type).get('Diff') * vat * num_of_products
    total_cost = constant_cost + differential_cost

    base_price = product_dct.get('products').get(product_name).get('prices').get('product')

    cost_per_unit = total_cost / num_of_products
    profit_pct = (suggested_price - cost_per_unit - int(base_price)) / suggested_price

    calculation_result_str = 'ריווחיות עם לוגו:  ' + "{0:.0f}%".format(profit_pct * 100) + '\n  עלות לוגו: ' + str(round(cost_per_unit, 2)) + '\n האם תרצה לחשב פעם נוספת?'

    msg_box = messagebox.askquestion(title='Calculation Result', message=calculation_result_str)
    if msg_box == 'yes':
        calculation_window(last_root)
    else:
        last_root.destroy()

def add_print_type(last_root, selected_product):
    ttk.Label(last_root, text='סוג הדפסה').grid(column=1, row=3)
    print_type_combo = ttk.Combobox(last_root, values=list(product_dct.get('products').get(selected_product).get('prices').get('prints').keys()))
    print_type_combo.grid(column=0, row=3)

    ttk.Label(last_root, text="כמות פריטים: ").grid(column=1, row=4, pady=3, sticky=E)
    num_of_products = StringVar()
    num_of_products_entry = ttk.Entry(last_root, width=7, textvariable=num_of_products)
    num_of_products_entry.grid(column=0, columnspan=3, row=4, pady=3)

    ttk.Label(last_root, text="מחיר מוצע ").grid(column=1, row=5, pady=3, sticky=E)
    suggested_price = StringVar()
    suggested_price_entry = ttk.Entry(last_root, width=7, textvariable=suggested_price)
    suggested_price_entry.grid(column=0, columnspan=3, row=5, pady=3)
    ttk.Button(last_root, text='חשב', command=lambda: calculate(last_root, selected_product, print_type_combo.get(), int(num_of_products.get()), int(suggested_price.get()))).grid(column=0, columnspan=2, row=6, padx=1, pady=2)


def calculation_window(last_root):
    last_root.title("Calculation Window")
    for child in last_root.winfo_children():
        child.destroy()

    ttk.Label(last_root, text='סוג מוצר').grid(column=1, row=0)
    product_combo = ttk.Combobox(last_root, values=list(product_dct.get('products').keys()))
    product_combo.grid(column=0, row=0)
    product_combo.current(0)

    ttk.Button(last_root, text='מצא סוגי הדפסה', command=lambda: add_print_type(last_root, product_combo.get())).grid(column=0, columnspan=2, row=2, padx=1, pady=2)


def price_changer(price_type, new_price, product_name):
    if price_type == 'product':
        product_dct.get('products').get(product_name).get('prices').get('product')
        product_dct['products'][product_name]['prices']['product'] = float(new_price)

        writer = open(product_dct_path, 'w')
        writer.write(str(product_dct))


def add_product(last_root, prod_name, entry_types, base_prices, diff_prices, prod_price):

    prints_dict = {}

    for i in range(len(entry_types)):
        prints_dict[entry_types[i].get()] = {'Base':base_prices[i].get(), 'Diff':diff_prices[i].get()}

    new_prod_dict = {'prices' : {'product': float(prod_price), 'prints': prints_dict}}

    product_dct['products'][prod_name] = new_prod_dict

    writer = open(product_dct_path, 'w')
    writer.write(str(product_dct))

    msg_box = messagebox.askquestion('Successful', 'Added Successfully, Would you like to return to main menu?', icon='warning')
    if msg_box == 'yes':
        main_window(last_root)
    else:
        last_root.destroy()

def delete_product(last_root, prod_name):
    del product_dct['products'][prod_name]

    msg_box = messagebox.askquestion('Successful', 'Deleted Successfully, Would you like to return to main menu?', icon='warning')
    if msg_box == 'yes':
        main_window(last_root)
    else:
        last_root.destroy()


def change_product_price(last_root, product_name):
    for child in last_root.winfo_children():
        child.destroy()
    ttk.Label(last_root, text='שינוי מחיר ' + product_name).grid(row=0)

    current_product_price = product_dct.get('products').get(product_name).get('prices').get('product')
    ttk.Label(last_root, text='מחיר נוכחי: ' + str(current_product_price)).grid(row=1)

    ttk.Label(last_root, text='מחיר חדש: ' + str(current_product_price)).grid(column=1, row=2)

    new_price = StringVar()
    new_price_entry = ttk.Entry(last_root, width=7, textvariable=new_price)
    new_price_entry.grid(column=0, row=2)

    ttk.Button(last_root, text='שנה מחיר', command=lambda: price_changer('product', new_price.get(), product_name)).grid(column=0, columnspan=2, row=1, padx=1, pady=2)


def destroy_all(root):
    for child in root.winfo_children():
        child.destroy()


def add_action_options(last_root, chosen_option):
    destroy_all(last_root)

    if chosen_option == 'שינוי מחיר בסיס של מוצר':

        ttk.Label(last_root, text='סוג מוצר').grid(column=1, row=0)
        product_combo = ttk.Combobox(last_root, values=product_dct.get('products').keys())
        product_combo.grid(column=0, row=0)
        product_combo.current(0)

        ttk.Button(last_root, text='אישור', command=lambda: change_product_price(last_root, product_combo.get())).grid(column=0, columnspan=2, row=1, padx=1, pady=2)

    elif chosen_option == 'הוספת מוצר':

        # product name
        ttk.Label(last_root, text='שם המוצר:').grid(column=1, row=0)
        new_prod_name = StringVar()
        new_prod_name_entry = ttk.Entry(last_root, width=7, textvariable=new_prod_name)
        new_prod_name_entry.grid(column=0, row=0)

        # product price
        ttk.Label(last_root, text='מחיר המוצר:').grid(column=1, row=1)
        new_prod_price = StringVar()
        new_prod_price_entry = ttk.Entry(last_root, width=7, textvariable=new_prod_price)
        new_prod_price_entry.grid(column=0, row=1)

        # product print types
        ttk.Label(last_root, text='סוגי הדפסות:').grid(column=1, row=2)
        product_prints_combo = ttk.Combobox(last_root, values=[i for i in range(1, 11)])
        product_prints_combo.grid(column=0, row=2)

        ttk.Button(last_root, text='אישור', command=lambda: render_print_types(product_prints_combo.get(), new_prod_name.get(), new_prod_price.get())).grid(column=0, row=3)

        def render_print_types(product_types_num, prod_name, prod_price):
            destroy_all(last_root)

            ttk.Label(last_root, text=prod_name, font=("Courier", 25)).grid(columnspan=2, row=0)

            entry_types = []
            base_prices = []
            diff_prices = []
            for i in range(0, int(product_types_num) * 3, 3):
                ttk.Label(last_root, text='סוג ההדפסה:').grid(column=1, row=i + 1)
                new_prod_print_type = Entry(last_root)
                new_prod_print_type.grid(column=0, row=i + 1)
                entry_types.append(new_prod_print_type)

                ttk.Label(last_root, text='מחיר בסיס להדפסה:').grid(column=1, row=i + 2)
                new_type_base_p = Entry(last_root)
                new_type_base_p.grid(column=0, row=i + 2)
                base_prices.append(new_type_base_p)

                ttk.Label(last_root, text='מחיר להדפסה נוספת:').grid(column=1, row=i + 3, pady=(0, 50))
                new_type_diff = Entry(last_root)
                new_type_diff.grid(column=0, row=i + 3, pady=(0, 50))
                diff_prices.append(new_type_diff)

            ttk.Button(last_root, text='אישור', command=lambda: add_product(last_root, prod_name, entry_types, base_prices, diff_prices, prod_price)).grid(pady=(0,10), columnspan=2)

    elif chosen_option == 'מחיקת מוצר':
        ttk.Label(last_root, text='בחר מוצר').grid(column=1, row=0)
        product_combo = ttk.Combobox(last_root, values=list(product_dct.get('products').keys()))
        product_combo.grid(column=0, row=0)
        product_combo.current(0)

        ttk.Button(last_root, text='מחק', command=lambda: delete_product(last_root, product_combo.get())).grid(column=0, columnspan=2, row=1, padx=1, pady=2)


def change_prices(last_root):
    for child in last_root.winfo_children():
        child.destroy()

    ttk.Label(last_root, text='בחר פעולה').grid(column=1, row=0)
    choose_action_combo = ttk.Combobox(last_root, values=['שינוי מחיר בסיס של מוצר', 'הוספת מוצר', 'מחיקת מוצר'])
    choose_action_combo.grid(column=0, row=0)
    ttk.Button(last_root, text='אישור', command=lambda: add_action_options(last_root, choose_action_combo.get())).grid(row=1, columnspan=2)


def main_window(last_root):
    if last_root is None:
        root = Tk()
        root.eval('tk::PlaceWindow . center')
        root.title('Main Page')
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
    else:
        for child in last_root.winfo_children():
            child.destroy()

        root = last_root

    ttk.Button(last_root, text='חישוב', command=lambda: calculation_window(root)).grid(column=0, columnspan=2, row=0, pady=20, padx=10)

    ttk.Button(last_root, text='שינוי ערכים', command=lambda: change_prices(root)).grid(column=0, row=1, padx=10, pady=20)
    ttk.Button(last_root, text='יציאה', command=exit).grid(row=1, column=1, pady=20, padx=10)
    root.mainloop()


main_window(None)


