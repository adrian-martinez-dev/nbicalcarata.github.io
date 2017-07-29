Ajustes de post instalación de Fedora
#####################################

:slug: ajustes-de-post-instalacion-de-fedora
:date: 2014/03/04 18:05:03
:category: linux
:tags: fedora
:link: 
:description: Ajustes de post instalación de Fedora
:type: text

Fedora es mi distro favorita, y esta es mi guía personal sobre los ajustes que hago despues de una instalación desde cero.
Mi netbook es una Sony Vaio de 11.6 pulgadas con las siguientes caracteristicas:


.. code:: sh

    Distribution: Fedora release 20 (Heisenbug)
    Kernel: Linux 3.13.5-200.fc20.x86_64 x86_64
    RAM: 3640664 kB
    Video: Advanced Micro Devices, Inc. [AMD/ATI] Wrestler [Radeon HD 6320]
    Audio: Advanced Micro Devices, Inc. [AMD/ATI] Wrestler HDMI Audio
    Advanced Micro Devices, Inc. [AMD/ATI] SBx00 Azalia (Intel HDA) (rev 40)
    Ethernet: Qualcomm Atheros AR8131 Gigabit Ethernet (rev c0)
    Wireless: Qualcomm Atheros AR9285 Wireless Network Adapter (PCI-Express) (rev 01)

=======
Ajustes
=======

Actualización del sistema

.. code:: sh

    su -
    yum update
    yum install gnome-tweak-tool Zim redshift-gtk cryptkeeper gparted powertop htop git git-core python-devel gnome-session-properties libreoffice-langpack-es

Para agregarle extensiones a gnome shell entramos a https://extensions.gnome.org/  y activamos las siguientes:

- User theme
- Dash to dock
- Media player indicator
- Coverflow alt tab
- Caffeine
- Drop down terminal
- Avanced volume mixer

Existe un detalle con la terminal que en lugar de mostrar el usuario en el prompt despliega ``bash-4.2$``, esto se corrige editando nuestro ``.bash_profile`` y le agregamos la linea

.. code:: sh

    export PS1="[\u@\h \W]\$ "

Driver Catalyst
_______________

**Atención, el siguiente paso ya no funciona en Fedora 20 debido a que hasta la fecha nadie mantiene el driver privativo**, lo adjunto para el caso de que se vuelva a empaquetar a los repositorios de RPM fusion.

.. code-block:: sh

    su
    yum update kernel
    yum --nogpgcheck install http://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-stable.noarch.rpm http://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-stable.noarch.rpm
    yum install akmod-catalyst xorg-x11-drv-catalyst xorg-x11-drv-catalyst-libs.i686
    mv /boot/initramfs-$(uname -r).img /boot/initramfs-$(uname -r)-radeon.img
    dracut /boot/initramfs-$(uname -r).img $(uname -r)

Y reiniciamos la máquina.

Powertop
________

Powertop es una utilidad que sirve para gestionar las opciones de ahorro de energia que tiene disponible nuestro hardware, nos muestra una lista de los dispositivos y la cantidad de energia que estan utilizando, y tambien nos permite saber si estas opciones estan activas.
Ejecutamos ``powertop`` con permisos de superusuario y al desplazarnos con tab en ``Tunables`` aparecen los dispositivos con su respectiva opcion de ahorro de energia, ``good`` para activada, ``bad`` para desactivada.

Existen varias maneras de que aparezcan en ``good``, la forma mas sencilla, que fue implementada en la versión 2.5 es con la opción ``-html``, con la cual nos genera un archivo html donde nos muestra los comandos a utilizar para hacer los cambios permanentes.

Ejecutamos:

.. code:: sh

    sudo su
    powertop -html

Esto nos genera un archivo llamado ``tml.html`` en nuestra carpeta ``home``, al abrirlo en la opción ``Tuning`` nos muestra los scripts a ejecutar al inicio para activar las gestiones de energia de los dispositivos que lo necesiten.

Creamos el script:

.. code:: sh

    gedit /usr/local/bin/startup.sh

Y pegamos los comandos, en mi caso deje desactivada el ahorro de energia para el raton y el teclado, porque es incomodo hacer click para despertarlo.

[gist:id=9734529 ]

Lo hacemos ejecutable y lo arrancamos 

.. code:: sh

    chmod +x /usr/local/bin/startup.sh
    /usr/local/bin/startup.sh

Si funciona sin problemas lo agregamos al arranque del sistema 

.. code:: sh

    gedit /etc/rc.d/rc.local 

Pegamos esto:

.. code:: sh

    #!/bin/bash
    /usr/local/bin/startup.sh
    exit

Le damos permisos de ejecución

.. code:: sh

    chmod +x /etc/rc.d/rc.local

Iniciamos el servicio y checamos su status

.. code:: sh

    systemctl start rc-local
    systemctl status rc-local

Y reiniciamos de nuevo, todo lo anterior hecho como root.


Codecs, java, flash y utilidades
________________________________

Para esto instalamos Fedy, desde http://satya164.github.io/fedy/, con el siguiente comando:

.. code:: sh

    su -c "curl http://satya164.github.io/fedy/fedy-installer -o fedy-installer && chmod +x fedy-installer && ./fedy-installer"

Audacious
_________

.. code:: sh

    sudo yum install audacious audacious-libs audacious-plugins audacious-plugins-freeworld audacious-plugins-freeworld-aac audacious-plugins-freeworld-ffaudio audacious-plugins-freeworld-mp3







Fedora es una gran distro, lo intente con opensuse y derivadas de debian, pero la verdad no me convencen tanto, solo espero que se resuelva pronto lo de Catalyst, aunque el driver libre funciona correctamente, lo ideal seria tener instalado el privativo para sacarle todo el jugo a la tarjeta gráfica.


