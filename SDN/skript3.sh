virtualenv virt_ryu_3_16/
source virt_ryu_3_16/bin/activate
cd /media/floodlight/home/ryu/virt_ryu_3_16/
git https://github.com/osrg/ryu.gitclone 
git clone https://github.com/osrg/ryu.git 
git checkout v3.16
ryu --version
sudo apt-get update
sudo apt-get install python-dev python-pip
cd ryu/
sudo pip install -r ./tools/pip-requires
sudo pip install six --upgrade
sudo python ./setup.py install
ryu --version
