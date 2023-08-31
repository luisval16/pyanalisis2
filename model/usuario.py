class Usuario:
    def __init__(self, id_usuario, usuario, contraseña):
        self.id_usuario = id_usuario
        self.usuario = usuario
        self.contraseña = contraseña

    def get_id_usuario(self):
        return self.id_usuario

    def set_id_usuario(self, id_usuario):
        self.id_usuario = id_usuario

    def get_usuario(self):
        return self.usuario

    def set_usuario(self, usuario):
        self.usuario = usuario

    def get_contraseña(self):
        return self.contraseña

    def set_contraseña(self, contraseña):
        self.contraseña = contraseña
