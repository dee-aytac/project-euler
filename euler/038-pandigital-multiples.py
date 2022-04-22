def is_pandigital(number):
    str_num = str(number)
    for i in range(1, 10):
        if not(str(i) in str_num):
            return False 
    return True

def pandigital_multiples(upper_limit):
    maximum_pandigital_product = -1
    for number in range(1, upper_limit):
        power = 1
        con_product = "" # concenated product
        while True:
            if len(con_product) > 9:
                break
            if len(con_product) == 9:
                print(con_product)
                if is_pandigital(con_product) and int(con_product) > maximum_pandigital_product:
                    maximum_pandigital_product = int(con_product)
                break

            new_product = number * power
            con_product += str(new_product)
            power += 1

    return maximum_pandigital_product


if __name__ == "__main__":
    print(pandigital_multiples(10000))