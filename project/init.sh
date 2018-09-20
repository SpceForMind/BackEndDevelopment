APACHE_CONFIG="FlaskApp"
HOST_STRING="127.0.0.1 gen.template"

#install python tolls and flask
bash python_tools.sh
#install apache2
bash apache2.sh

echo "Enter password for set access right to directory /var/www/"
sudo chmod -R ugo+rwx /var/www/
#Copy directory of project in /var/www/
cp -r www/* /var/www/
echo "Copy FlaskApp.conf in /etc/apache2/sites-available/"
sudo cp Apache/"$APACHE_CONFIG.conf" /etc/apache2/sites-available/"$APACHE_CONFIG.conf"
echo "Activate virtual host from $APACHE_CONFIG.conf"
sudo a2ensite $APACHE_CONFIG
sudo systemctl restart apache2
#Copy in /etc/hosts gen.template as domain which available by 127.0.0.1 ip address
sudo sh -c "echo '$HOST_STRING' >> /etc/hosts"
