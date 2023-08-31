class Cliente:
    def __init__(self, id_cliente, nombre, direccion, telefono, dui, email, id_usuario):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.dui = dui
        self.email = email
        self.id_usuario = id_usuario

    def get_id_cliente(self):
        return self.id_cliente

    def get_nombre(self):
        return self.nombre

    def get_direccion(self):
        return self.direccion

    def get_telefono(self):
        return self.telefono

    def get_dui(self):
        return self.dui

    def get_email(self):
        return self.email

    def get_id_usuario(self):
        return self.id_usuario
