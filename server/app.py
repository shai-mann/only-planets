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


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
