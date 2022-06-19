from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signup_view(request):
    if request.method == "post":
        form = UserCreationForm(request.post)
        if form.is_valid():
            form.save()
            # login
            return redirect('articles:list')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form':form})
