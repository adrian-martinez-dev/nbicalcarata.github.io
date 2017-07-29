Playonlinux sin audio en OpenSuse 13.1
######################################

:slug: playonlinux-sin-audio-en-opensuse-131
:date: 2014/02/11 14:50:12
:category: linux
:tags: playonlinux, wine, opensuse, quake live
:link: 
:description: Solucion al problema de audio de playonlinux en OpenSuse
:type: text

Debido a que id software decidió terminar con Quake Live en Linux, me puse a la tarea de instalarlo con playonlinux en opensuse 13.1 de 64 bits (abandoné Fedora porque hasta el momento nadie mantiene el driver catalyst de Ati). Me llevé la sorpresa de que el juego se ejecuta perfecto, solo que no tenia audio y al iniciar sesión no arranca si dejas seleccionada la opción "Remember me".
El audio lo solucioné instalando la libreria ``alsa-plugins-pulse-32bit``, y con el detalle del login solo basta desmarcar la opción "Remember me", asi que hay que teclear el nombre de usuario o correo y contraseña cada vez que arranquemos el juego. Happy fragging.
