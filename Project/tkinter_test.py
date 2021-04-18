from tkinter import *
from tkinter import ttk
window = Tk()


window.title("Flood Prediction using ML")
width = window.winfo_screenwidth()
height = window.winfo_screenheight()

window.geometry("%dx%d" % (width-50, height-50))
window.configure(background="grey")

Label(window, text="Flood Prediction using Machine Learning",
      font=("Arial", 25)).grid(row=0, column=5)


state_options = [
    "Andaman & Nicobar Islands",
    "Arunachal Pradesh"
    "Assam & Meghalaya",
    "Bihar",
    "Chhattisgarh",
    "Coastal Andhra Pradesh",
    "Coastal Karnataka",
    "East Madhya Pradesh",
    "East Rajasthan",
    "East Uttar Pradesh",
    "Gangetic West Bengal",
    "Gujarat Region",
    "Haryana Delhi & Chandigarh",
    "Himachal Pradesh",
    "Jammu & Kashmir",
    "Jharkhand",
    "Kerala",
    "Konkan & Goa",
    "Lakshadweep",
    "Madhya Maharashtra",
    "Matathwada",
    "Naga Mani Mizo Tripura",
    "North Interior Karnataka",
    "Orissa",
    "Punjab",
    "Rayalseema",
    "Saurashtra & Kutch",
    "South Interior Karnataka",
    "Sub Himalayan West Bengal & Sikkim",
    "Tamil Nadu",
    "Telangana",
    "Uttarakhand",
    "Vidarbha",
    "West Madhya Pradesh",
    "West Rajasthan",
    "West Uttar Pradesh"
]

month_options = [
    "jan",
    "feb",
    "mar",
    "apr",
    "may",
    "jun",
    "jul",
    "aug",
    "sep",
    "oct",
    "nov",
    "dec",
    "annual",
    "jf",
    "mam",
    "jjas",
    "ond"
]

Label().grid(row=2)
state_selection_label = Label(
    window, text="Select State").grid(row=3, column=5)
month_selection_label = Label(window, text="Month").grid(row=4, column=5)

# Entry(window).grid(row=3, column=6)
clicked = StringVar()
clicked.set("Please Select")
state_selected = OptionMenu(
    window, clicked, *state_options).grid(row=3, column=6)
month_selected = OptionMenu(
    window, clicked, *month_options).grid(row=4, column=6)


btn = ttk.Button(window, text="Submit").grid(row=5, column=6)


window.mainloop()
