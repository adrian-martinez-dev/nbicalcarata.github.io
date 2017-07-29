:Title: Universal Ctags
:Slug: universal-ctags
:Date: 2017-07-28 22:45:35
:Category: utilidades
:Tags: fedora, neovim

Instalación de Universal Ctags en Fedora 26
===========================================

.. code-block:: sh

    sudo dnf install autoconf automake
    git clone https://github.com/universal-ctags/ctags
    cd ctags
    ./autogen.sh
    ./configure
    make
    sudo make install

