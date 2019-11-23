from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Search
from .serializers import TapSearchSerializer
from rest_framework.decorators import api_view
from django.contrib import messages


@csrf_exempt
@api_view(['GET', 'POST'])
def TapSearchFunc(request):
    
    if request.method == 'GET':
        Searcher = Search.objects.all()
        serializer = TapSearchSerializer(Searcher, many=True)
        print(serializer.data)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':

        serializer = TapSearchSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            word = serializer.data['word']
            para = serializer.data['paragraph']
            resp = algo(para,word) 
            return JsonResponse(resp, status=201)
        return JsonResponse(serializer.errors, status=404)



def algo(content,word):

    para = []
    para = content.split('\n\n')
    dicti={}
    for j in range(len(para)):
        data=[]
        indexes = []
        data = para[j].split(' ')
        #print(data)
        for i in range(len(data)):
            if word == data[i]:
                indexes.append(i)
        dicti.update({str(j+1):indexes})
    return dicti
                
    
def TapSearchRender(request):
    if request.method == "POST":
        para = request.POST['para']
        word = request.POST['word']
        respo = algo(para,word)
        messages.info(request, respo)
    
    return render(request , 'index.html')