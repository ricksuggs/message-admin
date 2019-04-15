import React from "react";
import { render, cleanup } from "react-testing-library";
import "jest-dom/extend-expect";
import SourceDetail from "../SourceDetail";
import { MockedProvider } from "react-apollo/test-utils";

const props = {
  source: {
    id: 1,
    name: "Name_1",
    environment: "Env_1",
    encoding: "Encoding_1"
  }
};

afterEach(cleanup);

test("renders without crashing", () => {
  const { getByText, container } = render(
    <MockedProvider>
      <SourceDetail {...props} />
    </MockedProvider>
  );

  const nameInput = container.querySelector("input[value='Name_1']");

  expect(nameInput).toBeInTheDocument();
});
