Gnome terminal darth edition en Ubuntu 14.04
############################################

:slug: gnome-terminal-darth-edition-en-ubuntu-1404
:date: 2014-09-10 11:19:10 UTC-05:00
:category: linux
:tags: terminal
:link: 
:description: 
:type: text


Terminal con tema oscura independiente del tema gtk3, con la barra de titulo oculta al tener la terminal maximizada.

Descargamos gnome-terminal-darth-edition de aqui_.

.. _aqui: http://download.opensuse.org/repositories/home:/ivonunes/Fedora_20/x86_64/gnome-terminal-darth-edition-3.10.2-4.4.x86_64.rpm

Instalamos alien
-----------------

.. code:: sh

    sudo apt install alien

Convertimos el paquete a .deb
-----------------------------

.. code:: sh

    cd Descargas
    sudo alien gnome-terminal-darth-edition-3.10.2-4.4.x86_64.rpm 
    sudo apt remove gnome-terminal-data
    sudo apt remove gnome-terminal

Finalmente instalamos el paquete generado y éste es el resultado final:


Terminal maximizada
-------------------

.. image:: /images/Captura2014-09-1011:31:58.png
    :align: center

Ventana
-------

.. image:: /images/Captura2014-09-1011:34:07.png
    :align: center


