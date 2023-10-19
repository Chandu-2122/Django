from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth.models import auth
from .models import Election, Candidate, VotedOrNot, Vote
from django.contrib.auth.decorators import login_required



def register_view(request):
    messages = []
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']
        
        if password == confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.append('Username already exists.')
            elif User.objects.filter(email=email).exists():
                messages.append('Email already exists.')
            else:
                user = User(username=username, email=email, password=password)
                user.set_password(password)
                user.save()
                messages.append('User details registered successfully.')
                return render(request, 'live_image_capture.html')
        else:
            messages.append('Passwords did not match.')

    return render(request, 'signup.html', {'custom_messages': messages})
    

def login_view(request):
    messages = []
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            try:
                voted_or_not = VotedOrNot.objects.get(User = user)
                if voted_or_not.Has_voted:
                    messages.append('You have already voted.')
                    auth.logout(request)
                    return redirect('home')
                else:
                    return redirect('voting')
            except VotedOrNot.DoesNotExist:
                return redirect('voting')
        else:
            messages.append('Invalid credentials')
        
    return render(request, 'login.html', {'custom_messages': messages})





def home_view(request):
    return render(request, 'index.html')

def logout_view(request):
    return render(request, 'logout.html')



def live_image_capture_view(request):
    return render(request, 'live_image_capture.html')



@login_required
def voting_view(request):
    messages = []
    user = request.user
    voted_or_not = VotedOrNot.objects.filter(User=user).first()

    if voted_or_not and voted_or_not.Has_voted:
        messages.append('You have already voted')
        auth.logout(request)

        return render(request, 'logout.html')

    if request.method == 'POST':
        selected_candidate = request.POST.get('selected_candidate')

        if selected_candidate:
            try:
                candidate = Candidate.objects.get(Name=selected_candidate)
            except Candidate.DoesNotExist:
                messages.append('The selected candidate does not exist.')
                return render(request, 'voting.html')
            vote, created = Vote.objects.get_or_create(Candidate=candidate)
            vote.Vote_count += 1
            vote.save()
            if not voted_or_not:
                voted_or_not = VotedOrNot(User=user)
            voted_or_not.Has_voted = True
            voted_or_not.save()

            messages.append('Your vote has been counted.')
            auth.logout(request)
            return render(request, 'logout.html',  {'custom_messages': messages})

        else:
            error_message = "Please select a candidate"
            return render(request, 'voting.html', {'custom_messages': messages})

    else:
        election = Election.objects.filter(Is_active=True).first()
        candidates = Candidate.objects.all()
        data = {'election': election, 'candidates': candidates}
        return render(request, 'voting.html', data)

        
            

def results_view(request):
    return render(request, 'results.html')

def help_view(request):
    return render(request, 'help.html')