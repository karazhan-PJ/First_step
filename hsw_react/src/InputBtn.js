import React, { useState, useEffect, Component } from "react";
import Button from 'react-bootstrap/Button';

class UserInput extends Component {

  state = {
    id: '',
    password: ''
  }
  /* input value 변경 ==> onChange */
  appChange = (e) => {
    /*this.setState({
      id: e.target.value
    });*/
      
      alert('안녕');
  }

    render(){
        return (
            <>
            <Button variant="primary" onClick={this.appChange}>전송1</Button>{' '}
            <input type="text" />
            </>
            )
    }                 
}

export default UserInput;
