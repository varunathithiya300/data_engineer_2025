""" 
#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

"""
# We need two loops
n = 9
for i in range(n):
    result = chr(ord("a") + n -1 - i)
    print(result, end = " ")