from django.http import HttpResponse
from django.shortcuts import render
import operator

def letterprocess(request):
	text = request.GET['text']
	letterlist = text.split()
	list1 = {}
	for letter in letterlist:
		if letter in list1:
			list1[letter] += 1
		else:
			list1[letter] = 1

	list1 = sorted(list1.items() , key = operator.itemgetter(0) , reverse = False)
	return render(request , 'letterprocess.html' , {'list1' : list1})



def lettercount(request):
	return render(request , 'lettercount.html')
	