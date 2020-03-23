from graphics import *
import collections
import math
import re

class State:
    #The key of neighbors is the transtition value, the value on the "edge"
    #And teh neighbors[key] is actually the State to which it points
    key=None
    final=0
    initial=0
    #neighbors={} NEVEEEEEEEEERRRRRRRRR
    neighbors=None#DOGSHIT

    #state drawing vars
    #state=None
    point=None
    initialNode=None
    text=None
    finalNode=None
    downNumb=0
    upNumb=0
    farNode=0
    stateHeight=120
    neighLetters=None
    selfPoint=None
    selfN=0

    def __init__(self,key,final,initial):
        self.key=key
        self.final=int(final)
        self.initial=int(initial)
        #HERE DO IT
        self.neighbors=dict()#FCKING BUG LITTLE SHIT
    def appendNeighbor(self,key,state):
        self.neighbors[key]=state
"""
    def __init__(self,n,final,listOfNeighbors): 
        self.n=n
        self.final=int(final)
        #here the second element has to be the STATE and not the state key
        for key,state in listOfNeighbors:
            neighbors[key]=state

"""


class Automata:
    n,m=0,0
    automataStates=None
    answerHolder=None
    initial=None

    #drawing vars
    wrongAnswerColor='red'
    finalColor='blue'
    txtColor='white'
    nodeTextSize=20
    timeBetweenTests=4
    timeBetweenStates=0.5
    answerColor='SpringGreen2'
    circleRadius=30
    circleWidth=5
    circleColor='white'
    initialCircleColor='green'
    dX=100
    dY=300
    deplX=200
    deplY=200
    distanceY=15
    farNodeH=30

    def __init__(self,n,m,data):
        self.automataStates={}
        self.n=n
        self.m=m
        for key,final,initial in data:
            self.automataStates[key]=State(key,final,initial)
            if(int(initial)==1):
                self.initial=self.automataStates[key]
    
    def addTransition(self,stare,key,dest):
        self.automataStates[stare].appendNeighbor(key,self.automataStates[dest])

    def getAutomataStates(self):
        print (self.automataStates)
    
    def checkValidation(self,sequence):
        it=self.initial
        for x in sequence:
            if x in it.neighbors.keys():
                it=it.neighbors[x]
            else:
                return 0
        if it.final==1:
            return 1
        else:
            return 0
    def animateValidation(self,win,sequence,cnt,it):
        if(cnt==0):
            self.answerHolder=Text(Point(700,120),"".join(sequence))
            self.answerHolder.setSize(25)
            self.answerHolder.setTextColor('white')
            self.answerHolder.draw(win)
        if cnt==len(sequence):
            if it.final==1:
                it.finalNode.setOutline(self.finalColor)
                it.text.setTextColor(self.answerColor)
                self.answerHolder.setTextColor(self.answerColor)
                self.answerHolder.setText("Test was accepted!!")
                time.sleep(self.timeBetweenTests)
                it.finalNode.setOutline(self.circleColor)
                it.state.setOutline(self.circleColor)
                if(it.initial==1):
                    it.state.setOutline(self.initialCircleColor)
                it.text.setTextColor(self.circleColor)
                self.answerHolder.undraw()
            else:
                it.state.setOutline(self.wrongAnswerColor)
                it.text.setTextColor(self.wrongAnswerColor)
                self.answerHolder.setText('Test was rejected in '+it.key+" because it's not a final state")
                self.answerHolder.setTextColor('Red')
                time.sleep(self.timeBetweenTests)
                it.state.setOutline(self.circleColor)
                if(it.initial==1):
                    it.state.setOutline(self.initialCircleColor)
                it.text.setTextColor(self.circleColor)
                self.answerHolder.undraw()
            return None
        if sequence[cnt] in it.neighbors.keys():
            it.state.setOutline(self.answerColor)
            it.text.setTextColor(self.answerColor)
            it.neighLetters[sequence[cnt]]['transCost'].setTextColor(self.answerColor)
            self.answerHolder.setText("".join(sequence[cnt:]))
            win.itemconfig(it.neighLetters[sequence[cnt]]['transLine'],fill=self.answerColor)
            time.sleep(self.timeBetweenStates)
            self.animateValidation(win,sequence,cnt+1,it.neighbors[sequence[cnt]])
            it.state.setOutline(self.circleColor)
            if(it.initial==1):
                it.state.setOutline(self.initialCircleColor)
            it.text.setTextColor(self.txtColor)
            it.neighLetters[sequence[cnt]]['transCost'].setTextColor(self.txtColor)
            win.itemconfig(it.neighLetters[sequence[cnt]]['transLine'],fill=self.txtColor)
        else:
            it.state.setOutline(self.wrongAnswerColor)
            it.text.setTextColor(self.wrongAnswerColor)
            self.answerHolder.setText('Test was rejected in '+it.key+' because no '+sequence[cnt]+' transtition!')
            self.answerHolder.setTextColor('Red')
            time.sleep(self.timeBetweenTests)
            it.state.setOutline(self.circleColor)
            if(it.initial==1):
                it.state.setOutline(self.initialCircleColor)
            it.text.setTextColor(self.circleColor)
            self.answerHolder.undraw()




    #params --- what they do
    #self   --- obviously an Automata object
    #win    --- winGraph (on what it will draw)
    #maxcnt --- max nodes per line
    def drawAutomata(self,win,maxcnt):
        #########################################################################
        #drawing the automate
        cnt=0   #max 8 per line
        distX,distY=0,0 #the calculated distance between nodes
        #adds up with the self.delpX/Y
        for node in self.automataStates.values():
            if(cnt>=maxcnt):
                distY+=self.deplY
                distX=0
                cnt=0
            #drawing the nodes
            node.neighLetters={}
            node.point=Point(self.dX+distX,self.dY+distY)
            node.text=Text(node.point,node.key)
            node.text.setTextColor(self.txtColor)
            node.text.setSize(self.nodeTextSize)
            node.state=Circle(node.point,self.circleRadius)
            node.state.setWidth(self.circleWidth)
            node.state.setOutline(self.circleColor)
            if node.initial==1:
                node.state.setOutline(self.initialCircleColor)
            node.state.draw(win)
            if node.final==1:
                node.finalNode=Circle(node.point,self.circleRadius-2*self.circleWidth)
                node.finalNode.setWidth(self.circleWidth/2)
                node.finalNode.setOutline(self.circleColor)
                node.finalNode.draw(win)
            potato=Circle(node.point,50)


            node.text.draw(win)
            distX+=self.deplX
            cnt+=1
        for node in self.automataStates.values():
            for key,neigh in node.neighbors.items():
                if neigh.key==node.key:
                    if(node.selfN==0):
                        node.selfPoint=node.point.clone()
                        node.selfPoint.move(-self.circleRadius/2,-self.circleRadius*2)
                        node.selfPoint.setFill(self.circleColor)
                    elif(node.selfN%2==1):
                        node.selfPoint.move(self.circleRadius,0)
                    else:
                        node.selfPoint.move(-automata.circleRadius,4*self.circleRadius)
                    interStateY=node.point.getY()-math.sqrt((self.circleRadius)**2-(node.point.getX()-node.selfPoint.getX())**2)
                    myLine=win.create_line(node.selfPoint.getX(),interStateY,node.selfPoint.getX()-25,node.selfPoint.getY(),node.selfPoint.getX()+25,node.selfPoint.getY(),node.selfPoint.getX()+5,interStateY,fill='white',smooth="true",arrow="last",width=2)
                    letpnt=Text(Point(node.selfPoint.getX(),node.selfPoint.getY()-10),key)
                    letpnt.setTextColor("white")
                    letpnt.draw(win)
                    letpnt.setSize(15)
                    node.neighLetters[key]={"transCost":letpnt,"transLine":myLine,"to":neigh.key}
                    node.selfN+=1;
                else:
                    ok=0
                    maxheight=0
                    for x in self.automataStates.keys():
                        if(x==node.key or x==neigh.key) and ok==0:
                            ok=1
                        elif((x==node.key and ok==1) or (x==neigh.key and ok==1)):
                            break
                        elif(ok==1):
                            maxheight=max(maxheight,self.automataStates[x].stateHeight)
                    ok=0        
                    for x in self.automataStates.keys():
                        if((x==node.key or x==neigh.key) and ok==0):
                            ok=1
                        if((x==node.key and ok==1) or (x==neigh.key and ok==1)):
                            break
                        if(ok==1):
                            self.automataStates[x].stateHeight=2*maxheight+100
                    if(maxheight==0):
                        if(node.point.getX()<neigh.point.getX()):
                            myLine,myPoint=createCloseLine(win,node.point,neigh.point,1,self.circleRadius,key)
                        else:
                            myLine,myPoint=createCloseLine(win,node.point,neigh.point,-1,self.circleRadius,key)
                    else:
                        if(node.point.getX()<neigh.point.getX()):
                            node.upNumb-=1
                            neigh.upNumb-=1
                            myLine,myPoint=createFarLine(win,node.point,neigh.point,1,self.circleRadius,maxheight+self.farNodeH,key,node.upNumb,neigh.upNumb,self.distanceY,self.deplX)
                        else:
                            node.downNumb+=1
                            neigh.downNumb+=1
                            myLine,myPoint=createFarLine(win,node.point,neigh.point,-1,self.circleRadius,maxheight+self.farNodeH,key,node.downNumb,neigh.downNumb,self.distanceY,self.deplX)
                    node.neighLetters[key]={"transCost":myPoint,"transLine":myLine,"to":neigh.key}
        #DONE DRAWING AUTOMATA
        ###########################################################################

