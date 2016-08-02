# Copyright 2015 Google Inc.
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


from django.shortcuts import render
from django.http import HttpResponse
from collections import namedtuple
import json

import polls.forms_obu as FRMS
def index(request):
   return HttpResponse("HOLA")

def prueba(request):
	a  = '{"name": "John Smith", "hometown": "New York"}'
	dec_a=json.loads(a)
	return HttpResponse(dec_a['name'])

def complete_decode(request):
	data = request.POST.get('data')
	#your_string = '-'.join([str(message)])
	dec_data= json.loads(data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
	str_data=""
	for Obj in dec_data:
		str_data+="\n"+str(Obj)
	return HttpResponse(str_data)

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

def form_send(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FRMS.NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/param_post/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = FRMS.NameForm()

    return render(request, 'name.html', {'form': form})


def param_post(request):

	#your_string = ""
	#your_string += '-'.join([str(param)])

	#a = param
	username = request.POST.get('username')
	#your_string = '-'.join([str(message)])
	return HttpResponse("MSN: " + username )






def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


