from tkinter import *
import Db as dbs
import GUII as ui
from datetime import datetime
import sqlite3
with sqlite3.connect("mydatabase.db") as db:
    c=db.cursor()
now = datetime.now()

current_time = now.strftime("%H:%M:%S")

def guest_mode():
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()
    c.execute("UPDATE changes SET changes=0 WHERE name='manual' ")
    c.execute("UPDATE changes SET changes=0 WHERE name='automatic' ")
    c.execute("UPDATE changes SET changes=1 WHERE name='guest' ")
    c.execute("INSERT INTO history VALUES (?, ?)", ("Guest mode is on at", current_time))
    conn.commit()
    conn.close()

conn = sqlite3.connect('mydatabase.db')
c = conn.cursor()
c.execute("INSERT INTO history VALUES (?, ?)", ("Manual mode is on at", current_time))
conn.commit()
conn.close()