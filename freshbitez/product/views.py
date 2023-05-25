from django.shortcuts import render,redirect
from .models import products,comments

# Create your views here.
def product(request):
    data=products.objects.all()
    
    return render(request,"products.html",{"data":data})

def details(request):
    id1=request.GET["id"]
    data1=products.objects.get(id=id1)
    p=data1
    if p.discount is not None:
        disc=p.orgprice*p.discount/100
        price=p.orgprice-disc

    return render(request,"details.html",{"data1":data1,"price":price})


def commentsub(request):
    if request.method=="POST":
        message=request.POST["comment"]
        usr=request.POST["user"]
        id=request.POST["proid"]
        
        cmt=comments.objects.create(name=usr,msg=message,pro_id=id)
        cmt.save();
        return redirect("/product/details/?id="+str(id))
    
    else:
        return render(request,"details.html")
    
    