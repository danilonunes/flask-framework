from flask.views import MethodView

class Home(MethodView):
    def get(self):
        return "Teste ok"

home = Home.as_view('home')