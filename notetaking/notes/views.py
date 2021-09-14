from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import *


# Create your views here.


def index(request):
    notes = Note.objects.all()
    context = {
        'notes': notes
    }

    return render(request, 'index.html', context)


def note_detail(request, id):
    note = Note.objects.get(id=id)
    context = {
        'note_detail': note

    }
    return render(request, 'note_detail.html', context)


def edit_note(request, id):
    note = Note.objects.get(id=id)
    context = {
        'note_detail': note

    }
    return render(request, 'student_dashboard.html', context)


def delete_note(request, id):
    note = Note.objects.get(id=id)
    context = {
        'note_detail': note

    }
    return render(request, 'student_dashboard.html', context)


def student_dashboard(request):
    if request.method == 'POST':
        title = request.POST['title']
        subject = request.POST['subject']
        note_desc = request.POST['note_desc']
        is_private = request.POST.get('is_private', None)

        user = request.user
        student = Student.objects.filter(user=user).first()
        if is_private == 'private':
            result = True
        else:
            result=False
        res = Note.objects.create(
            student=student,
            note_title=title,
            subject=subject,
            note_desc=note_desc,
            is_private=result

        )

        print(res)

        return render(request, 'student_dashboard.html')

    try:
        student = Student.objects.get(user=request.user)
    except Exception as e:
        print(e)

    notes = Note.objects.filter(student=student)
    context = {
        'notes': notes
    }
    return render(request, 'student_dashboard.html', context)

def login_attempt(request):
    if request.method == 'POST':
        # print('method is post')
        # print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')

        # print('username is ', username)
        # print('password is ', password)


        user = User.objects.filter(username=username).first()

        if user is None:
            context = {'message': 'User is not registered'}
            return render(request, 'login.html', context)
        else:
            student = Student.objects.filter(user=user).first()
            if student:
                user = authenticate(username=username, password=password)
                print('user is ', user)
                if user is None:
                    context = {'message': 'Wrong password'}
                    return render(request, 'login.html', context)
                else:
                    login(request, user)
                    return redirect('/student_dashboard')
            else:
                context = {'message': 'User is not authorized'}
                return render(request, 'login.html', context)

    return render(request, 'login.html')


def logout_attempt(request):
    request.session.profile = None
    request.session.customer_session = None
    logout(request)
    return redirect('/')


def register_attempt(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.filter(username=username).first()
        # list_of_users = [
        #     {
        #         'user1': {
        #             'name': 'Raahim',
        #             'age': 25
        #         }
        #     },
        #     {
        #         'user2': {
        #             'name': 'Ali',
        #             'age': 25
        #         }
        #     }
        #
        # ]

        # SELECT * FROM students WHERE name = 'Raahim';
        if user:
            context = {'message': 'User already registered'}
            return render(request, 'register.html', context)
        else:
            user = User(username=username, email=email)
            user.set_password(password)
            user.save()
            Student.objects.create(
                user=user,
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone_number=phone_number,
            )
            context = {'message': 'User registered'}

            return render(request, 'register.html', context)
    return render(request, 'register.html')
