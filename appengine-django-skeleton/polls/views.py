# Copyright 2015 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from consult import hello
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.mail import EmailMessage
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
import datetime

#django.db.models.query.RawQuerySet

from polls.models import Vehiculo

def index(request):
   return HttpResponse("HOLA")

def prueba(request):

	a ="HOLA3"
	return HttpResponse(a)


def vehiculo_list(request):
	#vehiculos = Vehiculo.objects().all()
	#html = "Hi %s" % vehiculos
	your_string=""
	your_string += 'Hi'.join([str(V.inf_auto) for V in Vehiculo.objects.all()])

	return HttpResponse(your_string)
	#print vehiculos

	#return HttpResponse("Hi " + vehiculos)

def param_get(request, username=None):

	#your_string = ""
	#your_string += '-'.join([str(param)])

	#a = param
	message = request.GET.get('message', 'Mensaje')
	#your_string = '-'.join([str(message)])
	return HttpResponse("MSN: " + username + " => " + message)






def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


