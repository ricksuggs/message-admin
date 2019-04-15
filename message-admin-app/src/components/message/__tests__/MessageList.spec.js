import React from "react";
import { render, cleanup } from "react-testing-library";
import "jest-dom/extend-expect";
import {MessageList} from "../MessageList";
import { MockedProvider } from "react-apollo/test-utils";

const props = {
  loading: false,
  error: false,
  messages: [{
    id: 1,
    message: 'Message_1',
    status: 'Status_1',
    created_at: 'Timestamp_1',
    updated_at: 'Timestamp_2'
  }],
}

afterEach(cleanup);

test("renders without crashing", () => {
  const { getByText, container } = render(
    <MockedProvider>
      <MessageList {...props} />
    </MockedProvider>
  );

  const messageNode = getByText("Message_1");

  expect(messageNode).toBeInTheDocument();
});
