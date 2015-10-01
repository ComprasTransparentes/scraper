## Documentación de Scraper de Licitaciones y Órdenes de Compra

### API en Ruby on Rails que escribe los datos 

* Verificar que ruby (2.2.1) esté instalado. Si no existe Ruby, visitar https://www.ruby-lang.org/en/documentation/installation/
$ ruby -v


* Crear y usar el nuevo RVM gemset 
$ rvm use --create 2.2.1@nombre_de_instancia

* Ir al directorio donde se descargó el repositorio e instalar .rvmrc para el conjunto de gemas
$ cd awesome_rails_project
$ rvm --rvmrc 1.9.3@awesome_rails_project

* Verificar rvmrc
$ cd ..; cd -


* Instalar las gemas (rails está incluido)
$ bundle install

* Migraciones 
$ rake db:create
$ rake db:migrate

* Ejecutar el servidor 
$ rails s

###  Proceso en python para realizar la descarga de Licitaciones desde api.chilecompra.cl por fecha

* Requerimientos: python 2.7 y pip. 

* Instalar virtualenvwrapper para el manejo de librerías  
$ pip install virtualenvwrapper 

* Crear un virtualenv 
$ mkvirtual nombre_virtual_env  

* Desde la raiz del proyecto instalar las dependencias
$ pip install -r requirements.txt  

* Ejecutar el programa 
$ python parserLicitaciones.py  

###  Consideraciones 

* Es necesario modificar la BBDD de Tokens para poder acceder a la información. Los tokens de Chilecompra se obtienen desde http://api.mercadopublico.cl/participa.aspx
* Para trabajar en entorno de producción, es necesario modificar el archivo config/application.yml 
* Es posible parametrizar la fecha de inicio del scraper de Licitaciones, editando la línea 932 dl 
