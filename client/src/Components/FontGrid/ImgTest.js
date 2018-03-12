import React,  { Component } from 'react'

export class ImgTest extends Component {
  
  componentDidMount = () => {
    this.props.setSize(this.container)
  }
  render () {
    console.log(`${this.props.fileUrl}`)
    return (
          <img ref={(container) => { this.container = container; }} src={require(`../../img/${this.props.fileUrl}.jpg`)}/>
    );
  }
}


export default ImgTest
