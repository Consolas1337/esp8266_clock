clock1 = bytearray([
    0b11111,
    0b11111,
    0b01110,
    0b00100,
    0b00100,
    0b01010,
    0b10001,
    0b11111
]);
clock2 = bytearray([
    0b11111,
    0b10001,
    0b01010,
    0b00100,
    0b00100,
    0b01110,
    0b11111,
    0b11111
]);


def renderDate(): # Отрисовка даты
    lcd.move_to(4, 0)
    formated = "{:0=2}/{:0=2}/{:0=2}".format(RTC().datetime()[2],RTC().datetime()[1],int(str(RTC().datetime()[0])[:-2]))
    lcd.putstr(formated)
    
def renderTime(): # Отрисовка времени
    lcd.move_to(4, 1)
    formated = "{:0=2}:{:0=2}:{:0=2}".format(RTC().datetime()[4],RTC().datetime()[5],RTC().datetime()[6])
    lcd.putstr(formated)
    lcd.move_to(15, 1)

def renderClock():
    if RTC().datetime()[5]==0 and RTC().datetime()[6]==0: # Синхронизация времени раз в час
        parseTime()
        global stats
        stats = getCovidStats()
    renderDate()
    renderTime()
    gc.collect()

def startClock(): # Функция запуска отрисовки часов 
    lcd.clear()
    timeClk.init(period=1000, mode=Timer.PERIODIC, callback=lambda t:renderClock())

def stopClock(): # Функция остановки отрисовки часов
    timeClk.deinit()
    lcd.clear()

def startCovidScroller(x):
    DELAY = 4000 # ms
    stopClock()
    global paging, stats
    paging = (paging + 1) % 8
    if paging == 1:
        lcd.move_to(4, 0)
        lcd.putstr("COVID-19")
        lcd.move_to(3, 1)
        lcd.putstr("STATISTICS")
    if paging == 2:
        lcd.clear()
        lcd.move_to(0, 0)
        lcd.putstr("Cases:  "+stats["World cases"])
        lcd.move_to(0, 1)
        lcd.putstr("Current:"+stats["World current"])
    if paging == 3:
        lcd.clear()
        lcd.move_to(0, 0)
        lcd.putstr("Recovered:"+stats["World recovered"])
        lcd.move_to(0, 1)
        lcd.putstr("Deaths:   "+stats["World deaths"])
    if paging == 4:
        lcd.clear()
        lcd.move_to(5, 0)
        lcd.putstr("RUSSIA")
        lcd.move_to(3, 1)
        lcd.putstr("STATISTICS")
    if paging == 5:
        lcd.clear()
        lcd.move_to(0, 0)
        lcd.putstr("Cases:"+stats["Russian cases"])
        lcd.move_to(0, 1)
        if stats["Russian new cases"]=="-":
            lcd.putstr("New: ?")
        else:
            lcd.putstr("New: +"+stats["Russian new cases"])
    if paging == 6:
        lcd.clear()
        lcd.move_to(0, 0)
        lcd.putstr("Recovered:"+stats["Russian recovered"])
        lcd.move_to(0, 1)
        lcd.putstr("Deaths:   "+stats["Russian deaths"])
    if paging == 7: 
        startClock()
    
    
paging = 0
timeClk = Timer(1)
button.irq(handler=startCovidScroller,trigger=Pin.PULL_UP)
startClock()