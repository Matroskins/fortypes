import React, { Component } from 'react'
import { Container, Flex, Box, Button, Image } from 'rebass'
import { allFonts } from 'constants/index'
import FontCard from './FontGrid/FontCard'
import  Gallery  from './FontGrid/Gallery'

class MainPage extends Component {
  render() {
    console.log(allFonts)
    return (
      <Box bg="bG1" width={1} style={{minHeight: '100%'}} px={0} mx={0} maxWidth={2000}>
        <header>
          <Flex>
            <Box />
            <Box />
            <Box />
          </Flex>
        </header>
        <Container>
          {/* алфавит, вывводятся только те буквы, на которых есть картинк
                     Необходимо задать буквы в initial state(?) */}
        </Container>
        <Container>{/* сколько картинок найдено */}</Container>
        <Container>{/* поиск по тэгам */}</Container>
        <div>
          <Gallery>{allFonts.map(font => <FontCard font={font} key={font.id} />)}</Gallery>
        </div>
        <Flex>
          <Box>
            <Button children="Show more" />
          </Box>
        </Flex>
        <Container>
          <Flex>
            <Box>Share with your friends</Box>
            <Box>
              <Flex>
                <Box />
                <Box />
                <Box />
              </Flex>
            </Box>
          </Flex>
        </Container>
      </Box>
    )
  }
}

export default MainPage
