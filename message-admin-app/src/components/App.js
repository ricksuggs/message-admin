import React, { useState } from "react";
import { ApolloClient } from "apollo-client";
import { InMemoryCache } from "apollo-cache-inmemory";
import { ApolloProvider } from "react-apollo";
import { RestLink } from "apollo-link-rest";
import "./App.css";
import { Row, Col, Grid } from "react-flexbox-grid";
import SourceList from "./source/SourceList";
import SourceDetail from "./source/SourceDetail";

const restLink = new RestLink({
  uri: "/"
});

const client = new ApolloClient({
  link: restLink,
  cache: new InMemoryCache()
});

const App = () => {
  const [selectedSource, onSelectSource] = useState(null);
  return (
    <Grid className="app" fluid>
      <Row className="app-header">
        <Col>
          <h1 className="bp3-heading">Message Admin</h1>
        </Col>
      </Row>
      <Row className="app-body">
        <Col className="app-sidenav" xs={12} sm={4} md={4} lg={4}>
          <SourceList onSelectSource={onSelectSource} />
        </Col>
        <Col className="app-content" xs={12} sm={8} md={8} lg={8}>
          {selectedSource && <SourceDetail source={selectedSource} />}
        </Col>
      </Row>
    </Grid>
  );
};

const ApolloApp = () => (
  <ApolloProvider client={client}>
    <App />
  </ApolloProvider>
);

export default ApolloApp;
