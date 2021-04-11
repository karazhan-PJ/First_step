import axios from 'axios';

function App() {
  const url = "http://127.0.0.1:5000/youtube/channelList";
  axios.get(url)
    .then(function(response) {
        console.log("성공");
    })
    .catch(function(error) {
        console.log("실패");
    })
  
  return (
    <div className="App">
      Hello World
    </div>
  );
}

export default App;
