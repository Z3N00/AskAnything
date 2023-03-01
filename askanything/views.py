from django.http import HttpResponse
from django.shortcuts import render
import requests
import json
import creds

headers = {
"content-type": "application/json",
"X-RapidAPI-Key": creds.key,
"X-RapidAPI-Host": "you-chat-gpt.p.rapidapi.com"
}


def index(request):
    return render(request, 'index.html')

def result(request):
    question = request.POST.get('text', 'Please ask me something')
    
    
    payload = {
	"question": str(question),
	"max_response_time": 30
    }
    response = requests.request("POST", creds.url, json=payload, headers=headers)
    
    answer = json.loads(response.text)
    # print(type(answer))
    print(answer)
    params = {'question': question, 'answer': answer['answer']}
    return render(request, 'result.html', params)