def createCloseLine(win,point1,point2,inverse,circ,letter):
    point3=Point((point1.getX()+point2.getX())/2,point1.getY())
    myLine=win.create_line(point1.getX()+inverse*circ,point1.getY(),point3.getX(),point3.getY()+inverse*15,point2.getX()-inverse*circ,point2.getY()+inverse*5,fill='white',smooth="true",arrow="last",width=2)
    myPoint=Text(Point(point3.getX(),point3.getY()+inverse*((abs(point1.getX()-point2.getX())+abs(point1.getY()-point2.getY()))/10)),letter)
    myPoint.setTextColor("white")
    myPoint.setSize(15)
    myPoint.draw(win)
    return myLine,myPoint

def createFarLine(win,point1,point2,inverse,circ,height,letter,upOrDown1,upOrDown2,distanceY,distanceX):
    point3=Point((point1.getX()+point2.getX())/2,point1.getY()+(1 if upOrDown1>0 else -1)*height)
    distX1=Point(point1.getX()+inverse*math.sqrt(circ**2-(distanceY/upOrDown1)**2),point1.getY()+(1 if upOrDown1>0 else -1)*distanceY)
    distX2=Point(point2.getX()-inverse*math.sqrt(circ**2-(distanceY/upOrDown1)**2),point2.getY()+(1 if upOrDown1>0 else -1)*distanceY)
    myLine=win.create_line(distX1.getX(),distX1.getY(),point3.getX(),point3.getY(),distX2.getX(),distX2.getY(),fill='white',smooth="true",arrow="last",width=2)
    myPoint=Text(Point(point3.getX(),point3.getY()+inverse*(abs(point1.getX()-point2.getX())+abs(point1.getY()-point2.getY()))/8-inverse*40*((abs(point1.getX()-point2.getX())/distanceX)/2-1)),letter)
    myPoint.setTextColor("white")
    myPoint.setSize(15)
    myPoint.draw(win)
    return myLine,myPoint



