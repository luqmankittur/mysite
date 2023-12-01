from flask import *
import os

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

@app.route('/sitemap.xml')
def sitemap():
    filename = 'sitemap.xml'
    directory = os.path.join(app.root_path, 'static')  # Assuming 'static' is your static folder on PythonAnywhere

    response = make_response(send_from_directory(directory, filename))
    
    response.headers["Content-Type"] = "application/xml"
    response.headers["Content-Disposition"] = f"attachment; filename={filename}"

    return response

if __name__ == "__main__":
    app.run()

