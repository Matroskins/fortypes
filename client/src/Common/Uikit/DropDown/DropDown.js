import React from 'react'
import styled from 'styled-components'
import Dropdown, {
  DropdownToggle,
  DropdownMenu,
  DropdownMenuWrapper,
  MenuItem,
  DropdownButton
} from '@trendmicro/react-dropdown'
import '@trendmicro/react-buttons/dist/react-buttons.css'
import '@trendmicro/react-dropdown/dist/react-dropdown.css'

const DropDownNew = ({})=>(
  <Dropdown
    onSelect={(eventKey) => {
      console.log(eventKey)
    }}
>
    <DropdownToggle
        btnStyle="flat"
    >
        Toggler
    </DropdownToggle>
    <DropdownMenu>
        <MenuItem header>Header</MenuItem>
        <MenuItem eventKey={1}>link</MenuItem>
        <MenuItem divider />
        <MenuItem header>Header</MenuItem>
        <MenuItem eventKey={2}>link</MenuItem>
        <MenuItem eventKey={3} disabled>disabled</MenuItem>
        <MenuItem
            eventKey={4}
            title="link with title"
        >
            link with title
        </MenuItem>
        <MenuItem
            eventKey={5}
            active
            onSelect={(eventKey) => {
                alert(`Alert from menu item.\neventKey: ${eventKey}`);
            }}
        >
            link that alerts
        </MenuItem>
    </DropdownMenu>
</Dropdown>
)

export default DropDownNew