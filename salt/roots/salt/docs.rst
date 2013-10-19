FontHammer
==========

Development environment for the FontHammer project.

Build the Docker images
-----------------------

Before developing FontHammer, the Docker images must be build:

**This takes quite a while, so be patient**

::

    $ cd /vagrant/docker
    $ sudo docker build -rm -t strafelabs/fontforge:base base

This build step will prepare a Docker image that has a functioning version of
FontForge installed. The pre-built package that is available from the Ubuntu
package repository has an issue with segmentation faulting when you open a
font file. We work around this by rebuilding the package.

Next up is the image that we'll use to run the FontHammer tests. It's based on
the strafelabs/fontforge:base so it will not take long.

::

    $ sudo docker build -rm -t strafelabs/fonthammer:testrunner testrunner

Running the tests
-----------------

Run the tests:

::

    $ sudo docker run -v /vagrant:/opt/fonthammer -w /opt/fonthammer -i -t strafelabs/fonthammer:testrunner /bin/bash
    $ py.test

Code coverage report will be available afterwards at:

    http://localhost:8001
