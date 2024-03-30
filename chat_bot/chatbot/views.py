from django.shortcuts import render
from django.http import JsonResponse


def home(request):
    if request.method == 'POST':
        user_message = request.POST.get('message')
        bot_response = get_bot_response(user_message)
        return JsonResponse({'response' : bot_response})
    return render(request, 'home.html')


def get_bot_response(user_message):
    return f'{user_message}'