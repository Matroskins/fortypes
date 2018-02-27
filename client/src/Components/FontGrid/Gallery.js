import React,  { Component } from 'react'
import Isotope from 'isotope-layout';
import { Container } from 'rebass'
import './index.css'


const randomArray = Array(35).fill(3)

export class Grid extends Component {
  isotope = null;

  componentDidMount = () => {
    const grid = this.Grid;

    if (!this.isotope) {
      this.isotope = new Isotope(grid, {
        layoutMode: 'masonry',
        percentPosition: true,
        itemSelector: '.item',
        masonry: {
          columnWidth: '.grid-sizer'
        }
      });
      this.isotope.layout()
    }
    else{
      this.isotope.layout()
    }
  }
  render () {
    return (
      <div className="grid" ref={(c) => { this.Grid = c; }}>
        <div className="grid-sizer" />

        {randomArray.map((item, ind) => (
          <div
          className={'item'}
          style={{
            height: ind % 5 === 0 ? 50 : ind % 3 === 0 ? 200 : ind % 2 === 0 ? 150 : 100,
            width: ind % 5 === 0 ? 50 : ind % 3 === 0 ? 200 : ind % 2 === 0 ? 150 : 100,
            backgroundColor: 'black',
            margin: '5px'
          }} 
          key={`item_${ind}`}
        />
        ))}
      </div>
    );
  }
}


export default Grid
