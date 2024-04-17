import os,time,keyboard


class Screen:
    """
    class pour l'écran principal ce sera le master de toutes les autres class
    """
    def __init__(self) -> None:
        """
        initialisation de l'écran (taille et liste pour l'affichage)
        """
        # récupère la taille du terminal pour que ce soit la taille de la liste
        self.width,self.heigh=os.get_terminal_size()
        # met en place la liste qui va contenir l'affichage de l'écran
        self.list_screen=self.set_screen_list()

    def set_screen_list(self)->list:
        """
        utilise la taille du terminal pour générer une liste de la taille
        de celui ci afin de pouvoir afficher des elements a des position
        precise de l'écran
        """
        return [" "]*self.width*(self.heigh-1)
    
    def clear(self)->list:
        """
        remplace la liste de l'écran par une liste vierge
        """
        self.list_screen=self.set_screen_list()
    
    def affiche_screen(self)->bool:
        """
        affiche l'écran qui est une liste.
        """
        print(''.join(self.list_screen))
    


class Utilities(Screen):
    """
    class pour toutes les fonctions que se serait répéter dans
    les classes des widgets
    """
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
    """
    class pour un champ de saisie
    """
    def __init__(self,master:Screen,text:str=""):
        """
        le master est un object de la classe Screen
        le texte est celui a mettre dans le champs d'enter
        avant toute saisie
        """
        self.master=master
        self.text=list(text)
        self.forme=self.set_up_forme()
        self.x_pos=0
        self.y_pos=0

    def set_up_forme(self,text:list=[]):
        """
        assemble les différents composants de l'affichage du
        champ d'enter 
        """
        champ=list(">"+"".join(text))
        print(len(champ))
        forme=[["-"]*self.master.width,champ+[" "]*(self.master.width-len(champ)),["-"]*self.master.width]
        return forme

    def place(self,y_pos:int):
        """
        permet d'afficher l'entrer a une position y
        Attention : sans cette fonction l'affichage ne sera pas effectuer
        """
        self.y_pos=y_pos
        Utilities().add_to_screen(self.master,self.forme,y_pos=y_pos)

    def run(self):
        """
        fonction principal qui s'occupe d’enregistrer la saisie
        et de l'afficher sur l'écran
        """
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
    """
    class pour afficher un texte a l'écran
    """
    def __init__(self,master:Screen,text:str="") -> None:
        """
        le master est un object de la classe Screen
        le texte est celui a afficher
        """
        self.master=master
        self.text=[text]

    def add_line(self,new_text:str):
        """
        ajoute une novelle ligne au texte
        """
        self.text.append(new_text)

    def place(self,pos_x:int,pos_y:int):
        """
        permet d'afficher l'entrer a une position x,y
        Attention : sans cette fonction l'affichage ne sera pas effectuer
        """
        Utilities().add_to_screen(self.master,self.text,pos_x,pos_y)
        self.master.affiche_screen()

class Menu:
    """
    class pour la gestion de menu
    """
    def __init__(self,master:Screen,choix:list,pos_x:int,pos_y:int) -> None:
        """
        le master est un object de la classe Screen
        le paramètre choix est une liste de str qui comprend
        les différentes option du menu
        pos_x est la position en x
        respectivement pour pos_y
        """
        self.master=master
        self.cursor_pos=0
        self.choix=choix
        self.forme=[]
        self.pos_x=pos_x
        self.pos_y=pos_y

    def change(self,sens:int):
        """
        fonction pour switcher d'option sur le menu
        """
        if 0<=self.cursor_pos+sens<len(self.choix):
            self.cursor_pos+=sens

    def setup_forme(self):
        """
        assemble les différents composants de l'affichage
        du menu
        """
        for i in range(len(self.forme)):
            if i==self.cursor_pos:
                self.forme[i]=[">"]+self.forme[i][1:]
            else:
                self.forme[i]=[" "]+self.forme[i][1:]
        Utilities().add_to_screen(self.master,self.forme,self.pos_x,self.pos_y)
        self.master.affiche_screen()

    def run(self):
        """
        fonction principal qui permet de sectionner l'option
        et d'afficher les transition a l'écran
        """
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
