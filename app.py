from flask import Flask, render_template, request, Response
from flask_restful import Resource, Api
import pandas as pd
import matplotlib.pyplot as plt
import plotly
import plotly.express as px
import json
# Our modules.
import m14uf1_simex_part1
import mod_plots

app = Flask(__name__)
api = Api(app)

df = m14uf1_simex_part1.q0_read_correct_data()

# WEB SERVICES 

@app.route("/observation")
def patients():
    data = df.head(50)
    return Response(
        data.to_json(orient="records"),
        mimetype='application/json')


@app.route("/observation/<field>/<value>")
def query(field, value):
    data = df[df[field] == value]
    if data.empty:
        return {"error": "no data found", "field": field, "value": value}, 404

    # data = data.to_json(orient="records")
    return Response(
        data.to_json(orient="records"),
        mimetype='application/json')


# WEB PAGE ROUTES
@app.route("/")
def index():
    return render_template("index.html",title="Pe1")

# Pregunta 5. Crea 2 serveis web GET:
#               Un que mostri les 50 primeres files. Sintaxi:
#               ./observation
#               Un altre que mostri totes les files d'una enfermetat (DISEASE) indicada.
#               ./observation/DISEASE/MEASLES
@app.route("/q5_api")
def q5_api():
    return render_template("q5_api.html",title="Pe1-APIs")


# Pregunta 6. Mostra 2 gràfics a la pàgina web
#               Un on es vegi la incidència de les enfermetats d'un país(el que tu vulguis) 
#               des del 1980 fins el 2021, ambdós inclosos.
#               ./observation
#               Un gràfic que serveixi per comparar les dades d'una enfermetat amb molta incidència (per exemple MEASLES) Ç
#               a una agrupació de països del món que tingui almenys 3 països.
#               Tens 2 gràfics de mostra a la carpeta output (q6_plot1 i q6_plot2)
#               Pista: amb la funció de Pandas is_in pots seleccionar molts.
@app.route("/q6_plots")
def q6_plots():
    grafic1 = mod_plots.demo_plot()
    # Només és un exemple.
    south_mediterrean_countries: list[str] = ['Morocco', 'Algeria', 'Libya', 'Egypt', 'Jordan', 'Israel']
    return render_template("q6_plots.html",title="Pe1-Plots",grafic1=grafic1)

# Pregunta 7. Crea un mapa del món on es mostri la evolució dels casos de 
# xarampió = MEASLES cada any amb Plotly.
@app.route("/q7_map")
def q7_map():
    fig = mod_plots.map1(df)
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('q7_map.html',title="Pe1-Map",graphJSON=graphJSON)

# MAIN

if __name__ == "__main__":
    app.run()
    # app.run(debug=True)