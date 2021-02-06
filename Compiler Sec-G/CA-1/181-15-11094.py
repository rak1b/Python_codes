# _________________________.
# Name:Md Rakibul Islam    |
# ID:181-15-11094          |
# _________________________|

token= input('Enter Token : ')

read_file = open('in.txt')
write_file = open('out.txt','w')
txt = read_file.read()

def custom_split(text,token):
    if text[-1] != token:
        text=text+token
    text_list = []
    split_text = ''
    for char in text:
        if char == token:
            if split_text!='':
                text_list.append(split_text)
            split_text = ''
        else :
            split_text = split_text + char
    return text_list

def write_func(text_list,file):
    for text in text_list:
        file.write(text+'\n')
    print('Successfully Done 😃')




write_func(custom_split(txt,token),write_file)
