

import Editor from './components/Analysis';
import Home from './components/Home';
import Reports from './components/Reports';

import Symbols from './components/Symbols_Table';


import Errors from './components/Errors';
import Navigation from './components/Navigation';
import { Route, Switch } from 'react-router-dom';

function App() {
  return (
    <div className="App">
    
      <Navigation />
      <Switch>
        <Route exact path='/' component={Home} />
        <Route path='/Bienvenida' component={Home} />
        <Route path='/Analisis' component={Editor} />
        <Route path='/Reportes' component={Reports} />
        <Route path='/Errores' component={Errors} />
        <Route path='/TablaSimbolos' component={Symbols} />
      </Switch>
    </div>
  );
}

export default App;
