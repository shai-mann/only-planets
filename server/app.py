from flask import Flask, request

from planet_controller import PlanetController

app = Flask(__name__)

# Create the planet controller
planet_controller = PlanetController()


# define a GET endpoint for the /planet route, which will return a random planet
@app.route("/planet", methods=["GET"])
def get_planet():
    planet_id = planet_controller.create_planet()
    # send the planet's ID back to the client, to use in other API requests.
    return {"id": planet_id}


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
