# File: sudoku.py
# Programmers: Amor Dimaano


from random import*
from graphics import*
from math import*
from time import sleep
from string import*


class Button:
    def __init__(self, win, center, width, height, label):
        w = width/2.0
        h = height/2.0
        x = center.getX()
        y = center.getY()
        self.xmax = x+w
        self.xmin = x-w
        self.ymax = y+h
        self.ymin = y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.setSize(16)
        self.label.draw(win)
        self.deactivate()
    def clicked(self, p):
        return self.active and \
            self.xmin <= p.getX() <= self.xmax and \
            self.ymin <= p.getY() <= self.ymax
    def getLabel(self):
        return self.label.getText()
    def activate(self):
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = 1
    def deactivate(self):
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = 0
    def undraw(self):
        self.label.undraw()
        self.rect.undraw()


def diflevel(difwin):
    close = Button(difwin,Point(35,23),50,28,'EXIT')
    close.activate()
    beginner = Button(difwin,Point(175,275),125,35,'Beginner')
    beginner.activate()
    intermediate = Button(difwin,Point(175,212.5),125,35,'Intermediate')
    intermediate.activate()
    hard = Button(difwin,Point(175,150),125,35,'Hard')
    hard.activate()
    instructions = Button(difwin,Point(275,85),115,30,'instructions')
    instructions.activate()
    credits = Button(difwin,Point(275,35),75,30,'credits')
    credits.activate()
    t = 0
    while t==0:
        p = difwin.getMouse()
        if close.clicked(p):
            t = 1
            return 'close'
        elif beginner.clicked(p):
            t = 1
            return 'beginner'
        elif intermediate.clicked(p):
            t = 1
            return 'intermediate'
        elif hard.clicked(p):
            t = 1
            return 'hard'   
        elif instructions.clicked(p):
            ins = GraphWin('Instructions',500,300)
            ins.setCoords(0,0,500,300)
            ins.setBackground('white')
            institle = Text(Point(250,280),'INSTRUCTIONS')
            institle.draw(ins)
            ins1 = Text(Point(250,225),'The objective of the game is to fill all the blank squares in a game')
            ins1.draw(ins)
            ins2 = Text(Point(250,205),'with the correct numbers.')
            ins2.draw(ins)
            ins3 = Text(Point(250,175),'There are three very simple constraints to follow.')
            ins3.draw(ins)
            ins4 = Text(Point(250,160),'In a 9 by 9 square Sudoku game:')
            ins4.draw(ins)
            ins5 = Text(Point(250,142),'- Every row of 9 numbers must include all digits 1 through 9 in any order')
            ins5.setSize(10)
            ins5.draw(ins)
            ins6 = Text(Point(250,127),'- Every column of 9 numbers must include all digits 1 through 9 in any order')
            ins6.setSize(10)
            ins6.draw(ins)
            ins7 = Text(Point(250,112),'- Every 3 by 3 subsection of the 9 by 9 square must include all digits 1 through 9')
            ins7.setSize(10)
            ins7.draw(ins)
            insclose = Button(ins,Point(250,75),40,20,'OK')
            insclose.activate()
            s = 0
            while s==0:
                p = ins.getMouse()
                if insclose.clicked(p):
                    s = 1
                    ins.close()
        elif credits.clicked(p):
            credwin = GraphWin('Programmers',200,200)
            credwin.setCoords(0,0,200,200)
            credwin.setBackground('white')
            amor = Text(Point(100,150),'Amor Dimaano')
            amor.draw(credwin)
            amf = Text(Point(100,125),'IIBSM-AMF')
            amf.draw(credwin)
            paolo = Text(Point(100,100),'Juan Paolo Fernando')
            paolo.draw(credwin)
            ece = Text(Point(100,75),'IVBS-ECE')
            ece.draw(credwin)
            back = Button(credwin,Point(100,30),40,20,'OK')
            back.activate()
            s = 0
            while s==0:
                p = credwin.getMouse()
                if back.clicked(p):
                    s = 1
                    credwin.close()

