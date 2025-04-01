# Övning: Identifiera det logiska felet och korrigera koden för att
# få körbar kod.

def calculate_average(numbers):
    total = 0
    for number in numbers:
        total += number
    try:
        average = total / len(numbers)
    except ZeroDivisionError:
        return 0
    return average

numbers = []
print("Average:", calculate_average(numbers))
