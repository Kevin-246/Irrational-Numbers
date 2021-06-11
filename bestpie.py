from datetime import datetime
from decimal import Decimal
from decimal import getcontext
import sys


def pi() -> None:
    pi_digits = int(input("How many digits of pi to use?\nEnter here: "))

    if pi_digits <= 15:
        pi_digits = 15
    if pi_digits * 0.01 >= 1:
        pi_digits *= 1.01
    else:
        pi_digits += 1

    iterations = int(input("Enter the amount of iterations: "))

    filewrite = input("Do you want to write to file (default option is no (append to file))?\nEnter here: ").lower()

    getcontext().prec = int(pi_digits) + 1

    # TODO (for you): give the variable an actual name in lower case form, separated by '_'s if necessary
    s = int(pi_digits * 0.01 - 1)

    if s < 1:
        s = 1

    __slice = slice(0, -s)

    def fact(value):
        decimal = Decimal(1)
        for j in range(1, value + 1):
            decimal = decimal * j
        return decimal

    def product1(value):
        result = fact(4 * value) * (1103 + 26390 * value) / (fact(value) ** 4 * Decimal(396.0) ** (4 * value))
        return result

    def sum1(value) -> Decimal:
        result = Decimal(0)
        for j in range(value + 1):
            result += product1(i)
        return result

    def pie(value=500) -> Decimal:
        __pi = sum1(value) / 9801 * Decimal(8.0) ** Decimal(0.5)
        return __pi ** -1

    time1 = datetime.now()
    dpie = str(pie(iterations))[__slice]
    time2 = datetime.now()
    if filewrite:
        x = open("Decimal-Pi.txt", "a")
        x.write("3.\n")
        for i in range(0, int((len(dpie) - 2) / 50 + 0.5) + 1):
            n_slice = slice(i * 50 + 2, (i + 1) * 50 + 2)
            x.write(dpie[n_slice])
            x.write("\n")
    aslice = slice(0, int(pi_digits - s) + 2)
    api = open("data/pi_dec_1m.txt", "r")
    acpie = api.read()[aslice]
    api.close()
    print("Calculated PI: " + dpie)
    if acpie == dpie:
        print("The calculated Pi and the actual Pi are the same")
    else:
        print("The calculated Pi and the actual Pi are not the same")
    print("Time Needed To Calculate Pi: " + str(time2 - time1))


def e() -> None:
    try:
        digits = int(input("Digits Of E: "))
        getcontext().prec = digits
        time1 = datetime.now()
        print(Decimal.exp(Decimal(1)))
        time2 = datetime.now()
        print("Time Elapsed: " + str(time2 - time1))
    except ValueError:
        print("Non-integer values are not allowed.")


def golden_ratio() -> None:
    try:
        amount = int(input("Digits Of Golden Ratio: "))
        getcontext().prec = amount
        time1 = datetime.now()
    except ValueError:
        print("Non-integer values are not allowed.")
        sys.exit(1)
    else:
        print(Decimal(5).sqrt() / 2 + Decimal(0.5))
        time2 = datetime.now()
        print("Time Elapsed: " + str(time2 - time1))


print(pi())

# TODO: add an option to exit the program?
while True:
    irrational_number = input("Which irrational number do you want to calculate (such as pi)?\nEnter here: ").lower()
    if irrational_number == "pi":
        pi()
    elif irrational_number == "golden ratio":
        golden_ratio()
    elif irrational_number == "e":
        e()
    else:
        print("That irrational number doesn't exist in this program.")
