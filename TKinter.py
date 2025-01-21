from tkinter import Tk, Entry, Button, Label, StringVar
from xml.dom.minidom import Document

window = Tk()
window.geometry("600x250")
window.title(" igbo Dictionary")

entry_text = Entry(window)
entry_text.pack()

result=StringVar()
result_label= Label(window, textvariable=result)
result_label.pack()

igbo_dict = {
    "come": "bia",
    "go": "gawa",
    "head": "isi"
    "leg": "ukwu",
    "sit": "nodu"
    "car": "ugbo ala"
    "house": "ulo"
    "child": "nwa"
    "plate": "efere"
    "dog": "nkita"
    "bag": "akpa"
    "eye": "anya"
    "school": "ulo akwu"
     "phone": "ekwenti"
     "food": "nri"
   "ball" : "boolu"
    "cage": "onu"


}
Tabine|Edit|Test|Explain|Document|Ask
def search (word):
    if word in igbo_dict:
        result.set(igbo_dict[word])
    else:
        result.set("Not found")
        print("Not found")

        search_btn = Button(window, text="searc", command=lambda: search(entry_text.get())
        search_btn.pack()

        window.mainloop()

