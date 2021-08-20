

import Home from './components/Home';
import Navigation from './components/Navigation';
import { Route, Switch } from 'react-router-dom';

function App() {
  return (
    <div className="App">
      <Navigation />
      <Switch>
        <Route path='/Home' component={Home} />
      </Switch>
    </div>
  );
}

export default App;
