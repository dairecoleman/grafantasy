# script to automate stoping a local instance of grafantasy and other modules for quick testing/running/stopping
#
# Author: Daire Coleman
# Created: 19/9/2025

# Resolve the absolute path of this script
SCRIPT_PATH="$(readlink -f "$0")"
SCRIPT_DIR="$(dirname "$SCRIPT_PATH")"

echo "Script full path: $SCRIPT_PATH"
echo "Script directory: $SCRIPT_DIR"

# Node Exporter
NODE_EXPORTER_PID="$(pgrep node_exporter)"
kill "$NODE_EXPORTER_PID"
echo "killed $NODE_EXPORTER_PID"

# Prometheus
docker stop prometheus

# Grafana
cd "$SCRIPT_DIR/../modules/grafana/" || exit
docker compose down

