from datetime import datetime


def pi():
    from decimal import Decimal as D
    from decimal import getcontext

    piamount = int(input("How Much Digits Of PI: "))
    boolwrite = False

    if piamount <= 15:
        piamount = 15
    if piamount * 0.01 >= 1:
        piamount *= 1.01
    else:
        piamount += 1

    k = int(input("Amount Of Iterations: "))

    filewrite = input("Do You Want To Write To File(Default No It Will Append To The File): ").lower()

    if filewrite == "yes":
        boolwrite = True
    else:
        pass

    getcontext().prec = int(piamount) + 1

    S = int(piamount * 0.01 - 1)

    if S < 1:
        S = 1
    else:
        pass

    Slice = slice(0, -S)

    def fact(n):
        j = D(1)
        for i in range(1, n+1):
            j = j * i
        return j

    def product1(k):
        result = fact(4 * k) * (1103 + 26390 * k) / (fact(k) ** 4 * D(396.0) ** (4 * k))
        return result

    def product2(k):
        result = (-1) ** k * fact(6 * k) / (fact(k) ** 3 * fact(3 * k)) * (13591409 + 545140134 * k) / D(640320) ** (3 * k)
        return result

    def sum1(k):
        result = D(0)
        for i in range(k+1):
            result += product1(i)
        return result

    def sum2(k):
        result = D(0)
        for i in range(k+1):
            result += product2(i)
        return result

    def pie(k=500):
        pi = sum1(k) / 9801 * D(8.0) ** D(0.5)
        return pi ** -1

    def pie2(k=500):
        pi = sum2(k) * D(10005).sqrt() / 4270934400
        return pi ** -1

    time1 = datetime.now()
    dpie = str(pie(k))[Slice]
    time2 = datetime.now()
    dpie2 = str(pie2(k))[Slice]
    if filewrite:
        x = open("Decimal-Pi.txt", "a")
        x.write("3.\n")
        for i in range(0, int((len(dpie) - 2) / 50 + 0.5) + 1):
            Nslice = slice(i * 50 + 2, (i + 1) * 50 + 2)
            x.write(dpie[Nslice])
            x.write("\n")
    aslice = slice(0, int(piamount - S) + 2)
    api = open("data/pi_dec_1m.txt", "r")
    acpie = api.read()[aslice]
    api.close()
    print("Calculated PI: " + dpie)
    if acpie == dpie:
        print("The Calculated Pi And The Actual Pi Are The Same")
    else:
        print("The Calculated Pi And The Actual Pi Are Not The Same")
    print("Time Needed To Calculate PI: " + str(time2 - time1))


def e():
    from decimal import Decimal as D
    from decimal import getcontext
    try:
        digits = int(input("Digits Of E: "))
        getcontext().prec = digits
        time1 = datetime.now()
        print(D.exp(D(1)))
        time2 = datetime.now()
        print("Time Elapsed: " + str(time2 - time1))
    except ValueError:
        print("Please Use An Actual Integer")


def golden_ratio():
    from decimal import Decimal as D
    from decimal import getcontext
    import sys
    try:
        amount = int(input("Digits Of Golden Ratio: "))
        getcontext().prec = amount
        time1 = datetime.now()
    except ValueError:
        print("Please Use An Actual Integer")
        sys.exit(1)
    else:
        print(D(5).sqrt() / 2 + D(0.5))
        time2 = datetime.now()
        print("Time Elapsed: " + str(time2 - time1))


print(pi())

while True:
    irrational_number = input("Which Irrational Number Do You Want To Calculate: ").lower()
    if irrational_number == "pi":
        pi()
    elif irrational_number == "golden ratio":
        golden_ratio()
    elif irrational_number == "e":
        e()
    else:
        print("We Don't Have That Irrational Number In Our Code!!")
