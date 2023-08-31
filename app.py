from flask import Flask, render_template, request, redirect, session, flash
import mysql.connector
from model.usuario import Usuario
from model.empleado import Empleado
from model.cliente import Cliente

app = Flask(__name__)
app.secret_key = "mi_clave_secreta"

# Configura la conexión a la base de datos
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="sistema_ventas_AS2"
)


@app.route("/", methods=["GET", "POST"])
def login():
    mensaje = None
    if request.method == "POST":
        usuario = request.form["usuario"]
        contrasena = request.form["contrasena"]

        cursor = db.cursor()
        cursor.execute(
            "SELECT * FROM USUARIO WHERE usuario = %s AND Contraseña = %s", (usuario, contrasena))
        usuario_data = cursor.fetchone()
        print(usuario_data)
        if usuario_data:
            print("usuario_data")
            usuario_obj = Usuario(
                usuario_data[0], usuario_data[1], usuario_data[2])
            # Usa la clase Usuario
            session["usuario"] = usuario_obj.get_usuario()
            print(session["usuario"])
            return render_template("menu.html", nombre_usuario=session["usuario"])
        else:
            print("else")
            mensaje = "Usuario o contraseña incorrectos"

    return render_template("login.html", mensaje=mensaje)


@app.route("/menu")
def menu():
    if "usuario" in session:
        return render_template("menu.html", nombre_usuario=session["usuario"])
    else:
        return redirect("/")


@app.route("/logout")
def logout():
    session.pop("usuario", None)
    return redirect("/")


@app.route("/empleado", methods=["GET", "POST"])
def nuevo_empleado():

    if request.method == "POST":
        operacion = request.form["operacion"]

        if operacion == "insertar":
            # Insertar un nuevo empleado
            nombre = request.form["nombre"]
            cargo = request.form["cargo"]
            salario = request.form["salario"]
            direccion = request.form["direccion"]
            telefono = request.form["telefono"]
            dui = request.form["dui"]
            email = request.form["email"]

            # Realizar la inserción en la base de datos
            cursor = db.cursor()
            cursor.execute(
                "INSERT INTO USUARIO (Usuario, Contraseña) VALUES (%s, %s)", (nombre, '12345'))
            db.commit()

            id_usuario = cursor.lastrowid

            cursor.execute("INSERT INTO EMPLEADO (Nombre, Cargo, Salario, Dirección, Teléfono, Dui, Email, Id_Usuario) "
                           "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (nombre, cargo, salario, direccion, telefono, dui, email, id_usuario))
            db.commit()
            flash("Empleado insertado exitosamente", "success")
        elif operacion == "actualizar":
            # Actualizar un empleado existente
            id_empleado = request.form["id_empleado"]
            nombre = request.form["nombre"]
            cargo = request.form["cargo"]
            salario = request.form["salario"]
            direccion = request.form["direccion"]
            telefono = request.form["telefono"]
            dui = request.form["dui"]
            email = request.form["email"]

            # Realizar la actualización en la base de datos
            cursor = db.cursor()
            cursor.execute("UPDATE EMPLEADO SET Nombre = %s, Cargo = %s, Salario = %s, Dirección = %s, Teléfono = %s, Dui = %s, Email = %s WHERE Id_Empleado = %s",
                           (nombre, cargo, salario, direccion, telefono, dui, email, id_empleado))
            db.commit()
            flash("Empleado actualizado exitosamente", "success")

        return redirect("/empleado", code=302)

    # Obtén la lista de empleados desde la base de datos
    cursor = db.cursor()
    cursor.execute("SELECT * FROM EMPLEADO")
    empleados_data = cursor.fetchall()

    empleados = []
    for empleado_data in empleados_data:
        empleado = Empleado(empleado_data[0], empleado_data[1], empleado_data[2], empleado_data[3],
                            empleado_data[4], empleado_data[5], empleado_data[6], empleado_data[7], empleado_data[8])
        empleados.append(empleado)

    return render_template("empleado.html", empleados=empleados)


@app.route("/nuevo_cliente", methods=["GET", "POST"])
def nuevo_cliente():
    clientes = []
    if request.method == "POST":
        operacion = request.form["operacion"]

        if operacion == "insertar":
            nombre = request.form["nombre"]
            direccion = request.form["direccion"]
            telefono = request.form["telefono"]
            dui = request.form["dui"]
            email = request.form["email"]

            cursor = db.cursor()
            cursor.execute("INSERT INTO CLIENTE (Nombre, Dirección, Teléfono, Dui, Email) VALUES (%s, %s, %s, %s, %s)",
                           (nombre, direccion, telefono, dui, email))
            db.commit()

            flash("Cliente insertado exitosamente", "success")
        elif operacion == "actualizar":
            id_cliente = request.form["id_cliente"]
            nombre = request.form["nombre"]
            direccion = request.form["direccion"]
            telefono = request.form["telefono"]
            dui = request.form["dui"]
            email = request.form["email"]

            cursor = db.cursor()
            cursor.execute("UPDATE CLIENTE SET Nombre = %s, Dirección = %s, Teléfono = %s, Dui = %s, Email = %s WHERE Id_Cliente = %s",
                           (nombre, direccion, telefono, dui, email, id_cliente))
            db.commit()

            flash("Cliente actualizado exitosamente", "success")

        # return render_template("nuevo_cliente.html", clientes=clientes)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM CLIENTE")
    clientes_data = cursor.fetchall()

    for cliente_data in clientes_data:
        cliente = Cliente(cliente_data[0], cliente_data[1], cliente_data[2],
                          cliente_data[3], cliente_data[4], cliente_data[5], cliente_data[6])
        clientes.append(cliente)
    return render_template("nuevo_cliente.html", clientes=clientes)


if __name__ == "__main__":
    app.run(debug=True)
