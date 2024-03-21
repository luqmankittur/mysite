from flask import Flask, render_template, send_from_directory, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/download')
def download():
    return render_template("downloads.html")

@app.route('/privacy')
def privacy():
    return render_template("privacy.html")

@app.route('/cookie')
def cookie():
    return render_template("cookie.html")

@app.route('/pookie')
def pookie():
    return render_template("pookie.html")


@app.route('/sitemap.xml')
def sitemap():
    filename = 'sitemap.xml'
    directory = '/home/luqmank/mysite/assets'

    response = make_response(send_from_directory(directory, filename))
    
    response.headers["Content-Type"] = "application/xml"
    response.headers["Content-Disposition"] = f"attachment; filename={filename}"

    return response

@app.route('/robots.txt')
def robots_txt():
    filename = 'robots.txt'
    directory = '/home/luqmank/mysite/assets'

    response = make_response(send_from_directory(directory, filename))
    
    response.headers["Content-Type"] = "text/plain"
    response.headers["Content-Disposition"] = f"attachment; filename={filename}"

    return response

if __name__ == "__main__":
    app.run()

