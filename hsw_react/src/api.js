import axios from 'axios';

export const getManageApplication = (query) => {
    // axios 
    const url = "http://127.0.0.1:5000/youtube/channelList";
    axios.get(url, {
        params: {
            query: query
        }
    })
    .then(function(response) {
        console.log("성공");
    })
    .catch(function(error) {
        console.log("실패");
    })

   const result = '{"title":"'+ userId +'","thumbnail": "https://yt3.ggpht.com/ytc/AAUvwniqXEIYoNP_MJXZZblrAaQwddFaQlvFDn2XXS_p=s800-c-k-c0xffffffff-no-rj-mo"}';

  /*const result = {
    title: "Dummy Data",
    thumbnail: "https://yt3.ggpht.com/ytc/AAUvwniqXEIYoNP_MJXZZblrAaQwddFaQlvFDn2XXS_p=s800-c-k-c0xffffffff-no-rj-mo"
  };*/

  return JSON.parse(result);
};