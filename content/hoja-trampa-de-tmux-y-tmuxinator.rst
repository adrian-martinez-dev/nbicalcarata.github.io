Hoja trampa de Tmux y Tmuxinator
################################

:slug: hoja-trampa-de-tmux-y-tmuxinator
:date: 2014-08-01 16:16:43 UTC-05:00
:category: linux
:tags: tmux, tmuxinator
:link: 
:description: Lista de atajos de teclado de tmux y tmuxinator
:type: text

Aqui esta una lista de los atajos de teclado de *tmux* y comandos de *tmuxinator*, varios de ellos son personalizados, anexo los gists con mis configuraciones.

Tmux
----

.. code:: sh 
    
    tmux -2                 Inicia con soporte para 256 colores
    ctrl+a, c               Nueva pestaña
    ctrl+a, #               Ir a la pestaña #
    ctrl+a, s               Split horizontal
    ctrl+a, v               Split vertical
    ctrl+a, o               Moverse entre splits
    ctrl+a, x               Cerrar split o panel
    ctrl+a, !               Cerrar todos excepto el actual
    ctrl+a+flecha arriba    Redimensionar hacia arriba panel actual
    ctrl+a+flecha abajo     Redimendionar hacia abajo panel actual
    ctrl+a, [               Habilitar scroll (vim)
    q                       Salir del scroll mode
    
tmux.conf
=========

[gist:id=a8b972922a184560a02c]

Tmuxinator
----------

.. code:: sh

    mux new <nombre_del_proyecto>           Crea un proyecto nuevo
    mux start <nombre_del_proyecto>         Arranca el proyecto
    mux list                                Muestra una lista de los proyectos existentes
    mux delete <nombre_del_proyecto>        Borra el proyecto
    mux doctor                              Examina problemas con la configuración
    mux help                                Muestra la ayuda
