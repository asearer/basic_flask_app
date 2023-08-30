from flask import Flask, render_template

# Create a Flask app instance
app = Flask(__name__)

# Configuration (can also be placed in a separate config.py file)
app.config['SECRET_KEY'] = 'your_secret_key_here'

# Define a route and a view function
@app.route('/')
def index():
    return render_template('index.html')

# Run the app if this file is the entry point
if __name__ == '__main__':
    app.run(debug=True)
