from django.shortcuts import render


# Create your views here.
def admin_index(request):
    return render(request, 'blogadmin/admin_root.html')
