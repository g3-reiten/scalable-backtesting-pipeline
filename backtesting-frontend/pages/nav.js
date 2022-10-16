import { Navbar, Button, Link, Text } from "@nextui-org/react";
import { Layout } from "../components/navbar/Layout.js";
import { MelaLogo } from "../components/navbar/Logo.js";
import { useRouter } from "next/router";

export default function Nav() {
  const router = useRouter();
  return (
    <Layout>
      <Navbar isCompact isBordered variant="sticky">
        <Navbar.Brand>
          <MelaLogo />
          <Text b color="inherit" hideIn="xs">
            MELA
          </Text>
        </Navbar.Brand>
        <Navbar.Content hideIn="xs" variant="underline">
          <Navbar.Link href="/nav?page=2">BackTrader</Navbar.Link>
          <Navbar.Link href="/nav?page=1">BackTest</Navbar.Link>
        </Navbar.Content>
        <Navbar.Content>
          <Navbar.Item>
            Name
          </Navbar.Item>
          <Navbar.Item>
            <Button auto flat as={Link} href="#">
              Logout
            </Button>
          </Navbar.Item>
        </Navbar.Content>
      </Navbar>
      <style jsx>{`
        .active {
          font-size:70px;
        }
    `}</style>
    </Layout>
    
  )
}