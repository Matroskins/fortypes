import React, { Component } from 'react'
import { Flex } from 'rebass'
import styled from 'styled-components'
import Img from 'react-image'
import { compose, withState, withHandlers } from 'recompose'


const Container = styled.div`
  height: ${props => props.height};
  width: ${props => props.width};
`
const Image = ({source})=> { 
  const relativeWay = `../../img/${source}.jpg`
  return <img src={relativeWay} /> 
}

class ContainerImg extends Component {

  render() {
    const {font} = this.props
    // const containerWidth = width + width*0.2
    // const containerHeight = height + height*0.3

    const img=document.createElement("img");
    img.setAttribute("src",require(`../../img/${font.image.fileName}.jpg`))
    // .onload(()=>{
    //   imgSize.height=this.height + this.height*0.2
    //   imgSize.width = this.width + this.width*0.2
    // });  width={`${containerWidth}px`} height={`${containerHeight}px`}
    const containerWidth = img.width + img.width*0.2
    const containerHeight = img.height + img.height*0.3
    console.log(img.height)
    return (
      <Container >
        <Img  src={require(`../../img/${font.image.fileName}.jpg`)} />
        {/* <Image sorce = {font.image.fileName} /> */}
      </Container>
    )
  }
}

export default ContainerImg
