from django.shortcuts import render
from django.views import View
from apps.users.models import User
from django.http import JsonResponse
import re
# Create your views here.
class Username(View):
    def get(self,request,username):
        count=User.objects.filter(username=username).count()
        if not re.match('[a-zA-Z_-]{5,20}',username):
            return JsonResponse({'code': 200,'errmsg': 'The parameter is not satisfied'})
        return JsonResponse({'code':0,'count':count,'errmsg':'ok'})
        pass
