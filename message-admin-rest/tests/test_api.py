from flask import url_for, json
from api import run
from api.models import Source, Message
from datetime import timezone


def test_post_source(when, client):
    res = client.post(
        url_for("post_source", _method="POST"),
        json={"name": "test_1", "environment": "env_1", "encoding": "encoding_1"},
    )
    assert res.status == "200 OK"
    assert res.json["name"] == "test_1"
    assert "id" in res.json and res.json["id"]
    assert "created_at" in res.json and res.json["created_at"]
    assert "updated_at" in res.json


def test_put_source(when, client):

    source = Source(name="test_2", environment="env_2", encoding="encoding_2")

    run.db.session.add(source)
    run.db.session.commit()

    assert source.id

    res = client.put(
        url_for("put_source", id=source.id, _method="PUT"),
        json={"name": "test_2_updated"},
    )
    assert res.status == "200 OK"
    assert res.json["name"] == "test_2_updated"
    assert "id" in res.json and res.json["id"]
    assert (
        "created_at" in res.json
        and res.json["created_at"]
        == source.created_at.replace(tzinfo=timezone.utc).isoformat()
    )
    assert "updated_at" in res.json and res.json["updated_at"]


def test_delete_source(when, client):

    source = Source(name="test_3", environment="env_3", encoding="encoding_3")

    run.db.session.add(source)
    run.db.session.commit()

    assert source.id

    res = client.delete(url_for("delete_source", id=source.id, _method="DELETE"))
    assert res.status == "204 NO CONTENT"

    source = run.db.session.query(Source).filter(Source.id == source.id).first()
    assert source
    assert source.deleted_at


def test_post_source(when, client):

    source = Source(name="test_4", environment="env_4", encoding="encoding_4")

    run.db.session.add(source)
    run.db.session.commit()

    assert source.id

    res = client.post(
        url_for("post_message", _method="POST"),
        json={"source_id": source.id, "message": "message_1", "status": "status_1"},
    )
    assert res.status == "200 OK"
    assert res.json["message"] == "message_1"
    assert "id" in res.json and res.json["id"]
    assert "created_at" in res.json and res.json["created_at"]
    assert "updated_at" in res.json


def test_put_message(when, client):

    source = Source(name="test_5", environment="env_5", encoding="encoding_5")
    run.db.session.add(source)
    run.db.session.commit()
    assert source.id
    source_id = source.id

    message = Message(source_id=source_id, message="message_5", status="status_5")
    run.db.session.add(message)
    run.db.session.commit()
    assert message.id
    message_id = message.id

    res = client.put(
        url_for("put_message", id=message_id, _method="PUT"),
        json={"message": "message_5_updated"},
    )
    assert res.status == "200 OK"
    assert res.json["message"] == "message_5_updated"
    assert "id" in res.json and res.json["id"]
    assert (
        "created_at" in res.json
        and res.json["created_at"]
        == message.created_at.replace(tzinfo=timezone.utc).isoformat()
    )
    assert "updated_at" in res.json and res.json["updated_at"]


def test_delete_message(when, client):

    source = Source(name="test_5", environment="env_5", encoding="encoding_5")
    run.db.session.add(source)
    run.db.session.commit()
    assert source.id
    source_id = source.id

    message = Message(source_id=source_id, message="message_5", status="status_5")
    run.db.session.add(message)
    run.db.session.commit()
    assert message.id
    message_id = message.id

    res = client.delete(url_for("delete_message", id=message.id, _method="DELETE"))
    assert res.status == "204 NO CONTENT"

    message_deleted = (
        run.db.session.query(Message).filter(Message.id == message_id).first()
    )
    assert message_deleted
    assert message_deleted.deleted_at
