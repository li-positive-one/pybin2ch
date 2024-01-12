from pybin2ch.ref import bytes2c_adobe,bytes2c_allx
import os

def test_python_equal():
    for _ in range(1000):        
        d1=os.urandom(10)
    
        a2=bytes2c_allx(d1)
        d2=eval(f'b"{a2}"')

        a3=bytes2c_adobe(d1)
        d3=eval(f'b"{a3}"')


        assert d1==d2
        assert d1==d3