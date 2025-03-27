import logo from "./logo.svg";
import "./App.css";

function App() {
  return (
    <div>
      {/* Title and subtitle */}
      <h1>Only Planets</h1>
      <h2>Vote yes if you want to see more of this planet...</h2>

      {/* Planet image */}
      <img src={logo} alt={"planet"} />

      {/* Vote buttons */}
      <button>Yes</button>
      <button>No</button>
    </div>
  );
}

export default App;
