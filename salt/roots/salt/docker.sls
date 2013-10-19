docker-apt-sources:
  pkgrepo:
    - managed
    - name: deb http://get.docker.io/ubuntu docker main
    - key_url: https://get.docker.io/gpg
    - require_in:
      - pkg: lxc-docker
      - pkg: linux-image-generic-lts-raring

lxc-docker:
  pkg.installed

linux-image-generic-lts-raring:
  pkg.installed
