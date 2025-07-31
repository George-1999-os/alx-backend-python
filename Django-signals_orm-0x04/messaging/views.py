from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth.models import User

@login_required
def delete_user(request):
    """Allow logged-in user to delete their own account."""
    if request.method == "POST":
        request.user.delete()
        return redirect('home')  # or your logout/homepage URL
    return redirect('profile')  # or wherever appropriate
