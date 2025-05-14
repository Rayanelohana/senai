from flask import Flask, render_template, request
import os
#define a pasta onde estão os arquivos HTML , nesse caso, a raiz do projeto
template_dir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__, template_folder=template_dir)
#direcionamento para pg index.html
@app.route("/")
def home ():
    return render_template("index.html")

    if __name__== "__main__":
        app.run(host= "0.0.0.0", port=3000)
