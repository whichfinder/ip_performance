#!/usr/bin/env bash
exec bokeh serve & python plotter.py & locust -f check_ips.py