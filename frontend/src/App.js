import "./App.css";
import { Route, Switch } from "react-router-dom";
import DuckFeed from "./components/DuckFeed";

function App() {
  return (
    <>
      <Switch>
        <Route exact path="/" component={DuckFeed} />
      </Switch>
    </>
  );
}

export default App;
