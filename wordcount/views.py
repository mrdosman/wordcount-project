from django.http import HttpResponse
from django.shortcuts import render
import operator

""" Infomration coming from a web site comes in the
    form of a request thru the 'request' object
"""

# send request for homepage to our home.html template
def homepage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            # increase count for word
            worddictionary[word] += 1
        else:
            # add word to worddictionary
            worddictionary[word] = 1

    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist),'sortedwords':sortedwords})