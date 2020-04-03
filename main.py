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

timeClk = Timer(-1)

def renderClock():
    renderDate()
    renderTime()
    if RTC().datetime()[5]==0: # Синхронизация времени раз в час
        parseTime()
    
def renderDate(): # Отрисовка даты
    lcd.move_to(4, 0)
    formated = "{:0=2}/{:0=2}/{:0=2}".format(RTC().datetime()[2],RTC().datetime()[1],int(str(RTC().datetime()[0])[:-2]))
    lcd.putstr(formated)
    
def renderTime(): # Отрисовка времени
    lcd.move_to(4, 1)
    formated = "{:0=2}:{:0=2}:{:0=2}".format(RTC().datetime()[4],RTC().datetime()[5],RTC().datetime()[6])
    lcd.putstr(formated)
    lcd.move_to(15, 1)

def startClock(): # Функция запуска отрисовки часов
    lcd.clear()
    timeClk.init(period=1000, mode=Timer.PERIODIC, callback=lambda t:renderClock())

def stopClock(): # Функция остановки рендера
    timeClk.deinit()
    

startClock()

