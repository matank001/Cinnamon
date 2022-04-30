sudo su
apt install docker
apt install docker.io
docker pull splunk/splunk:latest
docker pull splunk/universalforwarder:latest

docker network create --driver bridge --attachable cinnamon

# put splunk folder in the correct path to maintain configuration

docker run --network cinnamon -d -p 8000:8000 -e "SPLUNK_START_ARGS=--accept-license" -e "SPLUNK_PASSWORD=Aa123456" -e "SPLUNK_ENABLE_LISTEN=9997" -v "/Cinnamon/splunk/data/var":/opt/splunk/var -v "/Cinnamon/splunk/data/etc":/opt/splunk/etc --name splunk1 --hostname splunk1 splunk/splunk:latest

docker run --network cinnamon -d -p 9997:9997 -e "SPLUNK_START_ARGS=--accept-license" -e "SPLUNK_PASSWORD=Aa123456" -e "SPLUNK_STANDALONE_URL=splunk1" -v "/Cinnamon/splunk/data/fwd":/opt/splunkforwarder/etc/ --name uf --hostname uf splunk/universalforwarder:latest


#if stops consuming add in the forwarder shell "./splunk monitor [vol_out path]