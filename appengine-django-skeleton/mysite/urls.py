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

from django.conf.urls import patterns, include
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin

from polls.views import index
from polls.views import prueba
from polls.views import vehiculo_list
from polls.views import current_datetime
from polls.views import param_get

urlpatterns = [
    url(r'^$', index),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^prueba/$', prueba),
    url(r'^veh/$', vehiculo_list),
    url(r'^time/$', current_datetime),
    url(r'^user/(?P<username>\w{1,50})/$', param_get)
]
