Needs Mosquitto broker installed and running on a server

For Raspberry Pi 4:

`sudo apt update && sudo apt upgrade`
`sudo apt install -y mosquitto mosquitto-clients`
`sudo systemctl enable mosquitto.service`
`cd /etc/mosquitto/conf.d/`
`sudo touch connect.conf`

In connect.conf, add the lines
`listener 1883`
and
`allow_anonymous true`

to enable anonymous access.

`sudo mosquitto -c /etc/mosquitto/conf.d/connect.conf` to run manually