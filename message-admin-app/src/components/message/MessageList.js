import React from "react";
import { graphql } from "react-apollo";
import gql from "graphql-tag";
import { Table, Column, Cell, TableLoadingOption } from "@blueprintjs/table";
import { HTMLTable } from "@blueprintjs/core";

const Query = gql`
  query($sourceId: String!) {
    messages(sourceId: $sourceId)
      @rest(type: "Messages", path: "source/:sourceId/message") {
      id
      message
      status
    }
  }
`;

const MessageList = ({ loading, error, messages }) => {
  const getCellRenderer = key => {
    if (messages) {
      return rowIndex => <Cell>{messages[rowIndex][key]}</Cell>;
    }
    return () => <Cell />;
  };

  const getLoadingOptions = loading => {
    if (loading) {
      return [
        TableLoadingOption.CELLS,
        TableLoadingOption.COLUMN_HEADERS,
        TableLoadingOption.ROW_HEADERS
      ];
    }
    return [];
  };

  if (error) {
    return <div>{error.message}</div>;
  }

  let statusStats = {};
  if (messages) {
    messages.forEach(message => {
      if (statusStats[message.status]) {
        statusStats[message.status] += 1;
      } else {
        statusStats[message.status] = 1;
      }
    });
  }

  return (
    <>
      {Object.keys(statusStats).map(key => {
        if (statusStats.hasOwnProperty(key)) {
          return (
            <div key={key}>
              {key}: {statusStats[key]}
            </div>
          );
        } else {
          return null;
        }
      })}
      <Table
        numRows={loading ? 10 : messages.length}
        loadingOptions={getLoadingOptions(loading)}
      >
        <Column
          key="message"
          name="Message"
          cellRenderer={getCellRenderer("message")}
        />
        <Column
          key="status"
          name="Status"
          cellRenderer={getCellRenderer("status")}
        />
      </Table>
    </>
  );
};
export default graphql(Query, {
  options: ({ sourceId }) => {
    return { variables: { sourceId } };
  },
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
      messages: data.messages,
      loading: false
    };
  }
})(MessageList);
