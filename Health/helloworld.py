"""from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello world ! ")"""


from django.shortcuts import render

def hello(request):
    context          = {}
    context['hello'] = 'Hello World - test'
    return render(request, 'hello.html', context)
    "return render(request, 'webchat/booking_form.html', context)"