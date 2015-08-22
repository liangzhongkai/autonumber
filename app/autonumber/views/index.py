#coding:utf-8
from django.shortcuts import render_to_response,render,get_object_or_404  
from django.http import HttpResponse, HttpResponseRedirect  
from django.contrib.auth.models import User  
from django.contrib import auth
from django.contrib import messages
from django.template.context import RequestContext

from django.forms.formsets import formset_factory
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from bootstrap_toolkit.widgets import BootstrapUneditableInput
from django.contrib.auth.decorators import login_required

"""
登录相关
"""
#登陆成功
@login_required
def index(request):
	username = request.session.get('username','')
	return render_to_response('index.html', RequestContext(request, {'username': username, 'has_permission':True, 'site_url':True, 'docsroot':''}))