import logo from "./logo.svg";
import "./App.css";
import React, { useState, useEffect } from "react";

// This is the URL of the API we are using to fetch the planet data
const API_URL = "http://localhost:8080/planet";

function App() {
  // This is a state variable that will store the planet object
  // When there is no planet, it will be null
  const [planet, setPlanet] = useState(null);

  // This function fetches the planet data from the API
  // It's "async", because it isn't instantaneous. While the API call is happening,
  // we still want to be able to do other things, so we tell React the function is async.
  async function fetchPlanet() {
    // We use the await keyword to wait for asynchronous operations to complete.
    const response = await fetch(API_URL);
    const data = await response.json();

    // Once we have the data, we update the state variable with the new data.
    setPlanet(data.planet);
  }

  // This is a useEffect hook, which will run the code inside it when the component is "mounted"
  // A component is mounted when it is created and added to the page (sometimes called the DOM).
  useEffect(() => {
    fetchPlanet();
  }, []);

  return (
    <div className="app-container">
      {/* Title and subtitle */}
      <h1 className="app-title">Only Planets</h1>
      <h2 className="app-subtitle">
        Vote yes if you want to see more of this planet...
      </h2>
      {/* Planet image */}
      {planet !== null && (
        <img src={planet.image} alt={"planet"} className="planet-image" />
      )}
      <p className="planet-name">
        {planet === null ? "Loading..." : planet.name}
      </p>
      {/* Vote buttons */}
      <div className="vote-buttons-container">
        {/* Note that the buttons use the same class - this is allowed! */}
        {/* Note they also use multiple classes - this is also allowed! */}
        <button className="vote-button vote-button-yes">Yes</button>
        <button className="vote-button vote-button-no">No</button>
      </div>
    </div>
  );
}

export default App;
