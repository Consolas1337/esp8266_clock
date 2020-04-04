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
    renderDate()
    renderTime()
    gc.collect()

def startClock(): # Функция запуска отрисовки часов 
    lcd.clear()
    timeClk.init(period=1000, mode=Timer.PERIODIC, callback=lambda t:renderClock())

def stopClock(): # Функция остановки отрисовки часов
    timeClk.deinit()
    lcd.clear()
    
def getCovidStats(): # Парсинг статистики COVID-19
    import urequests, json
    gc.collect()
    txt = urequests.get("http://cnsls.ru/covid.php/").text
    json = json.loads(txt)
    return json

def renderCovid():
    #def renderPage(pageNumber):
     #   if pageNumber==1:
      #      lcd.clear()
       #     lcd.move_to(3, 0)
        #    lcd.putstr("ALL CASES")
         #   lcd.move_to(7, 1)
          #  lcd.
    stopClock()
    stats = getCovidStats()
    lcd.move_to(4, 0)
    lcd.putstr("COVID-19")
    lcd.move_to(3, 1)
    lcd.putstr("STATISTICS")
    #covidClk = Timer(2)
    #covidClk.init(mode=Timer.ONE_SHOT, period=1000, callback=lambda t:)
    
timeClk = Timer(1)
startClock()