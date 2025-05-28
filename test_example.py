import flask
from flask import Flask
from flask import Response

import pytest

app = Flask("test")


@app.route("/hi")
async def hi():
    def gen():
        for i in range(100000):
            yield str(i)

    return Response(flask.stream_with_context(gen()))


def test_hi():
    with app.test_client() as client:
        response = client.get("/hi")

    assert response.status_code == 200
    response.data  # this should throw because flask aync is not handled correctly with stream_with_context
