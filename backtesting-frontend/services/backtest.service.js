const axios = require('axios').default;
import Router, { withRouter } from 'next/router'

export const BacktestService = {
    getBacktestOutput
};

function getBacktestOutput(query_data) {
    //const router = useRouter();
    axios.get("http://127.0.0.1:5000/backtest",
    {
        params: {
            "name":query_data.name,
            "stratagy":query_data.stratagy,
            "cash":query_data.cash,
            "commision":query_data.commision
        }
    })
    .then(function (response) {
        Router.push({
            pathname:"/nav",
            query:{"data":response.data}
        },'/nav')
    })
    .catch(function (error) {
        console.log(error);
    })
    .finally(function () {
    
    });
}