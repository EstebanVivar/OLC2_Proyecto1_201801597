

import Editor from './components/Editor';
import Home from './components/Home';
import Navigation from './components/Navigation';
import { Route, Switch } from 'react-router-dom';

function App() {
  return (
    <div className="App">
    
      <Navigation />
      <Switch>
        <Route path='/Bienvenida' component={Home} />
        <Route path='/Analisis' component={Editor} />
      </Switch>
    </div>
  );
}

export default App;
