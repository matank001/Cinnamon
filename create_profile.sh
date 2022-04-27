mkdir profile

# be sure that it has those cause if not we are in a bad prob...
sudo apt install make
sudo apt install gcc
sudo apt install dwarfdump

echo 'Done making...'
cd volatility/tools/linux/ && make
cd ../../../
cd profile
echo 'Done making...'
echo 1 | sudo -S zip $(lsb_release -i -s)_$(uname -r)_profile.zip ../volatility/tools/linux/module.dwarf /boot/System.map-$(uname -r)
