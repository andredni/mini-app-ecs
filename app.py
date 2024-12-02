from flask import Flask, Response
from prometheus_client import Counter, generate_latest, CollectorRegistry, Gauge

app = Flask(__name__)

# Prometheus Metriken
registry = CollectorRegistry()

request_counter = Counter(
    "http_requests_total",
    "Total number of HTTP requests",
    ["method", "endpoint"],
    registry=registry,
)

custom_metric = Gauge(
    "custom_metric_example",
    "An example of a custom gauge metric",
    ["label"],
    registry=registry,
)

@app.route("/")
def home():
    request_counter.labels(method="GET", endpoint="/").inc()
    custom_metric.labels(label="example").set(42)
    return "Hello, Prometheus!"

@app.route("/metrics")
def metrics():
    return Response(generate_latest(registry), mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

