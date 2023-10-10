from flask import Flask, request, jsonify
from prometheus_client import CollectorRegistry, Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# Create a counter metric to count requests
request_counter = Counter('app_requests_total', 'Total number of requests')

@app.route('/record', methods=['GET'])
def record_metric():
    request_counter.inc()
    return "Metric recorded: Request count incremented"

@app.route('/metrics', methods=['GET'])
def metrics():
    registry = CollectorRegistry()
    registry.register(request_counter)
    return generate_latest(registry), 200, {'Content-Type': CONTENT_TYPE_LATEST}

@app.route('/', methods=['GET'])
def hompage():
    return "Welcome to Custom Metrics Application"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
