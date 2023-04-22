# positional argument
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"what is it like in {location}")


greet_with("ankit", "sambhar")

greet_with("jaipur", "anotherPerson")


# instead of it you can use keyword argument

# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"what is it like in {location}")


# greet_with("ankit", "sambhar")

greet_with(location="jaipur", name="anotherPerson")