python-dev:
  pkg.installed

python-pip:
  pkg.installed

python-dev-packages:
  pip.installed:
    - names:
      - nose
      - coverage
    - require:
      - pkg: python-dev
      - pkg: python-pip
