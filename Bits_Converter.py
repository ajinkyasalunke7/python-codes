def bits_to_bytes(bit_amount):
    byte = bit_amount / 8
    return byte

def bytes_to_megabytes(byte_amount):
    megabyte = byte_amount / (1024 ** 2)
    return megabyte

def megabytes_to_gigabytes(megabyte_amount):
    gigabyte = megabyte_amount / 1024
    return gigabyte

def gigabytes_to_terabytes(gigabyte_amount):
    terabyte = gigabyte_amount / 1024
    return terabyte

# Taking user input for bits
bit_amount = float(input("Enter the amount in bits: "))
byte = bits_to_bytes(bit_amount)
megabyte = bytes_to_megabytes(byte)
gigabyte = megabytes_to_gigabytes(megabyte)
terabyte = gigabytes_to_terabytes(gigabyte)

print(f"{bit_amount} bits is equal to:")
print(f"{byte} bytes")
print(f"{megabyte} Megabytes")
print(f"{gigabyte} Gigabytes")
print(f"{terabyte} Terabytes")
