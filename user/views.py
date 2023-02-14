import logging

from django.contrib import messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404

from user.forms import UserForms
from user.models import CustomUser
logger = logging.getLogger(__name__)

def view_all_users(request):
    p = Paginator(CustomUser.objects.all(), 8)
    page = request.GET.get('page')
    users = p.get_page(page)
    context = {'users': users}
    return render(request, 'user/allusers.html', context)


def view_user_profile(request):
    user = User.objects.get(username=request.user)
    custom_user = CustomUser.objects.get(user=user)
    context = {'custom_user': custom_user}
    return render(request, 'user/userdetails.html', context)


def view_user_profile_id(request, id):
    custom_user = CustomUser.objects.get(id=id)
    context = {'custom_user': custom_user}
    return render(request, 'user/userdetails.html', context)

def update_user(request, id):

    if request.method == 'POST':
        user =get_object_or_404(CustomUser, id=id)
        # user = CustomUser.objects.filter(id=id)
        form = UserForms(request.POST or None, request.FILES,instance=user)

        if form.is_valid():
            form.save()
            messages.success(request, "Updated successfully")
            return redirect('view_books')

            # CustomUser.objects.filter(id=id).update(
            # first_name= request.POST['first_name'],
            # last_name = request.POST['last_name'],
            # phone = request.POST['phone'],
            # street = request.POST['street'],
            # city = request.POST['city'],
            # state = request.POST['state'],
            # zip_code = request.POST['zip_code'],
            # image = request.FILES['image']
        # )

    # messages.success(request, "Updated successfully" )
    return redirect('view_user_profile')

def user_details_admin(request, id):
    custom_user = CustomUser.objects.get(id=id)
    context = {'custom_user': custom_user}
    return render(request, 'user/userdetailsadmin.html', context)

def change_user_state(request, id):

    custom_user = get_object_or_404(CustomUser, id=id)
    if custom_user.user.is_active:
        custom_user.user.is_active = False
        logger.warning('User is deactivated')
    else:
        custom_user.user.is_active = True
        logger.warning('User is activated')
    custom_user.user.save()
    return redirect('view_all_users')

