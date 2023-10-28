from flask import Flask, render_template, request
from forecas import main as get_weather
from forecas import mainf as get_forecast

app =Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    data = None
    lst = None
    if request.method=="POST":
        city=request.form["cityName"]
        state=request.form["stateName"]
        country=request.form["countryName"]
        data = get_weather(city, state, country)
        lst =  get_forecast(city, state, country)
    return render_template("index.html", data=data, lst=lst)

if __name__ == "__main__":
    app.run(debug=True)