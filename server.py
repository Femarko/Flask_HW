import flask
from flask import jsonify, request, Response
from flask.views import MethodView


adv = flask.Flask('adv')


class HttpError(Exception):
    def __init__(self, status_code: int, description: str):
        self.status_code = status_code
        self.description = description


class AdvView(MethodView):

    def get(self, adv_id: int):
        pass

    def post(self):
        pass

    def patch(self, adv_id: int):
        pass

    def delete(self, adv_id: int):
        pass


class AuthorView(MethodView):

    def get(self, adv_id: int):
        pass

    def post(self, adv_id: int):
        pass

    def patch(self, adv_id: int):
        pass

    def delete(self, adv_id: int):
        pass

adv_view = AdvView.as_view("adv_view")
adv.add_url_rule("/adv/<int:adv_id>", view_func=adv_view, methods=["GET", "PATCH", "DELETE"])
adv.add_url_rule("/adv", view_func=adv_view, methods=["POST"])

author_view = AuthorView("author_view")
adv.add_url_rule("author/<int:author_id>", view_func=author_view, methods=["GET", "PATCH", "DELETE"])
adv.add_url_rule("/author", view_func=author_view, methods=["POST"])


if __name__ == "__main__":
    adv.run(debug=True)
