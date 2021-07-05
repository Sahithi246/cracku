from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
	list1=[]
	for i in range(1,51):
		list1.append(i)
	context={
	"data":list1
	}
	return render(request,'home.html',context)

def factor(request):
	list2=[]
	num1=int(request.GET['num1'])
	for i in range(1,num1+1):
		if(num1%i==0):
			list2.append(num1)

	context2={
	"data2":list2
	}



	return render(request,'result.html',{'result':ls})

def home2(request):
    return render(request, 'home2.html')