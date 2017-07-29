Configurando Vim
################

:slug: configurando-vim
:date: 2014/02/10 03:00:48
:category: editor
:tags: neovim
:link: 
:description: Configurando el editor de texto vim
:type: text

Despues de haber usado un tiempo la distribución spf-13 de vim opté por configurarlo a mi gusto para tener mas control sobre su comportamiento. Usar una distro predefinida es muy cómodo pero debido a que me encontré con uno que otro bug y como soy bastante quisquilloso al respecto decidí desinstalarla.

Para poder hacer esto hay que leerse los .vimrc de otras personas, esto es importante para saber que opciones se estan usando y por qué. El .vimrc de spf13 es muy fácil de leer, cada sección viene comentada con su funcionalidad respectiva.

======
Vundle
======

Es una abreviación de Vim Bundle, y sirve para administrar los plugins.

Instalación
___________

.. code:: sh

    git clone https://github.com/gmarik/vundle.git ~/.vim/bundle/vundle

Configuración
_____________

Ésta es una configuración de ejemplo para nuestro .vimrc, donde los bundles son los plugins que necesitemos instalar, estos son repos de github por lo que es una manera muy practica de tenerlos centralizados y actualizados.

.. code-block:: vim

    set nocompatible              " be iMproved, required
    filetype off                  " required

    " set the runtime path to include Vundle and initialize
    set rtp+=~/.vim/bundle/Vundle.vim
    call vundle#begin()
    " alternatively, pass a path where Vundle should install plugins
    "call vundle#begin('~/some/path/here')

    " let Vundle manage Vundle, required
    Plugin 'gmarik/Vundle.vim'

    " The following are examples of different formats supported.
    " Keep Plugin commands between vundle#begin/end.
    " plugin on GitHub repo
    Plugin 'tpope/vim-fugitive'
    " plugin from http://vim-scripts.org/vim/scripts.html
    Plugin 'L9'
    " Git plugin not hosted on GitHub
    Plugin 'git://git.wincent.com/command-t.git'
    " git repos on your local machine (i.e. when working on your own plugin)
    Plugin 'file:///home/gmarik/path/to/plugin'
    " The sparkup vim script is in a subdirectory of this repo called vim.
    " Pass the path to set the runtimepath properly.
    Plugin 'rstacruz/sparkup', {'rtp': 'vim/'}
    " Avoid a name conflict with L9
    Plugin 'user/L9', {'name': 'newL9'}

    " All of your Plugins must be added before the following line
    call vundle#end()            " required
    filetype plugin indent on    " required
    " To ignore plugin indent changes, instead use:
    "filetype plugin on
    " Brief help
    " :PluginList          - list configured plugins
    " :PluginInstall(!)    - install (update) plugins
    " :PluginSearch(!) foo - search (or refresh cache first) for foo
    " :PluginClean(!)      - confirm (or auto-approve) removal of unused plugins
    " see :h vundle for more details or wiki for FAQ
    " Put your non-Plugin stuff after this line

Con ``:PluginInstall`` se instalan o actualizan los plugins agregados, esto se puede hacer también desde linea de comandos con ``vim +PluginInstall +qall``

=======
Plugins
=======

Syntastic
_________

Este plugin sirve para el chequeo de sintáxis del código, para instalarlo agregamos a nuestro .vimrc

.. code:: vim

    Plugin 'scrooloose/syntastic'

Para comprobar los syntax checkers instalados se usa el comando ``:SyntasticInfo``

Para JavaScript me incliné por jshint al ser un poco mas flexible que jslint, influenciado por este post_.

.. _post: http://anton.kovalyov.net/p/why-jshint/

En caso de no tener instalado jshint:

.. code:: sh

    npm install jshint -g

El parametro ``-g`` es para instalarlo de forma global en el sistema.

Habilité el validador ``w3`` porque me volvi loco con el renderizado incorrecto de una pagina web que estaba modificando y resultó que el error era un simple tag sin cerrar, así que no me importa que me suelte mensajes cada vez que guardo el archivo (asi es como funcionan, este comportamiento puede modificarse).

.. code:: vim

    "Syntastic ================================
    let g:syntastic_javascript_checkers = ['jshint']
    let g:syntastic_html_checkers = ['w3']

Este post se estará actualizando regularmente, porque vim es muy extenso y nunca se termina de encontrarle funcionalidades nuevas.
