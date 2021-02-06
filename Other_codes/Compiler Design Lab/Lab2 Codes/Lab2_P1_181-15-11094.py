read_file = open('take_input.txt')
write_file = open('write_output.txt','w')

def count_letter(file):
    file = file.read()
    saving_letter = {}
    for letter in file:
        if letter not in saving_letter.keys():
            saving_letter[letter]= 1
        else:
            add_val = saving_letter[letter] + 1
            saving_letter[letter]= add_val
    return saving_letter

def write_output(x,file):
    text = ''
    for key,val in x.items():
        if '\n' in key:
            newline = f'\\n: {x[key]}'
            text = text + newline + '\n'
        else:
            letters = f'{key} : {x[key]}'
            text = text + letters + '\n'
    if file.write(text):
        print('Successfully Done 😃')


write_output(count_letter(read_file),write_file)

