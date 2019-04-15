import React from "react";
import { graphql } from "react-apollo";
import gql from "graphql-tag";
import { Menu, MenuItem } from "@blueprintjs/core";

const query = gql`
  query sources {
    sources @rest(type: "Sources", path: "source") {
      id
      name
      environment
      encoding
    }
  }
`;

export const SourceList = ({ loading, error, sources, onSelectSource }) => {
  if (loading) {
    return <div>Loading...</div>;
  }
  if (error) {
    return <div>{error.message}</div>;
  }
  return (
    <Menu>
      {sources.map(source => (
        <MenuItem
          className="source-list-item"
          key={source.id}
          onClick={() => onSelectSource(source)}
          text={source.name}
        />
      ))}
    </Menu>
  );
};
export default graphql(query, {
  props: ({ data }) => {
    if (data.loading) {
      return {
        loading: data.loading
      };
    }
    if (data.error) {
      return {
        error: data.error
      };
    }
    return {
      sources: data.sources,
      loading: false
    };
  }
})(SourceList);
