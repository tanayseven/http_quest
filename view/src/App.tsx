import * as React from 'react';
import './App.css';

import { Button, Card, TextField } from '@material-ui/core';

class App extends React.Component {
  public render() {
    return (
      <Card className="login-card">
        <div className="centered-container"><p>Login into Http Quest</p></div>
        <div className="centered-container"><TextField id="username" className="login-input" label="Username" variant="outlined"/></div>
        <div className="centered-container"><TextField id="password" className="login-input" label="Password" variant="outlined" type="password" /></div>
        <div className="centered-container"><Button className="login-input" variant="contained" color="primary">Login</Button></div>
        <div className="centered-container"><Button className="login-input" variant="contained" color="primary">Sign Up</Button></div>
      </Card>
    );
  }
}

export default App;
