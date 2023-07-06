from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, world!'

@app.route('/health')
def health_check():
    return 'OK'

@app.route('/ready')
def ready_check():
    return 'OK'

@app.route('/metrics')
def metrics():
    # Возвращаем метрики в формате Prometheus
    # Например, можно вернуть фиктивные метрики:
    data = {
        'metric1': 10,
        'metric2': 20
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
