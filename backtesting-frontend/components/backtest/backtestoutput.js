import Head from 'next/head'
import { useRouter } from 'next/router'
import {useEffect, useState} from 'react';
function display(val) {
    return(
        <div className="card bg-light text-dark mt-2 px-2 py-2">{val}</div>
    );
}
export function BacktestOutput({data}) {
    function getData() {
        return (
            
            <div>{data.map(display)}</div>
        );
    }
    
        return (
        <div className="container">
            <Head>
                <title>Mela</title>
                <link rel="icon" href="/logo.jpg" />
                <link href="//netdna.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet" />
            </Head>
            {getData()}
        <div id = "c1">
           
        </div>
        </div>
    );
}
