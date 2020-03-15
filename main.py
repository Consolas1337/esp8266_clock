customChar = bytearray([
  0b01010,
	0b10101,
	0b10001,
	0b01010,
	0b00100,
	0b00000,
	0b00000,
	0b00000
]);


def showTime():
  lcd.clear()
  def updateDate():
    lcd.move_to(0, 0)
    formated = "{:0=2}/{:0=2}/{:0=2}".format(RTC().datetime()[2],RTC().datetime()[1],int(str(RTC().datetime()[0])[:-2]))
    formated = "{: ^16}".format(formated)
    lcd.putstr(formated)
  def updateTime():
    updateDate()
    lcd.move_to(0, 1)
    formated = "{:0=2}:{:0=2}:{:0=2}".format(RTC().datetime()[4],RTC().datetime()[5],RTC().datetime()[6])
    formated = "{: ^16}".format(formated)
    lcd.putstr(formated)
    lcd.move_to(15, 1)
    lcd.putchar(chr(0))
    lcd.custom_char(0, customChar)
  timeClk = Timer(-1)
  timeClk.init(period=1000, mode=Timer.PERIODIC, callback=lambda t:updateTime())
showTime()