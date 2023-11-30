from flask import *
from flask_sitemapper import Sitemapper

sitemapper = Sitemapper()

app = Flask(__name__)
sitemapper.init_app(app)

@sitemapper.include(lastmod="09-08-2023")
@app.route('/')
def index():
    return render_template("index.html")

@sitemapper.include(lastmod="09-08-2023")
@app.route('/download')
def download():
    return render_template("downloads.html")

@sitemapper.include(lastmod="09-08-2023")
@app.route('/privacy')
def privacy():
    return render_template("privacy.html")

@sitemapper.include(lastmod="09-08-2023")
@app.route('/cookie')
def cookie():
    return render_template("cookie.html")

@app.route("/sitemap.xml")
def sitemap():
    return sitemapper.generate()


if __name__ == "__main__":
    app.run()

