from flask import jsonify
from app import create_app

app = create_app()

@app.route('/')
def index():
    return jsonify({'message': 'Welcome to the Job Posting API'})

if __name__ == '__main__':
    app.run(debug=True)
