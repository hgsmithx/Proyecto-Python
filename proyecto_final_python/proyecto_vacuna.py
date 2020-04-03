import requests
import json
from flask import Flask, render_template, jsonify, request, flash
from flaskext.mysql import MySQL
import pymysql
import pymysql.cursors
from flask.helpers import url_for

# Integrantes: Lincoln Smith - Ignacio Medina
app = Flask(__name__)
app.config["MYSQL_DATABASE_USER"] = "root"
app.config["MYSQL_DATABASE_DB"]  = "proyectovacuna"

app.secret_key = 'mysecretkey'

mysql = MySQL(app)
mysql.connect_args["autocommit"] = True
mysql.connect_args["cursorclass"] = pymysql.cursors.DictCursor


@app.route('/', methods=["GET","POST"])
def inicio():
	if request.method == 'POST':
		rut = request.form['rut']
		nombre = request.form['nombre']
		fecha = request.form['fecha_nac']

		cursor2 = mysql.get_db().cursor()
		sql2 = "SELECT paciente.rut FROM paciente" 
		cursor2.execute(sql2)
		contador  = 0
		rutPacientes = cursor2.fetchall()

		for row in rutPacientes:
			if rut == row['rut']:
				contador = contador + 1
		if contador == 0:
			cursor = mysql.get_db().cursor()
			sql = "INSERT INTO paciente (rut,nombre,fecha_nac)"
			sql += " VALUES (%s,%s,%s)"
			cursor.execute(sql,(rut,nombre,fecha))
			flash('Agregado Correctamente')
		else:
			flash("El rut del paciente ya existe")					
		

	cursor = mysql.get_db().cursor()
	consulta = "SELECT * FROM paciente"
	cursor.execute(consulta)
	enviarconsulta = cursor.fetchall()

	
	return render_template('paciente.html', variablehtml=enviarconsulta)

@app.route('/nuevoPaciente', methods=["GET", "POST"])
def nuevoPaciente():

	return render_template('agregar_paciente.html')	

@app.route('/nuevaVacuna')
def addVacuna():
		
	return render_template('nuevaVacuna.html') 	

@app.route('/agregarVacunacion/<string:rut>',methods=["GET","POST"])
def agregarVacunacion(rut):

	if request.method == "POST":
		idVacuna= request.form['idVacuna']
		RutPaciente = rut
		
		cursor2 = mysql.get_db().cursor()
		sql2 = "SELECT recibe.id_vacuna FROM recibe WHERE recibe.rut_paciente = %s" 
		cursor2.execute(sql2,(RutPaciente))
		contador  = 0
		contagiado = cursor2.fetchall()
		
		for row in contagiado:
			if int(idVacuna) == int(row['id_vacuna']):
				contador = contador + 1
		if contador == 0:
			cursorEnfermedad = mysql.get_db().cursor()
			sql3 = "INSERT INTO recibe (rut_paciente, id_vacuna)"
			sql3 += " VALUES (%s,%s)"
			cursorEnfermedad.execute(sql3,(RutPaciente,idVacuna))
			flash("El paciente ha sido vacunado")
		else:
			flash("El paciente ya posee esta Vacuna")

	cursor = mysql.get_db().cursor()
	cursor2 = mysql.get_db().cursor()
	sql1 = "SELECT * FROM paciente where rut = %s"
	cursor.execute(sql1,(rut))
	datos_paciente = cursor.fetchall()
	sql2 = "SELECT vacuna.idVacuna, vacuna.enfermedad from vacuna"
	cursor2.execute(sql2)
	enfermedad = cursor2.fetchall()
	return render_template('agregar_vacunacion.html',datosPaciente=datos_paciente,enfermedadPaciente=enfermedad)

@app.route('/verVacunaPaciente/<string:rut>')
def verDetallePaciente(rut):
	cursor = mysql.get_db().cursor()
	cursor2 = mysql.get_db().cursor()
	sql = "SELECT vacuna.enfermedad, recibe.fecha_vacuna FROM vacuna INNER JOIN recibe ON recibe.id_vacuna=vacuna.idVacuna INNER JOIN paciente ON recibe.rut_paciente = paciente.rut WHERE paciente.rut = %s"
	sql2 = "SELECT paciente.nombre FROM paciente WHERE rut = %s"
	cursor2.execute(sql2,(rut))
	nombrePaciente = cursor2.fetchall()
	cursor.execute(sql,(rut))
	detalleVacunaPaciente = cursor.fetchall()
	return render_template('ver_vacuna_paciente.html', nombrePaciente = nombrePaciente, detalleVacunaPaciente = detalleVacunaPaciente) 


@app.route('/vacunaPaciente/<string:idVacuna>')
def vacunaPaciente(idVacuna):

	cursor = mysql.get_db().cursor()
	cursor2 = mysql.get_db().cursor()
	sql = "SELECT paciente.nombre, paciente.rut, recibe.fecha_vacuna "
	sql += " FROM paciente INNER JOIN recibe ON paciente.rut=recibe.rut_paciente"
	sql += " INNER JOIN vacuna ON recibe.id_vacuna=vacuna.idVacuna"
	sql += " AND id_vacuna = %s"
	sql2 = "SELECT vacuna.enfermedad from vacuna where idVacuna = %s"
	cursor2.execute(sql2,(idVacuna))
	enfermedad = cursor2.fetchall()
	cursor.execute(sql,(idVacuna))
	vacunaPaciente = cursor.fetchall()
	return  render_template('vacunas_detalle.html',vp=vacunaPaciente,enfermedad=enfermedad)

@app.route('/ListadoVacunas', methods=["GET","POST"])
def listadoVacunas():
	cursor = mysql.get_db().cursor()

	if request.method == "GET":
		idVacuna = request.args.get('idVacuna', default = "", type = str)
		enfermedad = request.args.get('enfermedad', default = "", type = str)

	if request.method == "POST":
		enfermedad = request.form['enfermedad']
		cursor2 = mysql.get_db().cursor()
		sql2 = "SELECT vacuna.enfermedad FROM vacuna" 
		cursor2.execute(sql2)
		contador  = 0
		nombreEnfermedades = cursor2.fetchall()
		for row in nombreEnfermedades:
			if enfermedad == row['enfermedad']:
				contador = contador + 1
		if contador == 0:
			cursor = mysql.get_db().cursor()
			sql = "INSERT INTO vacuna (enfermedad)"
			sql += " VALUES (%s)"
			cursor.execute(sql,(enfermedad))
			flash('Agregado Correctamente')
		else:
			flash("La vacuna ingresada ya Existe")	


	consulta = "SELECT vacuna.idVacuna, vacuna.enfermedad, vacuna.fecha_registro FROM vacuna"
	cursor.execute(consulta)
	enviarconsulta = cursor.fetchall()
	
	return render_template('vacunas.html', variable2html=enviarconsulta)
	


if __name__ == "__main__":
	app.run(debug=True)