from flask import Flask

app = Flask(__name__)

from project.views import bp as bp

app.register_blueprint(bp)
app.secret_key = "ABCD"
app.session_cookie_name = 'sessionData1'