# Program to check if credit card number is valid

def checkSum():
    ip = input("Enter card number: ")

    length = len(ip)

    checkSum = 0
    afterCalc = 0


    for i in range(length):
        if length % 2 == 0:
                
            # For even numbered card numbers - this gets every other digit from first to second last
            if i % 2 == 0:
                # This doubles every other number in the card number starting from the first to the second last
                checkSum = int(ip[i])*2

                # When checkSum has only 1 digit i.e. it is < 10
                if checkSum < 10:
                    afterCalc += checkSum
                    # print(afterCalc)
                # When checkSum has 2 digits i.e. it is > 10
                else:
                    # The greatest digit possible is 9 and 9*2 is 18 which means that if checksum is over ten, the first digit has to be 1 and the second can be anything. We get the second digit of the number by doing % 10
                    afterCalc += 1 + checkSum % 10
                    # print(afterCalc)
        else:
            # For odd numbered card numbers - this gets every other digit from first to second last
            if i % 2 != 0:
                # This doubles every other number in the card number starting from the first to the second last
                checkSum = int(ip[i])*2

                # When checkSum has only 1 digit i.e. it is < 10
                if checkSum < 10:
                    afterCalc += checkSum
                    # print(afterCalc)
                # When checkSum has 2 digits i.e. it is > 10
                else:
                    # The greatest digit possible is 9 and 9*2 is 18 which means that if checksum is over ten, the first digit has to be 1 and the second can be anything. We get the second digit of the number by doing % 10
                    afterCalc += 1 + checkSum % 10
                    # print(afterCalc)


    for i in range(length):
        # For even numbered card numbers - to get digits starting from second to the last digit
        if i % 2 != 0:
            print(ip[i], "i")
            afterCalc += int(ip[i])

    print(afterCalc, "aftercalc")

    # Determine if checksum is passed
    if afterCalc % 10 == 0:
        print("Valid")
        print(checkCard(ip, length))
    else:
        print("INVALID")



def checkCard(cardNum, length):
    if length == 15 and (cardNum[0:2] == "34" or cardNum[0:2] == "37"):
        cardName = "AMEX"
    elif cardNum[0] == "4" and (length == 13 or length == 16):
        cardName = "VISA"
    elif int(cardNum[0:2]) > 50 and length == 16:
        cardName = "MASTERCARD"
    else:
        cardName = "UNKNOWN CARD TYPE"

    return cardName


# Initial function call
checkSum()


# 4003600000000014
# afterCalc 20
# 20%10 == 0
# Valid
# VISA