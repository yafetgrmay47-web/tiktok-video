from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("experiment.html")

@app.route("/video", methods=["POST"])
def video():
    return render_template("experiment video.html")

if __name__ == "__main__":
    app.run(debug=True)
    