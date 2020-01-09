from machine import Pin, PWM
import time, network, urequests,dht,urandom

sensor = dht.DHT11(Pin(0))         # 使用 D3 腳位取得溫溼度物件
led=Pin(2, Pin.OUT)
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect("bocheng", "123456789")
while not sta_if.isconnected():
    led.value(0)
    pass
led.value(1)
while True:
    sensor.measure()
    temp = sensor.temperature()
    wet = sensor.humidity()
    hot_index = sensor.temperature() + sensor.humidity()*0.1
    iftttURL = "http://maker.ifttt.com/trigger/IotFinal/with/key/dZ3wwtgPxaXqjEqEoGoddb"
    urequests.get(iftttURL + "?value1=" + str(temp) + "&value2=" + str(wet) + "&value3=" + str(hot_index))
    time.sleep(1800)