def main():
    #automat has to be given through the file
    #under this format
    #N M InitialState
    #N lines containing: Xstate FinalOrNot(0/1)
    #M lines containing: Xstate ValueOfTransition YState
    automat=None
    data=[]
    with open('input.in','r') as cin:
        states=[]
        firstLine=cin.readline().split()
        n,m=int(firstLine[0]),int(firstLine[1])
        initial=firstLine[2]
        for x in range(n):
            data.append(cin.readline().split())
            data[x].append(1 if data[x][0]==initial else 0)
        automat=Automata(n,m,data)
        for x in range(m):
            rel=cin.readline().split()
            automat.addTransition(rel[0],rel[1],rel[2])

    #In case of no graphics wanted, just the cmd(assuming any cmd argument means it wants graphichs)
    if(len(sys.argv)<2 or n>32):
        n=int(input())
        for x in range(n):
            sequence=[x for x in input()]
            if(automat.checkValidation(sequence)==1):
                print("Test was accepted")
            else:
                print("Test rejected")
    else:
        if(len(sys.argv)==4):
            automat.timeBetweenTests=float(sys.argv[2])
            automat.timeBetweenStates=float(sys.argv[3])
        #Drawing the automat
        #creating window
        win=GraphWin("DFA",1888,1000)
        win.setBackground('black')
        #creating text of input n and creating input entry
        inputN =Text(Point(220,20),"Enter number of testcases")
        inputN.setSize(20)
        inputN.setTextColor('white')
        inputN.draw(win)
        textEntry = Entry(Point(635,60),90)
        textEntry.setSize(16)
        textEntry.fill='black'
        textEntry.color='SpringGreen2'
        textEntry.draw(win)
        
        #drawing automate
        automat.drawAutomata(win,10)

        #getting the input with help of click
        #win.bind('<Return>',win.getMouse())
        win.getMouse()

        n=int(textEntry.getText())

        #reseting the type entry
        textEntry.undraw()
        textEntry.setText('')
        textEntry.draw(win)

        #changing text of input n to input testnumber
        inputTests=inputN.clone()
        inputTests.setText("Enter test number:")
        inputTests.move(-35,0)
        inputN.undraw()
        inputTests.draw(win)
        #creating a number test counter
        testText = Text(Point(330,20),n)
        testText.setSize(20)
        testText.setTextColor('white')
        testText.draw(win)



        for x in range(n):
            win.getMouse()
            sequence=[x for x in textEntry.getText()]
            automat.animateValidation(win,sequence,0,automat.initial)
            testText.undraw()
            testText.setText(n-x-1)
            testText.draw(win)
            textEntry.undraw()
            textEntry.setText('')
            textEntry.draw(win)
        automat.answerHolder.setText("Thanks for using my app")
        automat.answerHolder.setTextColor(automat.answerColor)
        automat.answerHolder.draw(win)
        win.getMouse()
        win.close()




