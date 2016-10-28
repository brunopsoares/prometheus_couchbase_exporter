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

By default, it will bind to port 9119, query Couchbase on 127.0.0.1:8091 and run queries configured in an external module `StatsMetrics <https://github.com/brunopsoares/statsmetrics>`_.
You can change these defaults as required by passing in options:

.. code-block::

   $ prometheus-couchbase-exporter -c <couchbase host:port> -p <port to listen>
