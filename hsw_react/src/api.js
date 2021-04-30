import axios from 'axios';

export const getManageApplication = (query) => {

    function api(){
        return new Promise(function(resolve){

            let result;
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
                resolve(response.data);
            })
            .catch(function(error) {
                console.log("실패");
            })

            return result;
        });
    }    

    async function apiTest(){
        var result = await api();
        alert(result);
        return result;
    }

    return apiTest();
};