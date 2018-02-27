import React, { Component } from 'react'
import {Flex} from 'rebass'
import FontCard from './FontCard'

const FontGrid = ({allFonts}) => (<Flex>{allFonts.map(font => <FontCard font={font} />)}</Flex>)

export default FontGrid