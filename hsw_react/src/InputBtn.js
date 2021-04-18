import React, { useState, useEffect, Component } from "react";
import Button from 'react-bootstrap/Button';

const UserInput = () => {
  const [name, setName] = useState(0);

  const change = (e) => {
    setName = e.targer.value;
  }
  const appChange = () => {
    alert();
  }

    return (
        <>
        <Button variant="primary" onClick={appChange}>전송1</Button>{' '}
        <input type="text" onChange={change} />
        </>
    )                
}

export default UserInput;
