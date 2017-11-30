RYU_VERSION=3.15
cd /usr/local/src
sudo mkdir ryu
sudo chown ${USER}:${USER} ryu
cd ryu
git clone https://github.com/osrg/ryu.git ryu-github --branch=v${RYU_VERSION}
cd ryu-github
python setup.py sdist
mv dist/ryu-${RYU_VERSION}.tar.gz ../ryu_${RYU_VERSION}.orig.tar.gz
rm -f ChangeLog AUTHORS   # Remove "sdist" generated files
cd ..
tar -xzf ryu_${RYU_VERSION}.orig.tar.gz
cd ryu-${RYU_VERSION}
mv debian/changelog debian/changelog-3.10
(MYNAME="$(getent passwd ${USER} | cut -f 5 -d : | cut -f 1 -d ,)";
 DOMAIN="${DOMAIN:-$(hostname --fqdn)}";
 NOW="$(date '+%a, %d %b %Y %H:%M:%S %z')";
 echo "ryu (${RYU_VERSION}-1) trusty; urgency=low";
 echo ""
 echo "  * Manually built Ryu ${RYU_VERSION} package"
 echo ""
 echo " -- ${MYNAME} <${USER}@${DOMAIN}>  ${NOW}"
 echo "") | tee debian/changelog
cat debian/changelog-3.10 | tee -a debian/changelog
rm debian/changelog-3.10
dpkg-buildpackage
cd /usr/local/src/ryu
sudo dpkg --install python-ryu_${RYU_VERSION}*deb ryu-bin_${RYU_VERSION}*deb
sudo dpkg --install python-ryu-doc_${RYU_VERSION}*deb
ryu-manager --version
