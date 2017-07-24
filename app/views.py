from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from  app.forms import PublisherForm1,PublisherForm2,PublisherForm,UserForm,ItemsbForm,ClientForm,User
from django.http import HttpResponse,HttpResponseRedirect,Http404
from app.models import Publisher,User,itemsb,Cliente
from  django.contrib import auth
from app import models
from  django.contrib.auth import  authenticate,login
from django.template.context import RequestContext
from django.shortcuts import render_to_response


# Create your views here.
# def login(request):
#
#     return  render(request,'login.html' )
#def table(request):
   # users = user_list.objects.all()
   # print(users.name)
    #return  render(request,'table.html',{'user_list':user_list})

#使用forms
def add_publisher1(request):
    if request.method == "POST":
            #如果是POST，接受post的数据
        name = request.POST['name']  #字典的方式获取
        city = request.POST.get('city') #get方法获取
        Publisher.objects.create(
            name = name,
            city = city,
        )
        return HttpResponse("添加成功！")
        #print(request.POST)
    else:
        return render(request,"add_publisher1.html",locals())

# 使用django form
def add_publisher2(request):
    if request.method == "POST" :
        publisher_form = PublisherForm2(request.POST)  #定义表单对象，初始化
        if publisher_form.is_valid():                   #is_vlaid 验证表单是否合法
            Publisher.objects.create(
                name = publisher_form.cleaned_data['name'],  #clwaned_data
                city = publisher_form.cleaned_data['city'],
                address = publisher_form.cleaned_data['address'],
                email = publisher_form.cleaned_data['email'],
            )
            return HttpResponse('添加成功！')
    else :
        publisher_form = PublisherForm2()  #定义一个表单
    return render(request,'add_publisher2.html',locals())

#使用MoodelForm
def add_publisher(request):
    if request.method == "POST" :
        publisher_form = PublisherForm(request.POST)   #表单对象，初始化
        if publisher_form.is_valid():                   #is_vlaid 验证表单是否合法
            #print(Publisher.POST)
            publisher_form.save()                     #save()添加数据
            return HttpResponse('添加成功！')
    else :
         publisher_form = PublisherForm()
    return render(request,'add_publisher.html',locals())

def login(request):
    # try:
    #     offset = int(offset)
    # except ValueError:
    #     raise Http404()
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        print('username:',username,'passwd:',password)
        count = models.User.objects.filter(username=username, password=password).count()
        print(count)
        if count >  0:
            return render_to_response('left_apply0.html')
        else:
            return HttpResponse("账户密码错误")
            # return HttpResponseRedirect('login?message=账户密码错误')
    else:
        userform = UserForm()
        return render(request, 'login.html', locals())


def register(request):
    userform =UserForm(request.POST)
    if request.method == 'POST':
        if userform.is_valid():
            userform.save()
            # return HttpResponse("注册成功！")
            return render(request, 'login.html', locals())
    return render(request, 'reg.html', locals())

def test(request):
    athlete = '0'
    athlete_list = [1,2,3,4,5,6,7,8,0]
    asdfghjkhgfds = 88
    value = 'asdfghjkhgfdsas'
    return render(request, 'test.html', locals())
def index(request):
    return render_to_response('index.html')

def Itemsb(request):
    itemsbform = ItemsbForm(request.POST)
    if request.method == 'POST':
        if itemsbform.is_valid():
            itemsbform.save()
            return HttpResponse("申报提交成功！")
    return render(request,'apply1.html',locals())

def apply1(request):
    return render_to_response('apply1.html')

import datetime
def current_datetime(request):
    now = datetime.datetime.now()
    templateHtml='time_now.html'
    data = {'now':str(now)}
    return  render_to_response(templateHtml,data)


def userlist(request):
    object_list = models.User.objects.all()
    data = {'object_list':object_list}
    templateHtml =  'userlist.html'
    return  render_to_response(templateHtml,data)

def insert_user(request):
    p1 = models.User(username='yqn')
    p1.save()
    html="<html><body>It is now %s.</body></html>" %'insert success!'
    return HttpResponse(html)

def home(request):
    return HttpResponse('SYSTEMA DE CLIENTES')

# def show_user(request):
#     data = {}
#     data['user_list']=Cliente.objects.all()
#     return render(request,'userlist.html',data)

# def cliente_create1(request):
# #     form = ClientForm(request.POST or None)
# #
# #     if form.is_valid():
# #         form.save()
# #         return redirect('user_list')
# #     return render(request,'cliente_novo.html',{'form':form})
#
# def  cliente_update(request,pk):
#     cliente = Cliente.objects.get(id=pk)
#
#     form = ClientForm(request.POST or None,instance=cliente)
#     if form.is_valid():
#         form.save()
#         return redirect('clienta_lista')
#     return render(request,'cliente_detali.html',{'object': cliente})

def show_user(request):
    data = {}
    data['user_list'] = User.objects.all()
    return  render(request,'userlist.html',data)

def create_user(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            userform.save()
            # return redirect('user_list')
            # return HttpResponse('创建成功！')
            return HttpResponseRedirect("/app/show_user")
    else:
        userform = UserForm()
    return  render(request,'user_ca.html',locals())

def user_del(request,pk):
    data = User.objects.get(id=pk)

    print('form=',data.username)
    if request.method == 'GET':
       data.delete()
       print('form1=', data.username)
       return redirect('user_list')
    return render(request,'userlist.html',{'object': data })

def user_update(request,pk):
    data = User.objects.get(id=pk)
    form = UserForm(request.POST or None, instance=data)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/app/show_user")
    return render(request,'user_update.html',{'form':form,'object':data})


