  #!/bin/bash

echo $(add-apt-repository ppa:ondrej/php -y)
echo 

echo $(apt update)
echo 

echo $(apt install php7.2 libapache2-mod-php7.2 -y)
echo 

echo $(apt install php7.2-curl -y )
echo 

echo $(apt install php7.2-gd -y)
echo 

echo $(apt install php7.2-recode -y)
echo 

echo $(apt install php7.2-tidy -y)
echo 

echo $(apt install php7.2-imagick -y)
echo 

echo $(apt install php7.2-fpm -y)
echo 

echo $(apt install php7.2-mbstring -y)
echo 

echo $(apt install php7.2-xml -y)
echo 

echo $(apt install php7.2-json -y)
echo 

echo $(apt install php7.2-common -y)
echo 

echo $(apt install php7.2-curl -y)
echo 

echo $(apt install php7.2-xmlrpc -y)
echo 

echo $(apt install php7.2-soap -y)
echo 

echo $(apt install php7.2-intl -y)
echo 

echo $(apt install php7.2-zip -y)
echo 

echo $(apt install php7.2-pgsql -y)
echo 

echo $(apt install php7.2-bcmath -y)
echo 

echo $(apt install composer -y)
echo 
