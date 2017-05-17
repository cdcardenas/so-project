Universidad ICESI

Christian Cárdenas

Jorge Arturo Hernandez

Ray Torres

Proyecto Final de sistemas operacionales

1.Montaje de la maquina virtual Ubuntu Server 16.04 

Para el montaje de maquina virtual empleamos virtualBox de oracle, en la maquina se definieron tres interfaces de red NAT, 
puente y solo anfitrion. la maquina tiene 10GB de almacenamiento y 1gb de ram

![][1]

![][2]

![][3]

![][4]

Aqui ya podemos ver el servidor ubuntu en funcionamiento


![][5]

Ahora debemos instalar los paquetes necesarios para el funcionamiento de python, esto lo hacemos mediante los siguientes comandos

    sudo apt-get install build-essential checkinstall
    sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev

Descargamos python 2.7 mediante el comando

    wget https://www.python.org/ftp/python/2.7.13/Python-2.7.13.tgz

descomprimimos el paquete con

    tar xzf Python-2.7.13.tgz
    
ahora compilamos Python, lo configuramos, finalmente lo instalamos usando los comandos

    cd Python-2.7.13
    sudo ./configure
    sudo make install

para revisar que haya quedado bien instalado usamos

    Python2.7 -V
    
ahora nos dirigimos a la carpeta home de usuario e instalmos  pip, virtualenv y Flask

    sudo wget https://bootstrap.pypa.io/get-pip.py
    python get-pip.py
    pip install virtualenv
    
    cd ~/
    mkdir envs
    cd envs
    virtualenv flask_env
    
para activar el ambiente usamos

    . flask_env/bin/activate
  
con el ambiente activo procedemos a instalar Flask

    pip install Flask
    
Ahora debemos clonar el repositorio que contiene la aplicacion web del segundo parcial para ello usamos git

    git clone git
    



  



[1]: images/1.PNG
[2]: images/2.PNG
[3]: images/3.PNG
[4]: images/4.PNG
[5]: images/5.PNG
