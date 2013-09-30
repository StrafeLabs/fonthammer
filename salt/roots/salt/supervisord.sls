supervisor:
  pkg:
    - installed
  service:
    - running
    - require:
      - pkg: supervisor

/etc/supervisor/conf.d/coveragereport.conf:
  file:
    - managed
    - source: salt://supervisor/coveragereport.conf
    - require:
      - pkg: supervisor
    - watch_in:
      - service: supervisor

coveragereport:
  supervisord:
    - running
    - restart: True
    - require:
      - pkg: supervisor
      - file: /var/fonthammer/coveragereport
