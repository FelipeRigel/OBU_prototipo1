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

from django.db import models



class Vehiculo(models.Model):
	id = models.IntegerField(primary_key=True, null=False) # Hash function de la matricula
	nivel_tecn = models.IntegerField(null=False) # Nivel de tecnificaciOn
	sensor_1 = models.FloatField(null=False) 
	sensor_2 = models.FloatField(null=False)
	sensor_3 = models.FloatField(null=False)
	inf_auto = models.CharField(max_length=200) # InformaciOn del vehiculo

class Vanet(models.Model):
	id_vehiculo = models.ForeignKey(Vehiculo) # Hash function de la matricula del vehiculo
	velocidad = models.FloatField(null=False) # Velocidad del vehiculo
	dist_e = models.FloatField(null=False) # Distancia euclidiana
	dist_a = models.FloatField(null=False) # Distancia acumulada
	p = models.BooleanField(null=False) # Nodo puntero
	v = models.BooleanField(null=False) # Nodo hoja
	id_p = models.IntegerField(null=False) # Identificador autoincrementable del puntero
	id = models.AutoField(primary_key=True, null=False) # Id de la VANET

class Vecindad(models.Model):
	id_vecindad = models.AutoField(primary_key=True, null=False)
	id_vehicul = models.ForeignKey(Vehiculo) 


# Create your models here.
