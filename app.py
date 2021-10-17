from flask import Flask

from app1 import registro_medico

app = Flask(__name__)

lista_pacientes = ["Marcos", "Maria"]
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
@app.route("/", methods= ["GET"])
def inicio():
    return "pagina de inicio"

@app.route("/registrop/<registro_paciente>", methods= ["GET", "POST"])
def registropaciente(registro_paciente):
    
    if registro_paciente:
        lista_pacientes.append(registro_paciente)
        return f"paciente registrado exitosamente, bienvenid@ {registro_paciente}\n{lista_pacientes}"
        


@app.route("/eliminarpaciente/<string:id_paciente>", methods = ["GET", "POST"])
def eliminarpaciente(id_paciente):
    if id_paciente in lista_pacientes:
        lista_pacientes.remove(id_paciente)
        return f"usuario ({id_paciente}) paciente eliminado correctamente {lista_pacientes}"


@app.route("/eliminarmedico/<string:id_medico>", methods = ["GET", "POST"])
def eliminarmedico(id_medico):
    if id_medico in lista_medicos:
        lista_medicos.remove(id_medico)
    return f"usuario ({id_medico}) medico eliminado correctamente {lista_medicos}" 


@app.route("/registrom/<string:id_medico>", methods= ["GET", "POST"])
def registromedico(id_medico):
    if id_medico:
        lista_medicos.append(id_medico)
        return f"Médico registrado exitosamente, bienvenid@ {id_medico}\n{lista_medicos}"
    

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

@app.route("/paginapaciente/<id_comentario>", methods= ["GET", "POST"])
def paginapaciente(id_comentario):
    if id_comentario in lista_comentarios:
        return lista_comentarios[id_comentario]
    else:
        return "El comentario que busca no existe"

@app.route("/paginaadmin/<id_comentario>", methods= ["GET", "POST"])
def paginaadmin(id_comentario):
    if id_comentario in lista_comentarios:
        return lista_comentarios[id_comentario]
    else:
        return "El comentario que busca no existe"

@app.route("/paginaadmin/eliminar_comentario/<eliminar_comentario>", methods= ["GET", "POST"])
def eliminar_comentarios(eliminar_comentario):
    if eliminar_comentario in lista_comentarios:
        del lista_comentarios[eliminar_comentario]
        return lista_comentarios
     

    

@app.route("/paginacitas/<string:id_cita>", methods= ["GET", "POST"])
def paginacitas(id_cita):
    if id_cita in lista_citas:
        return lista_citas[id_cita]
    else: 
        return f"la lista ({id_cita}) que está solicitando no se encuentra en nuestro sistema"

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