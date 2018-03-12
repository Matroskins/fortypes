import React, { Component } from 'react'
import { Flex } from 'rebass'
import styled from 'styled-components'
import { compose, withState, withHandlers } from 'recompose'
import ImgTest from './ImgTest'

const Container = styled.div`
  height: ${props => props.height};
  width: ${props => props.width};
`
class ContainerImg extends Component {

  render() {
    const {font, sizeArray} = this.props
    const {width, height} = sizeArray.find(size=> size.id === font.id)
    const containerWidth = width - width*0.5
    const containerHeight = height - height*0.5
    // const imgSize = {}
    // const img=document.createElement("img");
    // img.setAttribute("src",require(`../../img/${font.image.fileName}.jpg`))
    // .onload(()=>{
    //   imgSize.height=this.height + this.height*0.2
    //   imgSize.width = this.width + this.width*0.2
    // });
    // const containerWidth = img.width + img.width*0.2
    // const containerHeight = img.height + img.height*0.3
    // console.log(img.height)
    return (
      <Container width={`${containerWidth}px`} height={`${containerHeight}px`} >
        <img style={{width: width/4, height:height/4}}  src={require(`../../img/${font.image.fileName}.jpg`)} />
      </Container>
    )
  }
}

export default ContainerImg
