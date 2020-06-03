class Utilisateur:

    def __init__(self,role):
        self.Nom = None
        self.Email = None
        self.Mode_de_passe = None
        self.role= None

    def get_role(self):
        return self.role

    def set_role(self,role):
        self.role=role

    def get_Nom(self):
        return self.Nom

    def get_email(self):
        return self.Email

    def get_mdp(self):
        return self.Mode_de_passe

    def set_nom(self, Nom):
        self.Nom = Nom

    def set_mdp(self, mdp):
        self.Mode_de_passe = mdp

    def set_email(self, email):
        self.Email = email
