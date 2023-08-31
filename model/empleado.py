class Empleado:
    def __init__(self, id_empleado, nombre, cargo, salario, direccion, telefono, dui, email, id_usuario):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario
        self.direccion = direccion
        self.telefono = telefono
        self.dui = dui
        self.email = email
        self.id_usuario = id_usuario

    def get_id_empleado(self):
        return self.id_empleado

    def set_id_empleado(self, id_empleado):
        self.id_empleado = id_empleado

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_cargo(self):
        return self.cargo

    def set_cargo(self, cargo):
        self.cargo = cargo

    def get_salario(self):
        return self.salario

    def set_salario(self, salario):
        self.salario = salario

    def get_direccion(self):
        return self.direccion

    def set_direccion(self, direccion):
        self.direccion = direccion

    def get_telefono(self):
        return self.telefono

    def set_telefono(self, telefono):
        self.telefono = telefono

    def get_dui(self):
        return self.dui

    def set_dui(self, dui):
        self.dui = dui

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_id_usuario(self):
        return self.id_usuario

    def set_id_usuario(self, id_usuario):
        self.id_usuario = id_usuario
