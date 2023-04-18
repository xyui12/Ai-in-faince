import speech_recognition as sr
# from PIL import Image, ImageTk
from tkinter import *
from tkinter import messagebox, simpledialog

def login():
    username = username_entry.get()
    password = password_entry.get()
    if username == "bp" and password == "bp":
        # messagebox.showinfo("Success", "Hello Bhanu, Welcome to money wallet.")
        root.destroy() 
        open_main_window() 
    else:
        messagebox.showerror("Error", "Incorrect username or password")

def cancel():
    root.destroy()

def open_main_window(): 
    from PIL import Image, ImageTk

    class PaymentInterface:
        def __init__(self):
            self.balance = 0.0

            self.window = Tk()
            self.window.title("Money Wallet")
            self.window.geometry("700x450")

            bg_image = Image.open("aibg4.jpg")
            bg_photo = ImageTk.PhotoImage(bg_image)
            bg_label = Label(self.window, image=bg_photo)
            bg_label.place(x=0, y=0, relwidth=1, relheight=1)

            self.balance_label = Label(self.window, font = ("Arial", 20), text=f"Balance: ₹ {self.balance}")
            self.balance_label.place(x=270,y=30)

            self.add_money_button = Button(self.window, text="Add Money", font = ("Arial", 11), command=self.add_money)
            self.add_money_button.place(x=60,y=150)

            self.send_money_button = Button(self.window, text="Send Money", font = ("Arial", 11), command=self.send_money)
            self.send_money_button.place(x=60,y=210)

            self.check_balance_button = Button(self.window, text="Check Balance", font = ("Arial", 11), command=self.check_balance)
            self.check_balance_button.place(x=60,y=270)

            self.mobile_label = Label(self.window, font = ("Arial", 13), text="Mobile Recharge")
            self.mobile_label.place(x=200,y=100)

            self.prepaid_button = Button(self.window, text="Prepaid", font = ("Arial", 11), command=self.prepaid)
            self.prepaid_button.place(x=220,y=150)

            self.postpaid_button = Button(self.window, text="Postpaid", font = ("Arial", 11), command=self.postpaid)
            self.postpaid_button.place(x=220,y=210)

            self.electricity_label = Label(self.window, font = ("Arial", 13), text="Bill Payment")
            self.electricity_label.place(x=390,y=100)

            self.electricity_button = Button(self.window, text="Electricity", font = ("Arial", 11), command=self.electricity)
            self.electricity_button.place(x=400,y=150)

            self.water_button = Button(self.window, text="Water Bill", font = ("Arial", 11), command=self.water_bill)
            self.water_button.place(x=400,y=210)

            self.gas_button = Button(self.window, text="Gas Cylinder", font = ("Arial", 11), command=self.gas_bill)
            self.gas_button.place(x=400,y=270)

            self.insurance_label = Label(self.window, font = ("Arial", 13), text="Pay Insurance")
            self.insurance_label.place(x=570,y=100)

            self.car_insurance_button = Button(self.window, text="Car Insurance", font = ("Arial", 11), command=self.car_insurance)
            self.car_insurance_button.place(x=570,y=150)

            self.bike_insurance_button = Button(self.window, text="Bike Insurance", font = ("Arial", 11), command=self.bike_insurance)
            self.bike_insurance_button.place(x=570,y=210)

            self.exit_button = Button(self.window, text="Exit", font = ("Arial",12), command=self.window.destroy)
            self.exit_button.place(x=340,y=350)

            self.window.mainloop()

        def add_money(self):
            recognizer = sr.Recognizer()
            microphone = sr.Microphone()

            with microphone as source:
                recognizer.adjust_for_ambient_noise(source)
                messagebox.showinfo("Deposit", "Say to add amount.")
                audio = recognizer.listen(source)

            try:
                add_amount = float(recognizer.recognize_google(audio))
                password = simpledialog.askfloat("Deposit", f"You are adding ₹ {recognizer.recognize_google(audio)} \nEnter your password:")
                if password == 12345:
                    self.balance += add_amount
                    messagebox.showinfo("Money added Success", f"You have successfully added ₹ {add_amount} to your account. Your new account balance is ₹ {self.balance}.")
                    self.balance_label.config(text=f"Balance: ₹ {self.balance}")
                else:
                    messagebox.showerror("Deposit Error", " Your password is required. Please try again.")
            except sr.UnknownValueError:
                messagebox.showerror("Deposit Error", "Sorry, I did not understand that. Please try again.")
            except sr.RequestError:
                messagebox.showerror("Deposit Error", "Sorry, there was an error processing your request. Please try again.")

        def send_money(self):
            recognizer = sr.Recognizer()
            microphone = sr.Microphone()

            with microphone as source:
                recognizer.adjust_for_ambient_noise(source)
                messagebox.showinfo("Transfer", "Please speak to transfer amount.")
                audio = recognizer.listen(source)

            try:
                send_amount = float(recognizer.recognize_google(audio))
                if send_amount <= self.balance:
                    with microphone as source:
                        recognizer.adjust_for_ambient_noise(source)
                        messagebox.showinfo("Recipient Name", f"You are sending ₹ {recognizer.recognize_google(audio)} \nSay recipient name.")
                        audio = recognizer.listen(source)
                    recipient_name = recognizer.recognize_google(audio)
                    if recipient_name is not None and len(recipient_name.strip()) > 0:
                        self.balance -= send_amount
                        messagebox.showinfo("Transfer Success", f"Your transfer of ₹ {send_amount} to {recipient_name} is successful. Your new account balance is ₹ {self.balance}.")
                        self.balance_label.config(text=f"Balance: ₹ {self.balance}")
                    else:
                        messagebox.showerror("Transfer Error", " Recipient name is required. Please try again.")
                else:
                    messagebox.showerror("Transfer Failed", "You have insufficient balance, Please add money.")
            except ValueError:
                messagebox.showerror("Transfer Error", "Invalid transfer amount. Please try again.")
            except sr.UnknownValueError:
                messagebox.showerror("Transfer Error", "Sorry, I did not understand that. Please try again.")
            except sr.RequestError:
                messagebox.showerror("Transfer Error", "Sorry, there was an error processing your request. Please try again.")

        def check_balance(self):
            messagebox.showinfo("Account Balance", f"Your Account Balance is ₹ {self.balance}.")
            self.balance_label.config(text=f"Balance: ₹ {self.balance}")

        def prepaid(self):
            prepaid_number = simpledialog.askinteger("Prepaid", "Enter your mobile number:")
            if prepaid_number is not None:
                prepaid_amount = simpledialog.askinteger("Prepaid", "Enter amount:")
                if prepaid_amount <= self.balance:
                    self.balance -= prepaid_amount
                    messagebox.showinfo("Prepaid Success", f"Your recharge of ₹ {prepaid_amount} to number {prepaid_number} is successful. Your new account balance is ₹ {self.balance}.")
                    self.balance_label.config(text=f"Balance: ₹ {self.balance}")
                else:
                    messagebox.showerror("Error", "You have insufficient balance, Please add money.")

        def postpaid(self):
            postpaid_number = simpledialog.askinteger("Postpaid", "Enter your mobile number:")
            if postpaid_number is not None:
                postpaid_amount = simpledialog.askinteger("Postpaid", "Enter amount:")
                if postpaid_amount <= self.balance:
                    self.balance -= postpaid_amount
                    messagebox.showinfo("Postpaid Success", f"Your recharge of ₹ {postpaid_amount} to number {postpaid_number} is successful. Your new account balance is ₹ {self.balance}.")
                    self.balance_label.config(text=f"Balance: ₹ {self.balance}")
                else:
                    messagebox.showerror("Error", "You have insufficient balance, Please add money.")

        def electricity(self):
            recipient_name = simpledialog.askstring("Electricity Bill", "Enter company name:")
            if recipient_name is not None and len(recipient_name.strip()) > 0:
                electricity_amount = simpledialog.askfloat("Bill Amount", "Enter bill amount:")
                if electricity_amount <= self.balance:
                    self.balance -= electricity_amount
                    messagebox.showinfo("Electricity bill Success", f"Your electricity bill of ₹ {electricity_amount} to {recipient_name} is successful. Your new account balance is ₹ {self.balance}.")
                    self.balance_label.config(text=f"Balance: ₹ {self.balance}")
                else:
                    messagebox.showerror("Error", "You have insufficient balance, Please add money.")
            else:
                messagebox.showerror("Error", "Company name is required. Please try again.")
        
        def water_bill(self):
            recognizer = sr.Recognizer()
            microphone = sr.Microphone()

            with microphone as source:
                recognizer.adjust_for_ambient_noise(source)
                messagebox.showinfo("Company name", "Please speak your company name.")
                audio = recognizer.listen(source)

            try:
                recipient_name = recognizer.recognize_google(audio)
                if recipient_name is not None and len(recipient_name.strip()) > 0:
                    with microphone as source:
                        recognizer.adjust_for_ambient_noise(source)
                        messagebox.showinfo("Bill Amount", f"You are paying bill to {recognizer.recognize_google(audio)} \nSay bill amount.")
                        audio = recognizer.listen(source)
                    water_amount = float(recognizer.recognize_google(audio))
                    if water_amount <= self.balance:
                        self.balance -= water_amount
                        messagebox.showinfo("Transfer Success", f"Your transfer of ₹ {water_amount} to company {recipient_name} is successful. Your new account balance is ₹ {self.balance}.")
                        self.balance_label.config(text=f"Balance: ₹ {self.balance}")
                    else:
                        messagebox.showerror("Transfer Failed", "You have insufficient balance, Please add money.")
                else:
                    messagebox.showerror("Transfer Error", " Company name is required. Please try again.")
            except ValueError:
                messagebox.showerror("Transfer Error", "Invalid transfer amount. Please try again.")
            except sr.UnknownValueError:
                messagebox.showerror("Transfer Error", "Sorry, I did not understand that. Please try again.")
            except sr.RequestError:
                messagebox.showerror("Transfer Error", "Sorry, there was an error processing your request. Please try again.")

        def gas_bill(self):
            recipient_name = simpledialog.askstring("Gas Bill", "Enter company name:")
            if recipient_name is not None and len(recipient_name.strip()) > 0:
                gas_amount = simpledialog.askfloat("Bill Amount", "Enter bill amount:")
                if gas_amount <= self.balance:
                    self.balance -= gas_amount
                    messagebox.showinfo("Gas Bill Success", f"Your gas bill of ₹ {gas_amount} to {recipient_name} is successful. Your new account balance is ₹ {self.balance}.")
                    self.balance_label.config(text=f"Balance: ₹ {self.balance}")
                else:
                    messagebox.showerror("Error", "You have insufficient balance, Please add money.")
            else:
                messagebox.showerror("Error", "Company name is required. Please try again.")

        def car_insurance(self):
            recipient_name = simpledialog.askstring("Car Insurance ", "Enter insurance company name:")
            if recipient_name is not None and len(recipient_name.strip()) > 0:
                car_amount = simpledialog.askfloat("Insurance Amount", "Enter insurance amount:")
                if car_amount <= self.balance:
                    self.balance -= car_amount
                    messagebox.showinfo("Car insurance Success", f"Your insurance bill of ₹ {car_amount} to {recipient_name} is succcessful. Your new account balance is ₹ {self.balance}.")
                    self.balance_label.config(text=f"Balance: ₹ {self.balance}")
                else:
                    messagebox.showerror("Error", "You have insufficient balance, Please add money.")
            else:
                messagebox.showerror("Error", "Company name is required. Please try again.")

        def bike_insurance(self):
            recognizer = sr.Recognizer()
            microphone = sr.Microphone()

            with microphone as source:
                recognizer.adjust_for_ambient_noise(source)
                messagebox.showinfo("Company name", "Please speak insurance company name.")
                audio = recognizer.listen(source)

            try:
                recipient_name = recognizer.recognize_google(audio)
                if recipient_name is not None and len(recipient_name.strip()) > 0:
                    with microphone as source:
                        recognizer.adjust_for_ambient_noise(source)
                        messagebox.showinfo("Insurance Amount", f"You are paying bill to {recognizer.recognize_google(audio)} \nSay bill amount.")
                        audio = recognizer.listen(source)
                    bike_amount = float(recognizer.recognize_google(audio))
                    if bike_amount <= self.balance:
                        self.balance -= bike_amount
                        messagebox.showinfo("Transfer Success", f"Your transfer of ₹ {bike_amount} to company {recipient_name} is successful. Your new account balance is ₹ {self.balance}.")
                        self.balance_label.config(text=f"Balance: ₹ {self.balance}")
                    else:
                        messagebox.showerror("Transfer Failed", "You have insufficient balance, Please add money.")
                else:
                    messagebox.showerror("Transfer Error", " Company name is required. Please try again.")
            except ValueError:
                messagebox.showerror("Transfer Error", "Invalid transfer amount. Please try again.")
            except sr.UnknownValueError:
                messagebox.showerror("Transfer Error", "Sorry, I did not understand that. Please try again.")
            except sr.RequestError:
                messagebox.showerror("Transfer Error", "Sorry, there was an error processing your request. Please try again.")

    PaymentInterface() 

from PIL import Image, ImageTk
root = Tk()
root.title("Login Page")
root.geometry("450x250")

bg_image = Image.open("aibg3.jpg")
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

username_label = Label(root, text="Username",font = ("Arial", 12))
username_label.place(x=50, y=30)
username_entry = Entry(root, font=(8))
username_entry.place(x=150, y=30)

password_label = Label(root, text="Password", font = ("Arial", 12))
password_label.place(x=50, y=80)
password_entry = Entry(root, font=(8), show="*")
password_entry.place(x=150, y=80)

login_button = Button(root, text="Login", font = ("Arial", 12), command=login)
login_button.place(x=180, y=140)
cancel_button = Button(root, text="Cancel", font = ("Arial", 12), command=cancel)
cancel_button.place(x=260, y=140)

root.mainloop()
