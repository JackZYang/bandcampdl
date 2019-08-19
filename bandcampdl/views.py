from django.shortcuts import render
from django.http import HttpResponse
from .forms import getURL

def bandcampdlhome(request):
    from bs4 import BeautifulSoup
    import requests, re, os, json

    if request.method == 'POST':
        form = getURL(request.POST)
        
        if form.is_valid():
            url = form.cleaned_data['url']
            source = requests.get(url)

        soup = BeautifulSoup(source.text, 'lxml')

        #find stream links
        stream_regex = re.compile(r'"mp3-128":"(.*?)"}')
        streams = stream_regex.findall(soup.text)

        #find titles (first element is album name)
        title_regex = re.compile(r'"title":"(.*?)"')
        titles = title_regex.findall(soup.text)
        titles=titles[1:]
        combined = zip(titles, streams)

        #find album art
        album_art = soup.find("a", "popupImage")['href']
        
        return render(request, 'bandcampdl.html', {'form': form, 'combined': combined, 'album_art': album_art})
        
    form = getURL()
    return render(request, 'bandcampdl.html', {'form': form})