from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    return render(request, 'home.html', {'name': 'Thwe Yamin Aye'})
def web2(request):
    book = {'a':[{'name':"Algorithm Analysis",'price':'$25'},
                 {'name':"Arts",'price':'$20'},
                 {'name':"Accounting",'price':'$23'}],
            'b':[{'name':"Background Research",'price':'$24'},
                 {'name':"Business Strategy",'price':'$23'},
                 {'name':"Biology",'price':'$22'}],
            }
    bookname = request.POST['book']
    result = bookname.lower()
    result = book[result[0]]
    return render(request, 'find.html', {'result': result})