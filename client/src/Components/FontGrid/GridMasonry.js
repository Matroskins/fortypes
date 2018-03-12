import React, { Component } from 'react'
import Isotope from 'isotope-layout'
import { Container } from 'rebass'
import imagesLoaded from 'imagesloaded'
import ContainerImg from './ContainerImg'
import './index.css'

export class GridMasonry extends Component {
  isotope = null

  componentDidMount = () => {
    console.log('component did mount')
      const grid = this.Grid
      if (!this.isotope) {
        this.isotope = new Isotope(grid, {
          layoutMode: 'masonry',
          percentPosition: true,
          itemSelector: '.item',
          masonry: {
            columnWidth: '.grid-sizer',
          },
        })
        imagesLoaded(grid, ()=>{ this.isotope.layout()})
      } else {
        imagesLoaded(grid, ()=>{ this.isotope.layout()})
      }
  }
  render() {
    const {  allFonts, sizeArray } = this.props
    return (
          <div
            className="grid"
            ref={c => {
              this.Grid = c
            }}
          >
            <div className="grid-sizer" />

            {allFonts.map((font, ind) => {
              return <ContainerImg font={font} sizeArray={sizeArray} key={font.id} />
            })}
          </div>

    )
  }
}

export default GridMasonry
