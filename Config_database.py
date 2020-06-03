import sqlite3 as sql


class DataBase_Connection :

    def __init__(self):
        self.connection = sql.connect('mydb.db')
        self.Querycurs = self.connection.cursor()

    def create_table(self):
        self.Querycurs.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY,Nom TEXT,Email TEXT,Mode_de_passe TEXT,Role TEXT)''')
        self.get_connection().commit()


    # Insert a list to the table
    def AddEntry(self,Nom, Email, Mode_de_passe,Role):
        self.Querycurs.execute('''INSERT INTO users(Nom,Email,Mode_de_passe,Role) VALUES (?,?,?,?)''', (Nom, Email, Mode_de_passe,Role))

    # Return rows that exist in
    def dict_factory(self,cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    #Select all the users in the db
    def extract_from_data(self):
        self.Querycurs.row_factory = self.dict_factory

        self.Querycurs.execute("SELECT * from users")
        res = self.Querycurs.fetchall()
        return res

    #Select in specific user
    def load_user(self, Nom):
        self.Querycurs.row_factory = self.dict_factory
        self.Querycurs.execute("SELECT * FROM users WHERE Nom=?", (Nom,))
        res = self.Querycurs.fetchone()
        return res

    #Update a user
    def update(self, data, Name):
        self.Querycurs.row_factory = self.dict_factory
        self.Querycurs.execute("UPDATE users SET Nom= ? ,Email=? ,Mode_de_passe=? WHERE Nom=?",
                          (data[0], data[1], data[2], Name))
        res = self.Querycurs.fetchall()
        return res

    #Delete a user
    def delete(self, Nom):
        self.Querycurs.row_factory = self.dict_factory
        self.Querycurs.execute("DELETE FROM users WHERE Nom=?", (Nom,))
        res = self.Querycurs.fetchall()
        return res


    #Close connnetion
    def close_connection(self):
        self.Querycurs.close()
        self.connection.close()


    #Function to call connection and the cursor

    def get_connection(self):
        return self.connection
    def get_cursor(self):
        return self.Querycurs



    def create_role_table(self,Table_Name):
        self.Querycurs.execute("CREATE TABLE IF NOT EXISTS {} (id INTEGER PRIMARY KEY,role_Name TEXT)".format(Table_Name))
        self.get_connection().commit()

    def AddEntry_role(self,Nom,Role):
        self.Querycurs.execute("INSERT INTO {}(role_Name) VALUES (?)".format(Nom),
                               (Role,))

    def extract_from_role(self,Table_Name):
        self.Querycurs.row_factory = self.dict_factory

        self.Querycurs.execute("SELECT * from {}".format(Table_Name))
        res = self.Querycurs.fetchall()
        return res

    #Select roles
    def load_role(self, Nom):
        self.Querycurs.row_factory = self.dict_factory
        self.Querycurs.execute("SELECT * FROM {} ".format(Nom))
        res = self.Querycurs.fetchall()
        return res



    #Delete a user
    def delete_role(self,Table_Name, role):
        self.Querycurs.row_factory = self.dict_factory
        self.Querycurs.execute("DELETE FROM {} WHERE Nom=?".format(Table_Name), (role,))
        res = self.Querycurs.fetchall()
        return res

