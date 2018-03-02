import React from 'react'
import ReactDOM from 'react-dom'
import {Provider as ProviderRebass} from 'rebass'
import WebFont from 'webfontloader'
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider'
import './index.css'
import MainPage from './Components/MainPage'
import registerServiceWorker from './registerServiceWorker'


WebFont.load({
  google: {
    families: ['Anonymous+Pro', 'Playfair+Display:400,400i', 'sans-serif']
  }
});

ReactDOM.render(<MuiThemeProvider><ProviderRebass><MainPage /></ProviderRebass></MuiThemeProvider>, document.getElementById('root'))
registerServiceWorker()
