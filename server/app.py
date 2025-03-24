from flask import Flask, request

from nasa_controller import NASAController
from planet_controller import PlanetController

app = Flask(__name__)

# Create the planet controller
planet_controller = PlanetController()

# create the NASA controller
nasa_controller = NASAController()


# define a GET endpoint for the /planet route, which will return a random planet
@app.route("/planet", methods=["GET"])
def get_planet():
    # get a random planet from NASA
    planet = nasa_controller.get_random_planet()

    # create the planet in the planet controller
    planet = planet_controller.create_planet(planet)

    # Send the planet back to the client
    return {"planet": planet}


# define a GET endpoint for the /planets route, which will return a list of planets
# that the user has already seen and voted on.
@app.route("/planets", methods=["GET"])
def get_planets():
    planets = planet_controller.get_all_planets()
    # send the data back to the client
    return {"planets": planets}


# define a POST endpoint for the /planet route, which will allow the user to vote on a planet
@app.route("/vote/<planet_id>", methods=["POST"])
def vote_on_planet(planet_id):
    vote = request.args.get("vote")
    planet_controller.vote_on_planet(planet_id, vote)

    return {"success": True}


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
