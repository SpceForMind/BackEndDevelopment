#install python libraries and flask
sudo apt-get update
sudo apt-get -y install python3 ipython3 python3-flask curl
#remove old version of mod_wsgi(version for python2)
sudo apt-get -y remove libapache2-mod-wsgi
#install version mod_wsgi for python3
sudo apt-get -y install libapache2-mod-wsgi-py3
