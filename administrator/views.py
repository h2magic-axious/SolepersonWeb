from django.shortcuts import render


# Create your views here.
def admin_index(request):
    return render(request, 'blogadmin/admin_root.html', context={
        'admin_position': 'Test Admin Page',
        'breadcrumb_list': ['2021', '01', '19']
    })
