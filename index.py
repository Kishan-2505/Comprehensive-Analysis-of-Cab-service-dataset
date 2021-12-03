from flask import Flask, request, jsonify, render_template

app = Flask(__name__, static_url_path='/static')


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('/index.html')
if __name__ == '__main__':
    print('App is running')
    app.run()