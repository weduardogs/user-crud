import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from ..services.impl.user_service_impl import UserImpl
import logging


@csrf_exempt
def get_user_by_id(request, id):
    if request.method == 'GET':
        response = UserImpl.get_by_id(id)
        if "error" in response:
            return JsonResponse({'error': response.get('error')}, status=500)
        else:
            return JsonResponse(response, status=200, safe=False)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)


@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        response = UserImpl.create(json.loads(request.body))
        if "error" in response:
            return JsonResponse({'error': response.get('error')}, status=500)
        else:
            return JsonResponse(response, status=200, safe=False)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    

@csrf_exempt
def update_user(request, id):
    if request.method == 'PUT':
        response = UserImpl.update(json.loads(request.body), id)
        if "error" in response:
            return JsonResponse({'error': response.get('error')}, status=500)
        else:
            return JsonResponse(response, status=200,  safe=False)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)    
    

@csrf_exempt
def delete_user(request, id):
    if request.method == 'DELETE':
        response = UserImpl.delete(id)
        if "error" in response:
            return JsonResponse({'error': response.get('error')}, status=500)
        else:
            return JsonResponse(response, status=200, safe=False)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)    
    
@csrf_exempt
def get_active_users(request):
    if request.method == 'GET':
        response = UserImpl.getAllActive()
        return JsonResponse(response, status=200, safe=False)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)    
    
@csrf_exempt
def get_all_users(request):
    if request.method == 'GET':
        response = UserImpl.get_all()
        return JsonResponse(response, status=200,  safe=False)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)        





