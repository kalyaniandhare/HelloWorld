from django.shortcuts import render
from .models import Extractore, StoreData
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import UserForm
from django.shortcuts import redirect
from extractore import task
from django.contrib.auth.decorators import login_required

#@login_required
#def login_view(request):

@login_required
def home(request):
    return render(request, 'extractore/base.html')

@login_required
def show_user(request):
    data = Extractore.objects.all()
    return render(request, 'extractore/show_user.html',{'data1' : data})


@login_required
def userdata(request, pk):

    data = get_object_or_404(StoreData, pk=pk)
    print("user_data",data)
    return render(request, 'extractore/user_data.html', {'d': data})

@login_required
def user_detail(request, pk):

    data = get_object_or_404(Extractore, pk=pk)
    return render(request, 'extractore/user_detail.html', {'data': data})

@login_required
def user_edit(request,pk):

    print(request.method,pk)
    if request.method == "GET":
        user = Extractore.objects.get(pk=pk)
        print(user)
        form = UserForm(instance=user)
        #data = get_object_or_404(Extractore, pk=pk)
        return render(request,'extractore/user_edit.html', {'form': form})



def dashbord(request):

    return render(request,'extractore/dashbord.html')

@login_required
def new_user(request, pk= None):
    if request.method == "POST":
        form = UserForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.published_date = timezone.now()
            user.save()
            user_data = task.get_data(user.email_id,user.password)
            #return render(request, 'extractore/user_data.html',{'d' : user_data})
            return redirect('userdata', pk=user_data.pk)
    else:
        user = Extractore.objects.get(pk=pk) if pk else None
        form = UserForm(instance=user)

    return render(request,'extractore/user_edit.html', {'form':form})
