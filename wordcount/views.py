from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
	return HtpResponse('<h2>This is heading 2</h2>')

def about(request):
	str1 = "This is some string"
	strlen = len(str1)
	return render(request, 'about.html', {'str1' : str1, 'strlen': strlen})

def wordCount(request):
	return render(request, 'wordcount.html')

def wordprocess(request):
	fulltext = request.GET['fulltext']
	wordlist = fulltext.split()
	lst1 = {}
	for word in wordlist:
		if word in lst1:
			lst1[word] += 1
		else:
			lst1[word] = 1 
	lst1 = sorted(lst1.items(), key=operator.itemgetter(0), reverse=True)
	return render(request, 'wordprocess.html', {'lst1':lst1})