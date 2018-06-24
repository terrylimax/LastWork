from django.shortcuts import render, redirect
# from django.contrib import sessions
from .forms import LoginForm, RegistrationForm
import requests


def Login(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        token = requests.post('http://127.0.0.1:8000/get_token/', data={'username': username, 'password': password})
        request.session['token'] = token.json()['token']
        request.session['username'] = username
        return redirect('http://127.0.0.1:8080/getlists/')
    return render(request, 'login.html', {'form': form})


def Registration(request):
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        last_name = request.POST['last_name']
        first_name = request.POST['first_name']
        response = requests.post('http://127.0.0.1:8000/users/register/',
                                 data={'username': username, 'email': email, 'password': password,
                                       'last_name': last_name, 'first_name': first_name}).json()
        return redirect('http://127.0.0.1:8080/login/')
    return render(request, 'registr.tpl', {'form': form})


def Activate(request, activation_key):
    return render(request, 'activate.tpl')


def GetLists(request):
    if request.method == 'POST':
        title = request.POST['title']
        friend = request.POST['friend']
        if 'token' in request.session:
            header = {'Authorization': 'Token ' + request.session['token']}
            response = requests.post('http://127.0.0.1:8000/todolists/', data={'name': title,
                                                                               'friend': friend}, headers=header).json()
    lists = []
    if 'token' in request.session:
        header = {'Authorization': 'Token ' + request.session['token']}
        response = requests.get('http://127.0.0.1:8000/todolists/', headers=header)
        lists = response.json()
    else:
        return 'Авторизуйся'
    return render(request, 'getlists.tpl', {'lists': lists, 'header': 'Task lists'})


def ListDetails(request, list_id):
    if request.method == 'POST':
        friend = request.POST['friend']
        title = request.POST['title']
        if 'token' in request.session:
            header = {'Authorization': 'Token ' + request.session['token']}

            response = requests.put('http://127.0.0.1:8000/todolists/' + str(list_id) + '/',
                                    data={'name': title, 'friend': friend}, headers=header).json()
    details = []
    if 'token' in request.session:
        header = {'Authorization': 'Token ' + request.session['token']}
        user = request.session['username']
        response = requests.get('http://127.0.0.1:8000/todolists/' + str(list_id) + '/', headers=header)
        details = response.json()
    else:
        return 'Авторизуйся'
    return render(request, 'listdetails.tpl', {'details': details, 'header': 'Task list details', 'user':user})


def ListDelete(request, list_id):
    if 'token' in request.session:
        header = {'Authorization': 'Token ' + request.session['token']}
        response = requests.delete('http://127.0.0.1:8000/todolists/' + list_id + '/', headers=header)
    return redirect('http://127.0.0.1:8080/getlists/')


def GetTasks(request, list_id):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        completed = request.POST.get('completed', False)
        if completed:
            completed = True
        due_date = request.POST['due_date']
        priority = request.POST['priority']
        tags = request.POST['tags']
        #tags = tags.split()
        #print(tags)
        if 'token' in request.session:
            header = {'Authorization': 'Token ' + request.session['token']}
            response = requests.post('http://127.0.0.1:8000/todolists/' + str(list_id) + '/tasks/',
                                     data={'name': title, 'description': description,
                                           'priority': priority, 'completed': completed,
                                           'tags': tags, 'due_date': due_date}, headers=header).json()
    tasks = []
    if 'token' in request.session:
        header = {'Authorization': 'Token ' + request.session['token']}
        response = requests.get('http://127.0.0.1:8000/todolists/' + str(list_id) + '/tasks/', headers=header)
        tasks = response.json()
    else:
        return 'Авторизуйся'
    return render(request, 'gettasks.tpl', {'tasks': tasks, 'header': 'Tasks', 'list_id': str(list_id)})

def ShareGetTasks(request, list_id):
    tasks = []
    if 'token' in request.session:
        header = {'Authorization': 'Token ' + request.session['token']}
        response = requests.get('http://127.0.0.1:8000/todolists/' + str(list_id) + '/tasks/', headers=header)
        tasks = response.json()
    else:
        return 'Авторизуйся'
    return render(request, 'sharegettasks.tpl', {'tasks': tasks, 'header': 'Tasks', 'list_id': str(list_id)})


def TaskDetails(request, list_id, task_id):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        completed = request.POST.get('completed', False)
        if completed:
            completed = True
        due_date = request.POST['due_date']
        priority = request.POST['priority']
        tags = request.POST['tags']
        if 'token' in request.session:
            header = {'Authorization': 'Token ' + request.session['token']}
            response = requests.put('http://127.0.0.1:8000/todolists/' + str(list_id) + '/tasks/' + task_id + '/',
                                    data={'name': title, 'description': description,
                                          'priority': priority, 'completed': completed,
                                          'tags': tags, 'due_date': due_date}, headers=header).json()
    details = []
    if 'token' in request.session:
        header = {'Authorization': 'Token ' + request.session['token']}
        response = requests.get('http://127.0.0.1:8000/todolists/' + str(list_id) + '/tasks/' + str(task_id + '/'),
                                headers=header)
        details = response.json()
    else:
        return 'Авторизуйся'


    return render(request, 'taskdetails.tpl', {'details': details, 'header': 'Task details',
                                               'list_id': str(list_id)},)


def ShareTaskDetails(request, list_id, task_id):
    details = []
    if 'token' in request.session:
        header = {'Authorization': 'Token ' + request.session['token']}
        response = requests.get('http://127.0.0.1:8000/todolists/' + str(list_id) + '/tasks/' + str(task_id + '/'),
                                headers=header)
        details = response.json()
    else:
        return 'Авторизуйся'

    return render(request, 'sharetaskdetails.tpl', {'details': details, 'header': 'Task details',
                                               'list_id': str(list_id)}, )

def TaskDelete(request, list_id, task_id):
    if 'token' in request.session:
        header = {'Authorization': 'Token ' + request.session['token']}
        response = requests.delete('http://127.0.0.1:8000/todolists/' + list_id + '/tasks/' + task_id, headers=header)
    return redirect('http://127.0.0.1:8080/getlists/' + list_id + '/gettasks/')


def GetUsers(request):
    users = []
    if 'token' in request.session:
        header = {'Authorization': 'Token ' + request.session['token']}
        response = requests.get('http://127.0.0.1:8000/users/', headers=header)
        users = response.json()
    else:
        return 'Авторизуйся'
    return render(request, 'getusers.tpl', {'users': users, 'header': 'Users',
                                            'header1': 'First name', 'header2': 'Last name',
                                            'header3': 'E-mail'
                                            })


def Logout(request):
    request.session['token'] = None
    return redirect('http://127.0.0.1:8080/login/')