#When you run a python module with
#python fibo.py <arguments>
#the code in the module will be executed, just as if you imported it,
# but with the __name__ set to "__main__". That means that by adding 
# this code at the end of your module: 
def fib1(s:int)->int:
    print("fibo1")
    return 34

if __name__ =="__main__":
    import sys
    fib1(int(sys.argv[1]))


"""
(base) zcw@mukoedo1993:~/python_related_clone/Python_related/python_official_tutorial/chap6_Modules$ python fibo1.py 53
fibo1
(base) zcw@mukoedo1993:~/python_related_clone/Python_related/python_official_tutorial/chap6_Modules$ import fibo1

Command 'import' not found, but can be installed with:

sudo apt install imagemagick-6.q16                  # version 8:6.9.10.23+dfsg-2.1ubuntu11.2, or
sudo apt install imagemagick-6.q16hdri              # version 8:6.9.10.23+dfsg-2.1ubuntu11.2
sudo apt install graphicsmagick-imagemagick-compat  # version 1.4+really1.3.35-1

(base) zcw@mukoedo1993:~/python_related_clone/Python_related/python_official_tutorial/chap6_Modules$ python
Python 3.8.3 (default, Jul  2 2020, 16:21:59) 
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import fibo1
>>> 
"""