*This library is not yet functional, everything you see here is speculative*

FontHammer
==========

A Pythonic interface to the excellent FontForge_ font editor.

Installation
------------

FontForge first
~~~~~~~~~~~~~~~

FontHammer needs FontForge to be installed with the Python extension.

FontHammer will refuse to work if it cannot import the ``fontforge`` module
that it needs to function.

On Ubuntu/Debian::

    $ sudo apt-get install fontforge python-fontforge

On Mac OS X using Homebrew_::

    $ brew install fontforge

FontHammer
~~~~~~~~~~

Now install FontHammer::

    $ pip install fonthammer

Usage
-----

Create a new empty font ::

    from fonthammer.api import Font

    font = Font()

Import an SVG file into the font ::

    glyph = font.add_glyph('zoomicon.svg')

Saving ::

    font.save('iconfont.otf')

Development
-----------

FontHammer development uses Vagrant and Salt to configure a virtual machine you can hack on.

Before you start:

#. Install VirtualBox_
#. Install Vagrant_
#. Install salty-vagrant_

Clone FontHammer::

    $ git clone https://github.com/StrafeLabs/fonthammer.git

Bootstrap the VM::

    $ vagrant up

After it's provisioned::

    $ vagrant ssh

Follow the docs displayed as the "message of the day" once you login.

.. _FontForge: http://fontforge.org
.. _Homebrew: http://mxcl.github.io/homebrew/
.. _VirtualBox: https://www.virtualbox.org
.. _Vagrant: http://vagrantup.com
.. _salty-vagrant: https://github.com/saltstack/salty-vagrant
