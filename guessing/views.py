from multiprocessing import context
from django.shortcuts import redirect, render
from processor import Processor as Processor

# Create your views here.

def index(request):
     
    #request.session["score"]=0
    return render(request,'index.html')

def playAgain(request):
    
    return redirect('index')

def determineoutcome(request):
    guess=""
    
    randomValue = Processor.generateRandom()
    if request.method == 'POST':
        guess = request.POST.get("guess")
    
    # determine outcome 
    outcome = Processor.findoutcome(int(guess), randomValue)
    
    # update score 
    Oldscore = request.session.get('score',0)
    score = Processor.updateScore(int(guess),Oldscore,randomValue)
    request.session['score']=score
   
    
    #update number of tossess
    oldNumOfTosses =request.session.get('numOfToss',0)
    numOfTosses = Processor.updateNumberOfTosses(oldNumOfTosses)
    request.session['numOfToss']=numOfTosses
    
    
   
    
    
    context ={"outcome":outcome, "numOfTosses":numOfTosses}
    return render(request,'outcome.html',context)

def determineSummary(request):
    
    score = request.session.get('score',0)
    numOfTosses = request.session.get('numOfToss',0)
    serverScore = Processor.determineServerScrore(numOfTosses, score)
    
    context={"score": score,"numOfTosses":numOfTosses,"serverScore":serverScore }
    
    #resset the session 
    
    for key in list(request.session.keys()):
        del request.session[key]
    
    return render(request, 'summary.html',context)