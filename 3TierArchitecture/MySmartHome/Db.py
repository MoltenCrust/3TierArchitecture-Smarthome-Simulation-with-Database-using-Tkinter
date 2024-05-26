import sqlite3
with sqlite3.connect("mydatabase.db") as db:
    c=db.cursor()

# def drop_table():
#     c.execute("DROP TABLE history")
# drop_table()

c.execute("""CREATE TABLE IF NOT EXISTS users(
    username text,
    password text,
    email text
)""")

# Create table "mode"
c.execute("""CREATE TABLE IF NOT EXISTS mode(
    manual text,
    automatic text,
    guest text
)""")

# Create table "room"
c.execute("""CREATE TABLE IF NOT EXISTS room(
    bedroom text,
    bathroom text,
    livingroom text,
    kitchen text
)""")

# Create table ability
c.execute("""CREATE TABLE IF NOT EXISTS ability(
    users text,
    use_smarthome int,
    send_new_password,
    change_mode int,
    use_smarthome_when_guest_mode_inactivated int
)""")

# Create table changes 
c.execute("""CREATE TABLE IF NOT EXISTS changes(
    name text,
    changes int
)""")

# Create table history
c.execute("""CREATE TABLE IF NOT EXISTS history(
    history text,
    time text
)""")





# Set initial change update
def initial_change_update():
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()
    c.execute("UPDATE changes SET changes=1 WHERE name='manual' ")
    c.execute("UPDATE changes SET changes=0 WHERE name='automatic' ")
    c.execute("UPDATE changes SET changes=0 WHERE name='guest' ")
    c.execute("UPDATE changes SET changes=0 WHERE name='light_bed' ")
    c.execute("UPDATE changes SET changes=0 WHERE name='aircon_bed' ")
    c.execute("UPDATE changes SET changes=0 WHERE name='music_bed' ")
    c.execute("UPDATE changes SET changes=0 WHERE name='light_bath' ")
    c.execute("UPDATE changes SET changes=0 WHERE name='music_bath' ")
    c.execute("UPDATE changes SET changes=0 WHERE name='light_liv' ")
    c.execute("UPDATE changes SET changes=0 WHERE name='aircon_liv' ")
    c.execute("UPDATE changes SET changes=0 WHERE name='music_liv' ")
    c.execute("UPDATE changes SET changes=0 WHERE name='light_kit' ")
    c.execute("UPDATE changes SET changes=0 WHERE name='aircon_kit' ")
    c.execute("UPDATE changes SET changes=0 WHERE name='music_kit' ")
    conn.commit()
    conn.close()
initial_change_update()

def create_initial_changes():
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()
    c.execute("INSERT INTO changes VALUES (?, ?)", ("manual", 1))
    c.execute("INSERT INTO changes VALUES (?, ?)", ("automatic", 0))
    c.execute("INSERT INTO changes VALUES (?, ?)", ("guest", 0))
    c.execute("INSERT INTO changes VALUES (?, ?)", ("light_bed", 0))
    c.execute("INSERT INTO changes VALUES (?, ?)", ("aircon_bed", 0))
    c.execute("INSERT INTO changes VALUES (?, ?)", ("music_bed", 0))
    c.execute("INSERT INTO changes VALUES (?, ?)", ("light_bath", 0))
    c.execute("INSERT INTO changes VALUES (?, ?)", ("music_bath", 0))
    c.execute("INSERT INTO changes VALUES (?, ?)", ("light_liv", 0))
    c.execute("INSERT INTO changes VALUES (?, ?)", ("aircon_liv", 0))
    c.execute("INSERT INTO changes VALUES (?, ?)", ("music_liv", 0))
    c.execute("INSERT INTO changes VALUES (?, ?)", ("light_kit", 0))
    c.execute("INSERT INTO changes VALUES (?, ?)", ("aircon_kit", 0))
    c.execute("INSERT INTO changes VALUES (?, ?)", ("music_kit", 0))
    conn.commit()
    conn.close()

def insert_ability():
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()
    c.execute("INSERT INTO ability VALUES (?,?,?,?,?)", ("Admin", 0, 1, 0, 0))
    c.execute("INSERT INTO ability VALUES (?,?,?,?,?)", ("Parent", 1, 0, 1, 1))
    c.execute("INSERT INTO ability VALUES (?,?,?,?,?)", ("Parent1", 1, 0, 1, 1))
    c.execute("INSERT INTO ability VALUES (?,?,?,?,?)", ("Parent2", 1, 0, 1, 1))
    c.execute("INSERT INTO ability VALUES (?,?,?,?,?)", ("Children", 1, 0, 0, 1))
    c.execute("INSERT INTO ability VALUES (?,?,?,?,?)", ("Guest", 1, 0, 0, 0))
    conn.commit()
    conn.close()


def create_initial_users():
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES (?,?,?)", ("Admin", "admin123", "admin@gmail.com"))
    c.execute("INSERT INTO users VALUES (?,?,?)", ("Parent", "parent123", "parent@gmail.com"))
    c.execute("INSERT INTO users VALUES (?,?,?)", ("Parent1", "parent1123", "parent1@gmail.com"))
    c.execute("INSERT INTO users VALUES (?,?,?)", ("Parent2", "parent2123", "parent2@gmail.com"))
    c.execute("INSERT INTO users VALUES (?,?,?)", ("Children", "children123", "children@gmail.com"))
    c.execute("INSERT INTO users VALUES (?,?,?)", ("Guest", "guest123", "guest@gmail.com"))
    c.execute("INSERT INTO users VALUES (?,?,?)", ("Automatic", "automatic123", "automatic@gmail.com"))
    conn.commit()
    conn.close()

def add_user():
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES (?,?,?)", ("Automatic", "automatic123", "automatic@gmail.com"))
    conn.commit()
    conn.close()