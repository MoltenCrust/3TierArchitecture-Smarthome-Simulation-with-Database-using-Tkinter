from tkinter import *
from datetime import datetime
import Db as dbs
import Service as service
import sqlite3
import os

now = datetime.now()

current_time = now.strftime("%H:%M:%S")

with sqlite3.connect("mydatabase.db") as db:
    c=db.cursor()

number  = 0
number2 = 0
number3 = 0
number4 = 0
number5 = 0
number6 = 0
number7 = 0
number8 = 0
total_p = 0
total_temp = 0

is_on = True
is_on1 = True
is_on2 = True
is_on3 = True
is_on4 = True
is_on5 = True
is_on6 = True
is_on7 = True
is_on8 = True
is_on9 = True
is_on10 = True

def ready():
    ### SWITCH FUNCTIONS ###
    def switch():
        conn = sqlite3.connect('mydatabase.db')
        c = conn.cursor()
        global current_time
        global is_on
        if is_on:
            light_button.config(image=on)
            light.config(fg="green")
            is_on = False
            c.execute("UPDATE changes SET changes=1 WHERE name='light_bed' ")
            c.execute("INSERT INTO history VALUES (?, ?)", ("Bedroom light is on at", current_time))

        elif is_on == False:
            light_button.config(image=off)
            light.config(fg="grey")
            is_on = True
            c.execute("UPDATE changes SET changes=0 WHERE name='light_bed' ")
            c.execute("INSERT INTO history VALUES (?, ?)", ("Bedroom light is off at", current_time))

        conn.commit()
        conn.close()

    def switch1():
        conn = sqlite3.connect('mydatabase.db')
        c = conn.cursor()
        global current_time
        global is_on1
        if is_on1:
            aircon_button.config(image=on)
            aircon.config(fg="green")
            is_on1 = False
            c.execute("UPDATE changes SET changes=1 WHERE name='aircon_bed' ")
            c.execute("INSERT INTO history VALUES (?, ?)", ("Bedroom aircon is on at", current_time))

        else:
            aircon_button.config(image=off)
            aircon.config(fg="grey")
            is_on1 = True
            c.execute("UPDATE changes SET changes=0 WHERE name='aircon_bed' ")
            c.execute("INSERT INTO history VALUES (?, ?)", ("Bedroom aircon is off at", current_time))

        conn.commit()
        conn.close()

    def switch2():
        conn = sqlite3.connect('mydatabase.db')
        c = conn.cursor()
        global current_time
        global is_on2
        if is_on2:
            music_button.config(image=on)
            music.config(fg="green")
            is_on2 = False
            c.execute("UPDATE changes SET changes=1 WHERE name='music_bed' ")
            c.execute("INSERT INTO history VALUES (?, ?)", ("Bedroom music is on at", current_time))

        else:
            music_button.config(image=off)
            music.config(fg="grey")
            is_on2 = True
            c.execute("UPDATE changes SET changes=0 WHERE name='music_bed' ")
            c.execute("INSERT INTO history VALUES (?, ?)", ("Bedroom music is off at", current_time))

        conn.commit()
        conn.close()

    def switch3():
        conn = sqlite3.connect('mydatabase.db')
        c = conn.cursor()
        global current_time
        global is_on3
        if is_on3:
            light_button2.config(image=on)
            light2.config(fg="green")
            is_on3 = False
            c.execute("UPDATE changes SET changes=1 WHERE name='light_bath' ")
            c.execute("INSERT INTO history VALUES (?, ?)", ("Bathroom light is on at", current_time))

        else:
            light_button2.config(image=off)
            light2.config(fg="grey")
            is_on3 = True
            c.execute("UPDATE changes SET changes=0 WHERE name='light_bath' ")
            c.execute("INSERT INTO history VALUES (?, ?)", ("Bathroom light is off at", current_time))

        conn.commit()
        conn.close()

    def switch4():
        conn = sqlite3.connect('mydatabase.db')
        c = conn.cursor()
        global current_time
        global is_on4
        if is_on4:
            music_button2.config(image=on)
            music2.config(fg="green")
            is_on4 = False
            c.execute("UPDATE changes SET changes=1 WHERE name='music_bath' ")
            c.execute("INSERT INTO history VALUES (?, ?)", ("Bathroom music is on at", current_time))

        else:
            music_button2.config(image=off)
            music2.config(fg="grey")
            is_on4 = True
            c.execute("UPDATE changes SET changes=0 WHERE name='music_bath' ")
            c.execute("INSERT INTO history VALUES (?, ?)", ("Bathroom music is off at", current_time))

        conn.commit()
        conn.close()

    def switch5():
        conn = sqlite3.connect('mydatabase.db')
        c = conn.cursor()
        global current_time
        global is_on5
        if is_on5:
            light_button3.config(image=on)
            light3.config(fg="green")
            is_on5 = False
            c.execute("UPDATE changes SET changes=1 WHERE name='light_liv' ")
            c.execute("INSERT INTO history VALUES (?, ?)", ("Living room light is on at", current_time))

        else:
            light_button3.config(image=off)
            light3.config(fg="grey")
            is_on5 = True
            c.execute("UPDATE changes SET changes=0 WHERE name='light_liv' ")
            c.execute("INSERT INTO history VALUES (?, ?)", ("Living room light is off at", current_time))

        conn.commit()
        conn.close()

    def switch6():
        conn = sqlite3.connect('mydatabase.db')
        c = conn.cursor()
        global current_time
        global is_on6
        if is_on6:
            aircon_button2.config(image=on)
            aircon2.config(fg="green")
            is_on6 = False
            c.execute("UPDATE changes SET changes=1 WHERE name='aircon_liv' ")
            c.execute("INSERT INTO history VALUES (?, ?)", ("Living room aircon is on at", current_time))

        else:
            aircon_button2.config(image=off)
            aircon2.config(fg="grey")
            is_on6 = True
            c.execute("UPDATE changes SET changes=0 WHERE name='aircon_liv' ")
            c.execute("INSERT INTO history VALUES (?, ?)", ("Living room aircon is off at", current_time))

        conn.commit()
        conn.close()

    def switch7():
        conn = sqlite3.connect('mydatabase.db')
        c = conn.cursor()
        global current_time
        global is_on7
        if is_on7:
            music_button3.config(image=on)
            music3.config(fg="green")
            is_on7 = False
            c.execute("UPDATE changes SET changes=1 WHERE name='music_liv' ")
            c.execute("INSERT INTO history VALUES (?, ?)", ("Living room music is on at", current_time))

        else:
            music_button3.config(image=off)
            music3.config(fg="grey")
            is_on7 = True
            c.execute("UPDATE changes SET changes=0 WHERE name='music_liv' ")
            c.execute("INSERT INTO history VALUES (?, ?)", ("Living room music is off at", current_time))

        conn.commit()
        conn.close()

    def switch8():
        conn = sqlite3.connect('mydatabase.db')
        c = conn.cursor()
        global current_time
        global is_on8
        if is_on8:
            light_button4.config(image=on)
            light4.config(fg="green")
            is_on8 = False
            c.execute("UPDATE changes SET changes=1 WHERE name='light_kit' ")
            c.execute("INSERT INTO history VALUES (?, ?)", ("Kitchen light is on at", current_time))

        else:
            light_button4.config(image=off)
            light4.config(fg="grey")
            is_on8 = True
            c.execute("UPDATE changes SET changes=0 WHERE name='light_kit' ")
            c.execute("INSERT INTO history VALUES (?, ?)", ("Kitchen light is off at", current_time))

        conn.commit()
        conn.close()

    def switch9():
        conn = sqlite3.connect('mydatabase.db')
        c = conn.cursor()
        global current_time
        global is_on9
        if is_on9:
            aircon_button3.config(image=on)
            aircon3.config(fg="green")
            is_on9 = False
            c.execute("UPDATE changes SET changes=1 WHERE name='aircon_kit' ")
            c.execute("INSERT INTO history VALUES (?, ?)", ("Kitchen aircon is on at", current_time))

        else:
            aircon_button3.config(image=off)
            aircon3.config(fg="grey")
            is_on9 = True
            c.execute("UPDATE changes SET changes=0 WHERE name='aircon_kit' ")
            c.execute("INSERT INTO history VALUES (?, ?)", ("Kitchen aircon is off at", current_time))

        conn.commit()
        conn.close()

    def switch10():
        conn = sqlite3.connect('mydatabase.db')
        c = conn.cursor()
        global current_time
        global is_on10
        if is_on10:
            music_button4.config(image=on)
            music4.config(fg="green")
            is_on10 = False
            c.execute("UPDATE changes SET changes=1 WHERE name='music_kit' ")
            c.execute("INSERT INTO history VALUES (?, ?)", ("Kitchen music is on at", current_time))

        else:
            music_button4.config(image=off)
            music4.config(fg="grey")
            is_on10 = True
            c.execute("UPDATE changes SET changes=0 WHERE name='music_kit' ")
            c.execute("INSERT INTO history VALUES (?, ?)", ("Kitchen music is off at", current_time))

        conn.commit()
        conn.close()

    #################
    root = Tk()
    root.title("My Smart Home")
    root.geometry("850x540")
    root.resizable(False, False)


    def click():
        global number
        global total_p
        number += 1
        total_p += 1
        total_person.config(text=f"{total_p} 🧑")
        label1.config(text=number)
        time_func()

    def click2():
        global number2
        global total_temp
        global total_p
        total_temp += 1
        total_temperature.config(text=f"{total_temp} 🌡️")
        number2 += 1
        label2.config(text=number2)
        time_func()
    

    def click3():
        global number3
        global total_p
        total_p += 1
        total_person.config(text=f"{total_p} 🧑")
        number3 += 1
        label3.config(text=number3)
        time_func()

    def click4():
        global number4
        global total_temp
        total_temp += 1
        total_temperature.config(text=f"{total_temp} 🌡️")
        number4 += 1
        label4.config(text=number4)
        time_func()

    def click5():
        global number5
        global total_p
        total_p += 1
        total_person.config(text=f"{total_p} 🧑")
        number5 += 1
        label5.config(text=number5)
        time_func()

    def click6():
        global number6
        global total_temp
        total_temp += 1
        total_temperature.config(text=f"{total_temp} 🌡️")
        number6 += 1
        label6.config(text=number6)
        time_func()
        
    def click7():
        global number7
        global total_p
        total_p += 1
        total_person.config(text=f"{total_p} 🧑")
        number7 += 1
        label7.config(text=number7)
        time_func()

    def click8():
        global number8
        global total_temp
        total_temp += 1
        total_temperature.config(text=f"{total_temp} 🌡️")
        number8 += 1
        label8.config(text=number8)
        time_func()

    def minclick():
        global number
        global total_p
        if (number and total_p) != 0:
            total_p -= 1
            number -= 1
        total_person.config(text=f"{total_p} 🧑")
        label1.config(text=number)
        time_func()

    def minclick2():
        global number2
        global total_temp
        if (number2 and total_temp) != 0:
            total_temp -= 1
            number2 -= 1
        total_temperature.config(text=f"{total_temp} 🌡️")
        label2.config(text=number2)
        time_func()

    def minclick3():
        global number3
        global total_p
        if (number3 and total_p) != 0:
            total_p -= 1
            number3 -= 1
        total_person.config(text=f"{total_p} 🧑")
        label3.config(text=number3)
        time_func()

    def minclick4():
        global number4
        global total_temp
        if (number4 and total_temp) != 0:
            total_temp -= 1
            number4 -= 1
        total_temperature.config(text=f"{total_temp} 🌡️")
        label4.config(text=number4)
        time_func()

    def minclick5():
        global number5
        global total_p
        if (number5 and total_p) != 0:
            total_p -= 1
            number5 -= 1
        total_person.config(text=f"{total_p} 🧑")
        label5.config(text=number5)
        time_func()

    def minclick6():
        global number6
        global total_temp
        if (number6 and total_temp) != 0:
            total_temp -= 1
            number6 -= 1
        total_temperature.config(text=f"{total_temp} 🌡️")
        label6.config(text=number6)
        time_func()

    def minclick7():
        global number7
        global total_p
        if (number7 and total_p) != 0:
            total_p -= 1
            number7 -= 1
        total_person.config(text=f"{total_p} 🧑")
        label7.config(text=number7)
        time_func()

    def minclick8():
        global number8
        global total_temp
        if (number8 and total_temp) != 0:
            total_temp -= 1
            number8 -= 1
        total_temperature.config(text=f"{total_temp} 🌡️")
        label8.config(text=number8)
        time_func()

    def time_func():
        # aircon
        if (total_p != 0):
            if (number2  > 4) or (number4  > 4) or (number6 > 4) or (number8 > 4):
                all_aircon_on()
            elif (number2 <= 4) and (number4 <= 4) and (number6 <= 4) and (number8 <= 4):
                all_aircon_off()
        if (total_p == 0):
            all_aircon_off()

        e1 = int(my_entry.get())
        # Quiet hours
        if (total_p != 0) and (e1 >= 2200 and e1 < 2400) :
            three_lights_on()
            three_musics_on()

        elif (total_p != 0) and (e1 <= 600 and e1 >= 0) :
            three_lights_on()
            three_musics_on()

        elif (total_p == 0) and (e1 >= 2200 and e1 < 2400) :
            all_lights_off()
            all_music_off()

        elif (total_p == 0) and (e1 <= 600 and e1 >= 0) :
            all_lights_off()
            all_music_off()

        # Normal auto
        elif (e1 > 600 and e1 < 800):
            all_lights_off()

            if (total_p != 0):
                all_music_on()
            elif (total_p == 0):
                all_music_off()
            else:
                pass
        
        elif (e1 > 1100 and e1 < 1800):
            all_lights_off()
            if (total_p != 0):
                all_music_on()
            elif (total_p == 0):
                all_music_off()
            else:
                pass
        
        # Music at 08.00 - 11.00 whether there are people or not
        elif (e1 >= 800 and e1 <= 1100):
            all_music_on()
        
        # When it is starting to get dark; 18.00 - 06.00
        elif (e1 >= 1800 and e1 < 2200) and (total_p != 0):
            all_lights_on()

        elif (e1 >= 1800 and e1 < 2200) and (total_p == 0):
            all_lights_off()

        else:
            pass

    def three_lights_on():
        conn = sqlite3.connect('mydatabase.db')
        c = conn.cursor()
        global is_on
        global is_on3
        global is_on5
        global is_on8
        light_button.config(image=off)
        light_button2.config(image=on)
        light_button3.config(image=on)
        light_button4.config(image=on)
        light.config(fg="grey")
        light2.config(fg="green")
        light3.config(fg="green")
        light4.config(fg="green")
        is_on = True
        is_on3 = False
        is_on5 = False
        is_on8 = False
        c.execute("UPDATE changes SET changes=0 WHERE name='light_bed' ")
        c.execute("UPDATE changes SET changes=1 WHERE name='light_bath' ")
        c.execute("UPDATE changes SET changes=1 WHERE name='light_liv' ")
        c.execute("UPDATE changes SET changes=1 WHERE name='light_kit' ")
        conn.commit()
        conn.close()

    def three_musics_on():
        conn = sqlite3.connect('mydatabase.db')
        c = conn.cursor()
        global is_on2
        global is_on4
        global is_on7
        global is_on10
        music_button.config(image=off)
        music_button2.config(image=on)
        music_button3.config(image=on)
        music_button4.config(image=on)
        music.config(fg="grey")
        music2.config(fg="green")
        music3.config(fg="green")
        music4.config(fg="green")
        is_on2 = True
        is_on4 = False
        is_on7 = False
        is_on10 = False
        c.execute("UPDATE changes SET changes=0 WHERE name='music_bed' ")
        c.execute("UPDATE changes SET changes=1 WHERE name='music_bath' ")
        c.execute("UPDATE changes SET changes=1 WHERE name='music_liv' ")
        c.execute("UPDATE changes SET changes=1 WHERE name='music_kit' ")
        conn.commit()
        conn.close()

    #! SIMULATION#####################################################################################################
    # bedroom
    bedroom_simulation = Label(root,
                        text="Bedroom",
                        font=("lucida", 11), state=DISABLED)
    bedroom_simulation.place(x=550, y=304+20)

    label1 = Label(root, text=number, state=DISABLED)
    label1.place(x=662+20, y=304+27+20)

    label2 = Label(root, text=number2, state=DISABLED)
    label2.place(x=749+20, y=304+27+20)

    button1 = Button(root, text="People Counter", command=lambda:[click()], state=DISABLED)
    button1.place(x=620+20, y=304+20)

    button2 = Button(root, text="Room Temp", command=lambda:[click2()], state=DISABLED)
    button2.place(x=715+20, y=304+20)

    button3 = Button(root, text="-", command=lambda:[minclick()], state=DISABLED)
    button3.place(x=620+20, y=304+20+27)

    button4 = Button(root, text="-", command=lambda:[minclick2()], state=DISABLED)
    button4.place(x=715+20, y=304+20+27)

    # bathroom
    bathroom_simulation = Label(root,
                        text="Bathroom",
                        font=("lucida", 11), state=DISABLED)
    bathroom_simulation.place(x=550, y=304+54+20)

    label3 = Label(root, text=number3, state=DISABLED)
    label3.place(x=662+20, y=304+54+27+20)

    label4 = Label(root, text=number4, state=DISABLED)
    label4.place(x=749+20, y=304+54+27+20)

    button5 = Button(root, text="People Counter", command=click3, state=DISABLED)
    button5.place(x=620+20, y=304+54+20)

    button6 = Button(root, text="Room Temp", command=click4, state=DISABLED)
    button6.place(x=715+20, y=304+54+20)

    button7 = Button(root, text="-", command=minclick3, state=DISABLED)
    button7.place(x=620+20, y=304+54+20+27)

    button8 = Button(root, text="-", command=minclick4, state=DISABLED)
    button8.place(x=715+20, y=304+54+20+27)

    # living room
    living_room_simulation = Label(root,
                        text="Living Room",
                        font=("lucida", 11), state=DISABLED)
    living_room_simulation.place(x=550, y=304+54+54+20)

    label5 = Label(root, text=number5, state=DISABLED)
    label5.place(x=662+20, y=304+54+27+54+20)

    label6 = Label(root, text=number6, state=DISABLED)
    label6.place(x=749+20, y=304+54+27+54+20)

    button9 = Button(root, text="People Counter", command=click5, state=DISABLED)
    button9.place(x=620+20, y=304+54+54+20)

    button10 = Button(root, text="Room Temp", command=click6, state=DISABLED)
    button10.place(x=715+20, y=304+54+54+20)

    button11 = Button(root, text="-", command=minclick5, state=DISABLED)
    button11.place(x=620+20, y=304+54+54+20+27)

    button12 = Button(root, text="-", command=minclick6, state=DISABLED)
    button12.place(x=715+20, y=304+54+54+20+27)

    # kitchen
    kitchen_simulation = Label(root,
                        text="Kitchen",
                        font=("lucida", 11), state=DISABLED)
    kitchen_simulation.place(x=550, y=304+54+108+20)

    label7 = Label(root, text=number7, state=DISABLED)
    label7.place(x=662+20, y=304+54+27+54+54+20)

    label8 = Label(root, text=number8, state=DISABLED)
    label8.place(x=749+20, y=304+54+27+54+54+20)

    button13 = Button(root, text="People Counter", command=click7, state=DISABLED)
    button13.place(x=620+20, y=304+54+54+54+20)

    button14 = Button(root, text="Room Temp", command=click8, state=DISABLED)
    button14.place(x=715+20, y=304+54+54+54+20)

    button15 = Button(root, text="-", command=minclick7, state=DISABLED)
    button15.place(x=620+20, y=304+54+54+54+20+27)

    button16 = Button(root, text="-", command=minclick8, state=DISABLED)
    button16.place(x=715+20, y=304+54+54+54+20+27)

    # Set Time
    input_time = Label(root, text="Input Time", state=DISABLED)
    input_time.place(x=650, y=218)

    my_entry = Entry(root, width=8, state=DISABLED)
    my_entry.place(x=620+20+15, y=250)

    def all_music_on():
        conn = sqlite3.connect('mydatabase.db')
        c = conn.cursor()
        global is_on2
        global is_on4
        global is_on7
        global is_on10
        music_button.config(image=on)
        music_button2.config(image=on)
        music_button3.config(image=on)
        music_button4.config(image=on)
        music.config(fg="green")
        music2.config(fg="green")
        music3.config(fg="green")
        music4.config(fg="green")
        is_on2 = False
        is_on4 = False
        is_on7 = False
        is_on10 = False
        c.execute("UPDATE changes SET changes=1 WHERE name='music_bed' ")
        c.execute("UPDATE changes SET changes=1 WHERE name='music_bath' ")
        c.execute("UPDATE changes SET changes=1 WHERE name='music_liv' ")
        c.execute("UPDATE changes SET changes=1 WHERE name='music_kit' ")
        conn.commit()
        conn.close()

    def all_music_off():
        conn = sqlite3.connect('mydatabase.db')
        c = conn.cursor()
        global is_on2
        global is_on4
        global is_on7
        global is_on10
        music_button.config(image=off)
        music_button2.config(image=off)
        music_button3.config(image=off)
        music_button4.config(image=off)
        music.config(fg="grey")
        music2.config(fg="grey")
        music3.config(fg="grey")
        music4.config(fg="grey")
        is_on2 = True
        is_on4 = True
        is_on7 = True
        is_on10 = True
        c.execute("UPDATE changes SET changes=0 WHERE name='music_bed' ")
        c.execute("UPDATE changes SET changes=0 WHERE name='music_bath' ")
        c.execute("UPDATE changes SET changes=0 WHERE name='music_liv' ")
        c.execute("UPDATE changes SET changes=0 WHERE name='music_kit' ")
        conn.commit()
        conn.close()

    def all_aircon_on():
        conn = sqlite3.connect('mydatabase.db')
        c = conn.cursor()
        global is_on1
        global is_on6
        global is_on9
        aircon_button.config(image=on)
        aircon_button2.config(image=on)
        aircon_button3.config(image=on)
        aircon.config(fg="green")
        aircon2.config(fg="green")
        aircon3.config(fg="green")
        is_on1 = False
        is_on6 = False
        is_on9 = False
        c.execute("UPDATE changes SET changes=1 WHERE name='aircon_bed' ")
        c.execute("UPDATE changes SET changes=1 WHERE name='aircon_kit' ")
        c.execute("UPDATE changes SET changes=1 WHERE name='aircon_liv' ")
        conn.commit()
        conn.close()

    def all_aircon_off():
        conn = sqlite3.connect('mydatabase.db')
        c = conn.cursor()
        global is_on1
        global is_on6
        global is_on9
        aircon_button.config(image=off)
        aircon_button2.config(image=off)
        aircon_button3.config(image=off)
        aircon.config(fg="grey")
        aircon2.config(fg="grey")
        aircon3.config(fg="grey")
        is_on1 = True
        is_on6 = True
        is_on9 = True
        c.execute("UPDATE changes SET changes=0 WHERE name='aircon_bed' ")
        c.execute("UPDATE changes SET changes=0 WHERE name='aircon_bath' ")
        c.execute("UPDATE changes SET changes=0 WHERE name='aircon_liv' ")
        conn.commit()
        conn.close()

    def all_lights_on():
        conn = sqlite3.connect('mydatabase.db')
        c = conn.cursor()
        global is_on
        global is_on3
        global is_on5
        global is_on8
        light_button.config(image=on)
        light_button2.config(image=on)
        light_button3.config(image=on)
        light_button4.config(image=on)
        light.config(fg="green")
        light2.config(fg="green")
        light3.config(fg="green")
        light4.config(fg="green")
        is_on = False
        is_on3 = False
        is_on5 = False
        is_on8 = False
        c.execute("UPDATE changes SET changes=1 WHERE name='light_bath' ")
        c.execute("UPDATE changes SET changes=1 WHERE name='light_liv' ")
        c.execute("UPDATE changes SET changes=1 WHERE name='light_kit' ")
        c.execute("UPDATE changes SET changes=1 WHERE name='light_bed' ")
        conn.commit()
        conn.close()

    def all_lights_off():
        conn = sqlite3.connect('mydatabase.db')
        c = conn.cursor()
        global is_on
        global is_on3
        global is_on5
        global is_on8
        light_button.config(image=off)
        light_button2.config(image=off)
        light_button3.config(image=off)
        light_button4.config(image=off)
        light.config(fg="grey")
        light2.config(fg="grey")
        light3.config(fg="grey")
        light4.config(fg="grey")
        is_on = True
        is_on3 = True
        is_on5 = True
        is_on8 = True
        c.execute("UPDATE changes SET changes=0 WHERE name='light_bath' ")
        c.execute("UPDATE changes SET changes=0 WHERE name='light_liv' ")
        c.execute("UPDATE changes SET changes=0 WHERE name='light_kit' ")
        c.execute("UPDATE changes SET changes=0 WHERE name='light_bed' ")
        conn.commit()
        conn.close()

    def all_button_on():
        light_button["state"] = NORMAL
        light_button2["state"] = NORMAL
        light_button3["state"] = NORMAL
        light_button4["state"] = NORMAL
        music_button["state"] = NORMAL
        music_button2["state"] = NORMAL
        music_button3["state"] = NORMAL
        music_button4["state"] = NORMAL
        aircon_button["state"] = NORMAL
        aircon_button2["state"] = NORMAL
        aircon_button3["state"] = NORMAL

    def all_button_off():
        light_button["state"] = DISABLED
        light_button2["state"] = DISABLED
        light_button3["state"] = DISABLED
        light_button4["state"] = DISABLED
        music_button["state"] = DISABLED
        music_button2["state"] = DISABLED
        music_button3["state"] = DISABLED
        music_button4["state"] = DISABLED
        aircon_button["state"] = DISABLED
        aircon_button2["state"] = DISABLED
        aircon_button3["state"] = DISABLED

    total_person = Label(root, text=f"{total_p} 🧑", bg="DarkSeaGreen1")
    total_person.place(x=800, y=220)

    total_temperature = Label(root, text=f"{total_temp} 🌡️", bg="DarkSeaGreen1")
    total_temperature.place(x=803, y=245)


    #!################################################################################################################

    # Title label
    title = Label(root, text="My Smart Home", font=("lucida", 11, "bold"))
    title.place(x=150, y=20)

    # Dividing line
    l = Label(
        root, text="_______________________________________________________________________________________________________________________________________________________________________________________________________________")
    l.place(x=0, y=190)

    ### Bedroom ###
    room1 = Label(root, text="Bedroom", font=("lucida", 11, "underline"))
    room1.place(x=44, y=304)


    # Get the parent directory of the current script
    parent_directory = os.path.dirname(os.path.abspath(__file__))

    # Define the relative paths to the images
    on_relative_path = "on1.png"
    off_relative_path = "off1.png"

    on_relative_path = os.path.join("MySmartHome", "on1.png")
    off_relative_path = os.path.join("MySmartHome", "off1.png")

    # Load the images using the absolute paths
    on = PhotoImage(on_relative_path)
    off = PhotoImage(off_relative_path)


    # Light Button 1
    light = Label(root,
                    text="Light",
                    fg="grey",
                    font=("lucida", 11))
    light.place(x=44, y=330)

    light_button = Button(root, image=off, bd=0,
                    command=switch)
    light_button.place(x=190, y=327)

    # Air conditioner button 1
    aircon = Label(root,
                    text="Air Conditioner",
                    fg="grey",
                    font=("lucida", 11))
    aircon.place(x=44, y=357)

    aircon_button = Button(root, image=off, bd=0,
                    command=switch1,)
    aircon_button.place(x=190, y=355)

    # Music button 1

    music = Label(root,
                    text="Music",
                    fg="grey",
                    font=("lucida", 11))
    music.place(x=44, y=385)

    music_button = Button(root, image=off, bd=0,
                    command=switch2)
    music_button.place(x=190, y=383)    

    ### Bathroom ###
    room2 = Label(root, text="Bathroom", font=("lucida", 11, "underline"))
    room2.place(x=44, y=411)

    # Light Button 2
    light2 = Label(root,
                    text="Light",
                    fg="grey",
                    font=("lucida", 11))
    light2.place(x=44, y=437)

    light_button2 = Button(root, image=off, bd=0,
                    command=switch3)
    light_button2.place(x=190, y=435)

    # Music button 2
    music2 = Label(root,
                    text="Music",
                    fg="grey",
                    font=("lucida", 11))
    music2.place(x=44, y=465)

    music_button2 = Button(root, image=off, bd=0,
                    command=switch4)
    music_button2.place(x=190, y=463)

    ### Living Room ###
    room3 = Label(root, text="Living Room", font=("lucida", 11, "underline"))
    room3.place(x=310, y=304)

    # Light Button 3
    light3 = Label(root,
                    text="Light",
                    fg="grey",
                    font=("lucida", 11))
    light3.place(x=310, y=330)

    light_button3 = Button(root, image=off, bd=0,
                    command=switch5)
    light_button3.place(x=456, y=326)

    # Air conditioner button 2
    aircon2 = Label(root,
                    text="Air Conditioner",
                    fg="grey",
                    font=("lucida", 11))
    aircon2.place(x=310, y=357)

    aircon_button2 = Button(root, image=off, bd=0,
                    command=switch6)
    aircon_button2.place(x=456, y=354)

    # Music button 3
    music3 = Label(root,
                    text="Music",
                    fg="grey",
                    font=("lucida", 11))
    music3.place(x=310, y=385)

    music_button3 = Button(root, image=off, bd=0,
                    command=switch7)
    music_button3.place(x=456, y=382)    

    ### Kitchen ###
    room4 = Label(root, text="Kitchen", font=("lucida", 11, "underline"))
    room4.place(x=310, y=411)

    # Light Button 4
    light4 = Label(root,
                    text="Light",
                    fg="grey",
                    font=("lucida", 11))
    light4.place(x=310, y=437)

    light_button4 = Button(root, image=off, bd=0,
                    command=switch8)
    light_button4.place(x=456, y=434)

    # Air conditioner button 3
    aircon3 = Label(root,
                    text="Air Conditioner",
                    fg="grey",
                    font=("lucida", 11))
    aircon3.place(x=310, y=465)

    aircon_button3 = Button(root, image=off, bd=0,
                    command=switch9)
    aircon_button3.place(x=456, y=462)

    # Music button 4
    music4 = Label(root,
                    text="Music",
                    fg="grey",
                    font=("lucida", 11))
    music4.place(x=310, y=493)

    music_button4 = Button(root, image=off, bd=0,
                    command=switch10)
    music_button4.place(x=456, y=490)   

    def simulation_on():
        input_time["state"] = NORMAL
        my_entry["state"] = NORMAL
        bedroom_simulation["state"] = NORMAL
        bathroom_simulation["state"] = NORMAL
        living_room_simulation["state"] = NORMAL
        kitchen_simulation["state"] = NORMAL
        label1["state"] = NORMAL
        label2["state"] = NORMAL
        label3["state"] = NORMAL
        label4["state"] = NORMAL
        label5["state"] = NORMAL
        label6["state"] = NORMAL
        label7["state"] = NORMAL
        label8["state"] = NORMAL
        button1["state"] = NORMAL
        button2["state"] = NORMAL
        button3["state"] = NORMAL
        button4["state"] = NORMAL
        button5["state"] = NORMAL
        button6["state"] = NORMAL
        button7["state"] = NORMAL
        button8["state"] = NORMAL
        button9["state"] = NORMAL
        button10["state"] = NORMAL
        button11["state"] = NORMAL
        button12["state"] = NORMAL
        button13["state"] = NORMAL
        button14["state"] = NORMAL
        button15["state"] = NORMAL
        button16["state"] = NORMAL

    def simulation_off():
        input_time["state"] = DISABLED
        my_entry["state"] = DISABLED
        bedroom_simulation["state"] = DISABLED
        bathroom_simulation["state"] = DISABLED
        living_room_simulation["state"] = DISABLED
        kitchen_simulation["state"] = DISABLED
        label1["state"] = DISABLED
        label2["state"] = DISABLED
        label3["state"] = DISABLED
        label4["state"] = DISABLED
        label5["state"] = DISABLED
        label6["state"] = DISABLED
        label7["state"] = DISABLED
        label8["state"] = DISABLED
        button1["state"] = DISABLED
        button2["state"] = DISABLED
        button3["state"] = DISABLED
        button4["state"] = DISABLED
        button5["state"] = DISABLED
        button6["state"] = DISABLED
        button7["state"] = DISABLED
        button8["state"] = DISABLED
        button9["state"] = DISABLED
        button10["state"] = DISABLED
        button11["state"] = DISABLED
        button12["state"] = DISABLED
        button13["state"] = DISABLED
        button14["state"] = DISABLED
        button15["state"] = DISABLED
        button16["state"] = DISABLED


    # Entry
    Var1 = IntVar()
    Var1.set(0)

    def manual_mode():
        conn = sqlite3.connect('mydatabase.db')
        c = conn.cursor()
        kk = Var1.get()

        find_user = ("SELECT * FROM users WHERE username = ? and password = ? ")
        c.execute(find_user, [(username.get()), (password.get())])
        result = c.fetchall()

        if result:
            u = username.get()
            if (kk == 0) and (u == "Admin"): # pass to admin mode
                simulation_off()

            elif (u == "Automatic"):
                automatic_mode2()
                listbox["state"] = DISABLED
                label_admin["state"] = DISABLED
                new_password_entry["state"] = DISABLED
                new_password_button["state"] = DISABLED
                listbox["state"] = DISABLED
                
            elif (kk == 0) and (u != "Admin"): # manual
                c.execute("UPDATE changes SET changes=1 WHERE name='manual' ")
                c.execute("UPDATE changes SET changes=0 WHERE name='automatic' ")
                c.execute("UPDATE changes SET changes=0 WHERE name='guest' ")

                find_user = ("SELECT * FROM users WHERE username = ? ")
                c.execute(find_user, [(username.get())])
                result = c.fetchall()

                if result:
                    u = username.get()
                    if u == "Guest":
                        all_button_off()
                    else:
                        all_button_on()
        else:
            pass
        conn.commit()
        conn.close()

    def automatic_mode():
        conn = sqlite3.connect('mydatabase.db')
        global current_time
        c = conn.cursor()
        c.execute("UPDATE changes SET changes=0 WHERE name='manual' ")
        c.execute("UPDATE changes SET changes=1 WHERE name='automatic' ")
        c.execute("UPDATE changes SET changes=0 WHERE name='guest' ")
        c.execute("INSERT INTO history VALUES (?, ?)", ("Automatic mode is on at", current_time))
        conn.commit()
        conn.close()
        all_button_off()
        simulation_on()

    def automatic_mode2():
        conn = sqlite3.connect('mydatabase.db')
        global current_time
        c = conn.cursor()
        c.execute("UPDATE changes SET changes=0 WHERE name='manual' ")
        c.execute("UPDATE changes SET changes=1 WHERE name='automatic' ")
        c.execute("UPDATE changes SET changes=0 WHERE name='guest' ")
        c.execute("INSERT INTO history VALUES (?)", ("Automatic user logged in at {current_time}"))
        conn.commit()
        conn.close()
        manual["state"] = DISABLED
        guest["state"] = DISABLED
        all_button_off()
        simulation_on()

    # Mode
    Mode = Label(root, text="Mode", font=("lucida", 11))
    Mode.place(x=44, y=218)

    manual = Radiobutton(root, text="Manual", variable=Var1, value=0,
                            command=manual_mode)
    manual.place(x=44, y=242)

    automatic = Radiobutton(root, text="Automatic", variable=Var1, value=1,
                            command=automatic_mode, state=DISABLED)
    automatic.place(x=44, y=273)

    guest = Radiobutton(root, text="Guest", variable=Var1, value=2,
                            command=lambda:[service.guest_mode(), simulation_off(), all_button_on()], state=DISABLED)
    guest.place(x=150, y=257)

    def verify_account():
        with sqlite3.connect("mydatabase.db") as db:
            c=db.cursor()
            find_user = ("SELECT * FROM users WHERE username = ? and password = ? ")
            c.execute(find_user, [(username.get()), (password.get())])
            result = c.fetchall()

            if result:  
                a = Var1.get()
                u = username.get()
                if u == "Admin":
                    simulation_off()
                    admin_acc()
                elif u == "Parent":
                    parent_acc()
                elif u == "Parent1":
                    parent1_acc()
                elif u == "Parent2":
                    parent2_acc()
                elif u == "Children":
                    children_acc()
                elif u == "Automatic":
                    automatic_mode()

                elif u == "Guest":
                    conn = sqlite3.connect('mydatabase.db')
                    global current_time
                    c = conn.cursor()
                    c.execute("INSERT INTO history VALUES (?, ?)", ("Admin logged in at", current_time))
                    conn.commit()
                    conn.close()

                    error["text"] = "Log-in successfull."
                    print("Logged in as guest")
                    automatic["state"]  = DISABLED
                    manual["state"] = DISABLED
                    guest["state"] = DISABLED
                    light_button["state"] = DISABLED
                    light_button2["state"] = DISABLED
                    light_button3["state"] = DISABLED
                    light_button4["state"] = DISABLED
                    music_button["state"] = DISABLED
                    music_button2["state"] = DISABLED
                    music_button3["state"] = DISABLED
                    music_button4["state"] = DISABLED
                    aircon_button["state"] = DISABLED
                    aircon_button2["state"] = DISABLED
                    aircon_button3["state"] = DISABLED
                    new_password_button["state"] = DISABLED
                    new_password_entry["state"] = DISABLED
                    new_password_entry["state"] = DISABLED
                    label_admin["state"] = DISABLED
                    listbox["state"] = DISABLED
                    a = Var1.get()
                    if u == "Guest" and a == 2:
                        light_button["state"] = NORMAL
                        light_button2["state"] = NORMAL
                        light_button3["state"] = NORMAL
                        light_button4["state"] = NORMAL
                        music_button["state"] = NORMAL
                        music_button2["state"] = NORMAL
                        music_button3["state"] = NORMAL
                        music_button4["state"] = NORMAL
                        aircon_button["state"] = NORMAL
                        aircon_button2["state"] = NORMAL
                        aircon_button3["state"] = NORMAL
                        print("Guest mode enabled")
                    else:
                        print("Parent have not enabled guest mode")
            else:
                error["text"] = "Invalid username or password."
    #?##########################################################################################################################################

    def admin_acc():
        error["text"] = "Log-in successfull."
        print("Logged in as admin")

        listbox["state"] = NORMAL
        label_admin["state"] = NORMAL
        new_password_entry["state"] = NORMAL
        new_password_button["state"] = NORMAL
        listbox.insert(0, "Admin")
        listbox.insert(1, "Parent")
        listbox.insert(2, "Parent1")
        listbox.insert(3, "Parent2")
        listbox.insert(4, "Children")
        listbox.insert(5, "Guest")
        listbox.insert(6, "Automatic")

        light_button["state"] = DISABLED
        light_button2["state"] = DISABLED
        light_button3["state"] = DISABLED
        light_button4["state"] = DISABLED
        music_button["state"] = DISABLED
        music_button2["state"] = DISABLED
        music_button3["state"] = DISABLED
        music_button4["state"] = DISABLED
        aircon_button["state"] = DISABLED
        aircon_button2["state"] = DISABLED
        aircon_button3["state"] = DISABLED

        conn = sqlite3.connect('mydatabase.db')
        global current_time
        c = conn.cursor()
        c.execute("INSERT INTO history VALUES (?, ?)", ("Admin logged in at", current_time))
        conn.commit()
        conn.close()


    def parent_acc():
        simulation_off()
        error["text"] = "Log-in successfull."
        u = username.get()
        p = password.get()
        if u == "Parent" and p == "parent123":
            print("Logged in as parent")
        else:
            print("Error (parent)")
        #!
        manual["state"] = NORMAL
        automatic["state"] = NORMAL
        guest["state"] = NORMAL
        simulation_off()

        conn = sqlite3.connect('mydatabase.db')
        global current_time
        c = conn.cursor()
        c.execute("INSERT INTO history VALUES (?, ?)", ("Parent logged in at", current_time))
        conn.commit()
        conn.close()

    def parent1_acc():
        simulation_off()
        error["text"] = "Log-in successfull."
        u = username.get()
        p = password.get()
        if u == "Parent1" and p == "parent1123":
            print("Logged in as parent")
        else:
            print("Error (parent1)")
        #!
        manual["state"] = NORMAL
        automatic["state"] = NORMAL
        guest["state"] = NORMAL

        conn = sqlite3.connect('mydatabase.db')
        global current_time
        c = conn.cursor()
        c.execute("INSERT INTO history VALUES (?, ?)", ("Parent1 logged in at", current_time))
        conn.commit()
        conn.close()

    def parent2_acc():
        simulation_off()
        error["text"] = "Log-in successfull."
        u = username.get()
        p = password.get()
        if u == "Parent2" and p == "parent2123":
            print("Logged in as parent")
        else:
            print("Error (parent2)")
        #!
        manual["state"] = NORMAL
        automatic["state"] = NORMAL
        guest["state"] = NORMAL

        conn = sqlite3.connect('mydatabase.db')
        global current_time
        c = conn.cursor()
        c.execute("INSERT INTO history VALUES (?, ?)", ("Parent2 logged in at", current_time))
        conn.commit()
        conn.close()

    def children_acc():
        error["text"] = "Log-in successfull."
        u = username.get()
        p = password.get()
        if u == "Children" and p == "children123":
            print("Logged in as children")
        else:
            print("Error (children)")

        a = Var1.get()
        if (a == 0) or (a == 2):
            all_button_on()
        elif (a == 1):
            automatic["state"] = DISABLED
            manual["state"] = DISABLED
            guest["state"] = DISABLED
            all_button_off()
        else:
            pass

        conn = sqlite3.connect('mydatabase.db')
        global current_time
        c = conn.cursor()
        c.execute("INSERT INTO history VALUES (?, ?)", ("Children logged in at", current_time))
        conn.commit()
        conn.close()

    # USERS INFO MENU
    mainmenu = Menu(root)

    def email():
        window = Toplevel()
        window.geometry('300x150')
        curr = listbox.curselection()
        if curr == (0,):
            ll = "Admin"
        elif curr == (1,):
            ll = "Parent"
        elif curr == (2,):
            ll = "Parent1"
        elif curr == (3,):
            ll = "Parent2"
        elif curr == (4,):
            ll = "Children"
        elif curr == (5,):
            ll = "Guest"
        elif curr == (6,):
            ll = "Automatic"

        else:
            pass
        inbox = Message(window, text=ll, font=("lucida", 11, "bold"))
        inbox.pack()
        global n
        email_message = Message(window, text=f"New password: {n}")
        email_message.pack()
        email_message.config(bg='gold', padx=0)

    # Admin
    email_menu = Menu(mainmenu, tearoff=0)
    email_menu.add_command(label="Inbox", command=email)

    mainmenu.add_cascade(label="Email", menu=email_menu)

    root.config(menu=mainmenu)

    def users_new_password():
        send_new_pass_message["text"] = "Please select a user"

        cur = listbox.curselection()
        global current_time
        global n
        n = new_password_entry.get()
        conn = sqlite3.connect('mydatabase.db')
        c = conn.cursor()
        
        if cur == (0,):
            send_new_pass_message["text"] = "A new password has been sent to your email"
            c.execute("INSERT INTO history VALUES (?, ?)", ("New password sent to admin at", current_time))
        
        elif cur == (1,):
            send_new_pass_message["text"] = "New password sent to Parent"
            c.execute("INSERT INTO history VALUES (?, ?)", ("New password sent to Parent", current_time))

        elif cur == (2,):
            send_new_pass_message["text"] = "New password sent to Parent1"
            c.execute("INSERT INTO history VALUES (?, ?)", ("New password sent to Parent1", current_time))

        elif cur == (3,):
            send_new_pass_message["text"] = "New password sent to Parent2"
            c.execute("INSERT INTO history VALUES (?, ?)", ("New password sent to Parent2", current_time))

        elif cur == (4,):
            send_new_pass_message["text"] = "New password sent to Children"
            c.execute("INSERT INTO history VALUES (?, ?)", ("New password sent to Children", current_time))

        elif cur == (5,):
            send_new_pass_message["text"] = "New password sent to Guest"
            c.execute("INSERT INTO history VALUES (?, ?)", ("New password sent to Guest", current_time))

        elif cur == (6,):
            send_new_pass_message["text"] = "Automatic mode password changed"
            c.execute("INSERT INTO history VALUES (?, ?)", ("New password sent to Automatic", current_time))

        else:
            pass

        conn.commit()
        conn.close()

    listbox = Listbox(root, height=3, state=DISABLED)
    listbox.place(x=600, y=10)

    admin_page = Label(root, text="|Admin Page|", font=("lucida", 9), state=DISABLED)
    admin_page.place(x=700, y=100)
    sim_page = Label(root, text="|Simulation|", font=("lucida", 9), state=DISABLED)
    sim_page.place(x=550, y=250)

    #

    label_admin = Label(root, text="New Password", font=("lucida", 11), state=DISABLED)
    label_admin.place(x=490, y=66)
    new_password_entry = StringVar()
    new_password_entry = Entry(root, textvariable=new_password_entry, state=DISABLED)
    new_password_entry.insert(0, '')
    new_password_entry.place(x=600, y=69)
    new_password_button = Button(root, text="Send", font=("lucida", 11), command=lambda:[users_new_password(), update_password()], state=DISABLED)
    new_password_button.place(x=600, y=99)

    send_new_pass_message = Message(text="", width=160)
    send_new_pass_message.place(x=560, y=145)
    send_new_pass_message.config(bg='cyan', padx=0)
    #

    def update_password():
        conn = sqlite3.connect('mydatabase.db')
        c = conn.cursor()
        nn = new_password_entry.get()
        current = listbox.curselection()
        if current == (0,):
            rr = "admin@gmail.com"
        elif current == (1,):
            rr = "parent@gmail.com"
        elif current == (2,):
            rr = "parent1@gmail.com"
        elif current == (3,):
            rr = "parent2@gmail.com"
        elif current == (4,):
            rr = "children@gmail.com"
        elif current == (5,):
            rr = "guest@gmail.com"
        elif current == (6,):
            rr = "automatic@gmail.com"
        else:
            pass

        c.execute("UPDATE users SET password=? WHERE email=? ", (nn,rr))
        conn.commit()
        conn.close()


    username = Label(root, text="Username", font=("lucida", 11))
    username.place(x=83, y=66)
    password = Label(root, text="Password", font=("lucida", 11))
    password.place(x=84, y=89)

    username = StringVar()
    username = Entry(root, textvariable=username)
    username.insert(0, '')
    username.place(x=202, y=69)
    username.focus()

    password = StringVar()
    password = Entry(root, textvariable=password)
    password.insert(0, '')
    password.place(x=202, y=91)

    # Log in
    error = Message(text="", width=160)
    error.place(x=85, y=163)
    error.config(bg='lightgreen', padx=0)

    login = Button(root, text="Login", command=lambda:([verify_account(), manual_mode()]), height=1, width=5)
    login.place(x=245, y=125)

    root.mainloop()