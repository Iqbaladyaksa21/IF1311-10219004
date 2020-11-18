# kita belajar casting
# Merubah dari satu tipe ke tipe lain 

#integer
print("===Integer===")
data_int = 9;
print ("data =", data_int, ", type =", type(data_int))

data_float = float (data_int)
data_str   = str   (data_int)
data_bool  = bool  (data_int)
print ("data =", data_float, ", type =", type(data_float))
print ("data =", data_str, ", type =", type(data_str))
print ("data =", data_bool, ", type =", type(data_bool))

print("===float===")
data_float = 1.999999;
print ("data =", data_float, ", type =", type(data_float))

data_int   = int   (data_float)
data_str   = str   (data_float)
data_bool  = bool  (data_float)
print ("data =", data_int, ", type =", type(data_int))
print ("data =", data_str, ", type =", type(data_str))
print ("data =", data_bool, ", type =", type(data_bool))

print ("===bool===")
data_bool = 10;
print ("data =", data_bool, ", type =", type(data_bool))

data_int    = int   (data_bool)
data_str    = str   (data_bool)
data_float  = float (data_bool)
print ("data =", data_int, ", type =", type(data_int))
print ("data =", data_str, ", type =", type(data_str))
print ("data =", data_float, ", type =", type(data_float))

print ("===string===")
data_str = 1;
print ("data =", data_str, ", type =", type(data_str))

data_int    = int   (data_str)
data_bool    = bool (data_str)
data_float  = float (data_str)
print ("data =", data_int, ", type =", type(data_int))
print ("data =", data_bool, ", type =", type(data_bool))
print ("data =", data_float, ", type =", type(data_float))