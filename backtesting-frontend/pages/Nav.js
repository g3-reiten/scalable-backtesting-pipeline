import { Navbar, Button, Link, Text } from "@nextui-org/react";
import { Layout } from "../components/navbar/Layout.js";
import { MelaLogo } from "../components/navbar/Logo.js";

export default function Nav() {
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
          <Navbar.Link href="#">BackTrader</Navbar.Link>
          <Navbar.Link isActive href="#">BackTest</Navbar.Link>
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
    </Layout>
  )
}