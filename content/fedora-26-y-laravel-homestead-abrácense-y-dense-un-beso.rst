:Title: Fedora 26 y Laravel Homestead, abrácense y dense un beso
:Slug: fedora-26-y-laravel-homestead-abrácense-y-dense-un-beso
:Date: 2017-07-29 13:02:41
:Category: linux
:tags: fedora, laravel, homestead

Homestead en Fedora 26
======================

Instrucciones
*************

.. code-block:: sh

  vagrant box add laravel/homestead
  git clone https://github.com/laravel/homestead.git Homestead
  cd Homestead
  git checkout v5.4.0
  bash init.sh


Homestead.yml
*************

.. code-block:: yml

  folders:
      - map: ~/sitios
        to: /home/vagrant/sitios
        type: "nfs"

  sites:
      - map: interpos.app
        to: /home/vagrant/sitios/interpos/public

/etc/hosts
**********

.. code::

  192.168.10.10  interpos.app

Si tenemos código existente en la carpeta de proyectos:

.. code::

  php artisan config:clear

Soporte nfs
***********

.. code-block:: sh

  vagrant plugin install vagrant-bindfs
  sudo dnf install nfs-utils nfs-kernel-server firewall-config
  sudo systemctl enable nfs-server
  sudo systemctl start nfs-server
  sudo firewall-cmd --permanent --add-service=nfs
  sudo firewall-cmd --permanent --add-service=rpc-bind
  sudo firewall-cmd --permanent --add-service=mountd
  sudo firewall-cmd --reload

Debido a que desde la version 2.1.1 de ``nfs-utils`` esta deshabilitado el soporte a UDP por defecto, ``vagrant up``, se queda bloqueado en ``==> homestead-7: Mounting NFS shared folders...``, solo hay que editar ``/etc/sysconfig/nfs`` y añadir ``--udp`` a ``RPCNFSDARGS``, la anterios solución la encontré en este enlace_.

.. code::

  RPCNFSDARGS="--udp"
  
.. _enlace: https://robertbasic.com/blog/enable-udp-for-nfs-on-fedora/

Firewall con GUI
****************

Tomado de aqui_.

.. _aqui: https://meta.discourse.org/t/solved-nfs-mount-hangs-need-vagrant-file-for-fedora-23/41314/2

::

  Example for easily configuring firewalld using the "firewall-config" GUI:
  - Choose "Configuration: Permanent" from the drop down menu
  - Select the zone you want to modify (i chose "internal").
  - Go to the "Interfaces" tab, assign vboxnet0 (or other host-only adapter) to the zone.
  - Go to the "Services" tab, check "mountd", "nfs" and "rpc-bind"
  - Go to the global "Services" tab (next to "Zones"), select NFS and add Port 2049 UDP (only TCP is predefined).
  - Finally choose "Options/Reload Firewalld".
