from element import Screen,Utilities,Entry,Label,Menu
import time

if __name__=="__main__":
    print("debut des testes")
    fen=Screen()
    entry1=Entry(fen)
    entry1.place(3)
    print(entry1.run())
    label=Label(fen,"bonjour")
    label.place(10,8)
    fen.affiche_screen()
    time.sleep(3)
    fen.clear()
    fen.affiche_screen()
    menu=Menu(fen,["choix 1","choix 2","choix 3"],40,10)
    choix=menu.run()
    print(choix)


    
