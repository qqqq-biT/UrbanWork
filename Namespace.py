def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()

test_function()

try:
    inner_function()
except NameError as e:
    print(e)
# inner_function можно вызывать только внутри test_function, а вне ее она недоступна.
