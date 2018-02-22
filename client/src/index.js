import React from 'react'
import ReactDOM from 'react-dom'
import {Provider as ProviderRebass} from 'rebass'
import './index.css'
import MainPage from './Components/MainPage'
import registerServiceWorker from './registerServiceWorker'

ReactDOM.render(<ProviderRebass><MainPage /></ProviderRebass>, document.getElementById('root'))
registerServiceWorker()
