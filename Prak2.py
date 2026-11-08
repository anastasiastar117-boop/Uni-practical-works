# Завдання 1. Розширений конвертор температури

temp = float(input("Temperature in Celcius?").replace(",", "."))

tempFloat = float(temp)

tempK = tempFloat + 273.15
print("Temp in Kelvin", round(tempK, 3))

tempF = 1.8 * tempFloat + 32
print("Temp in F", round(tempF, 3))

tempR = tempK * 1.8
print("Temp in Renkin", round(tempR, 3))

tempRe = 0.8 * tempFloat
print("Temp in Reomura", round(tempRe, 3))

# Завдання 2. Паспорт вимірювального каналу

name = input("Welche physikalische Größe? / What physical quantity? (z.B. Temperatur)\n")
einheit = input("Welche Einheit? What unit? (z.B Das Celsius, das Kelvin, das Fahrenheit, Reaumur oder Rankine)\n")
untere_grenze = float(input("Untere Messbereichsrenze (Lower limit):").replace(",", "."))
obere_grenze = float(input("Obere Messbereichsrenze (Upper limit):").replace(",", "."))
messwert = float(input("Aktueller Messwert / Current value (Current value):").replace(",", "."))

breite = obere_grenze - untere_grenze
prozent = round((messwert - untere_grenze)/ breite * 100, 1)

print(f"Kanal / Channel: {name} {einheit}")
print(f"Bereich / Range: {untere_grenze} {einheit}, {obere_grenze} {einheit}, {breite} {einheit}")
print(f"Aktueller Wert / Current value: {messwert} {einheit} ({prozent}% des Bereichs)")

# Завдання 3. Розбір серійного номера датчика

serial = input("Geben Sie die Seriennummer ein.\n Bitte trennen Sie die Teile mit Bindestrichen (wie im Beispiel TMP-2026-000457-UA)\n Please enter the serial number and use hyphens to separate each part, like in the example below TMP-2026-000457-UA.\n").strip().upper()
teil = serial.split("-")

sensor_typ = teil[0]
jahr = int(teil[1])
nummer = int(teil[2])
land = teil[3]
aktuelles_jahr = 2026
alt = aktuelles_jahr - jahr

print(f"Sensortyp / Sensor type : {sensor_typ}")
print(f"Baujahr / Year of manufacture: {jahr}")
print(f"Nummer: {nummer}")
print(f"Land / Country: {land}")
print(f"Alt / Age: {alt} Jahre ( Stand:2026)")
