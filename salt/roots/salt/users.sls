/home/vagrant/.profile:
  file.managed:
    - source: salt://.profile
    - user: vagrant
    - group: vagrant
