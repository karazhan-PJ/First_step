import React from 'react';
import axios from 'axios';

function App() {
  return (
    <div className="App">
      Hello World!
    </div>
  );
}

function Axios_test() {
  axios({
    url: 'http://test/api/cafe/list/today',
    method: 'get',
    data: {
      foo: 'diary'
    }
  });
}

export default App;
