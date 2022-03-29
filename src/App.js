import "./App.css";
import { Route, BrowserRouter as Router, Switch } from "react-router-dom";
import Login from "./pages/Login";
// import Dashboard from "./pages/Dashboard";

function App() {
  return (
    <div className="App">
      <Router>
        <Switch>
          {/* <Route path="/dashboard" component={Dashboard} /> */}
            <Route path="/" component={Login} />
        </Switch>
      </Router>
    </div>
  );
}

export default App;
