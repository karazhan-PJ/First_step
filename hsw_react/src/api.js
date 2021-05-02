import axios from 'axios';

export const getManageApplication = (query) => {

    function api(){
        return new Promise(function(resolve){
            // axios 
            const url = "http://127.0.0.1:5000/youtube/channelList";
            axios.get(url, {
                params: {
                    query: query
                }
            })
            .then(function(response) {
                console.log("성공");
                resolve(response.data.result);
            })
            .catch(function(error) {
                console.log("실패");
            })
        });
    }    

    async function apiTest(){
        var result = await api();
        return result;
    }

    return apiTest();
};