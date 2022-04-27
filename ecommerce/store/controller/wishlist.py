from multiprocessing import context
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages

from store.models import Wishlist

from django.contrib.auth.decorators import login_required

@login_required(login_url='loginpage')
def index(request):
    wishlist = Wishlist.objects.filter(user=request.user)
    context={'wishlist': wishlist}
    return render(request,'store/wishlist.html', context)
