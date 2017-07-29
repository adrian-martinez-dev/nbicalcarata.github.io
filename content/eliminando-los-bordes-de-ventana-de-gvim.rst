Eliminando los bordes de ventana de GVim
########################################

:slug: eliminando-los-bordes-de-ventana-de-gvim
:date: 2014-06-14 19:42:16 UTC-05:00
:tags: vim, gvim 
:category: editor
:link: 
:description: Como quitar los bordes de la ventana de GVim
:type: text

Para quitar el borde de la ventana que aparece al maximizar *GVim* solo hay que crear un archivo *.gtkrc-2.0* en nuestro *home* y le pegamos éste código

.. code:: bash 

    style "vimfix" {
    bg[NORMAL] = "#242424" # this matches my gvim theme 'Normal' bg color.
    }
    widget "vim-main-window.*GtkForm" style "vimfix"


Antes y después

.. image:: /images/Captura192813.png

.. image:: /images/Captura193101.png

