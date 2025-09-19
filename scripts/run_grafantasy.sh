# script to automate starting a local instance of grafantasy for quick testing/running
# Phase 1
# start node_exporter, prometheus (docker), grafana (docker)
#
# Author: Daire Coleman
# Created: 17/11/2025

# Resolve the absolute path of this script
SCRIPT_PATH="$(readlink -f "$0")"
SCRIPT_DIR="$(dirname "$SCRIPT_PATH")"

echo "Script full path: $SCRIPT_PATH"
echo "Script directory: $SCRIPT_DIR"

# node_exporter

# start cmd
"$SCRIPT_DIR"/../modules/node_exporter/node_exporter > /dev/null 2>&1 &
echo "verifying step"
# verify its up before moving on
success=0
for i in $(seq 1 10); do
    if curl -s -o /dev/null http://localhost:9100/metrics ; then
        echo "✅ node_exporter is up (attempt $i)"
        success=1
        break
    fi
    echo "Waiting for node_exporter... ($i/10)"
    sleep 1
done

if [ $success -eq 0 ]; then
    echo "❌ node_exporter did not start after 10 seconds"
    exit 1
fi



# Prometheus
if docker run --name prometheus --rm -d -p 9090:9090 \
-v "$SCRIPT_DIR"/../modules/prometheus/prometheus.yml:/etc/prometheus/prometheus.yml \
prom/prometheus:main; then
    echo "✅ Prometheus container started"
else
    echo "❌ Prometheus failed to start"
fi
echo "run docker ps to inspect running containers for more info"


# Grafana
cd "$SCRIPT_DIR/../modules/grafana/" || exit
docker compose up -d
echo "Visit http://localhost:3000/ to view"
# TODO:script that gracefully exits all services 
