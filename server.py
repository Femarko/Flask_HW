import flask
from flask import jsonify
from flask.views import MethodView


app = flask.Flask('adv')

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

app.add_url_rule('/adv/<int:adv_id>', view_func=adv_view, methods=['GET', 'PATCH', 'DELETE'])
app.add_url_rule('/adv/<int:adv_id>', view_func=adv_view, methods=['POST'])

if __name__ == '__main__':
    app.run(debug=True)
