from flask import Flask

app = Flask(__name__)

lista_pacientes = ["Marcos", "Maria"]
lista_medicos = ["Pedro", "Carmen"]
lista_admin = ["Stiven"]
@app.route("/", methods= ["GET"])
def inicio():
    return "pagina de inicio"

@app.route("/registrop/<string:registro_paciente>", methods= ["GET", "POST"])
def registropaciente(registro_paciente=None):
    
    if registro_paciente:
        lista_pacientes.append(registro_paciente)
        return "paciente registrado exitosamente, bienvenid@ {registro_paciente}"


@app.route("/registrom", methods= ["GET", "POST"])
def registromedico():
    return "registro medico"

@app.route("/loginadmin/<login_admin>", methods= ["GET", "POST"])
def loginadmin(login_admin):
    if login_admin in lista_admin:
        return f"El usuario {login_admin} fue logueado exitosamente"
    else: 
        return f"El usuario {login_admin} no se encuentra registrado en la plataforma"

@app.route("/loginpaciente/<login_paciente>", methods= ["GET", "POST"])
def loginpaciente(login_paciente):
    if login_paciente in lista_pacientes:
        return f"El usuario {login_paciente} fue logueado exitosamente"
    else: 
        return f"El usuario {login_paciente} no se encuentra registrado en la plataforma"

@app.route("/loginmedico/<login_medico>", methods= ["GET", "POST"])
def loginmedico(login_medico):
    if login_medico in lista_medicos:
        return f"El usuario {login_medico} fue logueado exitosamente"
    else: 
        return f"El usuario {login_medico} no se encuentra registrado en la plataforma"

@app.route("/paginapaciente", methods= ["GET", "POST"])
def paginapaciente():
    return "pagina paciente"

@app.route("/paginaadmin", methods= ["GET", "POST"])
def paginaadmin():
    return "pagina admin"

@app.route("/paginacitas", methods= ["GET", "POST"])
def paginacitas():
    return "listado de citas"

@app.route("/paginacitadesc", methods= ["GET", "POST"])
def paginacitadesc():
    return "pagina descripcion de citas"

@app.route("/dashboard", methods= ["GET"])
def dashboard():
    return "dashboard administrativo"

@app.route("/perfilmedico", methods= ["GET", "POST"])
def perfilmedico():
    return "perfil medico"

@app.route("/resultadosbusqueda", methods= ["GET", "POST"])
def resultadosbusqueda():
    return "resultados de busqueda"

if __name__ == "__main__":
    app.run(debug=True)