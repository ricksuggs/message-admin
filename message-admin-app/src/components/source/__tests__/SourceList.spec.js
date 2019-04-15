import React from "react";
import { render, fireEvent, cleanup } from "react-testing-library";
import "jest-dom/extend-expect";
import { SourceList } from "../SourceList";
import { stub } from 'sinon';

const props = {
  loading: false,
  error: false,
  onSelectSource: stub(),
  sources: [{
    id: 1,
    name: 'Name_1',
    environment: 'Env_1',
    encoding: 'Encoding_1'
  }],
}

afterEach(cleanup);

test("renders without crashing", () => {
  const { getByText } = render(<SourceList {...props} />);

  const sourceNode = getByText("Name_1");

  expect(sourceNode).toBeInTheDocument();
});

test("responds to click events", () => {
  const { getByText } = render(<SourceList {...props} />);

  const sourceNode = getByText("Name_1");

  fireEvent.click(sourceNode);
  expect(props.onSelectSource.calledOnceWith(props.sources));

});
