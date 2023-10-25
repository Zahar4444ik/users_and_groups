from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import CustomGroup, CustomUser
from django.shortcuts import get_object_or_404
from .forms import UserForm, GroupForm
from django.contrib import messages


def users(request):
    all_users = CustomUser.objects.all()
    return render(request, 'users.html', {'users': all_users})


def groups(request):
    all_groups = CustomGroup.objects.all()
    return render(request, 'groups.html', {'groups': all_groups})


def add_user(request):
    all_groups = CustomGroup.objects.all()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ('New user was added!'))
            return redirect('users')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in field '{field}': {error}")
    return render(request, 'add_user.html', {'groups': all_groups})


def edit_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    all_groups = CustomGroup.objects.all()
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, ('Editing saved!'))
            return redirect('users')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in field '{field}': {error}")
            return render(request, 'edit_user.html', {'user': user, 'groups': all_groups})
    return render(request, 'edit_user.html', {'user': user, 'groups': all_groups})


def delete_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    if request.method == 'POST':
        user.delete()
        messages.success(request, f'{user.username} deleted successfully.')

        return redirect('users')
    return render(request, 'delete_user.html', {'user': user})


def add_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New group was added!')
            return redirect('groups')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in field '{field}': {error}")
    return render(request, 'add_group.html', {})


def edit_group(request, group_id):
    group = get_object_or_404(CustomGroup, id=group_id)
    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            messages.success(request, ('Editing saved!'))
            return redirect('groups')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in field '{field}': {error}")
    return render(request, 'edit_group.html', {'group': group})


def delete_group(request, group_id):
    group = get_object_or_404(CustomGroup, id=group_id)
    if request.method == 'POST':
        group.delete()
        messages.success(request, f'{group.name} deleted successfully.')

        return redirect('groups')
    return render(request, 'delete_group.html', {'group': group})

#TODO: Pagination