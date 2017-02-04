import RPi.GPIO as GPIO

import time

from eve import Eve
app = Eve()

@app.route('/dingding')
def ding_ding():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(21,GPIO.OUT)
    
    p = GPIO.PWM(21,50)
    #sets pin 21 to PWM and sends 50 signals per second
    #pin 21 is the MSIO or GPIO 13
	
    sleep=0.5
    
    p.start(7.5)	   
    for i in range(1,4) :
	#sends a 20% pulse to turn the servo CW
        p.ChangeDutyCycle(20)    
	time.sleep(sleep)			 

        p.ChangeDutyCycle(7.5)    
	time.sleep(sleep)			

    p.stop()
    GPIO.cleanup()
    return 'Ding ding !!'

if __name__ == '__main__':
    app.run(port=8000, host='0.0.0.0')
