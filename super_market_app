from tkinter import *
from tkinter import ttk, messagebox
import csv

signed_in = False
shopped = False

veg_dict = {'Tomato': 2, 'Lettuce': 0.5, 'White Onion': 1.5, 'Red Onion': 1.1, 'Potato': 0.90}
drinks_dict = {'Coca-Cola': 6, 'Sprite': 7.5, 'Water': 4.0, 'Sparkling Water': 4.50}


def pay_and_finish(root):
    messagebox.showerror('Successful', 'Delivery Sent!')
    root.destroy()
    main_window('', None)


def add_to_cart(order_dict, order_type):
    with open('order.txt', mode='a') as order_file:
        employee_writer = csv.writer(order_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        if order_type == 'veg':
            if order_dict.get('Tomato') != 0:
                employee_writer.writerow(['Tomato', order_dict.get('Tomato'), order_dict.get('Tomato') * veg_dict.get('Tomato')])
            if order_dict.get('Lettuce') != 0:
                employee_writer.writerow(['Lettuce', order_dict.get('Lettuce'), order_dict.get('Lettuce') * veg_dict.get('Lettuce')])
            if order_dict.get('White Onion') != 0:
                employee_writer.writerow(['White Onion', order_dict.get('White Onion'), order_dict.get('White Onion') * veg_dict.get('White Onion')])
            if order_dict.get('Red Onion') != 0:
                employee_writer.writerow(['Red Onion', order_dict.get('Red Onion'), order_dict.get('Red Onion') * veg_dict.get('Red Onion')])

        elif order_type == 'drinks':
            if order_dict.get('Coca-Cola') != 0:
                employee_writer.writerow(['Coca-Cola', order_dict.get('Coca-Cola'), order_dict.get('Coca-Cola') * drinks_dict.get('Coca-Cola')])
            if order_dict.get('Sprite') != 0:
                employee_writer.writerow(['Sprite', order_dict.get('Sprite'), order_dict.get('Sprite') * drinks_dict.get('Sprite')])
            if order_dict.get('Water') != 0:
                employee_writer.writerow(['Water', order_dict.get('Water'), order_dict.get('Water') * drinks_dict.get('Water')])
            if order_dict.get('Sparkling Water') != 0:
                employee_writer.writerow(['Sparkling Water', order_dict.get('Sparkling Water'), order_dict.get('Sparkling Water') * drinks_dict.get('Sparkling Water')])

    messagebox.showerror('Successful', 'Orders Added! Continue shopping or pay up')


def check_user_and_pass(user_name, password, root):
    with open('users.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            print(row)
            try:
                if row[0] == user_name and row[1] == password:
                    signed_in = True
                    root.destroy()
                    main_window(user_name, None)
            except Exception as e:
                print(e)

    if not signed_in:
        messagebox.showerror('Login Failed', 'User Name Or Password Are Wrong, Try Again')


def add_account(user_name, password, age, root):
    with open('users.txt', mode='a') as users_file:
        employee_writer = csv.writer(users_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        employee_writer.writerow([user_name.get(), password.get(), age.get()])

    messagebox.showerror('Success!', 'Successful Sign-Up! \n Try To Login')
    root.destroy()
    main_window('', None)


def main_window(usr_name, last_root):
    if last_root != None:
        last_root.destroy()

    root = Tk()
    root.eval('tk::PlaceWindow . center')
    root.title('Main Page')
    mainframe = ttk.Frame(root, padding='3 3 12 12 ')
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    error_txt = 'Sorry, you can\'t shop unless your\'e signed in...'
    if usr_name != '':
        ttk.Label(mainframe, text="Hey " + usr_name + "!", font=("Courier", 25)).grid(column=0, row=1, columnspan=2, pady=5)
        ttk.Button(mainframe, text='Shop', command=lambda: store_window(usr_name, root)).grid(column=0, row=2, padx=1, pady=2)
        ttk.Button(mainframe, text='Pay Up', command=lambda: pay_up(root, usr_name)).grid(column=1, row=2, padx=1, pady=2)
        ttk.Button(mainframe, text='Sign Out', command=lambda: main_window('',root)).grid(column=1, row=4,  pady=20)
        ttk.Button(mainframe,text='Quit', command= exit).grid(row=4,pady=20)




    else:
        ttk.Label(mainframe, text="Welcome To Our Store!", font=("Courier", 25)).grid(column=0, columnspan=2, row=1, pady=5)
        ttk.Button(mainframe, text='Sign In', command=lambda: login_window(root)).grid(column=0, row=2, padx=3, pady=4)
        ttk.Button(mainframe, text='Sign Up', command=lambda: sign_up_window(root)).grid(column=1, row=2, padx=3, pady=4)
        ttk.Button(mainframe, text='Shop', command=lambda: messagebox.showerror('Failure', error_txt)).grid(column=0, row=3, padx=3, pady=4)
        ttk.Button(mainframe, text='Pay Up', command=lambda: messagebox.showerror('Failure', error_txt)).grid(column=1, row=3, padx=3, pady=4)
        ttk.Button(mainframe,text='Quit', command= exit).grid(row=4, columnspan=2,pady=10)

    root.mainloop()



def pay_up(root, user_name):
    global shopped
    root.destroy()
    if not shopped:
        f = open('order.txt', 'r+')
        f.truncate(0)
    payup_root = Tk()
    payup_root.eval('tk::PlaceWindow . center')
    payup_root.title('Store Page')

    mainframe = ttk.Frame(payup_root, padding='3 3 12 12 ')
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    payup_root.columnconfigure(0, weight=1)
    payup_root.rowconfigure(0, weight=1)

    total_price=0



    with open('order.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        label = Label(mainframe, width=15, text='Product', relief=RIDGE, font='Helvetica 14 bold').grid(row=0, column=0)
        label = Label(mainframe, width=15, text='Quantity', relief=RIDGE, font='Helvetica 14 bold').grid(row=0, column=1)
        label = Label(mainframe, width=15, text='Price Per Product', relief=RIDGE, font='Helvetica 14 bold').grid(row=0, column=2)


        total_price=0
        # r and c tell us where to grid the labels
        r = 1
        for col in csv_reader:
            c = 0
            for row in col:
                # i've added some styling
                label = Label(mainframe, width=15, height=2, font='Helvetica 14',
                              text=row, relief=RIDGE)
                label.grid(row=r, column=c)

                if c==2:
                    total_price += float(row)

                c += 1
            r += 1

    ttk.Label(mainframe, text= 'Total Price:' + str(total_price), font=("Courier", 25)).grid(row=r+1,columnspan=3)
    ttk.Button(mainframe, text='Back to menu', command=lambda: main_window(user_name, payup_root)).grid(row=r + 2,column=2, columnspan=1)
    ttk.Button(mainframe, text='Send Delivery', command=lambda: pay_and_finish(payup_root)).grid(row=r + 2, column=0)


def store_window(usr_name, main_root):
    global shopped
    main_root.destroy()
    shopped = True
    f = open('order.txt', 'r+')
    f.truncate(0)
    store_root = Tk()
    store_root.eval('tk::PlaceWindow . center')
    store_root.title('Store Page')

    mainframe = ttk.Frame(store_root, padding='3 3 12 12 ')
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    store_root.columnconfigure(0, weight=1)
    store_root.rowconfigure(0, weight=1)

    notebook = ttk.Notebook(mainframe)
    vegetable_tab = ttk.Frame(notebook)
    drinks_tab = ttk.Frame(notebook)

    notebook.add(vegetable_tab, text='vegetable tab')
    notebook.add(drinks_tab, text='drinks tab')
    notebook.pack(expand=1, fill="both")

    ##### Vegetables ####
    ttk.Label(vegetable_tab, text='Tomatoes').grid(column=0, row=0)
    tomatoes_combo = ttk.Combobox(vegetable_tab, values=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    tomatoes_combo.grid(column=1, row=0)
    tomatoes_combo.current(0)

    ttk.Label(vegetable_tab, text='Lettuce').grid(column=0, row=1)
    lettuce_combo = ttk.Combobox(vegetable_tab, values=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    lettuce_combo.grid(column=1, row=1)
    lettuce_combo.current(0)

    ttk.Label(vegetable_tab, text='White Onion').grid(column=0, row=2)
    white_onion_combo = ttk.Combobox(vegetable_tab, values=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    white_onion_combo.grid(column=1, row=2)
    white_onion_combo.current(0)

    ttk.Label(vegetable_tab, text='Red Onion').grid(column=0, row=3)
    red_onion_combo = ttk.Combobox(vegetable_tab, values=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    red_onion_combo.grid(column=1, row=3)
    red_onion_combo.current(0)

    ttk.Label(vegetable_tab, text='Potato').grid(column=0, row=4)
    potato_combo = ttk.Combobox(vegetable_tab, values=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    potato_combo.grid(column=1, row=4)
    potato_combo.current(0)

    ttk.Button(vegetable_tab, text='Add To Cart', command=lambda: add_to_cart(
        {'Tomato': int(tomatoes_combo.get()), 'Lettuce': int(lettuce_combo.get()),
         'White Onion': int(white_onion_combo.get()),
         'Red Onion': int(red_onion_combo.get()), 'Potato': int(potato_combo.get())}, 'veg')).grid(column=0, row=5, columnspan=2)

    ###### Drinks ######
    ttk.Label(drinks_tab, text='Coca-Cola').grid(column=0, row=0)
    cola_combo = ttk.Combobox(drinks_tab, values=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    cola_combo.grid(column=1, row=0)
    cola_combo.current(0)

    ttk.Label(drinks_tab, text='Sprite').grid(column=0, row=1)
    sprite_combo = ttk.Combobox(drinks_tab, values=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    sprite_combo.grid(column=1, row=1)
    sprite_combo.current(0)

    ttk.Label(drinks_tab, text='Water').grid(column=0, row=2)
    water_combo = ttk.Combobox(drinks_tab, values=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    water_combo.grid(column=1, row=2)
    water_combo.current(0)

    ttk.Label(drinks_tab, text='Sparklink Water').grid(column=0, row=3)
    sparkling_combo = ttk.Combobox(drinks_tab, values=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    sparkling_combo.grid(column=1, row=3)
    sparkling_combo.current(0)

    ttk.Button(drinks_tab, text='Add To Cart', command=lambda: add_to_cart(
        {'Coca-Cola': int(cola_combo.get()), 'Sprite': int(sprite_combo.get()),
         'Water': int(water_combo.get()),
         'Sparkling Water': int(sparkling_combo.get())}, 'drinks')).grid(column=0, row=5, columnspan=2)

    ttk.Button(mainframe, text='Back To menu', command=lambda: main_window(usr_name, store_root)).pack()
    store_root.mainloop()


def login_window(main_root):
    main_root.destroy()
    login_root = Tk()
    login_root.eval('tk::PlaceWindow . center')
    login_root.title('Sign-in Page')

    mainframe = ttk.Frame(login_root, padding='3 3 12 12 ')
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

    Label(mainframe, text= 'Login Page',font='Helvetica 25 bold', bg='gray94', relief='raised').grid(row=0,columnspan=3)

    ttk.Label(mainframe, text="Enter User Name:  ").grid(column=1, row=1,pady=10, sticky=W)
    user_name = StringVar()
    user_name_entry = ttk.Entry(mainframe, width=7, textvariable=user_name)
    user_name_entry.grid(column=2, row=1,pady=10)

    ttk.Label(mainframe, text="Enter Password:  ").grid(column=1, row=2,pady=10, sticky=W)
    password = StringVar()
    password_entry = ttk.Entry(mainframe, width=7, textvariable=password, show='*')
    password_entry.grid(column=2, row=2,pady=10)

    ttk.Button(mainframe, text='Quit',
               command=exit).grid( row=3,pady=5,column=1)

    ttk.Button(mainframe, text='Login',
               command=lambda: check_user_and_pass(user_name.get(), password.get(), login_root)).grid(column=2, row=3,pady=5,sticky=W)


    login_root.mainloop()


def sign_up_window(main_root):
    main_root.destroy()
    sign_up_root = Tk()
    sign_up_root.eval('tk::PlaceWindow . center')
    sign_up_root.title("Registration Form")
    mainframe = ttk.Frame(sign_up_root, padding='3 3 12 12 ')
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

    user_name = StringVar()
    ttk.Label(mainframe, text='User Name:', width=10).grid(column=0, row=1)
    ttk.Entry(mainframe, textvariable=user_name, width=20).grid(column=1, row=1)

    password = StringVar()
    ttk.Label(mainframe, text='Password:', width=10).grid(column=0, row=2)
    ttk.Entry(mainframe, textvariable=password, width=20).grid(column=1, row=2)

    ttk.Label(mainframe, text='Age', width=10).grid(column=0, row=3)
    age_var = IntVar()
    ttk.Radiobutton(mainframe, text="Male", variable=age_var, value=1).grid(column=1, row=3, sticky=W)
    ttk.Radiobutton(mainframe, text="Female", variable=age_var, value=2).grid(column=1, row=3, sticky=E)

    ttk.Button(mainframe, text='Submit', width=20,
               command=lambda: add_account(user_name, password, age_var, sign_up_root)).grid(column=0, row=5,
                                                                                             columnspan=2)
    # it is use for display the registration form on the window
    sign_up_root.mainloop()


main_window('', None)
