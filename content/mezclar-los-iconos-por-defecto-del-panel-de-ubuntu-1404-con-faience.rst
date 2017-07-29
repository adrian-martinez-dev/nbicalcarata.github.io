Mezclar los iconos por defecto del panel de Ubuntu 14.04 con Faience
####################################################################

:slug: mezclar-los-iconos-por-defecto-del-panel-de-ubuntu-1404-con-faience
:date: 2014-06-11 06:10:26 UTC
:tags: ubuntu
:category: linux
:link: 
:description: 
:type: text

Existe un detalle que ya esta resuelto en *gnome shell*, los iconos del panel y los de la bandeja de sistema.
En *gnome shell* estan siguiendo ciertas lineas de diseño que benefician la experiencia de usuario, por ejemplo al hacer consistentes los iconos en el panel superior eliminaron el desastre que se convertia gnome 2 al cambiar de tema de iconos, en caso de que algunos indicadores no fueran soportados por éste.

En el caso de *unity* en *ubuntu 14.04*, el area de notificacion esta muy bien, mientras uses el tema por defecto.

Asi que para resolver esto, se puede tener lo mejor de los dos mundos, usar tu tema favorito en folders y aplicaciones, y los iconos de *ubuntu* por defecto en el panel, la combinacion es hermosa.
Para conseguirlo, en mi caso *faience* + *ubuntu mono light*, hacemos lo siguiente:

1. Instalamos los iconos *faenza* y *faience*
2. Presionamos **alt + f2** e ingresamos  
   
.. code:: sh
   
    gksu nautilus /usr/share/icons

3. Copiamos la carpeta *ubuntu-mono-light* (para panel claro) en el mismo directorio *icons*, y la renombramos (en mi caso *faience-mono-light*)
4. Editamos el archivo *index.theme* contenido en el folder nuevo, modificando **solo** las lineas siguientes:

.. code:: sh

    [Icon Theme]
    Name=Faience-Ubuntu-Mono-Light
    Comment=Faience + Ubuntu-Mono-Light
    Inherits=Faience-Ocre

5. Guardamos y con *unity tweak tool* escogemos nuestro tema personalizado.

.. image:: /images/captura92630.jpg
    :align: center

