from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from account.models import Profile
from leave.models import Leave
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Count

# Create your views here.
def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        role = request.POST['role']
        user = User.objects.create_user(username=username, password=password)
        Profile.objects.create(user=user, role=role)
        return redirect('login')
    return render(request, 'register.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if user.profile.role == 'admin':
                return redirect('admin_dashboard')
            else:
                return redirect('staff_dashboard')
    return render(request, 'login.html')

@login_required
def admin_dashboard(request):
    if request.user.profile.role != 'admin':
        return redirect('staff_dashboard')
    
    # ===== REAL-TIME DATA INSIGHTS =====
    total_staff = User.objects.filter(profile__role='staff').count()
    total_leaves = Leave.objects.count()
    pending_leaves = Leave.objects.filter(status='Pending').count()
    approved_leaves = Leave.objects.filter(status='Approved').count()
    rejected_leaves = Leave.objects.filter(status='Rejected').count()
    recent_leaves = Leave.objects.order_by('-start_date')[:5]
    
    context = {
        'total_staff': total_staff,
        'total_leaves': total_leaves,
        'pending_leaves': pending_leaves,
        'approved_leaves': approved_leaves,
        'rejected_leaves': rejected_leaves,
        'recent_leaves': recent_leaves,
    }
    
    return render(request, 'admin_dashboard.html', context)

@login_required
def staff_dashboard(request):
    return render(request, 'staff_dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def manage_staff(request):
    if request.user.profile.role != 'admin':
        return redirect('staff_dashboard')
    staff_list = User.objects.filter(profile__role='staff')
    return render(request, 'accounts/manage_staff.html', {'staff_list': staff_list})

@login_required
def add_staff(request):
    if request.user.profile.role != 'admin':
        return redirect('staff_dashboard')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(
            username=username,
            password=password
        )
        Profile.objects.create(
            user=user,
            role='staff'
        )
        return redirect('manage_staff')
    return render(request, 'accounts/add_staff.html')

@login_required
def edit_staff(request, id):
    if request.user.profile.role != 'admin':
        return redirect('staff_dashboard')
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        user.username = request.POST['username']
        if request.POST.get('password'):
            user.set_password(request.POST['password'])
        user.save()
        return redirect('manage_staff')
    return render(request, 'accounts/edit_staff.html', {'staff': user})

@login_required
def delete_staff(request, id):
    if request.user.profile.role != 'admin':
        return redirect('staff_dashboard')
    user = get_object_or_404(User, id=id)
    user.delete()
    return redirect('manage_staff')

