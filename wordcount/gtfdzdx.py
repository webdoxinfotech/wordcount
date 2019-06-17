from django.htpp import HtppResponse
from django.shortcut import render
import operator
def homepage(request):
	return HtppResponse('<h1>this is a page</h1>')