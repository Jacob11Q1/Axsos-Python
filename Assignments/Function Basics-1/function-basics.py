#1 The Output: is 5
def a():
    return 5;
print(a());

#2 The Output: is 10
def a():
    return 5;
print(a() + a());

#3 The Output: is 5
def a():
    return 5;
    return 10;
print(a());

#4 The Output: is 5
def a():
    return 5;
    print(10);
print(a());

#5 The Output: is 5 and None
def a():
    print(5);
x = a();
print(x);

#6 The Output: Error
def a(b,c):
    print(b + c);
print(a(1,2) + a(2,3));

#7 The Output: 25
def a(b,c):
    return str(b) + str(c);
print(a(2,5));

#8 The Output: 100 and 10
def a():
    b = 100;
    print(b);
    if b < 10:
        return 5;
    else:
        return 10;
    return 7;
print(a());

#9 The Output: 7 14 Error
def a(b,c):
    if b < c:
        return 7;
    else:
        return 14;
    return 3;
print(a(2,3));
print(a(5,3));
print(a(2,3) + (5,3));

#10 The Output: 8
def a(b,c):
    return b + c;
    return 10;
print(a(3,5));

#11 The Output: 500 500 300 500
b = 500;
print(b);
def a():
    b = 300;
    print(b);
print(b);
a();
print(b);

#12 The Output: 500 500 300 500
b = 500;
print(b);
def a():
    b = 300;
    print(b);
    return b;
print(b);
a();
print(b);

#13 The Output: 500 500 300 300
b = 500;
print(b);
def a():
    b = 300;
    print(b);
    return b;
print(b);
b = a();
print(b);

#14 The Output: 1 3 2
def a():
    print(1);
    b();
    print(2);
def b():
    print(3);
a();

#15 The Output: 1 3 5 10
def a():
    print(1);
    x = b();
    print(x);
    return 10;
def b():
    print(3);
    return 5;
y = a();
print(y);