if __name__=="__main__":
    main()
"""
        #drawing the automate
        maxcnt=8
        cnt=0   #max 8 per line
        automat.bX,automat.bY=150,200 #begining of X and Y of the automat
        distX,distY=0,0
        for node in automat.automataStates.values():
            if(cnt>maxcnt):
                distY+=automat.deplY
                cnt=0
            #drawing the nodes
            node.neighLetters={}
            node.point=Point(automat.dX+distX,automat.dY+distY)
            node.text=Text(node.point,node.key)
            node.text.setTextColor(automat.txtColor)
            node.text.setSize(automat.nodeTextSize)
            node.state=Circle(node.point,automat.circleRadius)
            node.state.setWidth(automat.circleWidth)
            node.state.setOutline(automat.circleColor)
            node.state.draw(win)
            node.text.draw(win)
            distX+=automat.deplX
            cnt+=1
        for node in automat.automataStates.values():
            for key,neigh in node.neighbors.items():
                if neigh.key==node.key:
                    if(node.selfN==0):
                        node.selfPoint=node.point.clone()
                        node.selfPoint.move(-automat.circleRadius/2,-automat.circleRadius*2)
                        node.selfPoint.setFill(automat.circleColor)
                    elif(node.selfN%2==1):
                        node.selfPoint.move(automat.circleRadius,0)
                    else:
                        node.selfPoint.move(-automata.circleRadius,4*automat.circleRadius)
                    interStateY=node.point.getY()-math.sqrt((automat.circleRadius)**2-(node.point.getX()-node.selfPoint.getX())**2)
                    myLine=win.create_line(node.selfPoint.getX(),interStateY,node.selfPoint.getX()-25,node.selfPoint.getY(),node.selfPoint.getX()+25,node.selfPoint.getY(),node.selfPoint.getX()+5,interStateY,fill='white',smooth="true",arrow="last",width=2)
                    letpnt=Text(Point(node.selfPoint.getX(),node.selfPoint.getY()-10),key)
                    letpnt.setTextColor("white")
                    letpnt.draw(win)
                    letpnt.setSize(15)
                    node.neighLetters[key]={"transCost":letpnt,"transLine":myLine,"to":neigh.key}
                    node.selfN+=1;
                else:
                    ok=0
                    maxheight=0
                    for x in automat.automataStates.keys():
                        if(x==node.key or x==neigh.key) and ok==0:
                            ok=1
                        elif((x==node.key and ok==1) or (x==neigh.key and ok==1)):
                            break
                        elif(ok==1):
                            maxheight=max(maxheight,automat.automataStates[x].stateHeight)
                    ok=0        
                    for x in automat.automataStates.keys():
                        if((x==node.key or x==neigh.key) and ok==0):
                            ok=1
                        if((x==node.key and ok==1) or (x==neigh.key and ok==1)):
                            break
                        if(ok==1):
                            automat.automataStates[x].stateHeight=maxheight+20
                    if(maxheight==0):
                        if(node.point.getX()<neigh.point.getX()):
                            myLine,myPoint=createCloseLine(win,node.point,neigh.point,1,automat.circleRadius,key)
                        else:
                            myLine,myPoint=createCloseLine(win,node.point,neigh.point,-1,automat.circleRadius,key)
                    else:
                        if(node.point.getX()<neigh.point.getX()):
                            node.upNumb+=1
                            neigh.upNumb+=1
                            myLine,myPoint=createFarLine(win,node.point,neigh.point,1,automat.circleRadius,maxheight+automat.farNodeH,key,node.upNumb,neigh.upNumb,automat.distanceY)
                        else:
                            node.downNumb+=1
                            neigh.downNumb+=1
                            myLine,myPoint=createFarLine(win,node.point,neigh.point,-1,automat.circleRadius,maxheight+automat.farNodeH,key,node.downNumb,neigh.downNumb,automat.distanceY)
"""



    #n=int(input())
    #for x in range(n):
    #    sequence=[x for x in input()]
    #    print (automat.checkValidation(sequence))
"""
    for x in automat.automataStates.values():
        print (hex(id(x.neighbors)))
        #print (x.neighbors)
        print (x)

    automat.automataStates['q'].neighbors['b']=5
    for x in automat.automataStates.values():
        print (hex(id(x.neighbors)))
        #print (x.neighbors)
        print (x)

"""

