
# Raspberry Pi Temperature Project - pitemps #

A friend gave me a [DHT11](https://www.adafruit.com/product/386), and I set out to rig it up to my Raspberry Pi.  This project is the result.  At the time, I was also exploring Django and Test-Driven Development, so, the web application included here is a demo of that.

The DHT22.py was adapted from a code sample I had found.  The file requires PIGPIO to run and must be configured to match the pin connections used in the rpi's GPIO pins.

Once everything is configured, running:

`nohup DHT22.py` 

makes regular writes to the database configured in django (I used mysql).  If the application server is running, the page will display the current temperature.  

## Next Steps ##

Build a graph-based front-end to display temperature history.

