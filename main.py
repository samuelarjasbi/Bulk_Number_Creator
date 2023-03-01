
import phonenumbers
from openpyxl import Workbook

# All ISPs codes
mtn = ["+98933", "+98935", "+98936", "+98937", "+98938",
       "+98939", "+98930", "+98901", "+98902", "+98903", "+98905"]
mci = ["+98910", "+98913", "+98990", "+98919", "+98992", "+98910", "+98912",
       "+98914", "+98915", "+98916", "+98917", "+98918", "+98991", "+98993"]
rtl = ["+98920", "+98921", "+98922", "+98923"]


# Create largest number with given Digit amount
def Last_number_with_N_digits(n):
    range_end = (10**n)-1
    return range_end


# Create left over numbers
def create_bulk(number):
    num = 7 - number
    output = []
    for i in range(0, Last_number_with_N_digits(num)+1):
        output.append(str(i).rjust(num, '0'))

    return output


# combine left over numbers with given data


def number_generator(isp, number, amount):
    output = []
    if isp.lower() == "mtn":
        for i in mtn:
            for n in create_bulk(amount):
                num = f"{i}{n}{number}"
                z = phonenumbers.parse(num, None)
                if phonenumbers.is_valid_number(z):
                    output.append(num)
    elif isp.lower() == "mci":
        for i in mci:
            for n in create_bulk(amount):
                num = f"{i}{n}{number}"
                z = phonenumbers.parse(num, None)
                if phonenumbers.is_valid_number(z):
                    output.append(num)
    elif isp.lower() == "rtl":
        for i in rtl:
            for n in create_bulk(amount):
                num = f"{i}{n}{number}"
                z = phonenumbers.parse(num, None)
                if phonenumbers.is_valid_number(z):
                    output.append(num)
    return output


def convert_to_excel(numbers: list):
    wb = Workbook()
    ws = wb.active
    for idx, i in enumerate(numbers):
        ws[f'A{idx+1}'] = i
    wb.save("Phone_numbers_output.xlsx")


isp = ''
while (True):
    try:
        isp = input(
            "please enter ISPs (MTN, MCI, RTL) or enter (exit) to close: ")
        print(isp)
    except:
        print("please enter the correct value")
        continue

    phone_number = input("please enter the number that you have: ")
    amount = len(phone_number)

    if isp.lower() == 'exit':
        break
    break


out = number_generator(isp, phone_number, amount)
convert_to_excel(out)
print(len(out))

# create_bulk(int(input("please enter amount of numbers that you have: ")))
