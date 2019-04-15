import React from "react";
import { Row, Col } from "react-flexbox-grid";
import MessageList from "../message/MessageList";
import { FormGroup, InputGroup } from "@blueprintjs/core";
import "./SourceDetail.css";

const SourceDetail = ({ source }) => (
  <>
    <Row className="source-detail-props">
      <Col xs>
        <FormGroup
          label="Name"
          labelFor="name-input"
          labelInfo="(required)"
          disabled
        >
          <InputGroup
            type="text"
            id="name-input"
            placeholder="Name"
            defaultValue={source.name}
          />
        </FormGroup>
        <FormGroup
          label="Environment"
          labelFor="environment-input"
          labelInfo="(required)"
          disabled
        >
          <InputGroup
            type="text"
            id="environment-input"
            placeholder="Environment"
            defaultValue={source.environment}
          />
        </FormGroup>
        <FormGroup
          label="Encoding"
          labelFor="encoding-input"
          labelInfo="(required)"
          disabled
        >
          <InputGroup
            type="text"
            id="encoding-input"
            placeholder="Encoding"
            defaultValue={source.encoding}
          />
        </FormGroup>
      </Col>
    </Row>
    <Row>
      <Col className="source-detail-messages" xs>
        <h3>Messages</h3>
        <MessageList sourceId={source.id} />
      </Col>
    </Row>
  </>
);

export default SourceDetail;
