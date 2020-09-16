from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import json
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html', {})

@login_required
def room(request):
    return render(request, 'room.html', {
        # 'room_name_json': mark_safe(json.dumps(room_name)),
        'username': mark_safe(json.dumps(request.user.username)),
    })

def jelly(request):
    return render(request, 'jelly.html')
