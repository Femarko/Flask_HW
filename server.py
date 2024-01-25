import flask
from flask import jsonify, request, Response
from flask.views import MethodView
from flask import Response

from models import Session, Adv

adv = flask.Flask('adv')


@adv.before_request
def before_request():
    session = Session()
    request.session = session


@adv.after_request
def after_request(response: Response):
    request.session.close()
    return response


class AdvView(MethodView):

    @property
    def session(self) -> Session:
        return request.session

    def get(self, adv_id: int):
        pass

    def post(self):
        adv_data = request.json
        new_adv = Adv(**adv_data)
        self.session.add(new_adv)
        self.session.commit()
        return jsonify({'id': new_adv.id})

    def patch(self, adv_id: int):
        pass

    def delete(self, adv_id: int):
        pass


adv_view = AdvView.as_view("adv_view")
adv.add_url_rule("/adv/<int:adv_id>", view_func=adv_view, methods=["GET", "PATCH", "DELETE"])
adv.add_url_rule("/adv", view_func=adv_view, methods=["POST"])

if __name__ == "__main__":
    adv.run(debug=True)
