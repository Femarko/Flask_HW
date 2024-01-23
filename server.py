import flask
from flask import jsonify
from flask.views import MethodView


adv = flask.Flask('adv')

class AdvView(MethodView):

    def get(self, adv_id: int):
        pass

    def post(self, adv_id: int):
        pass

    def patch(self, adv_id: int):
        pass

    def delete(self, adv_id: int):
        pass

adv_view = AdvView.as_view('adv_view')

adv.add_url_rule('/adv/<int:adv_id>', view_func=adv_view, methods=['GET', 'PATCH', 'DELETE'])
adv.add_url_rule('/adv/<int:adv_id>', view_func=adv_view, methods=['POST'])

if __name__ == '__main__':
    adv.run(debug=True)
