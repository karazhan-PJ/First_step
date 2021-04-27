import axios from 'axios';

export const getManageApplication = async (query) => {
    let result;

    function api(){
        return new Promise(function(){
            // axios 
            const url = "http://127.0.0.1:5000/youtube/channelList";
            axios.get(url, {
                params: {
                    query: query
                }
            })
            .then(function(response) {
                console.log("성공");
                console.log(JSON.stringify(response.data));

                result = response.data;
            })
            .catch(function(error) {
                console.log("실패");
            })
        });
    }
    
    await api();
    
    console.log('먼저 타는지');

    return result;
    /*
    if(!result){
        result = '{"title":"'+ query +'","thumbnail": "https://yt3.ggpht.com/ytc/AAUvwniqXEIYoNP_MJXZZblrAaQwddFaQlvFDn2XXS_p=s800-c-k-c0xffffffff-no-rj-mo"}';
        result = JSON.parse(result);
    }*/

  /*const result = {
    title: "Dummy Data",
    thumbnail: "https://yt3.ggpht.com/ytc/AAUvwniqXEIYoNP_MJXZZblrAaQwddFaQlvFDn2XXS_p=s800-c-k-c0xffffffff-no-rj-mo"
  };*/
};