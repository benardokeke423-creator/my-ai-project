from flask import Flask, render_template, send_file
import os

app = Flask(__name__, template_folder='../frontend/templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    video_path = '../videos/bunny.mp4'
    return send_file(video_path, mimetype='video/mp4', conditional=True)

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
