import string


def process_text(text):
    # Împarte șirul în două părți egale
    mid = len(text) // 2
    part1 = text[:mid]
    part2 = text[mid:]

    # Prelucrarea primei părți: majuscule și eliminarea spațiilor de la început și final
    part1 = part1.upper().strip()

    # Prelucrarea celei de-a doua părți: inversarea șirului, majusculă la început, eliminarea punctuației
    part2 = part2[::-1]  # Inversare șir
    part2 = part2.capitalize()  # Prima literă în majusculă

    # Eliminarea caracterelor de punctuație din a doua parte
    part2 = ''.join(char for char in part2 if char not in string.punctuation)

    # Combinarea celor două părți
    result = part1 + part2
    return result


# Exemplu de utilizare
text = """Python was invented in the late 1980s[41] by Guido van Rossum at Centrum Wiskunde & Informatica (CWI) in the Netherlands as a successor to the ABC programming language, which was inspired by SETL,[42] capable of exception handling and interfacing with the Amoeba operating system.[12] Its implementation began in December 1989.[43] Van Rossum shouldered sole responsibility for the project, as the lead developer, until 12 July 2018, when he announced his "permanent vacation" from his responsibilities as Python's "benevolent dictator for life" (BDFL), a title the Python community bestowed upon him to reflect his long-term commitment as the project's chief decision-maker[44] (he has since come out of retirement and is self-titled "BDFL-emeritus"). In January 2019, active Python core developers elected a five-member Steering Council to lead the project.[45][46]"""
processed_text = process_text(text)
print(processed_text)