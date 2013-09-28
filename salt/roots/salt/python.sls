python-dev:
  pkg.installed

python-pip:
  pkg.installed

python-dev-packages:
  pip.installed:
    - names:
      - pytest
      - mock
      - pytest-cov
    - require:
      - pkg: python-dev
      - pkg: python-pip
