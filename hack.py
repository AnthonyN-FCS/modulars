# Import necessary libraries
import requests
from flask import Flask, render_template

app = Flask(__name)

@app.route('/')
def fetch_and_display():
    # Replace the URL with the website you want to fetch
    url = 'https://'
    
    # Fetch the HTML content
    response = requests.get(url)
    html_content = response.text
    
    # Render the HTML template and pass the fetched content to the client side
    return render_template('index.html', html_content=html_content)

if __name__ == '__main__':
    app.run(debug=True)
