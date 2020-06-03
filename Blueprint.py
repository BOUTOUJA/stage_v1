from flask import Blueprint
from flask import jsonify, request

from Dao.Dao_Utilisateur import Dao_Utilisateur as Dao_u
from Dao.Dao_Role import Dao_Role as Dao_r

blueprint= Blueprint('Blueprint', __name__)


#Get request that return all the users
@Blueprint.route('v1/users', methods=['GET'])
def users():
    dao = Dao_u()
    res= dao.all_users()
    return jsonify(res)

#Get request that return a specific user
@Blueprint.route('v1/users/<nom:String>', methods=['GET'])
def find_user(nom):
    dao= Dao_u()
    res=dao.get_user(nom)
    return jsonify(res)


#Post request to put a user
@Blueprint.route('v1/add', methods=['POST'])
def add_user():
    data=request.get_json()
    dao = Dao_u()
    res= dao.add_user(data)
    resp = jsonify('User added successfully!',res)
    return resp

#PUT request to update a user
@Blueprint.route('v1/add/<name:String>',methods=['PUT'])
def update_user(Name):
    dao = Dao_u()
    re=request.get_json()
    liste=(re['Name'],re['Email'],re['Mode_de_passe'])
    res=dao.update_user(liste,Name)
    return jsonify(res)


# Request to DELETE a user from the database
@Blueprint.route('/delete/<name:String>', methods=['DELETE'])
def delete_user(name):
    dao= Dao_u()
    dao.delete(name)
    return jsonify("The user has been deleted successfully")



#Show all the roles that belongs to a specific user
@Blueprint.route('v1/roles/<name>',methods=['GET'])
def get_all_roles(name):
    dao_r=Dao_r()
    res=dao_r.get_user_role(name)
    return jsonify(res)


#Add a role to a specific user
@Blueprint.route('v1/addrole/<name:String>',methods=['post'])
def add_role(name):
    data=request.get_json()
    dao=Dao_r()
    res=dao.add_role(data, name)
    return jsonify(res)

#Request to DELETE a role user
@Blueprint.route('v1/delete/<name:String>/<role:String>',methods=['DELETE'])
def delete_role(name,role):
    dao=Dao_r()
    dao.DB.delete_role(name, role)
    return jsonify("The role has been deleted successefully")


