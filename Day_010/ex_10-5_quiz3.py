def outer_function(a, b):
    def inner_function(c, d):
        return c + d

    return inner_function(a, b)


result = outer_function(5, 10)
print(result)

# a = 5, which means c = 5. b = 10, which means d = 10. The output of inner_function becomes the output of outer_function.