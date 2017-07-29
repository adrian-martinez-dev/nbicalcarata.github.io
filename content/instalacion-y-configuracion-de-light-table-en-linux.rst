Instalación y configuración de Light Table en Linux
###################################################

:slug: instalacion-y-configuracion-de-light-table-en-linux
:date: 2014/01/09 17:39:30
:category: editor
:tags: html, clojure
:link: 
:description: 

Light Table es un editor de texto para programación web que actualmente se encuentra en fase alfa, el proyecto ganó el año pasado el crowfunding en kickstarter_ por la módica cantidad de $316,720 dolares y hace unos dias se liberó su código fuente como fué prometido inicialmente, asi como la infraestructura necesaria para plugins de terceros. El concepto es bastante interesante y promete mucho, el editor permite la evaluación en tiempo real del código escrito, y soporta Clojure, Clojurescript, JavaScript, Html y Python.

.. _kickstarter: http://www.kickstarter.com/projects/ibdknox/light-table 

Instalación
-----------

.. TEASER_END

Para instalarlo nos dirigimos a la pagina oficial del proyecto www.lighttable.com_ y bajamos el archivo correspondiente a la arquitectura de nuestra computadora, en mi caso 64 bits. Descomprimimos el archivo (esta carpeta yo la copié a */home/adrian/Programas*) y ejecutamos el archivo llamado LightTable

.. _www.lighttable.com: http://www.lighttable.com

Creamos su respectivo lanzador para que nos aparezca en el menú del sistema:

.. code:: sh

    sudo geany /usr/share/applications/LightTable.desktop

.. code:: sh

    [Desktop Entry]
    Name=LightTable
    Comment=LightTable
    Exec=/home/adrian/Programas/LightTable/ltbin
    Icon=/home/adrian/Programas/LightTable/core/img/lticon.png
    Terminal=false
    Type=Application

Y en caso de que se quiera poder ejecutar desde consola creamos un enlace simbolico en /usr/bin/local

.. code:: sh

    sudo ln -s /home/adrian/Programas/LightTable/LightTable /usr/local/bin/LightTable


Configuración
-------------

En la pantalla de bienvenida vienen los tutoriales para usarlo, en lo cual no abundaré aquí, solo expondré las configuraciones que hice como los behaviours y los keymaps. Los behaviours son una forma de ajustar las preferencias del editor, y los keymaps son los atajos de teclado. El lenguaje en el que esta principalmente programado es Clojure, un dialecto de lisp, el cual usa un paradigma de programación funcional, por lo tanto el sintaxis es algo diferente a lo que estamos acostumbrados.


Behaviours
----------

Presionamos *ctrl + space* y tecleamos *user behaviors* y damos *enter*, nos aparecerá esto:

.. code:: clojure

    ;; User behaviors
    ;; -----------------------------
    ;; Behaviors are stored as a set of diffs that are merged together
    ;; to create the final set of functionality that makes up Light Table. You can
    ;; modify these diffs to either add or subtract functionality.
    ;;
    ;; Behaviors are added to tags, objects with those tags then automatically gain
    ;; whatever logic the behavior imparts. To see a list of user-level behaviors,
    ;; start typing a word related to the functionality you want in between the square
    ;; brackets (e.g. "theme").

    {:+ {
         ;; The app tag is kind of like global scope. You assign behaviors that affect
         ;; all of Light Table here
         :app [(:lt.objs.style/set-skin "dark")]
    
         ;; The editor tag is applied to all editors
         :editor [:lt.objs.editor/no-wrap
                  (:lt.objs.style/set-theme "default")]
                  
         ;; Here we can add behaviors to just clojure editors
         :editor.clojure [(:lt.objs.langs.clj/print-length 1000)]}
    
     ;; You can use the subtract key to remove behavior that may get added by
     ;; another diff
     :- {:app []}}

Para editar el tema por defecto, en el tag *editor*, nos vamos a *set-theme*, borramos *default* (sin borrar las comillas) y presionamos *tab* para disparar el menu contextual del autocompletado y escogemos el que mas nos guste. Lo mismo con *set-skin*, podemos elegir entre dark o light (viene otra opcion llamada new dark, esa la ignoramos porque esta incompleta).

El autocompletado viene deshabilitado por defecto, si queremos habilitarlo agregamos:

.. code:: clojure
    
    (:lt.plugins.auto-complete/auto-show-on-input)

Habilitar números de linea

.. code:: clojure

    (:lt.objs.editor/line-numbers)

Cambiar la tipografía

.. code:: clojure

    (:lt.objs.style/font-settings "Inconsolata" 14 1)

Donde el orden de los argumentos es este: *"Fuente" <Tamaño> <Ancho de linea en ems>*

Para ver mas opciones del editor tecleamos : y presionamos tab, siempre cuidando que el corchete quede al final de todos los argumentos agregados al tag.


Keymaps
-------

*ctrl + space* dispara el menú principal que nos da todas las opciones del editor y a muchas de ellas le podemos añadir atajos de teclado.
Para agregar atajos de teclado damos *ctrl + space* y escribimos *user keymap* (de preferencia no debemos tocar los default behaviours y default keymaps, nos podemos meter en problemas).

.. code:: clojure

    ;; User keymap
    ;; -----------------------------
    ;; Keymaps are stored as a set of diffs that are merged together together
    ;; to create the final set of keys. You can modify these diffs to either add
    ;; or subtract bindings.
    ;;
    ;; Like behaviors, keys are bound by tag. When objects with those tags are active
    ;; the key bindings are live. Keys can be bound to any number of Light Table commands,
    ;; allowing you the flexibility to execute multiple operations together. To see a list
    ;; of all the commands you can execute, start typing a word related to the thing you
    ;; want to do in between the square brackets (e.g. type "editor").
    
    {:+ {:app {"f9" [:workspace.show]
               "f8" [:toggle-console]
               "ctrl-shift-n" [:tabset.new]
               "ctrl-shift-w" [:tabset.close]
               "ctrl-shift-h" [:tabset.prev]
               "ctrl-shift-l" [:tabset.next]
               "ctrl-shift-p" [:workspace.add-folder]}
    
         :editor {"alt-w" [:editor.watch.watch-selection]
                  "alt-shift-w" [:editor.watch.unwatch]}}}
                  
Estos son los atajos que yo agregué, recomiendo explorar bastante el editor antes de agregar atajos de teclado.

En lo personal este editor me gusta mucho, y aunque va en la version 0.6.0 lo encuentro bastante funcional y entretenido de usar, aunque no olvidemos que esta en desarrollo y hay todavia muchos detalles por corregir para poder utilizarlo sin problemas.


