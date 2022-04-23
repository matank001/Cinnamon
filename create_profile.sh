mkdir profile
echo 'Done making...'
cd volatility/tools/linux/ && make
cd ../../../
cd profile
echo 'Done making...'
zip $(lsb_release -i -s)_$(uname -r)_profile.zip ../volatility/tools/linux/module.dwarf /boot/System.map-$(uname -r)