import React,  { Component } from 'react'
import styled from 'styled-components'

const InvisibleContainer = styled.div`
  display:none;
`
class PerformSize extends Component {
  
  componentDidMount = () => {
    console.log('perform did mount')
    console.log(this.container)
    this.props.setSizeArray(this.props.font.id, this.container)
  }
  render () {
    console.log('in font')
    console.log(this.props.font)
    return (
      <InvisibleContainer>
        <img ref={(container) => { this.container = container; }} src={require(`../../img/${this.props.font.image.fileName}.jpg`)}/>
      </InvisibleContainer>
    );
  }
}


export default PerformSize
