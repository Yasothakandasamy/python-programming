list = ['GUVI'] 
def exploder(n):
     print n * 5
def my_map_simple(fun, list):
    for item in list:
    	fun(item)

my_map_simple(exploder, list)
