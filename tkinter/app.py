import tkinter as ttk
from tkinter import filedialog, messagebox
from tkinter.constants import END


def select_path():
    if radio_var.get() == 1:
        file_path = filedialog.askopenfilename()
    elif radio_var.get() == 2:
        file_path = filedialog.askdirectory()
    else:
        print("Error")

    entry.delete(0, END)
    entry.insert(ttk.END, file_path)

    print(file_path)


root = ttk.Tk()
root.title(u"DesktopExcelToPDFConverterInPython")
root.geometry("800x500")

# frameの作成
top_frame = ttk.Frame(root, bg='white', borderwidth=5, relief='ridge')
top_frame.pack(fill='x')

# columnconfigureを使用して、各列の幅を設定する
top_frame.columnconfigure(0, weight=1)
top_frame.columnconfigure(1, weight=1)
top_frame.columnconfigure(2, weight=1)
top_frame.columnconfigure(3, weight=1)

# radio bottom value
radio_var = ttk.IntVar()
radio_var.set(1)

# radioボタンの作成
file_radio = ttk.Radiobutton(
    top_frame, text='chose file', variable=radio_var, value=1)
file_radio.configure(background='white', foreground='black')
file_radio.grid(row=0, column=0, columnspan=2, sticky='e')

folder_radio = ttk.Radiobutton(
    top_frame, text='chose folder', variable=radio_var, value=2)
folder_radio.configure(background='white', foreground='black')
folder_radio.grid(row=0, column=2, columnspan=2, sticky='w')

# entryの作成
entry = ttk.Entry(top_frame, width=30)
entry.configure(background='white', foreground='black')
entry.grid(row=1, column=1, columnspan=2, sticky='we')
entry.focus_set()

button = ttk.Button(top_frame, text="Click me!", command=select_path)
button.configure(background='white', foreground='black')
button.grid(row=1, column=3, sticky='w')

# bttom frame
bottom_frame = ttk.Frame(root, bg='Blue')
bottom_frame.pack(fill='both', expand=True)

bottom_frame.rowconfigure(0, weight=1)

bottom_frame.columnconfigure(0, weight=1)
bottom_frame.columnconfigure(1, weight=1)
bottom_frame.columnconfigure(2, weight=1)
bottom_frame.columnconfigure(3, weight=1)

#side frame
side_frame = ttk.Frame(bottom_frame, bg='white', borderwidth=5, relief='ridge')
side_frame.grid(row=0, column=0, sticky='nswe')
ttk.Label(side_frame, text='side frame').pack()
ttk.Label(side_frame, text='side frame').pack()
ttk.Label(side_frame, text='side frame').pack()
ttk.Label(side_frame, text='side frame').pack()
ttk.Label(side_frame, text='side frame').pack()

#preview frame
preview_frame = ttk.Frame(bottom_frame, bg='white', borderwidth=5, relief='ridge')
preview_frame.grid(row=0, column=1, sticky='nswe',columnspan=3)


root.mainloop()