python-dev:
  pkg.installed

python-pip:
  pkg.installed

python-dev-packages:
  pip.installed:
    - names:
      - coverage
      - pytest
      - mock
    - require:
      - pkg: python-dev
      - pkg: python-pip
