from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render,redirect,HttpResponse
from  django.urls import reverse
from home import models
class UserAuth(MiddlewareMixin):
    def process_request(self,request):
        white_list = [
            reverse('login'),
            reverse('register'),
            reverse('index')
        ]
        if request.path in white_list:
            return
        user_id = request.session.get('user_id')
        if user_id:
            request.user_obj = models.UserInfo.objects.filter(id = request.session.get('user_id')).first()
            return
        else:
            return redirect('login')