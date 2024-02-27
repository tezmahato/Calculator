from django.shortcuts import render

# Create your views here.
def calculator(request):
    try:
        if request.method=='POST':
            express=request.POST['expression']
            print(express)
            result=eval(express)
        else:
            result=0
    except Exception as e:
        return render(request,'calculator.html',{'result':"Ivalid expression"})

        
    
    return render( request,'calculator.html',{'result':result})