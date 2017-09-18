from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models
from sets import Set

class Aquarium(models.Model):
	User=models.ForeignKey(User)
	Age=models.IntegerField(default=0)
	Volume=models.IntegerField(default=0)
	FilledVolume=models.IntegerField(default=0)
	Name=models.CharField(max_length=30)
	FishSet=Set()
	
	def AddNewFish(self, aFish=None, fishCount=0):
		while i < fishCount:
			fish=Fish.objects.create(fishType=aFish, lifeTime=aFish.GetLifeTime())
			fishSet.add(fish)
			i = i + 1
		
		return -1
	
	def Iterate(self, count):
		i = 0
		nerest=Set()
		while i < count:
			FishList = Fish.objects.filter(Aquarium=self)
			for x in FishList:
				fish=Fish.objects.get(id=x.id)
				if fish.CurrentTime==fish.FishTypeKey.TimeToGoNerest-1 or divmod((fish.CurrentTime-fish.FishTypeKey.TimeToGoNerest-1), fish.FishTypeKey.NerestPeriod)==0:
					j = 0
					while j < fish.FishTypeKey.MinFishCountInNerest:
						newFish=Fish.objects.create(FishTypeKey=fish.FishTypeKey, Aquarium=fish.Aquarium)
						newFish.save()
						j = j + 1
				if fish.CurrentTime==fish.LifeTime:
					fish.delete()
				else:
					fish.CurrentTime=fish.CurrentTime+1
					fish.save()
			'''
				if self.totalVolume > self.aquariumVolume:
					return
				if(x.LiveMonth())
					x.delete()
					self.fishSet.remove(x)
					self.totalVolume = self.totalVolume - x.fishType.LifeVolume
				y=x.Nerest()
				for y in nerest.all():
					self.fishSet.add(Fish(y)
					self.totalVolume = self.totalVolume + y.fishType.lifeVolume
			'''
			i = i + 1
			self.Age = self.Age + 1
		return
	
	
	def __unicode__(self):
		return self.Name


class FishType(models.Model):
	FishName=models.CharField(max_length=30)
	MinLifeTime=models.IntegerField(default=-1)
	MaxLifeTime=models.IntegerField(default=-1)
	LifeVolume=models.IntegerField(default=-1)
	TimeToGoNerest=models.IntegerField(default=-1)
	NerestPeriod=models.IntegerField(default=-1)
	MinFishCountInNerest=models.IntegerField(default=-1)
	MaxNerestCount=models.IntegerField(default=-1)
	DeathRate=models.IntegerField(default=-1)
	DeathRateTime=models.IntegerField(default=-1)
	
	def GetLifeTime(self):
		choices = [self.deathRate, 100-self.deathRate]
		if weighted_choice(choices) == 1:
			res = random.randint(self.minLifeTime, self.maxLifeTime)
		else:
			res = random.randint(0, self.deathRateTime)
		return res

	def Weighted_Choice(self, weights):
		totals = []
		running_total = 0

		for w in weights:
			running_total += w
			totals.append(running_total)

		rnd = random.random() * running_total
		for i, total in enumerate(totals):
			if rnd < total:
				return i

	def __unicode__(self):
		return self.FishName

class Fish(models.Model):
	FishTypeKey=models.ForeignKey(FishType)
	Aquarium=models.ForeignKey(Aquarium)
	Name=models.CharField(max_length=30, default="Fish")
	CurrentTime=models.IntegerField(default=0)
	LifeTime=models.IntegerField(default=17)
	
	@property
	def getFishTypeName(self):
		return FishType.objects.get(id=self.FishTypeKey.id).FishName

	@property
	def getFishStage(self):
		if self.CurrentTime < self.FishTypeKey.TimeToGoNerest:
			return 'Мольки'
		else:
			return 'Взрослые'
	
	def LiveMonth(self):
		self.currentTime = self.currentTime + 1
		if self.currentTime == self.lifeTime:
			return -1
		return 0
	'''
	def Nerest(self):
		if self.currentTime >= self.fishType.timeToGoNerest:
			if ((self.currentTime - self.fishType.timeToGoNerest) % self.fishType.nerestPeriod) == 0:
				fishCountInNerest = random.randint(self.fishType.minFishCountInNerest, self.fishType.maxNerestCount)
				nerestSet=Set()
				x=0
				for x<fishCountInNerest:
					nerestSet.add(Fish.objects.create(fishType=aFish, lifeTime=aFish.GetLifeTime()))
					x=x+1
				return nerestSet
	'''


# Create your models here.
