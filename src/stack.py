def greet2(name):
    print ("how are you, " + name + "?")


def bye():
    print ("ok bye!")


def greet(name):
    print ("hello, " + name + "!")
    greet2 (name)
    print ("gretting ready to say bye...")
    bye ()

greet("Nancy")

#主要介绍了栈原理，递归算法就是充分利用了堆栈的特性，要注意该算法容易造成内存溢出，
