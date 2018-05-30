=============================
Prometheus Couchbase Exporter
=============================

This Prometheus exporter runs configured queries against Couchbase and exports the results as Prometheus gauge metrics.

----------

Installation instructions:
--------------------------

Install via ``pip``:

.. code-block::

   $ pip install prometheus-couchbase-exporter

*See ``pip`` installation instructions at http://www.pip-installer.org/en/latest/installing.html*

Usage example:
--------------

By default, it will bind to port 9420, query Couchbase on 127.0.0.1:8091 and run queries configured in an external module `StatsMetrics <https://github.com/brunopsoares/statsmetrics>`_.
You can change these defaults as required by passing in options:

.. code-block::

   $ prometheus-couchbase-exporter -c <couchbase host:port> -p <port to listen>


Docker instructions:
--------------------

Environment variables
In order to configure the Couchbase exporter for use with other than default settings you can pass in the
following environment variables:

.. csv-table:: Environment variables
   :header: "Name", "Description", "Default value"
   :widths: 18, 26, 10

   "COUCHBASE_HOST", "Couchbase host address", "127.0.0.1"
   "COUCHBASE_PORT", "Couchbase port address", "8091"
   "COUCHBASE_USERNAME", "Couchbase username",
   "COUCHBASE_PASSWORD", "Couchbase password",
   "PROMETHEUS_PORT", "Prometheus port to listen", "9420"

Running the container

.. code-block::

   docker run -t -i -p 9420:9420 -e COUCHBASE_HOST=127.0.0.1 -e COUCHBASE_PORT=8091 billmoritz/couchbase-exporter
