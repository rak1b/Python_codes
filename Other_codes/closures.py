def greetings(greet):
    def greet_with_name(name):
        return f'{greet} {name}'
    return greet_with_name

say_hello = greetings('Hello')

print(say_hello('Rakib'))
