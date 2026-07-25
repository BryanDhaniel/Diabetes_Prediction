#!/bin/bash

echo "Memulai proses setup Prometheus dan Grafana tanpa Docker..."

# 1. Setup Prometheus
if [ ! -d "prometheus-2.53.0.linux-amd64" ]; then
    echo "Mengunduh Prometheus..."
    wget -q https://github.com/prometheus/prometheus/releases/download/v2.53.0/prometheus-2.53.0.linux-amd64.tar.gz
    tar -xzf prometheus-2.53.0.linux-amd64.tar.gz
    rm prometheus-2.53.0.linux-amd64.tar.gz
fi

echo "Menjalankan Prometheus di background (port 9090)..."
cd prometheus-2.53.0.linux-amd64
./prometheus --config.file="../Monitoring dan Logging/prometheus.yml" > prometheus.log 2>&1 &
cd ..

# 2. Setup Grafana
if [ ! -d "grafana-v11.1.0" ]; then
    echo "Mengunduh Grafana..."
    wget -q https://dl.grafana.com/oss/release/grafana-11.1.0.linux-amd64.tar.gz
    tar -xzf grafana-11.1.0.linux-amd64.tar.gz
    rm grafana-11.1.0.linux-amd64.tar.gz
fi

echo "Menjalankan Grafana di background (port 3000)..."
cd grafana-v11.1.0
./bin/grafana server > grafana.log 2>&1 &
cd ..

echo "========================================="
echo "SELESAI!"
echo "Prometheus berjalan di http://localhost:9090"
echo "Grafana berjalan di http://localhost:3000"
echo "========================================="
