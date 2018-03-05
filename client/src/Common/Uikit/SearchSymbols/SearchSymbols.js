import React from 'react'
import styled from 'styled-components'
import { compose, withState, withHandlers } from 'recompose'

const symbolsData = `
Received overcame oh sensible so at an. Formed do change merely to county it.
 Am separate contempt domestic to to oh. On relation my so addition branched. 
 Put hearing cottage she norland letters equally prepare too. 
 Replied exposed savings he no viewing as up. Soon body add 
 him hill. No father living really people estate if. 
 Mistake do produce beloved demesne if am pursuit. 
Sitting mistake towards his few country ask. 
You delighted two rapturous six depending 
objection happiness something the. Off nay 
impossible dispatched partiality 
unaffected. 
Norland adapted put ham cordial. 
Ladies talked may shy 
basket narrow see. Him she distrusts questions sportsmen. 
Tolerably pretended neglected on my earnestly by. Sex scale sir style truth ought. 
Prepared do an dissuade be so whatever steepest. 
Yet her beyond looked either day wished nay. By doubtful disposed do juvenile an.
 Now curiosity you explained immediate why behaviour. 
 An dispatched impossible of of melancholy favourable. 
 Our quiet not heart along scale sense timed. 
 Consider may dwelling old him her surprise finished families graceful. 
 Gave led past poor met fine was new.`
  .replace(/[^a-zA-Z]+/g, ' ')
  .split(' ')

function getLeftLetters(words, searchedSymbols) {
  //get letter from all the words that go before  searched symbols group
  function searchSymbolL(word, searchedSymbols) {
    const lettersInd = []
    let idx = word.indexOf(searchedSymbols)
    while (idx !== -1) {
      lettersInd.push(idx)
      idx = word.indexOf(searchedSymbols, idx + 1)
    }
    return lettersInd
      .filter(letterInd => letterInd !== 0)
      .map(letterInd => word[letterInd - 1])
      .reduce((concatArray, arrayEl) => [...concatArray, ...arrayEl], [])
  }

  return words
    .map(word => searchSymbolL(word, searchedSymbols))
    .reduce((concatArray, arrayEl) => [...concatArray, ...arrayEl], [])
    .map(symbol => symbol.toUpperCase())
}
function getRightLetters(words, searchedSymbols) {
  //get letter from all the words that go after  searched symbols group
  function searchSymbolR(word, searchedSymbols) {
    const lettersInd = []
    let idx = word.indexOf(searchedSymbols)
    while (idx !== -1) {
      lettersInd.push(idx)
      idx = word.indexOf(searchedSymbols, idx + 1)
    }
    return lettersInd
      .filter(letterInd => !(letterInd + searchedSymbols.length + 1 > word.length))
      .map(letterInd => word[letterInd + 1])
      .reduce((concatArray, arrayEl) => [...concatArray, ...arrayEl], [])
  }

  return words
    .map(word => searchSymbolR(word, searchedSymbols))
    .reduce((concatArray, arrayEl) => [...concatArray, ...arrayEl], [])
    .map(symbol => symbol.toUpperCase())
}
const SearchSymbols = ({ searchedSymbols }) => {
  const wordsIncludes = symbolsData.filter(word => word.includes(searchedSymbols))
  const symbolsNumber = wordsIncludes.length
  const uniqueLeftSymbols = [...new Set(getLeftLetters(wordsIncludes, searchedSymbols))].sort().join(' ')
  const uniqueRightSymbols = [...new Set(getRightLetters(wordsIncludes, searchedSymbols))].sort().join(' ')
  return (
    <div>
      <div>{`Current symbols ${searchedSymbols}`}</div>
      <div>{`Symbols number ${symbolsNumber}`}</div>
      <div>{`unique left symbols ${uniqueLeftSymbols}`}</div>
      <div>{`unique right symbols ${uniqueRightSymbols}`}</div>
    </div>
  )
}

const enhance = compose(
  withState('searchedSymbols', 'setSearchedSymbols', 'o'),
  withHandlers({
    changeItemId: props => (event, index, value) => {
      props.setItemId(value)
    },
  })
)

export default enhance(SearchSymbols)
