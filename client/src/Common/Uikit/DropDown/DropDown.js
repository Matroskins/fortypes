import React from 'react'
import styled from 'styled-components'
import { compose, withState, withHandlers } from 'recompose'
import SelectField from 'material-ui/SelectField'
import MenuItem from 'material-ui/MenuItem'

const SelectFieldNew = styled(SelectField)`
  & {
    &:nth-child(2) {
      & > div {
        & > div {
          display: inline-block !important;
          width: auto !important;
          &:hover {
            div {
                color: #fb6a3f !important;
                fill: #fb6a3f !important;
            }
          }
        }
      }
    }
  }
`
// undefined--undefined-294
const DropDownNew = ({ itemId, changeItemId }) => (
  <SelectFieldNew
    value={itemId}
    underlineStyle={{ display: 'none' }}
    iconStyle={{
      display: 'inline',
      padding: 0,
      position: 'static',
      verticalAlign: 'bottom',
      width: 'auto',
      height: 'auto',
      fill: 'black',
    }}
    labelStyle={{
      display: 'inline',
      padding: 0,
      top: 0,
      position: 'static',
      verticalAlign: 'bottom',
      width: 'auto',
      height: 'auto',
      lineHeight: 'auto',
    }}
    selectedMenuItemStyle={{color:'#fb6a3f'}}
    onChange={changeItemId}
  >
    <MenuItem value={1} primaryText="Never" />
    <MenuItem value={2} primaryText="Every Night" />
    <MenuItem value={3} primaryText="Weeknights" />
    <MenuItem value={4} primaryText="Weekends" />
    <MenuItem value={5} primaryText="Weekly" />
  </SelectFieldNew>
)

const enhance = compose(
  withState('itemId', 'setItemId', 1),
  withHandlers({
    changeItemId: props => (event, index, value) => {
      props.setItemId(value)
    }
  })
)

export default enhance(DropDownNew)
