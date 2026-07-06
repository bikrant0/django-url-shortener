from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ShortenURL
from django.shortcuts import render, redirect, get_object_or_404
import random
import string

def generate_short_alias():
    allowed_chars = string.ascii_letters + string.digits
    
    random_list = random.choices(allowed_chars, k=6)
    final_string = "".join(random_list)
    
    return (final_string)

    
@api_view(['POST'])
def create_short_url(request):
    long_url= request.data.get('original_url')
    my_new_alias = generate_short_alias()
    
    ShortenURL.objects.create(original_url = long_url, short_url = my_new_alias)
    
    return Response({
        "message": "Success",
        "original_url" : long_url,
        "short_url" : f"http://localhost:8000/{my_new_alias}"
    })
    
@api_view(['GET'])
def redirect_url(request, short_alias):
    url_object = get_object_or_404(ShortenURL, short_url=short_alias)
    url_object.usage_count += 1
    url_object.save()
    
    return redirect(url_object.original_url)
    