# Ding Ding!

REST api for a connected bell using [Eve](http://python-eve.org/index.html) working with a Raspberry (B+) on which a Servo is plugged.

## Hardware

![schmatics](http://i.imgur.com/YUFsiGi.png)

## Methods

### GET /dinding
Will orders the Servo to do three times a quarter circle. Returns "Ding ding!" when its over. 
