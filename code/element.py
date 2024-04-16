import os,time,keyboard


class Screen:
    def __init__(self) -> None:
        self.width,self.heigh=os.get_terminal_size()
        self.list_screen=self.set_screen_list()

    def set_screen_list(self)->list:
        return [" "]*self.width*(self.heigh-1)
    
    def clear(self):
        self.list_screen=self.set_screen_list()
    
    def affiche_screen(self)->bool:
        """
        affiche l'écran qui est une liste.
        """
        print(''.join(self.list_screen))
    


class Utilities(Screen):
    def __init__(self) -> None:
        pass
    def add_char_to_list(self,char:str,liste:list)->list:
        """
        vérifie si le caractère est dans ceux autorisé et si c'est le cas l'ajoute à la liste. 
        """
        if char in list("azertyuiopqsdfghjklmwxcvbn,;:&é\"'(-è_çà)=12345678#~{[|`\^@]90°+?./§AZERTYUIOPQSDFGHJKLMWXCVBN!"):
            liste.append(char)
        elif char=="backspace":
            liste=liste[:-1]
        elif char=="space":
            liste.append(' ')
        return liste
    def add_to_screen(self,master:Screen,forme:list,x_pos:int=0,y_pos:int=0)->list:
        """
        cette fonction ajoute le champ d'entrée dans l'écran
        """
        for i in range(len(forme)):
            for j in range(len(forme[i])):
                master.list_screen[((y_pos)+i)*master.width+(x_pos+j)]=forme[i][j]

class Entry:
    def __init__(self,master:Screen,text:str=""):
        self.master=master
        self.text=list(text)
        self.forme=self.set_up_forme()
        self.x_pos=0
        self.y_pos=0
    def set_up_forme(self,text:list=[]):
        forme=[["-"]*self.master.width,list(">"+"".join(text)),["-"]*self.master.width]
        return forme
    def place(self,y_pos:int):
        self.y_pos=y_pos
        Utilities().add_to_screen(self.master,self.forme,y_pos=y_pos)

    def run(self):
        self.master.affiche_screen()
        while True:
            key=keyboard.read_key()
            if key=="enter":
                break
            self.text=Utilities().add_char_to_list(key,self.text)
            self.forme=self.set_up_forme(self.text)
            self.place(self.y_pos)
            self.master.affiche_screen()
            time.sleep(0.1)
        time.sleep(0.5)
        self.forme=self.set_up_forme([" "]*self.master.width)
        self.place(self.y_pos)
        self.master.affiche_screen()
        return "".join(self.text)

class Label:
    def __init__(self,master,text="") -> None:
        self.master=master
        self.text=[text]
    def add_line(self,new_text):
        self.text.append(new_text)
    def place(self,pos_x,pos_y):
        Utilities().add_to_screen(self.master,self.text,pos_x,pos_y)
        self.master.affiche_screen()

class Menu:
    def __init__(self,master,choix:list,pos_x:int,pos_y:int) -> None:
        self.master=master
        self.cursor_pos=0
        self.choix=choix
        self.forme=[]
        self.pos_x=pos_x
        self.pos_y=pos_y
    def change(self,sens):
        if 0<=self.cursor_pos+sens<len(self.choix):
            self.cursor_pos+=sens
    def setup_forme(self):
        for i in range(len(self.forme)):
            if i==self.cursor_pos:
                self.forme[i]=[">"]+self.forme[i][1:]
            else:
                self.forme[i]=[" "]+self.forme[i][1:]
        Utilities().add_to_screen(self.master,self.forme,self.pos_x,self.pos_y)
        self.master.affiche_screen()
    def run(self):
        self.cursor_pos=0
        for i in self.choix:
            self.forme.append(list(' '+i))
        self.master.affiche_screen()
        while True:
            key=keyboard.read_key()
            if key=="enter":
                break
            elif key=='haut':
                self.change(-1)
                self.setup_forme()
                time.sleep(0.2)
            elif key=="bas":
                self.change(1)
                self.setup_forme()
                time.sleep(0.2)
        return self.choix[self.cursor_pos]
