

# Create plugin outputs
python2 volatility/vol.py -l 127.0.0.1::2325 --profile=$1 linux_psaux --output=xlsx --output-file=/vol/output/psaux.xlsx
python2 volatility/vol.py -l 127.0.0.1::2325 --profile=$1 linux_proc_maps --output=xlsx --output-file=/vol/output/proc_maps.xlsx

# Upload
python2 upload_files.py output 192.168.47.130 user 1
rm -r output/*
