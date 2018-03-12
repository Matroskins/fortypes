import React, { Component } from 'react'
import Isotope from 'isotope-layout'
import { Container } from 'rebass'
import ContainerImg from './ContainerImg'
import PerformSize from './PerformSize'
import GridMasonry from './GridMasonry'
import './index.css'

export class Grid extends Component {
  isotope = null
  state = {
    sizeArray: [],
    knowSize: false,
  }

  handleSaveSize = (id, container) => {
    const {setState} = this
    console.log('handle')
    console.log(container)
    console.log(`prev state`)
    const setStateF = (height, width) => {this.setState((prevState) =>{ return {sizeArray: [
      ...prevState.sizeArray,
      { id, height, width },
    ]}}) }
    container.onload = function(){ 
      setStateF(this.height, this.width)
    }
    
    console.log(this.state.sizeArray)
  }
  render() {
    const { allFonts } = this.props
    const { sizeArray } = this.state
    const knowSize = sizeArray.length === allFonts.length
    console.log('size array')
    console.log(sizeArray)
    return (
      <div>
        {knowSize && <GridMasonry sizeArray={sizeArray} allFonts={allFonts} />}
        {allFonts.map(font => {
          return <PerformSize setSizeArray={this.handleSaveSize} font={font} key={`item_${font.id}`} />
        })}
      </div>
    )
  }
}

export default Grid