def drawwin(win,level):
    outline = Rectangle(Point(102.5,204),Point(597.5,546))
    outline.setWidth(5)
    outline.draw(win)
    vseparator1 = Line(Point(267.5,204),Point(267.5,546))
    vseparator1.setWidth(5)
    vseparator1.draw(win)
    vseparator2 = Line(Point(432.5,204),Point(432.5,546))
    vseparator2.setWidth(5)
    vseparator2.draw(win)
    hseparator1 = Line(Point(102.5,318),Point(597.5,318))
    hseparator1.setWidth(5)
    hseparator1.draw(win)
    hseparator2 = Line(Point(102.5,432),Point(597.5,432))
    hseparator2.setWidth(5)
    hseparator2.draw(win)
    levellabel = Text(Point(350,623),level)
    levellabel.setSize(36)
    levellabel.setStyle('bold')
    levellabel.draw(win)
    check = Button(win,Point(200,125),125,35,'CHECK')
    check.activate()
    solve = Button(win,Point(350,125),125,35,'SOLVE')
    solve.activate()
    newgame = Button(win,Point(500,125),125,35,'NEW GAME')
    newgame.activate()
    return levellabel,check, solve, newgame
    
   
def beginner():
    # s = randrange(1,5,1)
    prob = []
    sol = []
    prob1 = [5,0,2,9,0,0,0,0,6,0,0,4,6,1,0,0,0,0,0,1,0,0,0,0,9,3,8,0,6,0,4,9,0,8,2,0,0,0,1,8,0,5,3,0,0,0,4,5,0,7,2,0,9,0,4,7,3,0,0,0,0,1,0,0,0,0,0,2,9,4,0,0,6,0,0,0,0,3,5,0,7]
    #prob.append(p1)
    sol1 = [5,8,2,9,3,7,1,4,6,9,3,4,6,1,8,7,5,2,7,1,6,2,5,4,9,3,8,3,6,7,4,9,1,8,2,5,2,9,1,8,6,5,3,7,4,8,4,5,3,7,2,6,9,1,4,7,3,5,8,6,2,1,9,1,5,8,7,2,9,4,6,3,6,2,9,1,4,3,5,8,7]
    #sol.append(s1)
    # p1 prob+s
    # s1 sol+s
    return prob1,sol1
    # return p1,s1 

def intermediate():
    prob1 = [0,2,0,8,0,6,0,9,0,0,0,3,2,0,9,5,0,0,0,0,0,0,5,0,0,0,0,0,3,7,6,0,1,9,5,0,6,0,0,0,2,0,0,0,4,0,8,1,9,0,5,7,3,0,0,0,0,0,6,0,0,0,0,0,0,8,5,0,4,1,0,0,0,7,0,3,0,8,0,4,0]
    sol1 = [7,2,5,8,3,6,4,9,1,8,4,3,2,1,9,5,6,7,9,1,6,4,5,7,2,8,3,4,3,7,6,8,1,9,5,2,6,5,9,7,2,3,8,1,4,2,8,1,9,4,5,7,3,6,5,9,4,1,6,2,3,7,8,3,6,8,5,7,4,1,2,9,1,7,2,3,9,8,6,4,5]
    return prob1,sol1


def hard():
    prob1= [0,7,0,0,0,0,0,9,4,5,0,0,6,0,3,0,0,0,0,0,0,0,0,0,1,3,6,0,0,1,0,6,0,0,0,0,8,0,0,9,0,5,0,0,7,0,0,0,0,1,0,6,0,0,0,9,5,0,0,0,0,0,0,0,0,0,2,0,7,0,0,5,4,3,0,0,0,0,0,8,0]
    sol1 = [6,7,3,8,2,1,5,9,4,5,1,9,6,4,3,8,7,2,2,8,4,5,7,9,1,3,6,3,4,1,7,6,2,9,5,8,8,2,6,9,3,5,4,1,7,9,5,7,4,1,8,6,2,3,7,9,5,3,8,4,2,6,1,1,6,8,2,9,7,3,4,5,4,3,2,1,5,6,7,8,9]
    return prob1, sol1


