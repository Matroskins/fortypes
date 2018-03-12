import React, { Component } from 'react'
import Masonry from 'react-mason'
import ContainerImg from './ContainerImg'
 
const Gallery =({allFonts})=> (
      <Masonry>
        {
          allFonts.map(font => <ContainerImg font={font} key={`img_${font.id}`} />)
        }
      </Masonry>
    )
export default Gallery