import { Text, Spacer } from "@nextui-org/react";
import { Box } from "./Box.js";
import { Backtest } from "../backtest.js";
import { Backtrade } from "../backtrader.js";
import { useRouter } from 'next/router';
import {useEffect, useState} from 'react';
import {BacktestOutput} from '../backtest/backtestoutput';
function page() {
  const router = useRouter();
  if (router.query.page) {
    let val = router.query.page;
    if (val == "1") {
      return (
        <Backtest />
      );
    } else if (val == "2"){
      return (
        <Backtrade />
      );
    }
  } else if(router.query.data){
    let data = router.query.data;
    return (
      <BacktestOutput data={data}/>
    );
  }
  
  
}
export const Content = () => (
  <Box css={{px: "$12", mt: "$8", "@xsMax": {px: "$10"}}}>
    {page()}
  </Box>
);