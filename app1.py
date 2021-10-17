from flask import Flask
from flask import make_response
from flask import render_template as render
from flask import redirect
from flask import request

app = Flask(__name__)


lista_pacientes = {
    'marcos@gmail.com': {'nombres': 'Marcos', 'apellidos':'Sanchez', 'email': 'marcos@gmail.com', 'item': 'item 1', 'identificacion': '213', 'telefono': '134342', 'contrasena': '1234'},
    'dn@gmail.com': {'nombres': 'Daniela', 'apellidos':'Giraldo', 'email': 'dn@gmail.com', 'item': 'item 1', 'identificacion': '215343', 'telefono': '145342', 'contrasena': '432'}
}
lista_medicos = ["Pedro", "Carmen"]
lista_admin = ["Stiven"]
lista_comentarios = {
"1": "Marcos: Muy buena atencion por parte de los medicos",
"2": "Maria: Gracias por la pronta atencion",
"3": "Dr. Pedro: Por este espacio no se pueden pedir citas, para ello vaya al apartado de citas"

}
lista_citas = {
"medicogeneral":"Pedro: 6am - 12pm", 
"psicologia":"Carmen: 8am - 3 pm", 
"neurologia": "Carlos: 12pm - 8 pm", 
"cuidado del embarazo":"Laura: 12pm - 6 pm", 
"pediatria": "Karol: 7am - 3 pm", 
"cardiologia":"Mario: 6 am - 2 pm"}




# VARIABLES
sesion_iniciada = False
sesion_paciente_iniciada = False
sesion_medico_iniciada = False
sesion_super_iniciada = False
regis_paciente = False
regis_medico = False

# RUTAS


# Home
@app.route("/", methods=["GET", "POST"])
def inicio():
    return render("inicio/inicio.html")

# Login
@app.route("/login_paciente", methods=["GET", "POST"])
def login_paciente():
    global sesion_paciente_iniciada
    sesion_paciente_iniciada = True
    
    return render(
        "login/login_paciente/login_paciente.html" #,
        # sesion_paciente_iniciada=sesion_paciente_iniciada
        )

@app.route("/login_medico", methods=["GET", "POST"])
def login_medico():
    global sesion_medico_iniciada
    sesion_medico_iniciada = True
    return render(
        "login/login_medico/login_medico.html"#,
        # sesion_medico_iniciada=sesion_medico_iniciada
        )

@app.route("/login_superadmin", methods=["GET", "POST"])
def login_super():
    global sesion_super_iniciada
    sesion_super_iniciada = True
    return render(
        "login/login_superadmin/login_superadmin.html"#,
        # sesion_super_iniciada=sesion_super_iniciada
        )


# Registro
@app.route("/registro_paciente", methods=["GET", "POST"])
def registro_paciente():
    global regis_paciente
    regis_paciente = True
    return render(
        "registro/registro_paciente/registro_paciente.html"#,
        # regis_paciente=regis_paciente
        )

@app.route("/registro_medico", methods=["GET", "POST"])
def registro_medico():
    global regis_medico
    regis_medico = True
    return render(
        "registro/registro_medico/registro_medico.html"#,
        # regis_medico=regis_medico
        )

# @app.route("/registro_super", methods=["GET", "POST"])
# def registro_super():
#     return "Pagina de registro de datos para los superadministradores"



# Pagina de perfil
@app.route("/perfil_paciente", methods=["GET", "POST"])
def perfil_paciente():
    return render("perfiles/perfil_paciente/perfil_paciente.html")

""" @app.route("/perfil_medico", methods=["GET", "POST"])
def perfil_medico():
    return render("perfiles/perfil_medico/perfil_paciente.html")

@app.route("/perfil_super", methods=["GET", "POST"])
def perfil_super():
    return render("perfiles/perfil_suoeradmin/perfil_paciente.html") """



# Listado de citas medicas
@app.route("/listado_citas", methods=["GET", "POST"])
def citas():
    return render("listado_citas/listado_citas.html")


# Detalle de la cita
@app.route("/detalle_cita", methods=["GET", "POST"])
def detalle_cita():
    return render("detalle_cita/detalle_cita.html")


# Pagina de paciente
@app.route("/pagina_paciente", methods=["GET", "POST"])
def pagina_paciente():
    if request.method=="POST":
        email = request.values("email")
        contrasena = request.values("contrasena")
        if email in lista_pacientes:
            pass
        else:
            return redirect('/login_paciente')
        
    return render("pagina_paciente/pagina_paciente.html")


@app.route("/salir", methods=["POST"])
def cerrar_sesion():
    global sesion_iniciada
    sesion_iniciada = False
    return redirect('/')





if __name__=='__main__':
    app.run(debug=True)