def drawpuzzle(win,prob):
    lstprob = []
    count = 1
    for i in prob:
        if count<=9:
            if count==1:
                x = 130
            y = 527
            if i!=0:
                a = Text(Point(x,y),i)
                a.setSize(18)
                a.setStyle('bold')
                a.draw(win)
                lstprob.append(a)
                count = count + 1
                x = x + 55
            else:
                a = Entry(Point(x,y),1)
                a.setSize(15)
                a.setStyle('bold italic')
                a.draw(win)
                lstprob.append(a)
                count = count + 1
                x = x + 55
        elif count<=18:
            if count==10:
                x = 130
            y = 489
            if i!=0:
                a = Text(Point(x,y),i)
                a.setSize(18)
                a.setStyle('bold')
                a.draw(win)
                lstprob.append(a)
                count = count + 1
                x = x + 55
            else:
                a = Entry(Point(x,y),1)
                a.setSize(15)
                a.setStyle('bold italic')
                a.draw(win)
                lstprob.append(a)
                count = count + 1
                x = x + 55
        elif count<=27:
            if count==19:
                x = 130
            y = 451
            if i!=0:
                a = Text(Point(x,y),i)
                a.setSize(18)
                a.setStyle('bold')
                a.draw(win)
                lstprob.append(a)
                count = count + 1
                x = x + 55
            else:
                a = Entry(Point(x,y),1)
                a.setSize(15)
                a.setStyle('bold italic')
                a.draw(win)
                lstprob.append(a)
                count = count + 1
                x = x + 55
        elif count<=36:
            if count==28:
                x = 130
            y = 413
            if i!=0:
                a = Text(Point(x,y),i)
                a.setSize(18)
                a.setStyle('bold')
                a.draw(win)
                lstprob.append(a)
                count = count + 1
                x = x + 55
            else:
                a = Entry(Point(x,y),1)
                a.setSize(15)
                a.setStyle('bold italic')
                a.draw(win)
                lstprob.append(a)
                count = count + 1
                x = x + 55
        elif count<=45:
            if count==37:
                x = 130
            y = 375
            if i!=0:
                a = Text(Point(x,y),i)
                a.setStyle('bold')
                a.setSize(18)
                a.draw(win)
                lstprob.append(a)
                count = count + 1
                x = x + 55
            else:
                a = Entry(Point(x,y),1)
                a.setSize(15)
                a.setStyle('bold italic')
                a.draw(win)
                lstprob.append(a)
                count = count + 1
                x = x + 55
        elif count<=54:
            if count==46:
                x = 130
            y = 337
            if i!=0:
                a = Text(Point(x,y),i)
                a.setStyle('bold')
                a.setSize(18)
                a.draw(win)
                lstprob.append(a)
                count = count + 1
                x = x + 55
            else:
                a = Entry(Point(x,y),1)
                a.setStyle('bold italic')
                a.setSize(15)
                a.draw(win)
                lstprob.append(a)
                count = count + 1
                x = x + 55
        elif count<=63:
            if count==55:
                x = 130
            y = 299
            if i!=0:
                a = Text(Point(x,y),i)
                a.setStyle('bold')
                a.setSize(18)
                a.draw(win)
                lstprob.append(a)
                count = count + 1
                x = x + 55
            else:
                a = Entry(Point(x,y),1)
                a.setSize(15)
                a.setStyle('bold italic')
                a.draw(win)
                lstprob.append(a)
                count = count + 1
                x = x + 55
        elif count<=72:
            if count==64:
                x = 130
            y = 261
            if i!=0:
                a = Text(Point(x,y),i)
                a.setSize(18)
                a.setStyle('bold')
                a.draw(win)         
                lstprob.append(a)
                count = count + 1
                x = x + 55
            else:
                a = Entry(Point(x,y),1)
                a.setSize(15)
                a.setStyle('bold italic')
                a.draw(win)
                lstprob.append(a)
                count = count + 1
                x = x + 55
        elif count<=81:
            if count==73:
                x = 130
            y = 223
            if i!=0:
                a = Text(Point(x,y),i)
                a.setStyle('bold')
                a.setSize(18)
                a.draw(win)
                lstprob.append(a)
                count = count + 1
                x = x + 55
            else:
                a = Entry(Point(x,y),1)
                a.setStyle('bold italic')
                a.setSize(15)
                a.draw(win)
                lstprob.append(a)
                count = count + 1
                x = x + 55
    return lstprob


def checker(win,prob,sol,close):
    error = 0
    for i in range(len(prob)):
        a = sol[i]
        b = prob[i]
        c = b.getText()
        if c!='':
            c = int(c)
            
        if a!=c:
            b.setTextColor('red')
            error = error + 1
    return error
        

def errorprompt(result):
    win = GraphWin('Errors',200,100)
    win.setCoords(0,0,200,100)
    win.setBackground('white')
    error = Text(Point(86,80),'Errors:')
    error.draw(win)
    errnum = Text(Point(122,80),str(result))
    errnum.draw(win)
    tryagain = Button(win, Point(60,25),95,25,'Try Again')
    tryagain.activate()
    close = Button(win, Point(160,25),60,25,'Close')
    close.activate()
    t = 0
    while t==0:
        p = win.getMouse()
        if tryagain.clicked(p):
            t = 1
            win.close()
            return 'tryagain'
        elif close.clicked(p):
            t = 1
            win.close()
            return 'close'


