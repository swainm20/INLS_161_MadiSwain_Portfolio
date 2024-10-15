from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template('index.html', datetime=current_time)

if __name__ == '__main__':
    app.run(debug=True)

