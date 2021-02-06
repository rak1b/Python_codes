token= input('Enter Token : ')
text= input(f'Enter Text With {token} : ')

print(text,token)
def custom_split(text,token):
    if text[-1] != token:
        text=text+token
    text_list = []
    split_text = ''
    for i in text:
        if i == token:
            text_list.append(split_text)
            split_text = ''
        else :
            split_text = split_text + i
    for text in text_list:
        print(text)


custom_split(text,token)