def noerror(check,solve):
    check.deactivate()
    solve.deactivate()
    noerrorwin = GraphWin('No Error',150,150)
    noerrorwin.setCoords(0,0,150,150)
    noerrorwin.setBackground('white')
    noerrortext = Text(Point(75,100),'PUZZLE FINISHED')
    noerrortext.draw(noerrorwin)
    ok = Button(noerrorwin,Point(75,50),40,30,'OK')
    ok.activate()
    t = 0
    while t==0:
        p = noerrorwin.getMouse()
        if ok.clicked(p):
            t = 1
            noerrorwin.close()

def solver(win,prob,sol):
    for i in range(len(sol)):
        a = prob[i]
        a.setText(sol[i])
        a.setTextColor('blue')


def main():
    # Draw Window
    win = GraphWin("Sudoku",700,700)
    win.setCoords(0,0,700,700)
    win.setBackground('white')
    # Draw Close Button
    close = Button(win,Point(39,20),56,23,'EXIT')
    close.activate()
    # Draw 1st Window View
    sudokulabel = Image(Point(350,350),'sudokulabel.gif')
    sudokulabel.draw(win)
    play = Button(win,Point(350,200),100,50,'PLAY')
    play.activate()
    t = 0
    while t==0:
        p = win.getMouse()
        if close.clicked(p):
            t = 2
            win.close()
        if play.clicked(p):
            t = 1
            sudokulabel.undraw()
            play.undraw()
            # Draw Difficulty Level Window
            difwin = GraphWin("Difficulty Level",350,350)
            difwin.setCoords(0,0,350,350)
            difwin.setBackground('white')
            level = diflevel(difwin)
            difwin.close()
            if level=='close':
                t = 2
                win.close()
            else:
                levellabel,check, solve, newgame = drawwin(win,level)
            if level=='beginner':
                prob,sol = beginner()
                lstprob = drawpuzzle(win,prob)
            elif level=='intermediate':
                prob,sol = intermediate()
                lstprob = drawpuzzle(win,prob)
            elif level=='hard':
                prob,sol = hard()
                lstprob = drawpuzzle(win,prob)
            while t==1:
                p = win.getMouse()
                if close.clicked(p):
                    t = 2
                    win.close()
                elif check.clicked(p):
                    checkresult = checker(win,lstprob,sol,close)
                    if checkresult==0:
                        noerror(check,solve)
                    if checkresult!=0:
                        answertoprompt = errorprompt(checkresult)
                        if answertoprompt=='close':
                            t = 2
                            win.close()
                        elif answertoprompt=='tryagain':
                            for i in range(len(lstprob)):
                                b = lstprob[i]
                                a = sol[i]
                                c = b.getText()
                                if c!='':
                                    c = int(c)
                                b.setTextColor('black')
                                if a!=c:
                                    b.setText('')
                elif solve.clicked(p):
                    solve.deactivate()
                    check.deactivate()
                    solver(win,lstprob,sol)
                    s = 0
                    while s==0:
                        p = win.getMouse()
                        if newgame.clicked(p):
                            s = 1
                            for i in range(len(lstprob)):
                                a = lstprob[i]
                                a.undraw()
                            difwin = GraphWin("Difficulty Level",350,350)
                            difwin.setCoords(0,0,350,350)
                            difwin.setBackground('white')
                            level = diflevel(difwin)
                            difwin.close()
                            levellabel.setText(level)
                            if level=='close':
                                t = 2
                                win.close()
                            if level=='beginner':
                                prob,sol = beginner()
                                lstprob = drawpuzzle(win,prob)
                            elif level=='intermediate':
                                prob,sol = intermediate()
                                lstprob = drawpuzzle(win,prob)
                            elif level=='hard':
                                prob,sol = hard()
                                lstprob = drawpuzzle(win,prob)
                            check.activate()
                            solve.activate()
                        elif close.clicked(p):
                            s = 1
                            t = 2
                            win.close()
                elif newgame.clicked(p):
                    check.deactivate()
                    solve.deactivate()
                    for i in range(len(lstprob)):
                        a = lstprob[i]
                        a.undraw()
                    difwin = GraphWin("Difficulty Level",350,350)
                    difwin.setCoords(0,0,350,350)
                    difwin.setBackground('white')
                    level = diflevel(difwin)
                    difwin.close()
                    levellabel.setText(level)
                    check.activate()
                    solve.activate()
                    if level=='close':
                        t = 2
                        win.close()
                    if level=='beginner':
                        prob,sol = beginner()
                        lstprob = drawpuzzle(win,prob)
                    elif level=='intermediate':
                        prob,sol = intermediate()
                        lstprob = drawpuzzle(win,prob)
                    elif level=='hard':
                        prob,sol = hard()
                        lstprob = drawpuzzle(win,prob)

main()
