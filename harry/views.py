from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'index.html')

def analyze(request):
    djtxt=request.POST.get('text','default')

    punctuation=request.POST.get('punctuation','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremove=request.POST.get('newlineremove','off')
    spaceremove=request.POST.get('spaceremove','off')
    charcount=request.POST.get('charcount','off')

    # Remove punctuation
    if punctuation=='on':
        punctuations = '''!()-[]{};:'",<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtxt:
            if char not in punctuations:
                analyzed=analyzed+char
                parms={
                    'purpose':'Removed Punctuation',
                    'analyzed_text':analyzed
                }
        djtxt=analyzed

    #Capitalize 
    if fullcaps=='on':
        analyzed=""
        for char in djtxt:
            analyzed=analyzed+char.upper()
            parms={
                'purpose':'Transform to Uppercase',
                'analyzed_text':analyzed
            }   
        djtxt=analyzed
    
    # New Line remove
    if newlineremove=='on':
        analyzed=""
        for char in djtxt:
            if char !='\n' and char !='\r':
                analyzed=analyzed+char
                parms={
                    'purpose':'New Line Removed',
                    'analyzed_text':analyzed
                }
        djtxt=analyzed

    # Space Remove  
    if spaceremove=='on':
        analyzed=""
        for index,char in enumerate (djtxt):
                if not(djtxt[index]==" " and djtxt[index+1]==" "):
                    analyzed=analyzed+char
                    parms={
                    'purpose':'Space Removed',
                    'analyzed_text':analyzed
                }
        djtxt=analyzed

    # Char count
    if charcount == 'on':
        analyzed=""
        for char in djtxt:
            analyzed=len(djtxt)
            parms={
                    'purpose':'Total Characters',
                    'analyzed_text':analyzed
                } 
    if (punctuation !='on' and fullcaps !='on' and newlineremove !='on' and spaceremove !='on' and charcount !='on'):
        return HttpResponse("Please select any operation and try again later")

    else:
        return render(request,'analyze.html',parms)      
    
def nav(request):
    site='''<h1> Welcome to my personal Navbar <h1>
     <p> Click here to go <a href="https://www.youtube.com/" target=_blank> Youtube </a> </p>
     <p> Click here to go <a href="https://www.facebook.com/" target=_blank> Facebook </a> </p>
     <p> Click here to go <a href="https://www.w3schools.com/" target=_blank> Geeksforgeeks </a> </p>
     <p> Click here to go <a href="https://www.geeksforgeeks.org/"  target=_blank> W3school </a> </p>'''
    return HttpResponse(site)

def about(request):
    return render(request,'about.html')  

def addition(request):
    a=int(request.POST['text1'])
    b=int(request.POST['text2'])
    c=a+2*b
    context={
        'a':c
    }
    return render(request,'add.html',context)


    
# def capfirst(request):
#     return HttpResponse('<h1> Capital word <a href="/">First</a></h1>')

# def newlineremove(request):
#     return HttpResponse('<h1> New Line <a href="/">Remove</a></h1>')

# def spaceremove(request):
#     return render(request,'remove.html')
#     # return HttpResponse('<h1>Space will <a href="/">Remove</a></h1>')

# def charcount(request):
#     return HttpResponse('<h1> Character <a href="/">Count</a></h1>')

