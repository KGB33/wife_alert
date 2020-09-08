# Wife Alert

_A simple Flask app used to send commands to a RaspberryPi._


These commands activate various electonics on the Pi to alert the
wife without startling her.

# Installation

## via Docker

Note:
  > To access the GPIO pins Docker needs access to the `/dev/gpiomem` device.
  > Start the container with the following flag: `--device /dev/gpiomem`.
  > For more information see this [stackoverflow](https://stackoverflow.com/questions/30059784/docker-access-to-raspberry-pi-gpio-pins) post

## via Source

### Requirments
  * Python3
  * Redis
  * Poetry

# Wireings

![circut diagram](/img/circuit.svg)
