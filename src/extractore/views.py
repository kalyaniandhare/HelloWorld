from django.shortcuts import render
from .models import Extractore, StoreData
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import UserForm
from django.shortcuts import redirect
from extractore import task
 
def show_user(request):
    data = Extractore.objects.all()
    value = task.get_data(data)
    user= StoreData()
    user.username = value[0]['username']
    user.useremailid = value[0]['useremailid']
    user.email_from = value[0]['email_from']
    user.email_to =  value[0]['email_to']
    user.date = value[0]['date']
    user.subject = value[0]['subject']
    user.filename = value[0]['filename']
    user.filedata = value[0]['filedata']
    user.save()
    print(value)
    return render(request, 'extractore/show_user.html',{'data' : data})



def user_detail(request, pk):

    data = get_object_or_404(Extractore, pk=pk)
    return render(request, 'extractore/user_detail.html', {'data': data})

def new_user(request):
    
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.published_date = timezone.now()
            print(user)
            user.save()
            return redirect('user_detail', pk=user.pk)
    else:
        form = UserForm()
    return render(request,'extractore/user_edit.html', {'form':form})
