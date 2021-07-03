from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@api_view(["GET"])
def welcome(request):
    content = {"message": "Minha primeira view em Django!"}
    return JsonResponse(content)



@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def users(request):
    users = [
        {'id':'1','nome':'Paulo Lins','nota1':'3.5','nota2':'8.7', 'media':'6.1','situacao':'APROVADO'},
        {'id':'2','nome':'Lucas Souza','nota1':'8.0','nota2':'7.3', 'media':'7.6','situacao':'APROVADO'},
        {'id':'3','nome':'Pedro Silva','nota1':'5.0','nota2':'5.0', 'media':'5.0','situacao':'RECUPERAÇÃO'},
        {'id':'4','nome':'Ana Lima','nota1':'8.0','nota2':'5.0', 'media':'6.5','situacao':'APROVADO'},
        {'id':'5','nome':'Bruno Freire','nota1':'4.0','nota2':'0', 'media':'2.0','situacao':'RECUPERAÇÃO'},
        {'id':'6','nome':'Maria Silva','nota1':'10.0','nota2':'10.0', 'media':'10.0','situacao':'APROVADO'},
        {'id':'7','nome':'Bruna Santos','nota1':'7.7','nota2':'3.2', 'media':'5.4','situacao':'RECUPERAÇÃO'},

    ]

    return JsonResponse(users, safe=False)
