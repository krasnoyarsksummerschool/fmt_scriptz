#!/usr/bin/python
#
# adapted from
#http://www.pythonware.com/library/tkinter/introduction/dialog-windows.htm#AEN1500
#
from Tkinter import *
import os
import schedule
import pickle

class Dialog(Toplevel):

    def __init__(self, parent, title = ""):

        Toplevel.__init__(self, parent)
        self.transient(parent)

        if title:
            self.title(title)

        self.parent = parent

        self.result = None

        body = Frame(self)
        self.initial_focus = self.body(body)
        body.pack(padx=5, pady=5)

        self.buttonbox()

        self.grab_set()

        #if not self.initial_focus:
        #    self.initial_focus = self

        #self.protocol("WM_DELETE_WINDOW", self.cancel)

        self.geometry("+%d+%d" % (parent.winfo_rootx()+50,
                                  parent.winfo_rooty()+50))

        self.wait_window(self)


    ############################ Create the dialog w/ entryfields
    def body(self, master):
      # labeling:
      for j in range(4):
        Label(master, text=str(j+1)+': time').grid(row=0, column=2*j+1)
        Label(master, text='score').grid(row=0,column=2*j+2)

      self.entryfields={}
      for i,t in enumerate(schedule.svalka):

        Label(master, text=schedule.latex2greek[t['TEAM']]+":", font='System 11 roman').grid(row=i+1, sticky=E, pady=3)

        this_e = []
        for j in range(4):
          #time
          self.et = Entry(master)
          self.et.grid(row=i+1, column=2*j+1)
          self.et.config(width=5, font=('Verdana 11 roman') )
          self.et.bind('<Escape>',self._clear)  

          # score
          self.es= Entry(master)
          self.es.grid(row=i+1, column = 2*j+2, padx=12)
          self.es.config(width=3)
          self.es.bind('<Escape>',self._clear)  

          this_e.append((self.et,self.es))
          self.entryfields[ t['TEAM'] ] = (i, this_e)  # i is the index in schedule.svalka

      Label(master,text="Esc: clears the field\t Enter: recomputes the rankings", font='Verdana 11 italic').grid(row=i+2, sticky=W,columnspan=9)
      Label(master, text="Enter times in mins<no space>secs, e.g. 1856 is 18m56s, 101 is 1m1s etc ", font='Verdana 11 italic').grid(row=i+3, sticky=W, columnspan=9)

      # TheMainThing
      self.bind('<Return>', self.recompute )


    def buttonbox(self):
        # add standard button box. override if you don't want the
        # standard buttons
        box = Frame(self)

        w = Button(box, text="Load", width=10, command=self.load)
        w.pack(side=RIGHT, padx=5, pady=5)
        w = Button(box, text="Recompute", width=10, command=self.recompute)
        w.pack(side=RIGHT, padx=5, pady=5)

        box.pack()

    def load(self, event=None):  #FIXME
        for team in schedule.svalka:
          entry = self.entryfields[team['TEAM']][1]
          for s,e in zip( team['SCORES'],entry ):
             e[0].delete( 0,END )
             e[0].config(background='#FFFFFF')
             # convert seconds back to mins<no space>secs
             if s[0] != None: 
                  mins, secs = str(s[0]/60), str(s[0]%60)
                  if mins=='0': mins=''
                  if len(secs)==1: secs = '0'+secs 
                  e[0].insert(0,mins+secs)

             e[1].delete(0,END)
             e[1].config(background='#FFFFFF')
             if s[1] != 0: e[1].insert(0,str(s[1]))
        return None

    # <Escape> clears the entry field
    def _clear(self,event):
      self.focus_get().delete(0,END)
      self.focus_get().config(background='#FFFFFF')
      return None


    ######################################## TheMainThing
    def recompute(self,event=None):
      # if it was red, change it to white
      where_focus=self.focus_get()
      if where_focus != self: where_focus.config(background="#FFFFFF")

      for team in self.entryfields.keys():
        idx=self.entryfields[team][0]
        for j,prblm in enumerate( self.entryfields[team][1] ):
           is_ok, time, score = self._evaluate(prblm)
           if not is_ok: 
              return False
           schedule.svalka[idx]['SCORES'][j] = (time,score)     
      svalka_file=open('svalka.pkl','wb')
      pickle.dump(schedule.svalka, svalka_file)
      svalka_file.close()
      os.system('./final_ordered_list')
      return True


    # validate the 'zayavka'. If ok, return time in secs and score
    def _evaluate(self,prblm):
      strTime, strScore = prblm[0].get(), prblm[1].get()
      if len(strTime)==0 and len(strScore)==0: # net zayavki
         return True, None, 0
      else:
         # both must be non-empty
         if len(strTime)==0 and len(strScore)>0:
            self._signal_err(prblm[0])
            return False, -101,-101
         if len(strTime)>0 and len(strScore)==0:
            self._signal_err(prblm[1])
            return False, -101,-101

         if not (strTime.isdigit() or strTime=='None'):
           self._signal_err(prblm[0])
           return False, -101, -101
         if not strScore.isdigit():
           self._signal_err(prblm[1])
           return False, -101, -101

         #score
         score = int(strScore)
         if score<0 or score>2:
           self._signal_err(prblm[1])
           return False, -101,-101

         #time
         if strTime=='None': 
           return True, None, 0
         else:
           rawTime = int(strTime)

           mins, secs = rawTime/100, rawTime%100 
           if 0<=mins<=20  and 0<=secs<=59:
             time = mins*60+secs  # convert to seconds  
           else:
             self._signal_err(prblm[0])
             return False, -101,-101

         return True, time,score 

      
    def _signal_err(self,entrybox):
      entrybox.config(background='#FF1111')
      return None


