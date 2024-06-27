from flask import Flask, render_template, jsonify

app = Flask(__name__)


project_list = [
    {
        'id': 1,
        "title": "Quiz (Using Tkinter)",
        "description": "This is a program which uses the OpenWeatherMap API to get weather data based on your longitude and latitude. Based on the data recived from the API it checkes for the possibilities of Rainfall, if there is any possibility of raining then it will alert you through your gmail.",
        "image_src": "static/images/quiz.jpg"
    },
    {
        'id': 2,
        "title": "Arcade Games (Pong, Crossy road)",
        "description": "This is a program which uses the OpenWeatherMap API to get weather data based on your longitude and latitude. Based on the data recived from the API it checkes for the possibilities of Rainfall, if there is any possibility of raining then it will alert you through your gmail.",
        "image_src": "static/images/game.jpg"
    },
    {
        'id': 3,
        "title": "Rainfall Alert",
        "description": "This is a program which uses the OpenWeatherMap API to get weather data based on your longitude and latitude. Based on the data recived from the API it checkes for the possibilities of Rainfall, if there is any possibility of raining then it will alert you through your gmail.",
        "image_src": "static/images/rainfall.jpg"
    },
    {
        'id': 4,
        "title": "Automated Amazon Price Tracker",
        "description": "This is a program which uses the OpenWeatherMap API to get weather data based on your longitude and latitude. Based on the data recived from the API it checkes for the possibilities of Rainfall, if there is any possibility of raining then it will alert you through your gmail.",
        "image_src": "static/images/amazon.jpg"
    },
    {
        'id': 5,
        "title": "Automatic Parking Ticket Generator",
        "description": "This is a program which uses the OpenWeatherMap API to get weather data based on your longitude and latitude. Based on the data recived from the API it checkes for the possibilities of Rainfall, if there is any possibility of raining then it will alert you through your gmail.",
        "image_src": "static/images/pay_parking.jpg"
    }
]



@app.route("/")
def home_page():
    return render_template('home.html',
                           projects=project_list)


@app.route("/api/projects")
def list_projects():
    return jsonify(project_list)





if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
