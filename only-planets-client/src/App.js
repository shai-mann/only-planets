import logo from "./logo.svg";
import "./App.css";

function App() {
  return (
    <div className="app-container">
      {/* Title and subtitle */}
      <h1 className="app-title">Only Planets</h1>
      <h2 className="app-subtitle">
        Vote yes if you want to see more of this planet...
      </h2>

      {/* Planet image */}
      <img src={logo} alt={"planet"} className="planet-image" />

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
