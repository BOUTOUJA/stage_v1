from Config_database import DataBase_Connection
from Models.Utilisateur import Utilisateur
from Models.Role import Role


class Dao_Utilisateur :

    def __init__(self):
        self.new_role = Role()
        self.new_user = Utilisateur(self.new_role)
        self.DB = DataBase_Connection()

    def all_users(self):
        self.DB.create_table()
        res = self.DB.extract_from_data()
        self.DB.close_connection()
        return res
    def get_user(self,nom):
        self.DB.create_table()
        res = self.DB.load_user(nom)
        res_role = self.DB.extract_from_role(nom)
        res['Role']=res_role
        self.DB.close_connection()
        return res
    def add_user(self,data_from_json):
        self.DB.create_table()
        self.DB.create_role_table(data_from_json['Name'])
        self.new_user.set_nom(data_from_json['Name'])
        self.new_user.set_email(data_from_json['Email'])
        self.new_user.set_mdp(data_from_json['Mode_de_passe'])
        self.new_user.set_role(data_from_json['Role'])
        self.DB.AddEntry(self.new_user.get_Nom(), self.new_user.get_email(), self.new_user.get_mdp(),self.new_user.get_role())
        self.DB.get_connection().commit()
        self.DB.close_connection()
        return self.new_user.__dict__

    def add_role(self,data_from_json,Name):
        self.DB.create_role_table(Name)
        self.new_role.set_role(data_from_json['Role'])
        self.DB.AddEntry_role(Name,self.new_role.get_role())
        self.DB.get_connection().commit()
        res= self.DB.load_role(Name)
        self.DB.close_connection()
        return res

    def update_user(self,modification_list,Name):
        self.DB.create_table()
        self.DB.update(modification_list, Name)
        resp=self.DB.load_user(modification_list[0])
        self.DB.get_connection().commit()
        self.DB.close_connection()
        return resp

    def delete(self,Name):
        self.DB.delete(Name)
        self.DB.get_connection().commit()
        self.DB.close_connection()
