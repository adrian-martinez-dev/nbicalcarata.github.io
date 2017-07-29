Solución al error de dependencias de libGL.so.1 en Crunchbang Waldorf
#####################################################################

:slug: solución-al-error-de-dependencias-de-libglso1-en-crunchbang-waldorf
:date: 2013/12/18 00:19:05
:category: linux
:tags: crunchbang
:link: 
:description: 


Despues de una instalación fallida de Steam en CrunchBang 11 (basado en Debian 7) me aparecía un error con smplayer sobre la ausencia de el paquete libGL.so.1, y con vlc el uso del procesador se me disparaba al 100%, al parecer esto tuvo que ver con la instalación de librerías de compatibilidad con 32 bits para poder ejecutar Steam.

.. code:: sh

	[adrian@crunchbang ~]$ sudo apt-get install libgl1-mesa-glx:i386
	Leyendo lista de paquetes... Hecho
	Creando árbol de dependencias       
	Leyendo la información de estado... Hecho
	No se pudieron instalar algunos paquetes. Esto puede significar que
	usted pidió una situación imposible o, si está usando la distribución
	inestable, que algunos paquetes necesarios no han sido creados o han
	sido movidos fuera de Incoming.
	La siguiente información puede ayudar a resolver la situación:

	Los siguientes paquetes tienen dependencias incumplidas:
	libgl1-mesa-glx:i386 : Depende: libc6:i386 (>= 2.3.6-6~) pero no a instalarse
                        Depende: libdrm2:i386 (>= 2.3.1) pero no va instalarse
                        Depende: libgcc1:i386 (>= 1:4.1.1) pero no va a instalarse
                        Depende: libglapi-mesa:i386 (= .0.5-4+deb7u2) pero no va a instalarse
                        Depende: libstdc++6:i386 (>= 4.1.1) pero no va a instalarse
                        Depende: libx11-6:i386 (>= 2:1.4.99.1) pero no va a instalarse
                        Depende: libx11-xcb1:i386 pero no va a instalarse
                        Depende: libxcb-glx0:i386 (>= 1.8) pero no va a instalarse
                        Depende: libxcb1:i386 pero no va a instalarse
                        Depende: libxdamage1:i386 (>= 1:1.1) pero no va a instalarse
                        Depende: libxext6:i386 pero no va a instalarse
                        Depende: libxfixes3:i386 pero no va a instalarse
                        Depende: libxxf86vm1:i386 pero no va a instalarse
                        Recomienda: libgl1-mesa-dri:i386 (>= 7.2) pero no va a instalarse
	E: No se pudieron corregir los problemas, usted ha retenido paquetes rotos.
	
.. TEASER_END

El "usted ha retenido paquetes rotos" me pareció algo severo, teniendo en cuenta que si tengo la libreria instalada (de 64 bits) pero en fin, leyendo bastante encontré la solución aqui_ 

.. _aqui: http://superuser.com/questions/653926/how-to-fixerror-while-loading-shared-libraries-libgl-so-1

En mi caso lo resolví desinstalando las librerías de 32 bits y ejecutando los siguientes comandos:

.. code::

	[adrian@crunchbang ~]$ sudo ldconfig
	[sudo] password for adrian: 
	[adrian@crunchbang ~]$ ls -l /usr/lib/x86_64-linux-gnu/libGLU.so.1
	lrwxrwxrwx 1 root root 19 jun  5  2013 /usr/lib/x86_64-linux-gnu/libGLU.so.1 -> libGLU.so.1.3.08005
	[adrian@crunchbang ~]$ dpkg -S libGL.so.1
	libgl1-mesa-glx:amd64: /usr/lib/x86_64-linux-gnu/libGL.so.1.2
	libgl1-mesa-glx:amd64: /usr/lib/x86_64-linux-gnu/libGL.so.1

ldconfig sirve para volver a crear el cache de las librerías compartidas, y con ello así nos olvidamos de este problema, o al menos hasta que vuelva a intentar instalar Steam.




