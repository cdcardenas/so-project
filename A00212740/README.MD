Universidad ICESI

Christian Cárdenas A00212740

Jorge Arturo Hernandez A00317220

Ray Torres A00309856

Proyecto Final de sistemas operacionales

URL: https://github.com/cdcardenas/so-project/

1.Montaje de la maquina virtual Ubuntu Server 16.04 

Para el montaje de maquina virtual empleamos virtualBox de oracle, en la maquina se definieron tres interfaces de red NAT, 
puente y solo anfitrion. la maquina tiene 10GB de almacenamiento y 1gb de ram

![][1]

![][2]

![][3]

![][4]

Aqui ya podemos ver el servidor ubuntu en funcionamiento


![][5]

Descripcion:

-- para configurar las interfaces de red en ubuntu en necesario configurar el archivo interfaces localizado en 

    sudo vi   /etc/network/interfaces
    
En este archivo es necesario agregar el tipo de enlace que deseamos: estatico o dinamico y el nombre de la interfaz, entre otras configuraciones

-- para configurar los puertos es necesario verificar primero el funcionamiento del firewall, que en ubunto se llama ufw(uncomplicated firewall) y esta desactivado por defecto

--finalmente vale la pena resaltar que a diferencia de CentOS donde el usuario tiene acceso a un usuario root con todos los privilegios de administrador, en ubuntu ese usuario no existe, en cambio por medio del comando sudo se puede acceder a permisos de alto nivel


Ahora debemos instalar las dependencias necesarias para el funcionamiento de python, esto lo hacemos mediante los siguientes comandos

    sudo apt-get install build-essential checkinstall
    sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev

Descargamos python 2.7 mediante el comando, vale la pena aclarar que ubuntu viene por defecto con python 3, sin embargo se decidio usar python 2.7 para evitar algun inconveniente que pueda llegar a surgir.

    wget https://www.python.org/ftp/python/2.7.13/Python-2.7.13.tgz

descomprimimos el paquete con

    tar xzf Python-2.7.13.tgz
    
ahora compilamos Python, lo configuramos, finalmente lo instalamos usando los comandos, usando el comando install en vez de altinstall nos aseguramos que cuando ejecutemos python, ejecute la version 2.7 y no la que viene por defecto

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
    pip install flask_restplus
    pip install sqlite
    pip install flask-sqlalchemy
    
Ahora debemos clonar el repositorio que contiene la aplicacion web del segundo parcial para ello usamos git

    git clone https://github.com/cdcardenas/so-exam2.git
    
antes de poder lanzar la aplicacion debemos abrir los puertos que usaremos con la aplicacion en este caso vamos a abrir los puertos 80 y 8080 usando los siguientes comandos

        sudo ufw allow 80
        sudo ufw allow 8080
        sudo ufw enable
        
Ahora y ya con los puertos abiertos podemos ejecutar la aplicacion web
que se vera de esta forma:

![][6]
![][7]
![][8]
![][9]

Debido  a que algunas consultas necesitan de programas particulares como sysstat,debemos antes de lanzar la aplicacion instalar estas dependencias con:

        sudo apt-get install sysstat

![][10]

finalmente para la validacion de ejecucion del servicio de netstat se uso el comando 

        sudo netstat -plnt

![][11]
        





  



[1]: images/1.PNG
[2]: images/2.PNG
[3]: images/3.PNG
[4]: images/4.PNG
[5]: images/5.PNG
[6]: images/6.PNG
[7]: images/7.PNG
[8]: images/8.PNG
[9]: images/9.PNG
[10]: images/10.PNG
[11]: images/netstat.PNG

