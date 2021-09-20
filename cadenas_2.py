def print_name(names):
    upper_name = names.upper()
    lower_name = names.lower()
    fullname_list = names.split()
    for idx, name in enumerate(fullname_list):
        fullname_list[idx] = name.capitalize()
    capitalize_name = " ".join(fullname_list)
    # capitalize_name = names.capitalize()
    print("\n",lower_name,"\n",upper_name,"\n",capitalize_name)

def run():
    fullname = input("Introduzca su nombre completo: ")
    print_name(fullname)


if __name__ == '__main__':
    run()
