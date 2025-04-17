# def even_numbers(max_value):
#     num = 0
#     while num <= max_value:
#         yield num
#         num += 2

# generator = even_numbers(10)

# for item in generator:
#     print(item)



def my_generator():
	print('before yield')
	yield 1
	print('yielded 1')
	yield 2
	print('yielded 2')
	yield 3
	print('yielded 3, finished')

def main():
	gen = my_generator()
	print('start')
	v1 = gen.__next__()
	print('called __next__(), v1=%s' % v1)
	v2 = gen.__next__()
	print('called __next__(), v2=%s' % v2)
	v3 = gen.__next__()
	print('called __next__(), v3=%s' % v3)
	v4 = gen.__next__()  # should be exception

main()