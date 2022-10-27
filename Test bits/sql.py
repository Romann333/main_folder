import sqlite3 

con = sqlite3.connect("trash_bin/tutorial.db")
cur = con.cursor()
# cur.execute("CREATE TABLE movie(title, year, score)")

# cur.execute('drop table if exists baby')
# cur.execute('drop table mama')
# con.commit()

# cur.execute('''CREATE TABLE if not exists mama(
#     mama_id integer, 
#     date, 
#     day, 
#     home
#     )''')


# cur.execute('''CREATE TABLE if not exists baby(
# baby_id integer primary key AUTOINCREMENT ,
# mama_id integer,
# title, 
# year, 
# score,
# foreign key (mama_id) REFERENCES mama(mama_id) ON DELETE CASCADE
# )''')


cur.execute('''CREATE TABLE if not exists INVESTORS(
        investor_id integer,
        name_of_investor text,
        site text,
        info_card text,
        stage text text,
        check_size text,
        focus text,
        investment_geography text
)''')

cur.execute('''CREATE TABLE if not exists MANAGERS(
        manager_id integer primary key autoincrement,
        investor_id integer,
        manager_name text,
        role text,
        contacts text,
        foreign key (investor_id) references INVESTORS(investor_id) on delete cascade
)''')


# print(res.fetchone())
# print(res.fetchall())

# con.commit()             #Подтверждение после каждого INSERT

# data =  ["Monty Python Live \n at the Hollywood Bowl", 1983332, 7.3349],
   
# a = 5
# data = [
#     [a, "https://connect.visible.vc/investors/1982-ventures", 1982, 7.9],
#     [a, "Monty Python's The Meaning of Life", 1983, 7.5],
#     [a, "Monty Python's Life of Brian", 1979, 8.0],
# ]
# cur.executemany('''insert into baby(
#                 mama_id, 
#                 title, 
#                 year, 
#                 score) values(?, ?, ?, ?)''', data)

# cur.execute('insert into baby(')
# cut.execute('delete from baby')
# cur.execute('drop table INVESTORS')

mng = [1, '3', '5', '7']
cur.executemany('''insert into MANAGERS(
                                investor_id,
                                manager_name,
                                role,
                                contacts 
                                ) values(?, ?, ?, ?)''', (mng,) )









con.commit()
con.close()