def toRoman(num):
    if int(num) >= 5000:
        return "Sorry, the maxinum number is 4000"
    copy = int(num)
    count = 0
    roman = ""
    while int(copy) >= 1000 and count <= 2:
        count += 1
        roman += "M"
        copy -= 1000
    count = 0
    if int(copy) >= 900:
        roman += "CM"
        copy -= 900
    elif int(copy) >= 800:
        roman += "DCCC"
        copy -= 800
    elif int(copy) >= 700:
        roman += "DCC"
        copy -= 700
    elif int(copy) >= 600:
        roman += "DC"
        copy -= 600
    elif int(copy) >= 500:
        roman += "D"
        copy -= 500
    elif int(copy) >= 400:
        roman += "CD"
        copy -= 400
    while int(copy) >= 100 and count <= 2:
        count += 1
        roman += "C"
        copy -= 100
        count = 0
    if int(copy) >= 90:
        roman += "XC"
        copy -= 90
    elif int(copy) >= 80:
        roman += "LXXX"
        copy -= 80
    elif int(copy) >= 70:
        roman += "LXX"
        copy -= 70
    elif int(copy) >= 60:
        roman += "LX"
        copy -= 60
    elif int(copy) >= 50:
        roman += "L"
        copy -= 50
    elif int(copy) >= 40:
        roman += "XL"
        copy -= 40
    while int(copy) >= 10 and count <= 2:
        count += 1
        roman += "X"
        copy -= 10
    count = 0
    if int(copy) >= 9:
        roman += "IX"
        copy -= 9
    elif int(copy) >= 8:
        roman += "VIII"
        copy -= 8
    elif int(copy) >= 7:
        roman += "VII"
        copy -= 7
    elif int(copy) >= 6:
        roman += "VI"
        copy -= 6
    elif int(copy) >= 5:
        roman += "V"
        copy -= 50
    elif int(copy) >= 4:
        roman += "IV"
        copy -= 4
    while int(copy) >= 1 and count <= 2:
        count += 1
        roman += "I"
        copy -= 1
    return roman
    raise NotImplementedError
