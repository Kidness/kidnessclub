# -*- coding: utf-8 -*-

from django.db import models
from datetime import *

# Room 
class Room(models.Model):
	name = models.CharField(max_length=200)
	floor = models.CharField(max_length=200, blank=True,null=True)
	building = models.CharField(max_length=200, blank=True,null=True)

	def __unicode__(self):
		return unicode(self.name)

# Age 
class Age(models.Model):
	age = models.CharField(max_length=200)

	def __unicode__(self):
		return unicode(self.age)

# Program 		
class Programm(models.Model):
	name = models.CharField(max_length=200)
	age = models.ForeignKey(Age)	

	def __unicode__(self):
		return unicode(self.name)
	
class Service(models.Model):
	name = models.CharField(max_length=200)
	programm = models.ForeignKey(Programm)	
	price = models.DecimalField (max_digits=10, decimal_places=2)
	
	# Fields for abonement
	number_of_visits = models.IntegerField(blank=True)
	
	def __unicode__(self):
		return unicode(self.name)

class Card(models.Model):
	number = models.CharField(max_length=200)

	def __unicode__(self):
		return unicode(self.number)
	
class Source(models.Model):
	name = models.CharField(max_length=200)

	def __unicode__(self):
		return unicode(self.name)
	
# Staff class
class Staff(models.Model):
	first_name = models.CharField(max_length=200)	
	last_name = models.CharField(max_length=200, blank=True)
	mobile_phone = models.CharField(max_length=200, blank=True)
	address = models.CharField(max_length=200, blank=True)
	email = models.CharField(max_length=200, blank=True)
	trainer = models.BooleanField()
	
	def __unicode__(self):
		return unicode(self.first_name + " " + self.last_name)

class Client(models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	birth_day = models.DateField(auto_now_add = True,blank=True,null=True)
	mobile_phone = models.CharField(max_length=200, blank=True,null=True)
	work_phone = models.CharField(max_length=200, blank=True,null=True)
	address = models.CharField(max_length=200, blank=True,null=True)
	email = models.CharField(max_length=200, blank=True,null=True)
	contract_day = models.DateField(auto_now_add = True,blank=True)
	comments = models.CharField(max_length=200, blank=True,null=True)
	source = models.ForeignKey(Source,null=True)	
	card = models.ForeignKey(Card, null=True)
	manager = models.ForeignKey(Staff, null=True)
	parent = models.ForeignKey('self', null=True)
	
	
	def __unicode__(self):
		return unicode(self.first_name + " " + self.last_name)

class ClientRelations(models.Model):
	clientid = models.ForeignKey(Client)
	relationid = models.ForeignKey(Client,related_name='+')
	
# Group	
class Group(models.Model):
	name = models.CharField(max_length=200)	
	schedule = models.CharField(max_length=200)	
	room = models.ForeignKey(Room)
	trainer = models.ForeignKey(Staff)

	def __unicode__(self):
		return unicode(self.name)

class ServiceUsage(models.Model):
	client = models.ForeignKey(Client)	
	service = models.ForeignKey(Service)
	payed = models.IntegerField()
	available = models.IntegerField()
	
class Exercise(models.Model):
	trainer = models.ForeignKey(Staff)
	room = models.ForeignKey(Room)
	group = models.ForeignKey(Group)
	exercise_day = models.DateField()

class ClientGroup(models.Model):
	client = models.ForeignKey(Client)
	group = models.ForeignKey(Group)
	
	#def __unicode__(self):
	#	return unicode(self.client.__unicode__() + " " + self.group)
    
    
class ClientExercise(models.Model):
	client = models.ForeignKey(Client)
	exercise = models.ForeignKey(Exercise)
		
class StaffProgramm(models.Model):
	staff = models.ForeignKey(Staff)
	programm = models.ForeignKey(Programm)
