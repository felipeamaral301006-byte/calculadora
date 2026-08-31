import math
def calculator_T (o,n):
    if o == "sin":
        sin(n)
    elif o == "cos":
        cos(n)
    elif o == "tan":
        tan(n)
    elif o == "sec":
        sec(n)
    elif o == "cossec":
        cossec(n)
    elif o == "arcsin":
        arcsin(n)
    elif o == "arccos":
        arccos(n)
    elif o == "arctan":
        arctan(n)
    elif o == "arcsec":
        arcsec(n)
    elif o == "cossec":
        cossec(n)
    elif o == "arcsin":
        arcsin(n)
    elif o == "arccos":
        arccos(n)
    elif o == "arccos":
        arccos(n)
    elif o == "arctan":
        arctan(n)
    elif o == "arcsec":
        arcsec(n)
    elif o == "arccossec":
        arccossec(n)
def calculator(n,o,m):
    n = n_
    o = o_
    m = m_
    if o_ == "+":
        sum(n,m)
    elif o_ == "-":
        sub(n,m)
    elif o_ == "*":
        mult(n,m)
    elif o_ == "/":
        div(n,m)
    elif o_ == "sin":
        sin(m)
    elif o_ == "cos":
        cos(m)
    elif o_ == "tan":
        tan(m)
    elif o_ == "sec":
        sec(m)
    elif o_ == "cossec":
        cossec(m)
    elif o_ == "arcsin":
        arcsin(m)
    elif o_ == "arccos":
        arccos(m)
    elif o_ == "arctan":
        arctan(m)
    elif o_ == "arcsec":
        arcsec(m)
    elif o_ == "cossec":
        cossec(m)
    elif o_ == "arcsin":
        arcsin(m)
    elif o_ == "arccos":
        arccos(m)
    elif o_ == "arccos":
        arccos(m)
    elif o_ == "arctan":
        arctan(m)
    elif o_ == "arcsec":
        arcsec(m)
    elif o_ == "arccossec":
        arccossec(m)
def sum (n,m):
    sum_n_m = n + m
    print(f"{sum_n_m}")
def sub (n,m):
    sub_n_m = n - m
    print(f"{sub_n_m}")
def mult (n,m):
    mult_n_m = n * m
    print(f"{mult_n_m}")
def div (n,m):
    div_n_m = n / m
    print(f"{div_n_m}")
def sin (a):
    sin_a_ = math.sin(a)
    print(f"{sin_a_:.6f}")
def cos (a):
    cos_a = math.cos(a)
    print(f"{cos_a:.6f}")
def tan (a):
    tan_a_ = math.tan(a)
    print(f"{tan_a_:.6f}")
def cotan (a):
    cotan_a_ = 1/(math.tan(a))
    print(f"{cotan_a_:.6f}")
def sec (a):
    sec_a_ = 1/(math.cos(a))
    print(f"{sec_a_:.6f}")
def cossec (a):
    cossec_a_ = 1/(math.sin(a))
    print(f"{cossec_a_:.6f}")
def arcsin (a):
    a_ = math.degrees(a)
    arcsin_a_ = math.degrees(math.asin(a_))
    print(f"{arcsin_a_:.6f}")
def arccos (a):
    a_ = math.degrees(a)
    arccos_a_ = math.degrees(math.acos(a_))
    print(f"{arccos_a_:.6f}")
def arctan (a):
    a_ = math.degrees(a)
    arctan_a_ = math.degrees(math.atan(a_))
    print(f"{arctan_a_:.6f}")
def arccotan (a):
    a_ = math.degrees(a)
    arccotan_a_ = math.degrees(math.atan(1/a_))
    print(f"{arccotan_a_:.6f}")
def arcsec (a):
    a_ = math.degrees(a)
    arcsec_a_ = math.degrees(math.acos(1/a_))
    print(f"{arcsec_a_:.6f}")
def arccossec (a):
    a_ = math.degrees(a)
    arccossec_a_ = math.degrees(math.asin(1/a_))
    print(f"{arccossec_a_}")
print("If you want calculate trigonomety operations press T ")
type_ = input()
if type_ == "T":
    while True:
        print("Input the math operation with each term separated by a space:")
        o, n = input().split()
        n_ = float(n)
        n_radians = math.radians(n_)
        o_ = str(o)
        calculator_T(o_,n_radians)
else:
    while True:
        print("Input the math operation with each term separated by a space:")
        n, o, m = input().split()
        n_ = float(n)
        o_ = str(o)
        m_ = float(m)
        calculator(n_,o_,m_)



