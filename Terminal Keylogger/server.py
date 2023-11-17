from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def handle_key_data():
    key = request.json.get('key')
    print(f"Received key: {key}")
    return 'Key received by the server'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
