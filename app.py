from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return 'This is the GREATEST home page anyone has ever created'

@app.route('/about')
def about():
    return 'This is the most amazing about page EVER!!!'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
