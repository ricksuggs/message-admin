import React from "react";
import { render, fireEvent, cleanup } from "react-testing-library";
import "jest-dom/extend-expect";
import { App } from "../App";
import { MockedProvider } from 'react-apollo/test-utils';

const mocks = [
  {
    request: {
      query: null,
      variables: {},
    },
    result: {
      data: {},
    },
  },
];

afterEach(cleanup);

test("renders without crashing", () => {
  const { getByText } = render(<MockedProvider><App /></MockedProvider>);

  const titleNode = getByText("Message Admin");

  expect(titleNode).toBeInTheDocument();
});
