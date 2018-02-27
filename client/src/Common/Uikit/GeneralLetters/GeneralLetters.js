import React from 'react'
import styled from 'styled-components'

const Container = styled.div`
  position: relative;
  width: 317px;
  text-align: center;
`
const LettersNum = styled.div`
  display:inline;
  font-family: 'Playfair Display', serif;
  font-style: italic;
  font-size: 118px;
  font-weight: 900;
  line-height: 1.27;
  opacity: 0.75;
  letter-spacing: normal;
  text-align: center;
  color: #ffa185;
`
const LettersLabel = styled.div`
  font-family: 'Anonymous Pro', monospace;
  font-size: 28px;
  font-weight: bold;
  letter-spacing: 30px;
  color: #000000;
  position: absolute;
  bottom: 20px;
`

const GeneralLetters = ({lettersNum, lettersLabel}) => (
  <Container>
    <LettersNum>{lettersNum}</LettersNum>
    <LettersLabel>{lettersLabel}</LettersLabel>
  </Container>
)

export default GeneralLetters