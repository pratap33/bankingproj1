from django.shortcuts import render
from django.views.generic import View
from .models import user1
class Homepage(View):
    def get(self,request):
        return render(request, 'homepage.html')
class Loginpage(View):
    def get(self,request):
        return render(request, 'loginpage.html')
class Loginpage1(View):
    def get(self,request):
        return render(request, 'loginpage1.html')
class Showpage(View):
    def post(self,request):
        return render(request, 'showpage.html')
def insert(request):
    try:
         rec=user1.objects.filter(uname=request.POST['t1'],pwrd=int(request.POST['t2']))
    except user1.DoesNotExist :
        return render(request, 'errorpage.html')
    except ValueError:
        return render(request, 'errorpage.html')
    else:
        return render(request, 'showpage.html', {'records': rec})
def function(request):
    try:
        rec = user1.objects.filter(uname=request.GET['t1'], pwrd=request.GET['t2'])
    except user1.DoesNotExist :
        return render(request, 'errorpage1.html')
    except ValueError:
        return render(request, 'errorpage1.html')
    else:
        return render(request, 'showpage1.html', {'records': rec})
def split(request):
    rec = user1.objects.filter(uname=request.POST['t6'])
    for p in rec:
        a = p.actbal
    fname = request.POST['t3']
    samt= int(request.POST['t4'])
    fnum = int(request.POST['t5'])
    if (a >= samt):
        a=a-samt
        user1.objects.filter(uname=request.POST['t6']).update(actbal=a,splitbal=samt,paidto=fname,facnum=fnum)
        re = user1.objects.filter(uname=request.POST['t6'])
        return render(request, 'outlook.html', {'record': re})
    else:
        return render(request, 'errorpage1.html')

