"""
CWE-79: Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')
This file demonstrates a basic XSS vulnerability where user input is rendered without sanitization.
"""

from flask import Flask, request

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    # Vulnerable: User input is directly inserted into HTML without sanitization
    username = request.args.get('name', 'Guest')

    # CWE-79: This allows XSS attacks through the 'name' parameter
    # Example malicious input: <script>alert('XSS')</script>
    html_response = f"""
    <html>
        <head><title>Welcome</title></head>
        <body>
            <h1>Welcome, {username}!</h1>
            <p>Thanks for visiting our site.</p>
        </body>
    </html>
    """

    return html_response

@app.route('/search')
def search():
    # Another XSS vulnerability with search query
    query = request.args.get('q', '')

    # CWE-79: Unsanitized search query reflected in response
    return f"<h2>Search results for: {query}</h2><p>No results found.</p>"

if __name__ == '__main__':
    app.run(debug=True)

