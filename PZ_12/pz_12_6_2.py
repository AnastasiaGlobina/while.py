#2. Составить генератор (yield), который переведет символы строки из верхнего
# регистра в нижний.
def to_lower(input_string):
    for char in input_string:
        if char.isupper():
            yield char.lower()
        else:
            yield char
input_string = "Hello, World!"
output_string = ''.join(to_lower(input_string))
print(output_string)
