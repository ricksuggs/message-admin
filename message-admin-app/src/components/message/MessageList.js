import React from "react";
import { graphql } from "react-apollo";
import gql from "graphql-tag";
import { Table, Column, Cell, TableLoadingOption } from "@blueprintjs/table";
import { HTMLTable } from "@blueprintjs/core";
import { Row, Col } from "react-flexbox-grid";

const Query = gql`
  query($sourceId: String!) {
    messages(sourceId: $sourceId)
      @rest(type: "Messages", path: "source/:sourceId/message") {
      id
      message
      status
      created_at
      updated_at
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
      <Row>
        <Col xs>
          <h4>Summary Statistics</h4>
          <HTMLTable condensed bordered>
            <thead>
              <tr>
                <td>Status</td>
                <td>Count</td>
              </tr>
            </thead>
            <tbody>
              {Object.keys(statusStats).map(key => {
                if (statusStats.hasOwnProperty(key)) {
                  return (
                    <tr key={key}>
                      <td>{key}</td>
                      <td>{statusStats[key]}</td>
                    </tr>
                  );
                } else {
                  return null;
                }
              })}
            </tbody>
          </HTMLTable>
        </Col>
      </Row>

      <h4>Messages</h4>
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
        <Column
          key="created_at"
          name="Created At"
          cellRenderer={getCellRenderer("created_at")}
        />
        <Column
          key="updated_at"
          name="Updated At"
          cellRenderer={getCellRenderer("updated_at")}
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
