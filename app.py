from flask import Flask, render_template, request
import pdfplumber


app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')
@app.route('/signup')   # ✅ THIS must exist
def signup():
    return render_template("signup.html")
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")
@app.route("/login")
def login():
    return render_template("login.html")
@app.route("/resume-builder")
def resume_builder():
    return render_template("resumebuilder.html")
@app.route("/ats")
def ats():
    return render_template("ats.html")
@app.route("/aicover")
def aicover():
    return render_template("aicover.html")
@app.route("/temp")
def temp():
    return render_template("temp.html")
@app.route("/pricing")
def pricing():
    return render_template("pricing.html")
@app.route("/blog")
def blog():
    return render_template("blog.html")
@app.route("/faq")
def faq():
    return render_template("faq.html")
@app.route("/support")
def support():
    return render_template("support.html")
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/analysis")
def analysis():
    return render_template("analysis.html")
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('resume')

    if not file or file.filename == '':
        return "No file uploaded"

    text = ""

    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""

    return render_template('result.html', extracted_text=text)



if __name__ == '__main__':
    app.run(debug=True)