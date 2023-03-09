
# # All ISPs codes
# mtn = ["+98933", "+98935", "+98936", "+98937", "+98938",
#        "+98939", "+98930", "+98901", "+98902", "+98903", "+98905"]
# mci = ["+98910", "+98913", "+98990", "+98919", "+98992", "+98910", "+98912",
#        "+98914", "+98915", "+98916", "+98917", "+98918", "+98991", "+98993"]
# rtl = ["+98920", "+98921", "+98922", "+98923"]


import itertools
import vobject


def generate_numbers(number):
    """Generate a list of 11 digit numbers with missing digits replaced by every possible digit from 0 to 9"""

    # Find the positions of the stars in the input number
    star_positions = [i for i in range(len(number)) if number[i] == "*"]

    # Generate a list of every possible digit permutation for the missing positions
    digit_permutations = [[str(digit) for digit in range(10)]
                          for _ in range(len(star_positions))]
    digit_combinations = itertools.product(*digit_permutations)
    digit_combinations = [''.join(x) for x in digit_combinations]

    # Replace the stars in the input number with each possible digit combination to generate a list of 11 digit numbers
    numbers = []
    for digits in digit_combinations:
        new_number = number
        for i in range(len(star_positions)):
            new_number = new_number[:star_positions[i]] + \
                digits[i] + new_number[star_positions[i]+1:]
        numbers.append(new_number)

    return numbers


number = "92116*4*86"
contacts = generate_numbers(number)

# Create a VCF file with the generated contacts
vcard_list = []
for contact in contacts:
    vcard = vobject.vCard()
    vcard.add('fn').value = "Contact " + contact
    vcard.add('tel').value = "+98" + contact
    vcard_list.append(vcard)

with open("contacts.vcf", "w") as vcf_file:
    for vcard in vcard_list:
        vcf_file.write(vcard.serialize())
        vcf_file.write('\n')
