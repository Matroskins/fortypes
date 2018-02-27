import React, { Component } from 'react'
import { Box, Label, Flex } from 'rebass'
import styled from 'styled-components'
import Heart from 'svg/heart-black.svg'
import { compose, withState, withHandlers } from 'recompose'

const FontCardContainer = styled.div`
  width: ${({ isHover }) => (isHover ? 60 : 45)}px;
  height: ${({ isHover }) => (isHover ? 60 : 45)}px;
  background-color: ${({ bg }) => bg};
`

const FontCard = ({ font, isHover, toggleHover }) => (
  <Box onMouseEnter={toggleHover} onMouseLeave={toggleHover}>
    <FontCardContainer bg={font.image.color} isHover={isHover} />
    {isHover && (
      <Flex>
        <Box>{font.author_name}</Box>
        <Box>
          {font.popularity}
          <img src={Heart}/>
        </Box>
      </Flex>
    )}
  </Box>
)

const enhance = compose(
  withState('isHover', 'setHoverState', false),
  withHandlers({
    toggleHover: props => () => props.setHoverState(!props.isHover),
  })
)

export default enhance(FontCard)
