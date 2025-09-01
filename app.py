import tkinter as tk
from math import sin, cos, tan, log
import random

# تابع برای انجام محاسبات
def calculate(operation):
    try:
        # ارزیابی عبارت ریاضی
        result = eval(operation)
        entry_var.set(result)
        history.append(operation + " = " + str(result))  # ذخیره تاریخچه
        update_history()
    except Exception as e:
        # در صورت خطا، پیام خطا را نمایش می‌دهد
        entry_var.set("خطا")

# تابع برای افزودن عدد یا علامت به نمایشگر
def press(key):
    current = entry_var.get()
    entry_var.set(current + str(key))

# تابع برای پاک کردن نمایشگر
def clear():
    entry_var.set("")

# تابع برای به‌روزرسانی تاریخچه
def update_history():
    history_display.delete(1.0, tk.END)  # پاک کردن نمایشگر تاریخچه
    for item in history:
        history_display.insert(tk.END, item + "\n")  # نمایش تاریخچه

# تابع محاسبات مالی
def calculate_interest(principal, rate, time):
    # محاسبه بهره مرکب
    try:
        principal = float(principal)
        rate = float(rate)
        time = float(time)
        return principal * (1 + rate / 100) ** time
    except ValueError:
        return "خطا"

# تابع محاسبات آماری
def calculate_statistics(numbers):
    try:
        numbers = list(map(float, numbers.split(',')))  # تبدیل ورودی به لیست اعداد
        mean = sum(numbers) / len(numbers)
        variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
        stddev = variance ** 0.5
        return f"میانگین: {mean}, واریانس: {variance}, انحراف معیار: {stddev}"
    except Exception:
        return "خطا"

# تابع تبدیل واحد
def convert_temperature(celsius):
    try:
        celsius = float(celsius)
        return (celsius * 9/5) + 32  # سلسیوس به فارنهایت
    except ValueError:
        return "خطا"

# ایجاد پنجره اصلی
root = tk.Tk()
root.title("ماشین حساب پیشرفته")
root.geometry("600x600")
root.config(bg="#2e2e2e")  # رنگ پس‌زمینه

# متغیر برای نمایشگر
entry_var = tk.StringVar()
history = []  # لیست برای ذخیره تاریخچه

# ایجاد نمایشگر
entry = tk.Entry(root, textvariable=entry_var, font=('Arial', 20), bd=10, insertwidth=2, width=14, borderwidth=4)
entry.grid(row=0, column=0, columnspan=4)

# ایجاد نمایشگر تاریخچه
history_display = tk.Text(root, height=10, width=50, bg="#3e3e3e", fg="white")
history_display.grid(row=5, column=0, columnspan=4)

# دکمه‌های عددی و عملیاتی
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+',
    'sin', 'cos', 'tan', 'log',
    'interest', 'stats', 'convert', 'random'
]

# ایجاد دکمه‌ها و چیدمان آن‌ها
row_val = 1
col_val = 0
for button in buttons:
    if button == 'C':
        tk.Button(root, text=button, padx=20, pady=20, command=clear, bg="#5d5d5d", fg="white").grid(row=row_val, column=col_val)
    elif button == '=':
        tk.Button(root, text=button, padx=20, pady=20, command=lambda: calculate(entry_var.get()), bg="#5d5d5d", fg="white").grid(row=row_val, column=col_val)
    elif button in ['sin', 'cos', 'tan', 'log']:
        tk.Button(root, text=button, padx=20, pady=20, command=lambda key=button: press(key + '('), bg="#5d5d5d", fg="white").grid(row=row_val, column=col_val)
    elif button == 'interest':
        tk.Button(root, text=button, padx=20, pady=20, command=lambda: press('calculate_interest('), bg="#5d5d5d", fg="white").grid(row=row_val, column=col_val)
    elif button == 'stats':
        tk.Button(root, text=button, padx=20, pady=20, command=lambda: press('calculate_statistics('), bg="#5d5d5d", fg="white").grid(row=row_val, column=col_val)
    elif button == 'convert':
        tk.Button(root, text=button, padx=20, pady=20, command=lambda: press('convert_temperature('), bg="#5d5d5d", fg="white").grid(row=row_val, column=col_val)
    elif button == 'random':
        tk.Button(root, text=button, padx=20, pady=20, command=lambda: press(str(random.randint(1, 100))), bg="#5d5d5d", fg="white").grid(row=row_val, column=col_val)
    else:
        tk.Button(root, text=button, padx=20, pady=20, command=lambda key=button: press(key), bg="#5d5d5d", fg="white").grid(row=row_val, column=col_val)
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# اجرای حلقه اصلی
root.mainloop()
