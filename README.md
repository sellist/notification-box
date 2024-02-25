# Notification Box

My partner and I often work in the same room with headphones on, and when we want to get each other's attention we either text or message each other, or wave our arms frantically. So, in lieu of that, I decided to program this Pico W client to interface with a Mosquitto broker running on a Raspberry Pi 4 server.

A client will have a 10mm arcade button with LED, and when pressed it will send a message to the "push" topic to the MQTT broker and have a blocking sleep. When not blocked, it will listen to that broker on that same topic and light up when a message is recieved. Simple project, but was a way to learn how to set up/use MQTT messaging and 3d printing.

## RPi4 setup
`sudo apt update && sudo apt upgrade`
`sudo apt install -y mosquitto mosquitto-clients`
`sudo systemctl enable mosquitto.service`
`cd /etc/mosquitto/conf.d/`
`sudo touch connect.conf`

In `connect.conf`, use your editor of choice to add:
`listener 1883`
and
`allow_anonymous true` 

To run the broker, use command:
`sudo mosquitto -c /etc/mosquitto/conf.d/connect.conf`
