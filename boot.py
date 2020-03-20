import uos, gc, webrepl, network, ntptime, utime
from time import sleep_ms, ticks_ms
from machine import I2C, Pin, freq, RTC, Timer
from esp8266_i2c_lcd import I2cLcd

SSID = "SSID"
PASS = "PASSWORD"

freq(160000000) # Адский разгон до 160MHz
webrepl.start() # Запуск REPL
gc.enable()    # Активация сборщика мусора


# Подключение экранчика по i2c
i2c = I2C(scl=Pin(2), sda=Pin(0), freq=400000) # GPIO2 scl; GPIO0 sda;
lcd = I2cLcd(i2c, 0x27, 2, 16) # Адрес I2C 0x27 или 39
lcd.clear() 

#Вывод статуса загрузки прошивки
lcd.putstr("Loading...")
lcd.move_to(0, 1)
lcd.putstr("Setup Wi-Fi")

# Подключение к домашней Wi-Fi сети
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
if not wifi.isconnected():
    wifi.connect(SSID, PASS)
    while not wifi.isconnected():
        pass

def getNetInfo():
  lcd.clear()
  lcd.putstr("WiFi connected!")
  lcd.move_to(0, 1)
  lcd.putstr("IP:"+wifi.ifconfig()[0])
getNetInfo()

# Синхронизация времени по NTP серверу
sleep_ms(50)
time = ntptime.time()
time = time + 5*60*60 # Часовой пояс +5
tm = utime.localtime(time)
RTC().datetime((tm[0], tm[1], tm[2], tm[6] + 1, tm[3], tm[4], tm[5], 0))

sleep_ms(250)
