import sqlite3

conn = sqlite3.connect('IRC_IOT_B_Pi1.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS MCcondition(unix REAL, datestamp TEXT, local TEXT, status TEXT, temp REAL, humid REAL)')
    
def data_entry():
    c.execute("INSERT INTO MCcondition VALUES(161565165, '2018-08-16', 'Oven 1', 'yellow', 85, 60) ")
    conn.commit()
    c.close()
    conn.close()
    
    
create_table()
data_entry()
