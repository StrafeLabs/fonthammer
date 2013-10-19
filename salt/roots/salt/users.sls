/home/vagrant/.profile:
  file.managed:
    - source: salt://.profile
    - user: vagrant
    - group: vagrant

vagrant-user-groups:
  user:
    - present
    - name: vagrant
    - groups:
      - vagrant
      - wheel
      - docker
    - require:
      - pkg: lxc-docker
