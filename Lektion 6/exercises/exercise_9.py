"""= = = = = =
Exercise 9-10
= = = = = = """
# Skapa ett program som ber om en rad från en dikt från användaren.
# Raden skrivs in i en textfil "poem.txt".
# Programmet skriver ut sista ordet i filen.

from defaults import DEFAULTS

__all__ = ['main']

def main():
    """main of exercise 9"""
    def get_poem() -> list:
        poem = []
        while row := input("Type a line of poetry (<return> to end input): "):
            poem.append(f"{row}\n")
        return poem

    print(__doc__)
    poem_file = DEFAULTS['poem']['fileName']
    poem = get_poem()
    if poem:
        last_word = poem[-1].split(" ")[-1]
        print(f"last word = {last_word}")
        yes_no = input("Save poem to file (y/n)? ").lower()
        if yes_no == "y":
            try:
                with open(poem_file, "w", encoding="utf8") as file:
                    file.writelines(poem)
            except OSError as exception:
                print(f"{exception}")
        else:
            print("Ok, not saving poem")
        # view poem?
        yes_no = input("View poem (y/n)? ").lower()
        if yes_no == "y":
            print(f"{''.join(poem)}")

if __name__ == "__main__":
    print(__doc__)
    main()
