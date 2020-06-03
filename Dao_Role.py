from Config_database import DataBase_Connection
from Models.Role import Role
from Models.Utilisateur import Utilisateur

class Dao_Role :

    def __init__(self):
        self.new_role = Role()
        self.new_user = Utilisateur(self.new_role)
        self.DB = DataBase_Connection()

    def add_role(self, data_from_json, name):
        self.DB.create_role_table(name)
        self.new_role.set_role(data_from_json['Role'])
        self.DB.AddEntry_role(name, self.new_role.get_role())
        self.DB.get_connection().commit()
        res= self.DB.load_role(name)
        self.DB.close_connection()
        return res

    def get_user_role(self, name):
        res=self.DB.load_role(name)
        self.DB.close_connection()
        return res
    def delete_role(self,name, role):
        self.DB.delete_role(name, role)
        self.DB.get_connection().commit()
        self.DB.close_connection()
