from django.shortcuts import render,render_to_response

from django.http import HttpResponse
# Create your views here.

class Person(object):
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def say(self):
        return "I'm " + self.name

def index(req):
    return HttpResponse('<h1>Hello World! ZZH@Django</h1>')

def home(req):
    return render_to_response('index1.html',{})

def haha(req):
    #user = {'name':'tom','age':23,'sex':'male'}  #key-value格式就是字典
    user = Person('max',27,'male')
    book_list = ['python','java','php','web']

    return render_to_response('self.html',{'title':'mypage','user':user,'book_list':book_list}) 
                                            #左边这些个title、user、book_list都是html中的变量，
                                            # 可以引用代码里面的，一定要一致

