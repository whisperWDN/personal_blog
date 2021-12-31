from django.shortcuts import render
from .models import Author
from .serializers import AuthorSerializer


# Create your views here.
def author_register(request):
    if request.method == 'GET':
        return render(request, 'author/register.html', {})
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        realname = request.POST.get('realname')
        authors = Author.objects.filter(username=username)
        if len(authors) > 0:
            return render(request, 'author/register.html', {'msg_code': 0, 'msg_info': '账号已经存在，请使用其他账号注册'})
        author = Author(username=username, password=password, realname=realname)
        author.save()
        return render(request, 'author/login.html', {'msg_code': 0, 'msg_info': '账号注册成功'})


def author_login(request):
    if request.method == "GET":
        return render(request, 'author/login.html', {})
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            author = Author.objects.get(username=username, password=password)
            serializers = AuthorSerializer(author, many=False)
            request.session['author'] = serializers.data

            return render(request, 'author/index.html', {'msg_code': 0, 'msg_info': '登陆成功'})
        except:
            return render(request, 'author/login.html', {'msg_code': -1, 'msg_info': '密码有误，请重新登录'})
