#add tkinter basic template

from tkinter import *
root=Tk()
root.title("My Drivers License")
root.geometry("400x400")


root.configure(bg="white")
canvas = Canvas(root, width=400, height=400)
canvas.create_image(0, 0, anchor=NW)
canvas.create_rectangle(0, 0, 410, 55, fill="#fcd408")


label_heading = canvas.create_text(200, 35, font=('Times', '24', 'bold italic'), text="Drivers License")
label_id_tag = canvas.create_text(37, 70, font=('Times', '12'), text="ID :")
label_name_tag = canvas.create_text(50, 120, font=('Times', '12'), text="Name :")
label_dob_tag = canvas.create_text(50, 150, font=('Times', '12' ), text="D.O.B :")
label_pin_tag = canvas.create_text(65, 180, font=('Times', '12'), text="Pin Number :")
label_adress_tag = canvas.create_text(50, 210, font=('Times', '12'), text="Adress :")
label_authorization_tag = canvas.create_text(67, 240, font=('Times', '12'), text="Authorization :")

#add label for name
label_id=Label(root)
#add label for grade
label_name=Label(root)
#add label for Subjects
label_dob=Label(root)
label_pin=Label(root)
label_adress=Label(root)
label_authorization=Label(root)
#add function
def myCardDetails():  
    label_id['text'] = 19849548543
    label_name['text'] = "Krisha Sureka"
    label_dob['text'] = "23 February 2009"
    label_pin['text'] = "560384"
    label_adress['text'] = "Disney Land, Honk Kong"
    label_authorization['text'] = ["two", "four", "six"]

#add button
button1=Button(root,text="Show ID card", command=myCardDetails)
button1.configure(width=20, activebackground="#9EC6EE", relief=FLAT)
button1_window = canvas.create_window(100, 300, anchor=CENTER, window=button1)
label_id_window = canvas.create_window(120, 70, anchor=CENTER, window=label_id)
label_name_window = canvas.create_window(120, 120, anchor=CENTER, window=label_name)
label_dob_window = canvas.create_window(120, 150, anchor=CENTER, window=label_dob)
label_pin_window = canvas.create_window(155, 180, anchor=CENTER, window=label_pin)
label_adress_window = canvas.create_window(155, 210, anchor=CENTER, window=label_adress)
label_authorization_window = canvas.create_window(155, 240, anchor=CENTER, window=label_authorization)
canvas.pack()

#tkinter basic template end statement
root.mainloop()