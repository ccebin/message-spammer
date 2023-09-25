import tkinter as tk
from tkinter import ttk
from tkinter import font as tkfont
import keyboard
import threading
import time


is_running = False
stop_thread = False


def send_message():
    message = message_entry.get()
    if message:
        keyboard.write(message)
        keyboard.press_and_release('enter')

def auto_send_message():
    global is_running, stop_thread
    interval = int(interval_entry.get())  
    while is_running:
        send_message()
        time.sleep(interval / 1000)
        if stop_thread:
            break

def start_or_stop():
    global is_running, stop_thread
    if not is_running:
        try:
            interval = int(interval_entry.get())
        except ValueError:
            return  
        is_running = True
        stop_thread = False
        interval_entry.config(state="disabled")
        message_entry.config(state="disabled")
        threading.Thread(target=auto_send_message).start()
        start_stop_button.config(text="Durdur", bg="red")
        send_button.config(state="disabled")
    else:
        is_running = False
        stop_thread = True
        interval_entry.config(state="normal")
        message_entry.config(state="normal")
        start_stop_button.config(text="Başlat", bg="green")
        send_button.config(state="normal")


app = tk.Tk()
app.title("cebin Spammer")


app.iconbitmap('icon.ico')


app.geometry("400x300")
app.resizable(width=False, height=False)


app.attributes("-alpha", 0.8) 
app.configure(bg="black")  


app.update_idletasks()
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
x = (screen_width - app.winfo_reqwidth()) // 2
y = (screen_height - app.winfo_reqheight()) // 2
app.geometry("+{}+{}".format(x, y))


custom_font = tkfont.Font(family="Arial", size=16)


message_label = tk.Label(app, text="Mesajınızı girin:", fg="green", bg="black", font=custom_font)
message_label.pack(pady=(50, 5))

message_entry = tk.Entry(app, bg="white", fg="black", width=30, font=custom_font)
message_entry.pack(pady=5)


interval_label = tk.Label(app, text="Gönderme aralığını ms cinsinden girin:", fg="green", bg="black", font=custom_font)
interval_label.pack()



style = ttk.Style()
style.configure("TEntry", foreground="black", background="white")  
interval_entry = ttk.Entry(app, validate="key", validatecommand=(app.register(lambda P: P.isdigit()), '%P'), width=30, font=custom_font, style="TEntry")
interval_entry.pack()


start_stop_button = tk.Button(app, text="Başlat", command=start_or_stop, fg="white", bg="green", width=10, font=custom_font)
start_stop_button.pack(pady=20)


app.mainloop()
