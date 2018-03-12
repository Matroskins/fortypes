import React, { Component } from 'react'
import { Flex } from 'rebass'
import { compose, withState, withHandlers } from 'recompose'
import getRenderedSize from 'react-rendered-size'
import Gallery from './Gallery'
import FontCard from './FontCard'

class ControllerGallery extends Component {

  state = {
    containersSize: []
  }
  componentWillMount() {
    console.log('will mount')
    const containersSize = this.props.allFonts.map(font => {
      const size = getRenderedSize(<img src={require(`../../img/${font.image.fileName}.jpg`)} />)
      size['id'] = font.id
      return size
    })
    // this.setState({containersSize})
    console.log(containersSize)
  }
  render() {
    console.log('will render')
    return (
      // <Gallery containersSize={this.state.containersSize} allFonts={this.props.allFonts}/>
      <div>1</div>
    )
    // return (
    //   <div>
    //     {this.props.allFonts.map(font => <img src={require(`../../img/${font.image.fileName}.jpg`)} key={font.id}/>)}
    //   </div>
    // )
  }
}

export default ControllerGallery
