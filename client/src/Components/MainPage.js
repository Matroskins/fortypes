import React, { Component } from 'react'
import DropDownNew from 'Common/Uikit/DropDown/DropDown'
class MainPage extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <h1 className="App-title">Welcome to React</h1>
          <DropDownNew />
        </header>
        <p className="App-intro">
          To get start, edit <code>src/App.js</code> and save to reload.
        </p>
      </div>
    );
  }
}

export default MainPage;
