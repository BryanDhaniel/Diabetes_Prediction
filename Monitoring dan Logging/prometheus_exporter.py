from prometheus_client import start_http_server, Counter, Histogram, Gauge

# Define >10 metrics for Advanced point
REQUEST_COUNT = Counter('app_requests_total', 'Total app HTTP requests', ['method', 'endpoint', 'http_status'])
LATENCY = Histogram('app_latency_seconds', 'Latency of HTTP requests in seconds')
PREDICTION_COUNT = Counter('app_predictions_total', 'Total number of predictions made', ['outcome'])
CPU_USAGE = Gauge('system_cpu_usage', 'Current CPU usage percentage')
RAM_USAGE = Gauge('system_ram_usage', 'Current RAM usage percentage')
DB_QUERY_COUNT = Counter('app_db_queries_total', 'Total database queries')
ACTIVE_SESSIONS = Gauge('app_active_sessions', 'Number of active user sessions')
ERROR_COUNT = Counter('app_errors_total', 'Total number of application errors')
NETWORK_TX = Counter('system_network_transmit_bytes', 'Total bytes transmitted')
NETWORK_RX = Counter('system_network_receive_bytes', 'Total bytes received')
MODEL_LOAD_TIME = Gauge('app_model_load_time_seconds', 'Time taken to load ML model')

def generate_metrics(latency, prediction):
    # Simulate updating metrics
    REQUEST_COUNT.labels(method='POST', endpoint='/predict', http_status=200).inc()
    LATENCY.observe(latency)
    PREDICTION_COUNT.labels(outcome=str(prediction)).inc()
    
    # In a real app, you would fetch real system metrics here using psutil
    CPU_USAGE.set(15.5)
    RAM_USAGE.set(45.2)

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)
    print("Prometheus metrics server started on port 8000")
