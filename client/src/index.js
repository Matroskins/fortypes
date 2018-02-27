import React from 'react'
import ReactDOM from 'react-dom'
import {Provider as ProviderRebass} from 'rebass'
import {theme} from './constants/index'
import './index.css'
import MainPage from './Components/MainPage'
import registerServiceWorker from './registerServiceWorker'

ReactDOM.render(<ProviderRebass theme={theme}><MainPage /></ProviderRebass>, document.getElementById('root'))
registerServiceWorker()
