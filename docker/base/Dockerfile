FROM ubuntu:12.10
MAINTAINER Rob Madole

# Update so that we will find python-fontforge
RUN apt-get update

# Dependencies
RUN apt-get install -y python python-dev python-pip

# FontForge has a nasty Segmentation Fault if you try and load a file.
#
# See https://bugs.launchpad.net/ubuntu/+source/fontforge/+bug/805752
#
# To get around it, we're going to rebuild the package.

# We need to get the source files for the package, so add the source
RUN echo "deb-src http://archive.ubuntu.com/ubuntu quantal main universe multiverse" >> /etc/apt/sources.list

# Grab the information for the sources
RUN apt-get update

# These are build tools that we'll need
RUN sudo apt-get install build-essential fakeroot dpkg-dev

# We're going to build this in a temporary directory
RUN mkdir /tmp/fontforge_build

# Get the source
RUN cd /tmp/fontforge_build; sudo apt-get source fontforge
# Build the dependencies for it
RUN cd /tmp/fontforge_build; sudo apt-get -y build-dep fontforge
# Patch the source files
RUN cd /tmp/fontforge_build; dpkg-source -x fontforge_0.0.20120101+git-2ubuntu1.dsc

# Build this
RUN cd /tmp/fontforge_build/fontforge-0.0.20120101+git/; dpkg-buildpackage -rfakeroot -b

# Install all the newly built packages
RUN cd /tmp/fontforge_build; dpkg -i libfontforge1_0.0.20120101+git-2ubuntu1_amd64.deb
RUN cd /tmp/fontforge_build; dpkg -i fontforge-nox_0.0.20120101+git-2ubuntu1_amd64.deb
RUN cd /tmp/fontforge_build; dpkg -i python-fontforge_0.0.20120101+git-2ubuntu1_amd64.deb

# And finally, kill the temporary build directory
RUN rm -rf /tmp/fontforge_build
