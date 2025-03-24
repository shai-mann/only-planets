from flask import Flask
import random

app = Flask(__name__)


# define a GET endpoint for the /planet route, which will return a random planet
@app.route("/planet", methods=["GET"])
def get_planet():
    # for now, generate a random planet ID. In the future, this will be real planet data.
    planet_id = random.randint(0, 1000000)
    # send the data back to the client
    return {"id": planet_id}


# define a GET endpoint for the /planets route, which will return a list of planets
# that the user has already seen and voted on.
@app.route("/planets", methods=["GET"])
def get_planets():
    # for now, generate a random list of planet IDs. In the future, this will be real planet data.
    planet_ids = [random.randint(0, 1000000) for _ in range(10)]
    # send the data back to the client
    return {"ids": planet_ids}


# define a POST endpoint for the /planet route, which will allow the user to vote on a planet
@app.route("/vote/<planet_id>", methods=["POST"])
def vote_on_planet(planet_id):
    # send the data back to the client
    return {"id": planet_id}


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
