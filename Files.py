with open ('referat.txt', 'r', encoding = 'utf-8') as example:
    content = example.read()
    lenght_content = len(content)
    splitted_content = content.split()
    amount_words = len(splitted_content)
    print("\nДлина строки составляет - {} символов".format(lenght_content))
    print("\nКоличество слов = {} шт.".format(amount_words))

    value = ""

with open ('referat.txt', 'r+', encoding = 'utf-8') as rewrite:
    for sign in rewrite:
        sign = sign.replace(".","!")
        
        sign = value + sign
        
        value = sign
    print ("\n{}".format(sign))
        
    

with open ('referat2.txt', 'w', encoding = 'utf-8') as new_file:
            new_file.write(sign)

    