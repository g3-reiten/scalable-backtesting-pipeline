import { Text, Spacer } from "@nextui-org/react"
import { Box } from "./Box.js"
import { Backtest } from "../backtest.js";

export const Content = () => (
  <Box css={{px: "$12", mt: "$8", "@xsMax": {px: "$10"}}}>
    <Backtest />
  </Box>
);