# Övning: Lägg till loggmeddelanden för att spåra variabler
# och körningsflöde och hitta vad som skapar det felaktiga svaret.

def calculate_area(length: float, width: float) -> float:
    area = length * width
    if __debug__:
        print(f"type(length): {type(length)}")
        print(f"type(width): {type(width)}")
        print("Length:", length)
        print("Width:", width)
        print("Area:", area)
    return length * width

print(calculate_area(10, 5))
