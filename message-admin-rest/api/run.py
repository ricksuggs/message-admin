from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from pathlib import Path
from api.models import Source, Message
from flask_marshmallow import Marshmallow
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:////{Path.cwd()}/db.sqlite"
# app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy(app)
ma = Marshmallow(app)


class SourceSchema(ma.ModelSchema):
    class Meta:
        model = Source


class MessageSchema(ma.ModelSchema):
    class Meta:
        model = Message


source_schema = SourceSchema()
sources_schema = SourceSchema(many=True)
message_schema = MessageSchema()
messages_schema = MessageSchema(many=True)


@app.route("/source", methods=["GET"])
def get_sources():
    sources = db.session.query(Source).all()
    return sources_schema.jsonify(sources)


@app.route("/source/<string:id>", methods=["GET"])
def get_source(id):
    source = db.session.query(Source).filter(Source.id == id).first()
    if not source:
        return ("", 404)
    return source_schema.jsonify(source)


@app.route("/source/<string:source_id>/message", methods=["GET"])
def get_source_messages(source_id):
    messages = db.session.query(Message).filter(Message.source_id == source_id).all()
    return messages_schema.jsonify(messages)


@app.route("/source", methods=["POST"])
def post_source():
    source_json = request.get_json()
    source = Source(
        name=source_json.get("name"),
        environment=source_json.get("environment"),
        encoding=source_json.get("encoding"),
    )
    db.session.add(source)
    db.session.commit()
    return source_schema.jsonify(source)


@app.route("/source/<string:id>", methods=["PUT"])
def put_source(id):
    source_json = request.get_json()
    source = db.session.query(Source).filter(Source.id == id).first()
    if not source:
        return ("", 404)

    source.name = source_json.get("name")
    source.environment = source_json.get("environment")
    source.encoding = source_json.get("encoding")

    db.session.add(source)
    db.session.commit()

    return source_schema.jsonify(source)


@app.route("/source/<string:id>", methods=["DELETE"])
def delete_source(id):
    source = db.session.query(Source).filter(Source.id == id).first()
    if not source:
        return ("", 404)

    source.deleted_at = datetime.utcnow()
    db.session.add(source)
    db.session.commit()

    return ("", 204)


@app.route("/message", methods=["GET"])
def get_messages():
    messages = db.session.query(Message).all()
    return messages_schema.jsonify(messages)


@app.route("/message/<string:id>", methods=["GET"])
def get_message(id):
    message = db.session.query(Source).filter(Message.id == id).first()
    return message_schema.jsonify(message)


@app.route("/message", methods=["POST"])
def post_message():
    message_json = request.get_json()
    message = Message(
        source_id=message_json.get("source_id"),
        message=message_json.get("message"),
        status=message_json.get("status"),
    )
    db.session.add(message)
    db.session.commit()
    return message_schema.jsonify(message)


@app.route("/message/<string:id>", methods=["PUT"])
def put_message(id):
    message_json = request.get_json()
    message = db.session.query(Message).filter(Message.id == id).first()
    if not message:
        return ("", 404)

    message.source_id = message_json.get("source_id")
    message.message = message_json.get("message")
    message.status = message_json.get("status")

    db.session.add(message)
    db.session.commit()

    return message_schema.jsonify(message)


@app.route("/message/<string:id>", methods=["DELETE"])
def delete_message(id):
    message = db.session.query(Message).filter(Message.id == id).first()
    if not message:
        return ("", 404)

    message.deleted_at = datetime.utcnow()
    db.session.add(message)
    db.session.commit()

    return ("", 204)


if __name__ == "__main__":
    app.run()
