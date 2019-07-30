"""
Functional tests for The Void
"""

import pytest

import the_void


@pytest.fixture
def client():
    """
    Fixture that creates a new Flask testing client
    """
    the_void.app.config["TESTING"] = True
    client = the_void.app.test_client()
    return client


def test_home_works(client):
    r = client.get("/")
    assert r.status_code == 200

    r = client.get("/", headers={"Dummy": "Hey"})
    assert r.status_code == 200

    r = client.post("/")
    assert r.status_code == 200

    r = client.post("/", headers={"Dummy": "Hey"})
    assert r.status_code == 200

    r = client.post("/", json={"body": "electric"})
    assert r.status_code == 200


def test_path_works(client):
    r = client.get("/one")
    assert r.status_code == 200

    r = client.get("/one/of-these")
    assert r.status_code == 200

    r = client.get("/one/of-these/things")
    assert r.status_code == 200

    r = client.get("/one/of-these/things/is-not")
    assert r.status_code == 200

    r = client.get("/one/of-these/things/is-not/likeTheOthers")
    assert r.status_code == 200

    r = client.get("/one/of-these/things/does-not")
    assert r.status_code == 200

    r = client.get("/one/of-these/things/does-not/Belong")
    assert r.status_code == 200
