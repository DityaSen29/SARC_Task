from django.shortcuts import render, redirect

def home(request):
    if request.method == 'POST':
        choice = request.POST.get('choice')
        if choice == 'yes':
            return redirect('congrats')
        else:
            return redirect('try_again')
    return render(request, 'poll/home.html')

def congrats(request):
    return render(request, 'poll/congrats.html')

def try_again(request):
    return render(request, 'poll/try_again.html')
