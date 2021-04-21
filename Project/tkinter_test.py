from tkinter import *
from tkinter import ttk
from main import main
import json

# Global variables
window = Tk()
state_options = [
    "Andaman & Nicobar Islands",
    "Arunachal Pradesh",
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

month_options = {
    "January": "jan",
    "February": "feb",
    "March": "mar",
    "April": "apr",
    "May": "may",
    "June": "jun",
    "July": "jul",
    "August": "aug",
    "September": "sep",
    "October": "oct",
    "November": "nov",
    "December": "dec",
    "Annual": "annual",
    "January - February": "jf",
    "March - April - May": "mam",
    "June - July - August - September": "jjas",
    "October - November - December": "ond"
}
state = StringVar()
month = StringVar()

main_object = main()
[x, y] = main_object.prepare_data()

[x_train, x_test, y_train, y_test] = main_object.prepare_model(x, y)
# print([x_train, x_test, y_train, y_test])


def output_to_gui():
    results = open('output.json', 'r')
    results = json.load(results)
    row_value = 10

    for result in results['scores']:
        print(result)
        Label(window, text="Algorithm:",
              font=("Helvetica", 25)).grid(row=row_value, column=4)
        Label(window, text=result['algorithm'], font=(
            "Helvetica", 25)).grid(row=row_value, column=5)

        Label(window, text="Prediction:",
              font=("Helvetica", 25)).grid(row=row_value, column=4)
        if(result['prediction'] == 'Yes'):
            Label(window, text="Yes it will flood!", font=(
                "Helvetica", 25)).grid(
                row=row_value+1, column=5)
        else:
            Label(window, text="No it will not flood!", font=(
                "Helvetica", 25)).grid(
                row=row_value+1, column=5)
        Label(window, text="Accuracy (in %):",
              font=("Helvetica", 25)).grid(row=row_value, column=4)
        Label(window, text=result['accuracy'], font=(
            "Helvetica", 25)).grid(row=row_value+2, column=5)
        Label().grid(row=row_value+3)
        row_value += 4


def run_algorithms():
    print(state.get())
    print(month.get())
    main_object.knn_algorithm(x_train, x_test, y_train,
                              y_test, state.get(), month_options[month.get()])
    main_object.logistic_regression(x_train, x_test, y_train,
                                    y_test, state.get(), month_options[month.get()])
    main_object.support_vector_algorithm(x_train, x_test, y_train,
                                         y_test, state.get(), month_options[month.get()])
    main_object.decision_tree(x_train, x_test, y_train,
                              y_test, state.get(), month_options[month.get()])
    output_to_gui()
    return


def state_and_month_selection():
    # Lables for the drop-down menus
    state_selection_label = Label(
        window, text="Select State/Region").grid(row=3, column=5)
    month_selection_label = Label(
        window, text="Select Month").grid(row=4, column=5)

    # State drop-down menu
    state.set("Please Select")
    state_selected = OptionMenu(
        window, state, *state_options).grid(row=3, column=6)

    # Month dropdown menu
    month.set("Please Select")
    month_selected = OptionMenu(
        window, month, *month_options).grid(row=4, column=6)

    # Submit Button
    btn = ttk.Button(window, text="Submit",
                     command=run_algorithms).grid(row=5, column=6)


def gui_base():
    window.title("Flood Prediction using ML")
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()

    window.geometry("%dx%d" % (width-50, height-50))
    window.configure(background="grey")

    Label(window, text="Flood Prediction using Machine Learning",
          font=("Arial", 25)).grid(row=0, column=5)
    Label().grid(row=2)         # Empty Line


gui_base()
state_and_month_selection()

window.mainloop()
