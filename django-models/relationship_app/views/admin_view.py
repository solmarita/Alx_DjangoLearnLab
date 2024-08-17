
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

@login_required
def admin_view(request):
    if request.user.userprofile.role != 'Admin':
        return HttpResponseForbidden("You do not have permission to view this page.")
    return render(request, 'relationship_app/admin_view.html')