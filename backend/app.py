from flask import Flask, render_template, jsonify

app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/videos')
def get_videos():
    videos = [
        {
            "title": "Big Buck Bunny",
            "thumb": "/static/BigBuckBunny.jpg",
            "source": "https://storage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4"
        },
        {
            "title": "Sintel",
            "thumb": "/static/Sintel.jpg",
            "source": "https://storage.googleapis.com/gtv-videos-bucket/sample/Sintel.mp4"
        },
        {
            "title": "Tears of Steel",
            "thumb": "/static/TearsOfSteel.jpg",
            "source": "https://storage.googleapis.com/gtv-videos-bucket/sample/TearsOfSteel.mp4"
        }
    ]
    return jsonify(videos)

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
