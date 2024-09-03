from flask import jsonify, Response

from app import adv


class HttpError(Exception):
    def __init__(self, status_code: int, description: str | list[str]):
        self.status_code = status_code
        self.description = description


@adv.errorhandler(HttpError)
def error_handler(error: HttpError) -> Response:
    response = jsonify({"error": error.description})
    response.status_code = error.status_code
    return response
