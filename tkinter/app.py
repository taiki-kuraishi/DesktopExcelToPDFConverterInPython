import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox

def say_helloWorld():
    # tkinter.messagebox.showinfo(title="Say",message="Hello, World!")
    file_path = filedialog.askopenfilename()

    if file_path:
        print("Selected file:", file_path)
    else:
        print("No file selected.")

root = tk.Tk()
button = tkinter.Button(root,text="Click me!",command=say_helloWorld)
button.pack()
root.title(u"DesktopExcelToPDFConverterInPython")
root.geometry("800x500")
root.mainloop()