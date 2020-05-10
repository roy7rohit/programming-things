def outer_func(msg):
    def inner_func():
        print(msg)

    return inner_func
my_func = outer_func('hi how are you')
my_func()




# def outer_func():
#     message = 'hello'

#     def inner_func():
#         print(message)
#     return inner_func

# my_func = outer_func()
# my_func()
# my_func()
# my_func()

# # def outer_func(msg):
# #     message = msg

# #     def inner_func():
# #         print(message)
# #     return inner_func

# # my_func = outer_func('hello')
# # my_func()

# #clousers
# import logging
# logging.basicConfig(filename = 'example.log', level = logging.INFO)

# def logger(func):
#     def log_func(*args):
#         logging.info('running "{}" with arguments{}'.format(func.__name__, args))
#         print(func(*args))
#     return log_func

# def add(x, y):
#     return x + y

# def sub(x, y):
#     return x - y

# def mult(x, y):
#     return x * y

# def div(x, y):
#     return x / y

# add_logger = logger(add)
# sub_logger = logger(sub)
# mult_logger = logger(mult)
# div_logger = logger(div)

# add_logger(4, 5)
# sub_logger(9, 6)
# mult_logger(4, 5)
# div_logger(9, 3)

