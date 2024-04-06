from django.http import HttpResponse , JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.template import loader
from myapp.models import Ticket
from django.conf import settings  
from django.core.serializers import serialize  # include this
import json# include this
from myapp.forms import AppForm


def check_session(view_func):
    def wrapped_view(request, *args, **kwargs):
        # Perform session checking logic here
        print()
        # if not request.session.get('username'):
        if 'username' not in request.COOKIES:
            # return HttpResponseForbidden("Session not valid. Please log in.")
            return redirect('login')
        return view_func(request, *args, **kwargs)
    return wrapped_view


@require_http_methods(['POST'])
@csrf_exempt
@check_session
def ticket(request):
    try: 
        # Access form data from POST request
        form_data = request.POST
        # Access uploaded files from POST request
        files_data = request.FILES

        # Do something with the form data and files
        # For example, you can access form fields by name:
        subject = form_data.get('subject')
        discription = form_data.get('discription')
        ticket_type = form_data.get('ticket_type')
        comment = form_data.get('comment')
        active = form_data.get('active')
        if active == 'on':
            active = True
        else: 
            active = False
        print(form_data)
        mem = Ticket(subject = subject,discription = discription, ticket_type=ticket_type, comment=comment, active= active)
        mem.full_clean()
        mem.save()
        return JsonResponse({'message' : 'context'}, status = 200)
    except Exception as e :
        print(e)
        return JsonResponse({'message' : 'ERROR in updatedelete'}, safe=False, status = 500)  