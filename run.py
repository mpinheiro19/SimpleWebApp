from flask import Flask, render_template
from app.controller_instrutor import instructor_bp

app = Flask(__name__)

app.register_blueprint(instructor_bp)

@app.route("/")
def home():
    return render_template("index.html", title="Home")


if __name__=="__main__":
    app.run(debug=True)