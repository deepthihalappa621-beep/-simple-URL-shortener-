from flask import Flask, request, redirect

app = Flask(__name__)

# Store URLs in memory
url_database = {}

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>URL Shortener</title>
    </head>
    <body style="font-family:Arial;text-align:center;margin-top:100px;">
        <h1>Simple URL Shortener</h1>

        <form action="/shorten" method="post">
            <input type="url" name="long_url"
                   placeholder="Enter Long URL"
                   required
                   style="width:400px;padding:10px;">
            <br><br>

            <button type="submit"
                    style="padding:10px 20px;">
                Shorten URL
            </button>
        </form>
    </body>
    </html>
    """

@app.route("/shorten", methods=["POST"])
def shorten():
    long_url = request.form["long_url"]

    code = str(len(url_database) + 1)

    url_database[code] = long_url

    return f"""
    <h2>Short URL Created</h2>

    <p>
    <a href="/{code}">
    http://127.0.0.1:5000/{code}
    </a>
    </p>

    <a href="/">Create Another</a>
    """

@app.route("/<code>")
def redirect_url(code):
    if code in url_database:
        return redirect(url_database[code])

    return "<h2>URL Not Found</h2>"

if __name__ == "__main__":
    app.run(debug=True)