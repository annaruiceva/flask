from flask import Flask, render_template

app = Flask(__name__,
            template_folder='templates',
            static_folder='static',
            )

@app.route('/')
def main():
    return render_template("index.html", text="что-то на русском")


if __name__ == '__main__':
    app.run(port="8000")
