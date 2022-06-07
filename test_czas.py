import time
# time.sleep(10) # zatrzymaj program na 10 sekund

from datetime import datetime, timedelta, timezone
obiekt_daty_1 = datetime.now(tz=None) # czas teraz
print(obiekt_daty_1)

obiekt_daty_2 = datetime(2022, 10, 1, 22, 13) # inny czas (2022-10-01 22:13:00)
print(obiekt_daty_2)

rok, miesiac = obiekt_daty_1.year, obiekt_daty_1.month
print(miesiac, rok)

obiekt_daty = obiekt_daty_1.replace(hour=10) # zmień godzinę
print(obiekt_daty)

# zmiana obiektu daty na tekst
data_obiekt = datetime.today()
print(data_obiekt)
print(type(data_obiekt))
data_tekst = data_obiekt.strftime('%Y-%m-%d')
print(data_tekst)
print(type(data_tekst))
roznica_czasu = timedelta(days=2)
print(roznica_czasu)

# ---------------------------------------------------------

print(datetime(year=1979, month=4, day=17, hour=21, minute=30, second=35, tzinfo=timezone.utc))

data = datetime.today()
print(data.year)

data_1 = datetime(year=1979, month=4, day=17, hour=21, minute=30, second=35)
data_2 = datetime.today()

for data in [data_1, data_2]:
    print("Cała data:       ", data)
    print("Rok:             ", data.year)
    print("Miesiąc:         ", data.month)
    print("Dzień:           ", data.day)
    print("Godzina:         ", data.hour)
    print("Minuta:          ", data.minute)
    print("Sekunda:         ", data.second)
    print("Mikrosekunda:    ", data.microsecond)
    print("Strefa czasowa:  ", data.tzinfo)
    print()

obiekt_daty = datetime.today()
obiekt_daty_1 = obiekt_daty.replace(year=2002, hour=12)
print(obiekt_daty_1)

