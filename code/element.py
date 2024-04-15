import os,time,keyboard


class Screen:
    def __init__(self) -> None:
        self.width,self.heigh=os.get_terminal_size()
        self.list_screen=self.set_screen_list()

    def set_screen_list(self)->list:
        return [" "]*self.width*(self.heigh-1)
    
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
        pass
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
    def place(self):
        Utilities().add_to_screen(self.master,self.text)

    



if __name__ == "__main__":
    fen=Screen()
    entry1=Entry(fen)
    entry1.place(3)
    print(entry1.run())




# class Utilitie:
#     def __init__(self,heigh,width,screen) -> None:
#         self.heigh=heigh
#         self.width=width
#         self.screen=screen
#         self.center=(width//2,heigh//2)
#     def clear_screen(self):
#         self.screen=[" "]*self.width*(self.heigh-1)
#     def password(self):
#         def add_char(char):
#             if char in list("azertyuiopqsdfghjklmwxcvbn,;:&é\"'(-è_çà)=12345678#~{[|`\^@]90°+?./§AZERTYUIOPQSDFGHJKLMWXCVBN!"):
#                 self.passw.append(char)
#                 forme[2]=["#",' ',' ',' '," "]+["*"]*len(self.passw)+["_"]*(10-len(self.passw))+[" ",' ',' ',' ',"#"]
#             elif char=="backspace":
#                 self.passw=self.passw[:-1]
#                 forme[2]=["#",' ',' ',' '," "]+["*"]*len(self.passw)+["_"]*(10-len(self.passw))+[" ",' ',' ',' ',"#"]
#         def affiche():
#             for i in range(len(forme)):
#                 if i!=2:
#                     forme[i]=list(forme[i])
#             for i in range(len(forme)):
#                 for j in range(len(forme[i])):
#                     self.screen[((self.center[1]-2)+i)*width+(self.center[0]-10+j)]=forme[i][j]
#             print(''.join(self.screen))
#         forme=["####################",
#                "#     Password     #",
#                "#    __________    #",
#                "####################"]
#         self.passw=[]
#         while len(self.passw)<10:
#             add_char(keyboard.read_key())
#             affiche()
#             time.sleep(0.2)
#         return ''.join(self.passw)
#     def select_choices(self,choix:list,pos):
#         def change(sens):
#             if 0<=self.cursor_pos+sens<len(choix):
#                 self.cursor_pos+=sens
#         def affiche():
#             for i in range(len(forme)):
#                 if i==self.cursor_pos:
#                     forme[i]=[">"]+forme[i][1:]
#                 else:
#                     forme[i]=[" "]+forme[i][1:]
#             for i in range(len(forme)):

#                 for j in range(len(forme[i])):
#                     self.screen[((pos[1])+i)*width+(pos[0]+j)]=forme[i][j]
#             print(''.join(self.screen))
#         forme=[]
#         self.cursor_pos=0
#         for i in choix:
#             forme.append(list(' '+i))
#         while True:
#             key=keyboard.read_key()
#             if key=="enter":
#                 break
#             elif key=='haut':
#                 change(-1)
#                 affiche()
#                 time.sleep(0.2)
#             elif key=="bas":
#                 change(1)
#                 affiche()
#                 time.sleep(0.2)
#         return choix[self.cursor_pos]
#     def entry(self,y_pos:int):
#         """
#         place un champ d'entrée a la position y \n
#         (le champ prend toute la taille de la console)
#         elle a pour fonction propre :\n
#          - add_char qui prend en parametre un caractère
#          - add_to_screen qui ajoute les elements à la list screen
#          - affiche_screen qui affiche l'ecran

#         """
#         def add_char(char:str)->None:
#             """
#             cette fonction permet d'ajouter les caractères taper a la phrase du champ d'entrée
#             """
#             if char in list("azertyuiopqsdfghjklmwxcvbn,;:&é\"'(-è_çà)=12345678#~{[|`\^@]90°+?./§AZERTYUIOPQSDFGHJKLMWXCVBN!"):
#                 self.text.append(char)
#             elif char=="backspace":
#                 self.text=self.text[:-1]
#             elif char=='space':
#                 self.text.append(' ')
#             forme[1]=[">"]+self.text+[" "]*(self.width-(len(self.text)+1))
#         def add_to_screen()->None:
#             """
#             cette fonction ajoute le champ d'entrée dans l'ecran
#             """
#             for i in range(len(forme)):
#                 for j in range(len(forme[i])):
#                     self.screen[((y_pos)+i)*width+(j)]=forme[i][j]
#         def affiche_screen()->None:
#             """
#             cette fonction affiche l'ecran
#             """
#             print(''.join(self.screen))
#         forme=[["-"]*width,[">"]+[" "]*(width-1),["-"]*width]
#         self.text=[]
#         add_to_screen()
#         affiche_screen()
#         time.sleep(1)
#         while True:
#             key=keyboard.read_key()
#             if key=="enter":
#                 break
#             add_char(key)
#             add_to_screen()
#             affiche_screen()
#             time.sleep(0.2)