from flask import Flask, render_template, request

app = Flask(__name__)

from pickle import FALSE

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/formularioCalcular', methods=['GET', 'POST'])
def formularioCalcular():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        tarros = int(request.form['cant_tarros'])
        tot_sd = tarros * 9000
        if(edad >= 18 and edad <= 30):
            dcto = tot_sd * 0.15
            tot_cd = tot_sd - tot_sd * 0.15
            return render_template('formularioCalcular.html', nombre_cliente = nombre, total_sd = tot_sd, descuento = dcto, total_cd = tot_cd)
        elif(edad > 30):
            dcto = tot_sd * 0.25
            tot_cd = tot_sd - tot_sd * 0.25
            return render_template('formularioCalcular.html', nombre_cliente = nombre, total_sd = tot_sd, descuento = dcto, total_cd = tot_cd)
        else:
            dcto = 0
            return render_template('formularioCalcular.html', nombre_cliente = nombre, total_sd = tot_sd, descuento = dcto, total_cd = tot_sd)

    return render_template('formularioCalcular.html')

@app.route('/nombresFormulario', methods=['GET', 'POST'])
def nombresFormulario():
    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']
        usuarios = ["juan","pepe"]
        passwords = ["admin","user"]
        if(usuario == usuarios[0] and password == passwords[0]):
            mns = "Bienvenido Aministrador juan"
            return render_template('nombresformulario.html', mensaje = mns)
        elif(usuario == usuarios[1] and password == passwords[1]):
            mns = "Bienvenido Usuario pepe"
            return render_template('nombresFormulario.html', mensaje = mns)
        else:
            mns = "Usuario o contraseña incorrectos"
            return render_template('nombresFormulario.html', mensaje = mns)
    return render_template('nombresFormulario.html')

if __name__ == '__main__':
    app.run(debug=True)