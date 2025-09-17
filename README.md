# Grafantasy

Grafantasy is a personal monitoring and visualization toolkit built with a combination of modules and displayed with Grafana.

## Overview

Right now this repo contains:

- **node_exporter** which exposes metrics on a linux machine 
- **Prometheus** (`modules/prometheus/prometheus.yml`)  
- **Scripts** to start Prometheus and node_exporter (`scripts/run_grafantasy.sh`)  

> Note: Prometheus binaries are **not included**. See setup instructions below.

## Setup (WIP)

### Using Docker (recommended)

If you have Docker installed, you can run Prometheus without including binaries:

```bash
scripts/run_grafantasy.sh
