from flask import Flask, url_for, render_template, request, redirect, flash
from process import Video


app = Flask(__name__)
app.secret_key = "zehahaha"


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        return redirect(url_for('process'))
    else:
        return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():

    ERROR = None

    try:
        global URL
        URL = str(request.form.get('user_url'))
        vid = Video(URL)

        TITLE = vid.title()
        THUMBNAIL = vid.thumbnail()
        SIZE = vid.size()

    except Exception as e:
        ERROR = e
        flash(e, "success")

    return render_template('process.html', title=TITLE, thumbnail=THUMBNAIL, size=SIZE, error=ERROR)


@app.route('/download', methods=['POST'])
def download():
    # flash("Video started downloading...", "info")

    ERROR = None
    MSG1 = None
    MSG2 = None

    try:
        down_vid = Video(URL)

        TITLE = down_vid.title()
        THUMBNAIL = down_vid.thumbnail()
        SIZE = down_vid.size()

        # download
        down_vid.download()
        # flash("Video downloaded successfully !", "success")

    except Exception as e:
        ERROR = e
        # flash(e, "success")

    return render_template('process.html', title=TITLE, thumbnail=THUMBNAIL, size=SIZE, error=ERROR, msg1=MSG1, msg2=MSG2)


if __name__ == '__main__':
    app.run(debug=True)
