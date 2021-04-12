//import axios from 'axios';
//import 'bootstrap/dist/css/bootstrap.min.css';
//import Table from 'react-bootstrap/Table'
import ManageTable from './ManageTable'

function App() {
  /*const url = "http://127.0.0.1:5000/youtube/channelList";
  axios.get(url)
    .then(function(response) {
        console.log("성공");
    })
    .catch(function(error) {
        console.log("실패");
    })*/
  // const result = '{"video_id": "None", "channel_title": "농구채널 침착맨", "channel_id": "UChSS5LWz8ej-aLlp_63Fw_g", "video_publish_date": 1402755404.0, "video_title": "농구채널 침착맨", "video_description": "남는건 영상뿐.", "video_category": "None", "video_thumbnail": "https://yt3.ggpht.com/ytc/AAUvwngjnAJVJ9NexF8yfgvLRsy2GuhPLqj-jWnutHenFA=s800-c-k-c0xffffffff-no-rj-mo"}'
  // const jsonList = JSON.parse(result);
  // alert(jsonList);
  
  return (
    <ManageTable/>
  );
}

export default App;
