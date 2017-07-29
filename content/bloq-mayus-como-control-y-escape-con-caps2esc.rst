:Title: Bloq mayus como Control y Escape con caps2esc
:Slug: bloq-mayus-como-control-y-escape-con-caps2esc
:Date: 2017-07-28 18:08:07
:Category: utilidades
:Tags: fedora, neovim

El uso de vim se vuelve mas natural cuando se remapea la tecla bloq mayus como control, de esta forma los comandos son insertados de forma ergonomica, ya que la posicion de los dedos permanece la mayor parte del tiempo en el centro del teclado.
Con caps2esc_ es posible hacer esto, ademas se vuelve una tecla escape adicional (cuando se teclea por si sola), y actua como control cuando se presiona en combinación con alguna otra tecla.

.. _caps2esc: https://github.com/oblitum/caps2esc

Instalación de caps2esc en Fedora 26
====================================

.. code-block:: sh

    sudo dnf install systemd-devel libevdev-devel
    git clone https://github.com/oblitum/caps2esc.git
    cd caps2esc
    gcc caps2esc.c -o caps2esc -I/usr/include/libevdev-1.0 -levdev -ludev
    sudo su
    cp caps2esc /usr/bin

    echo "[Unit]
    Description=caps2esc

    [Service]
    ExecStart=/usr/bin/nice -n -20 /usr/bin/caps2esc

    [Install]
    WantedBy=multi-user.target" > /etc/systemd/system/caps2esc.service

    systemctl enable caps2esc
    systemctl start caps2esc
    exit

Los comandos anteriores instalan las dependencias, se clona el repositorio, compilan con gcc, se copia el binario a /usr/bin, se establece un servicio de systemd para que se inicie con el sistema, este servicio se activa y se arranca.


