# Övning: Lägg till exception för att hantera fel
# som kan uppstå vid körning av koden.

numerator = 10
denominator = 0

try:
    result = numerator / denominator
except ZeroDivisionError as exception:
    print(repr(exception))
    result = None
print("Result:", result)
