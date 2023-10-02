import tkinter as tk

def submit():
    user_input = entry.get()
    result_label.config(text=f"You entered: {user_input}")


app = tk.Tk()
app.title("Unique Python Form")


label = tk.Label(app, text="Enter something:")
entry = tk.Entry(app)
submit_button = tk.Button(app, text="Submit", command=submit)
result_label = tk.Label(app, text="")


label.grid(row=0, column=0, padx=10, pady=10)
entry.grid(row=0, column=1, padx=10, pady=10)
submit_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)


app.mainloop()
