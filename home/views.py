from django.shortcuts import render,get_object_or_404
from home.models import Method
from django.db.models import Q

# Create your views here.
def index(request):
    query=request.GET.get('q')
    if query:
        query=query.title()
        print(query)
        methods=Method.objects.filter(Q(name__icontains=query))

    else:
        methods=Method.objects.all()

    return render(request,'home/index.html',locals())


def method_detail(request,slug):
    method=get_object_or_404(Method,slug=slug)
    return render(request,'home/method_detail.html',locals())
from home.forms import OrderForm
from django.contrib import auth

def order(request,slug):
    method = get_object_or_404(Method, slug=slug)

    user = auth.get_user(request)
    if request.method=='POST':
        form=OrderForm(data=request.POST,initial={'method':method,'author':user})
        if form.is_valid():
            new_comment=form.save(commit=False)
            new_comment.method=method
            new_comment.author=user

            print(new_comment)
            new_comment.save()
            return render(request,'home/order_complated.html')
    else:
        form=OrderForm(initial={'method':method,'author':user})
    return render(request,'home/method_order.html',locals())