include:
  - python

fonthammer-installed:
  pip.installed:
    - name: fonthammer
    - editable: file:///vagrant
    - require:
      - pkg: python-pip

/etc/motd:
  file.managed:
    - source: salt://motd
