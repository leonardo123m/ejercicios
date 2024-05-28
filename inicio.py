from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash
import pymysql

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/layout')
def layout():
    return render_template("layout.html")



@app.route('/ej1', methods=['GET', 'POST'])
def ej1():
    if request.method == 'POST':
        try:
            base = float(request.form['base'])
            altura = float(request.form['altura'])
            area = (base * altura) / 2
            return render_template("ej1.html", area=area)
        except ValueError:
            error = "Por favor, ingrese valores numéricos para la base y la altura."
            return render_template("ej1.html", error=error)
    else:
        return render_template("ej1.html")



@app.route('/ej2', methods=['GET', 'POST'])
def ej2():
    if request.method == 'POST':
        try:
            f = float(request.form['fahrenheit'])
            C= (5/9) * (f - 32)
            return render_template("ej2.html", c=C)
        except ValueError:
            error = "Por favor, ingrese valores numéricos para los grados."
            return render_template("ej2.html", error=error)
    else:
        return render_template("ej2.html")



@app.route('/ej3', methods=['GET', 'POST'])
def ej3():
    if request.method == 'POST':
        try:
            c = float(request.form['cal'])
            if c <= 5:
                mensaje = "REPROBADO"
            elif c==6:
                mensaje = "SUFICIENTE"
            elif c==7:
                mensaje = "REGULAR"
            elif c==8 or c==9:
                mensaje = "NOTABLE"
            elif c==10:
                mensaje = "EXCELENTE"
            else:
                raise ValueError("La calificación debe estar entre 1 y 10.")
            return render_template("ej3.html", mensaje=mensaje, cal=c)
        except ValueError:
            error = "Por favor, ingrese calificacion de 1 a 10"
            return render_template("ej3.html", error=error)
    else:
        return render_template("ej3.html")

@app.route('/ej4', methods=['GET', 'POST'])
def ej4():
    if request.method == 'POST':
        try:
            paga=0
            a = int(request.form['al'])
            if a <=99 and a>=50:
                paga=70 * a
                mensaje = "costo es de $70 por alumno"
                mensaje2 = f"Renta a autobus es de ${paga}"
            elif  a <=49 and a>=30:
                paga= 95 * a
                mensaje = "Costo es de $95 por alumno"
                mensaje2 = f"Renta a autobus es de ${paga}"
            elif a<30:
                paga=3500/a
                mensaje2 = f"Costo es de ${paga} por alumno"
                mensaje = "Renta a autobus es de $3500"
            elif a>99:
                mensaje = "Error: Maximo de alumnos: 99"
                mensaje2 = "Vuelva a intentarlo"
            else:
                raise ValueError("Por vafor, ingrese cantidad de alumnos valida")
            return render_template("ej4.html", pa=mensaje, au=mensaje2)
        except ValueError:
            error = "Por favor, ingrese calificacion de 1 a 10"
            return render_template("ej4.html", error=error)
    else:
        return render_template("ej4.html")




@app.route('/ej5', methods=['GET', 'POST'])
def ej5():
    if request.method == 'POST':
        try:
            nu = int(request.form['n'])
            m = []
            for i in range(1,11):  
                r = i * nu
                fila = f"{nu} * {i} = {r}"
                m.append(fila)
            return render_template("ej5.html", t=m)
        except ValueError:
            error = "Por favor, ingrese números válidos"
            return render_template("ej5.html", error=error)
    else:
        return render_template("ej5.html")


@app.route('/diseños.css')
def serve_css():
    return send_from_directory('static', 'diseños.css')

if __name__ == "__main__":
    app.run(debug=True)
