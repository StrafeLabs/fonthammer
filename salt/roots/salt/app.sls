{% set docs_rst = "/var/fonthammer/docs.rst" %}

/etc/motd:
  file.managed:
    - source: salt://motd

python-docutils:
  pkg.installed

{{ docs_rst }}:
  file.managed:
    - source: salt://docs.rst

make-man-page-from-docs:
  cmd:
    - run
    - name: rst2man {{ docs_rst }} /usr/share/man/man7/fonthammer.7
    - require:
      - file: {{ docs_rst }}
      - pkg: python-docutils
