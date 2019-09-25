import os
import sys
Elementos = []
class Elemento:
    def __init__(self, nome, simbolo, z, a, tipo, estado):
        self.nome = nome
        self.simbolo = simbolo
        self.z = z
        self.a = a
        self.tipo = tipo
        self.estado = estado
        Elementos.append(self)
hidrogenio = Elemento('Hidrogenio','H', 1, 1,'Nao metal','gasoso')
litio = Elemento('Litio','LI',3, 6,'Metal alcalino','solido')
sodio = Elemento('Sodio','Na', 11, 22,'Metal alcalino','solido')
potassio = Elemento('Potassio','K', 19, 39,'Metal alcalino','solido')
rubidio  = Elemento('Rubidio','Rb', 37, 85,'Metal alcalino','solido')
cesio = Elemento('Cesio','Cs', 55, 132,'Metal alcalino','solido')
francio = Elemento('Francio','Fr', 87, '223','Metal alcalino','solido')
berilio =  Elemento('Berilio','Be', 4, 9,'Metal alcalino-terroso','solido')
magnesio =  Elemento('Magnesio','Mg', 12, 24,'Metal alcalino-terroso','solido')
calcio =  Elemento('Calcio','Ca', 20, 40,'Metal alcalino-terroso','solido')
estroncio =  Elemento('Estroncio','Sr', 38, 87,'Metal alcalino-terroso','solido')
bario =  Elemento('Bario','Ba', 56, 137,'Metal alcalino-terroso','solido')
radio =  Elemento('Radio','Ra', 88, 226,'Metal alcalino-terroso','solido')
escandio =  Elemento('Escandio','Sc', 21, 44,'Metal de transicao','solido')
itrio = Elemento('Itrio','Y', 39, 88,'Metal de transicao','solido')
titanio = Elemento('Titanio','Ti', 22, 47,'Metal de transicao','solido')
zirconio = Elemento('Zirconio','Zr', 40, 90,'Metal de transicao','solido')
hafnio = Elemento('Hafnio','Hf', 72, 178,'Metal de transicao','solido')
rutherfordio = Elemento('Rutherfordio','Rf', 104, 261,'Metal de transicao','sintetico')
vanadio = Elemento('Vanadio','V', 23, 50,'Metal de transicao','solido')
niobio = Elemento('Niobio','Nb', 41, 92,'Metal de transicao','solido')
tantalio = Elemento('Tantalio','Ta', 73, 180,'Metal de transicao','solido')
dubnio = Elemento('Dubnio','Db', 105, 262,'Metal de transicao','sintetico')
cromo = Elemento('Cromo','Cr', 24, 51,'Metal de transicao','solido')
molibdenio = Elemento('Molibdenio','Mo', 42, 95,'Metal de transicao','solido')
tungstenio = Elemento('Tungstenio','W', 74, 183,'Metal de transicao','solido')
seaborgio = Elemento('Seaborgio','Sg', 106, 266,'Metal de transicao','sintetico')
manganes = Elemento('Manganes','Mn', 25, 54,'Metal de transicao','solido')
tecnecio = Elemento('Tecnecio','Tc', 43, 98,'Metal de transicao','sintetico')
renio = Elemento('Renio','Re', 75, 186,'Metal de transicao','solido')
bohrio = Elemento('Bohrio','Bh', 107, 264,'Metal de transicao','sintetico')
ferro = Elemento('Ferro','Fe', 26, 55,'Metal de transicao','solido')
rutenio = Elemento('Rutenio','Ru', 44, 101,'Metal de transicao','solido')
osmio = Elemento('Osmio','Os', 76, 190,'Metal de Metal','solido')
hassio = Elemento('Hassio','Hs', 108, 269,'Metal de transicao','sintetico')
cobalto = Elemento('Cobalto','Co', 27, 58,'Metal de transicao','solido')
rodio = Elemento('Rodio','Rh', 45, 102,'Metal de transicao','solido')
iridio = Elemento('Iridio','Ir', 77, 192,'Metal de transicao','solido')
meitnerio = Elemento('Meitnerio','Mt', 109, 268,'Metal de transicao','sintetico')
niquel = Elemento('Niquel','Ni', 28, 58,'Metal de transicao','solido')
paladio = Elemento('Paladio','Pd', 46, 106,'Metal de transicao','solido')
platina = Elemento('Platina','Pt', 78, 195,'Metal de transicao','solido')
darmstadio = Elemento('Darmstadio','Ds', 110, 271,'Metal de transicao','sintetico')
cobre = Elemento('Cobre','Cu', 29, 63,'Metal de transicao','solido')
prata = Elemento('Prata','Ag', 47, 107,'Metal de transicao','solido')
ourto = Elemento('Ouro','Au', 79, 196,'Metal de transicao','solido')
roentgenlum = Elemento('Roentgenlum','Rg', 111, 272,'Metal de transicao','sintetico')
zinco = Elemento('Zinco','Zn', 30, 65,'Metal de transicao','solido')
cadmio = Elemento('Cadmio','Cd', 48, 112,'Metal de transicao','solido')
mercurio = Elemento('Mercurio','Hg', 80, 200,'Metal de transicao','liquido')
copernicio = Elemento('Copernicio','Cn', 112, 285,'Metal de transicao','sintetico')
boro = Elemento('Boro','B', 5, 10,'Semimetal','solido')
carbono = Elemento('Carbono','C', 6, 12,'Nao metal','solido')
nitrogenio = Elemento('Nitrogenio','N', 7, 14,'Nao metal','gasoso')
oxigenio = Elemento('Oxigenio','O', 8, 15,'Nao metal','gasoso')
fluor = Elemento('Fluor','F', 9, 18,'Halogenio','gasoso')
helio = Elemento('Helio','He', 2, 4,'Gas nobre','gasoso')
neon = Elemento('Neon','Ne', 10, 20,'Gas nobre','gasoso')
aluminio = Elemento('Aluminio','Al', 13, 26,'Metal de pos transicao','solido')
galio = Elemento('Galio','Ga', 31, 69,'Metal de pos transicao','solido')
indio = Elemento('Indio','In', 49, 114,'Metal de pos transicao','solido')
talio = Elemento('Talio','Tl', 81, 204,'Metal de pos transicao','solido')
nihonio = Elemento('Nihonio','Nh', 113, 284,'Metal de pos transicao','sintetico')
silicio = Elemento('Silicio','Si', 14, 28,'Semimetal','solido')
germanio = Elemento('Germanio','Ge', 32, 72,'Semimetal','solido')
estanho = Elemento('Estanho','Sn', 50, 118,'Metal de pos transicao','solido')
chumbo = Elemento('Chumbo','Pb', 82, 207,'Metal de pos transicao','solido')
flerovio = Elemento('Flerovio','Fl', 114, 289,'Metal de pos transicao','sintetico')
fosforo = Elemento('Fosforo','P', 15, 30,'Nao metal','solido')
arsenio = Elemento('Arsenio','As', 33, 74,'Semimetal','solido')
antimonio = Elemento('Antimonio','Sb', 51, 121,'Semimtal','solido')
bismuto = Elemento('Bismuto','Bi', 83, 208,'Nao metal','solido')
moscovio = Elemento('Moscovio','Mc', 115, 293,'Metal pos transicao','sintetico')
enxofre = Elemento('Enxofre','S', 16, 32,'Nao metal','solido')
selenio = Elemento('Selenio','Se', 34, 78,'Nao metal','solido')
telurio = Elemento('Telurio','Te', 52, 127,'Semimetal','solido')
polonio = Elemento('Polonio','Po', 84, 209,'Semimetal','solido')
livemorio = Elemento('Livemorio','Lv', 116, 293,'Metal pos transicao','sintetico')
cloro = Elemento('Cloro','Cl', 17, 35,'Halogenio','gasoso')
bromo = Elemento('Bromo','Br', 35, 79,'Halogenio','liquido')
iodo = Elemento('Iodo','I', 53, 126,'Halogenio','solido')
astato = Elemento('Astato','At', 85, 210,'Halogenio','solido')
tenesso = Elemento('Tenesso','Ts', 117, 294,'Halogenio','sintetico')
argonio = Elemento('Argonio','Ar', 18, 39,'Gas nobre','gasoso')
criptonio = Elemento('Criptonio','Kr', 36, 83,'Gas nobre','gasoso')
xenonio = Elemento('Xenonio','Xe', 54, 131,'Gas nobre','gasoso')
radonio = Elemento('Radonio','Rn', 86, 222,'Gas nobre','gasoso')
oganessonio = Elemento('Oganessonio','Og', 118, 294,'Gas nobre','sintetico')
lantanio = Elemento('Lantanio','La', 57, 138,'Lantanoide','solido')
cerio = Elemento('Cerio','Ce', 58, 140,'Lantanoide','solido')
praseodimio = Elemento('Praseodimio','Pr', 59, 140,'Lantanoide','solido')
neodimio = Elemento('Neodimio','Nd', 60, 144,'Lantanoide','solido')
promecio = Elemento('Promecio','Pm', 61, 145,'Lantanoide','sintetico')
samario = Elemento('Samario','Sm', 62, 150,'Lantanoide','solido')
europio = Elemento('Europio','Eu', 63, 151,'Lantanoide','solido')
gadolinio = Elemento('Gadolinio','Gd', 64, 157,'Lantanoide','solido')
terbio = Elemento('Terbio','Tb', 65, 158,'Lantanoide','solido')
disprosio = Elemento('Disprosio','Dy', 66, 162,'Lantanoide','solido')
holmio = Elemento('Holmio','Ho', 67, 164,'Lantanoide','solido')
erbio = Elemento('Erbio','Er', 68, 167,'Lantanoide','solido')
tulio = Elemento('Tulio','Tm', 69, 168,'Lantanoide','solido')
iterbio = Elemento('Iterbio','Yb', 70, 173,'Lantanoide','solido')
lutencio = Elemento('Lutencio','Lu', 71, 174,'Lantanoide','solido')
actinio = Elemento('Actinio','Ac', 89, 227,'Actnoide','solido')
torio = Elemento('Torio','Th', 90, 232,'Actnoide','solido')
protactinio = Elemento('Protactinio','Pa', 91, 231,'Actnoide','solido')
uranio = Elemento('Uranio','U', 92, 238,'Actnoide','solido')
netunio = Elemento('Netunio','Np', 93, 237,'Actnoide','sintetico')
plutonio = Elemento('Plutonio','Pu', 94, 244,'Actnoide','sintetico')
americio = Elemento('Americio','Am', 95, 243,'Actnoide','sintetico')
curio = Elemento('Curio','Cm', 96, 247,'Actnoide','sintetico')
berquelio = Elemento('Berquelio','Bk', 97, 247,'Actnoide','sintetico')
californio = Elemento('Californio','Cf', 98, 251,'Actnoide','sintetico')
einstenio = Elemento('Einstenio','Es', 99, 252,'Actnoide','sintetico')
fermio = Elemento('Fermio','Fm', 100, 257,'Actnoide','sintetico')
mendelevio = Elemento('Mendelevio','Md', 101, 258,'Actnoide','sintetico')
nobelio = Elemento('Nobelio','No', 102, 259,'Actnoide','sintetico')
laurencio = Elemento('Laurencio','Lr', 103, 262,'Actnoide','sintetico')
from tkinter import *
import random
janela = Tk()
imagem = PhotoImage(file = "IMGMENU.gif")
pontos = 0
chances = 4
loop = None
class Menu:
    def __init__(self, parent):
        self.Parent = parent
        self.fundo = Label(parent ,image = imagem)
        self.fundo.place(relx=0.5, rely=0.5, anchor="c")
        
        self.texto = Label(parent ,background= '#3a3a3a', text="T A B E L A  P E R I O D I C A ", width=30,font=("Arial",16), fg="yellow")
        self.texto.place(relx=0.5, rely=0.2, anchor="c")
        
        self.BJogar = Button(self.fundo)
        self.BJogar.config(text="Jogar", background="#bfbfbf",width=64, font=("Arial", 8) ,command=self.Jogo)
        self.BJogar.place(relx=0.5, rely=0.45, anchor="c")

        self.BTabela = Button(self.fundo)
        self.BTabela.config(text="Tabela Periodica", background="#bfbfbf",width=64, font=("Arial",8))
        self.BTabela.place(relx=0.5, rely=0.5, anchor="c")

        self.BRank = Button(self.fundo)
        self.BRank.config(text="Pontuacao", background="#bfbfbf",width=64, font=("Arial",8))
        self.BRank.place(relx=0.5, rely=0.55, anchor="c")

        self.BSobre = Button(self.fundo)
        self.BSobre.config(text="Creditos", background="#bfbfbf",width=28, font=("Arial",8),  command=self.Creditos)
        self.BSobre.place(relx=0.4325, rely=0.6, anchor="c")

        self.BSair = Button(self.fundo)
        self.BSair.config(text="Sair", background="#bfbfbf",width=28, font=("Arial",8), command=Sair)
        self.BSair.place(relx=0.5672, rely=0.6, anchor="c")
        self.loop = None

        self.CSLabel = Frame(parent ,background="#6b6b6b", height=100)
        self.CSLabel2 = Frame(parent ,background="#6b6b6b", height=100)
        self.CCenter = Label(parent ,background="#3a3a3a", text=Creditos, fg="#d1fffc",font=("Arial",10))
        self.CSVoltar = Button(parent, width=90 , text="Voltar ao menu", font=("Arial",8), background="#22f7c2",highlightbackground="#29f721", command= lambda: self.VoltarMenu(2))
        self.RSVoltar = Button(parent, width=90 , text="Voltar ao menu", font=("Arial",8), background="#22f7c2",highlightbackground="#29f721", command= lambda: self.VoltarMenu(3))
        self.Save = " "
    def Escrever(self):
        try:
            escrever = self.Jogador.get("1.0",'end-1c')
            self.Perder.pack_forget()
            self.a = "%s:%s\n " %(escrever, str(pontos))
            self.Save = self.Save.replace(" ",self.a)
            print(self.Save)
            self.VoltarMenu(1)
        except:
            print('ok')
        
    def BotoesDoJogo(self, btao):
        global chances
        if chances != 0:
            global loop
            loop = janela.after(0, self.Jogo)
            if btao != Oescolhido.nome:
                print("tranquilo")
                chances -=1
                Sorteio()
            else:
                loop = janela.after(0, self.Jogo)
                global pontos
                pontos +=1
                print(btao)
                Sorteio()
        else:
            w = str(self.Parent.winfo_width())
            h = str(self.Parent.winfo_height())
            self.Perder = Label(self.Parent, width=(w), height =(h), background="#3a3a3a")
            self.FrameJo = Frame(self.Perder, width=150, height=50, background="#3a3a3a", )
            self.Jogador= Text(self.FrameJo, width="15",height="1",background="#d1fcff")
            self.PBotao = Button(self.Perder, width=20, text="Confirmar",command=self.Escrever)
            self.Perder.pack()
            self.FrameJo.place(relx=0.5, rely=0.5, anchor="c")
            self.PBotao.place(relx=0.425, rely=0.6)
            self.Jogador.pack()
    def Jogo(self):
        self.fundo.place_forget()
        self.texto.place_forget()
        
        self.Jinfo = Canvas(self.Parent, width=300, height =100, background="#3a3a3a")
        self.Jinfo.create_text(260,10, text="Nao metal",fill="#00ff37", font=("Arial", 8))
        self.Jinfo.create_text(170,10,text="Metal alcalino",fill="#ffb600", font=("Arial", 8))
        self.Jinfo.create_text(60,10,text="Metal alcalino - terroso",fill="#f6ff00", font=("Arial", 8))
        self.Jinfo.create_text(50,40,text="Metal de transicao",fill="#f32cf7", font=("Arial", 8))
        self.Jinfo.create_text(170,40,text="Semimetal",fill="#47f77c", font=("Arial", 8))
        self.Jinfo.create_text(260,40,text="Halogenio",fill="#00a9ff", font=("Arial", 8))
        self.Jinfo.create_text(60,70,text= "Gas nobre",fill="#00ffe5", font=("Arial", 8))
        self.Jinfo.create_text(170,70,text="Metal de pos transicao",fill="#77f96b", font=("Arial", 8))
        self.Jinfo.create_text(260,70,text="Lantanoide",fill="#ffbb00", font=("Arial", 8))
        self.Jinfo.create_text(60,90,text="Actnoide",fill="#ff0087", font=("Arial", 8))
        
        self.JElem = Label(self.Parent, width=400, height=400, background = "#3a3a3a")
        self.JBack = Canvas(self.JElem, width=100, height=100, background=corzinhaback())
        self.JBack.create_text(50,50, text=Oescolhido.simbolo,font=("Arial",30))
        self.JBack.create_text(19,10, text=Oescolhido.a,font=("Arial",14))
        self.JBack.create_text(19,90, text=Oescolhido.z,font=("Arial",14))

        self.JJanela = Canvas(self.Parent, width=300, height =100, background="#3a3a3a", highlightbackground="#ffd84c")
        self.JJanela.create_text(52,40, text="chances : "+ str(chances), fill="#ff5a3d", font=("Arial", 14))
        self.JJanela.create_text(55,60, text=" Pontos : "+ str(pontos), fill="#a9ff3a", font=("Arial",14))
        
        self.JMenu = Button(self.JJanela, width=30 ,background="#bfbfbf", text="Voltar ao menu")
        self.JMenu.config(command= lambda: self.VoltarMenu(1))

        self.JB1 = Button(self.Parent, width=20, background="#bfbfbf", text=B1.nome, command= lambda btao=B1.nome :self.BotoesDoJogo(btao))
        self.JB2 = Button(self.Parent, width=20, background="#bfbfbf", text=B2.nome, command= lambda btao=B2.nome :self.BotoesDoJogo(btao))
        self.JB3 = Button(self.Parent, width=20, background="#bfbfbf", text=B3.nome, command= lambda btao=B3.nome :self.BotoesDoJogo(btao))
        self.JB4 = Button(self.Parent, width=20, background="#bfbfbf", text=B4.nome, command= lambda btao=B4.nome :self.BotoesDoJogo(btao))
        
        self.JBack.pack()
        self.JMenu.place(relx=0.5, rely=0.2, anchor="c")
        self.JBack.pack()
        self.JMenu.place(relx=0.5, rely=0.2, anchor="c")
        self.JB1.place(relx=0.3, rely=0.6)
        self.JB2.place(relx=0.3, rely=0.7)
        self.JB3.place(relx=0.6, rely=0.6)
        self.JB4.place(relx=0.6, rely=0.7)
        self.JJanela.place(relx=0.01, rely=0.01)
        self.JElem.place(relx=0.5, rely=0.4, anchor="c")
        self.Jinfo.place(relx=0.4, rely=0.01)

    def cancelar(self, a):
        if a == 1:
            global lop
            loop = janela.after(0,tela(janela))
            print(loop)
            self.VoltarMenu(1)

    def VoltarMenu(self, a):
        print("voltou ao menu")
        global pontos
        pontos = 0
        print(pontos)
        global chances
        chances = 4
        print(chances)
        chances = 4
        if a == 1:
            self.cancelar(1)
        if a == 2:
            self.CSLabel.pack_forget()
            self.CCenter.pack_forget()
            self.CSLabel2.pack_forget()
            self.CSVoltar.destroy()
        if a == 3:
            self.RCenter.pack_forget()
            self.CSLabel.pack_forget()
            self.CSLabel2.pack_forget()
            self.RSVoltar.place_forget()
            
            
        self.BSair.place(relx=0.5672, rely=0.6, anchor="c")
        self.BSobre.place(relx=0.4325, rely=0.6, anchor="c")
        self.BRank.place(relx=0.5, rely=0.55, anchor="c")
        self.BTabela.place(relx=0.5, rely=0.5, anchor="c")
        self.BJogar.place(relx=0.5, rely=0.45, anchor="c")
        self.texto.place(relx=0.5, rely=0.2, anchor="c")
        self.fundo.place(relx=0.5, rely=0.5, anchor="c")
    def Creditos(self):
        self.fundo.place_forget()
        self.texto.place_forget()

        self.CSLabel.pack(fill=X)
        self.CCenter.pack(fill=X)
        self.CSLabel2.pack(side=BOTTOM,fill=X)
        self.CSVoltar.place(relx=0.5 ,rely=0.93, anchor="c")
    def Pontuacao(self):
        self.fundo.place_forget()
        self.texto.place_forget()               
        self.RCenter = Label(self.Parent ,background="#3a3a3a", text=self.Save, fg="#d1fffc",font=("Arial",10))
        self.CSLabel.pack(fill=X)
        self.RCenter.pack(fill=X)
        self.CSLabel2.pack(side=BOTTOM,fill=X)
        self.RSVoltar.place(relx=0.5 ,rely=0.93, anchor="c")
        
    

tela = Menu
def Sorteio():
    lista1=[]
    a = 0
    n = Elementos[0]
    
    while a <= 4:
        n = Elementos[random.randrange(0,118)]
        if n not in lista1 or n.tipo != "":
            lista1.append(n)
            a+=1
        else:
            a = a
    global Oescolhido
    Oescolhido = lista1[random.randrange(0,3)]
    global B1
    B1 = lista1[random.randrange(0,3)]
    lista1.remove(B1)
    global B2
    B2 = lista1[random.randrange(0,2)]
    lista1.remove(B2)
    global B3
    B3 = lista1[random.randrange(0,1)]
    lista1.remove(B3)
    global B4
    B4 = lista1[0]
    lista1.remove(B4)

def corzinhaback():
    if Oescolhido.tipo.lower() == "Nao metal".lower():
        return("#00ff37")
    elif Oescolhido.tipo.lower() == "Metal alcalino".lower():
        return("#ffb600")
    elif Oescolhido.tipo.lower() == "Metal alcalino - terroso".lower():
        return("#f6ff00")
    elif Oescolhido.tipo.lower() == "Metal de transicao".lower():
        return("#f32cf7")
    elif Oescolhido.tipo.lower() == "Semimetal".lower():
        return("#47f77c")
    elif Oescolhido.tipo.lower() == "Halogenio".lower():
        return("#00a9ff")
    elif Oescolhido.tipo.lower() == "Gas nobre".lower():
        return("#00ffe5")
    elif Oescolhido.tipo.lower() == "Metal de pos transicao".lower():
        return("#77f96b")
    elif Oescolhido.tipo.lower() == "Lantanoide".lower():
        return("#ffbb00")
    else:
        return("#ff0087")

def Sair():
    janela.destroy()
li=[]
li=[Elementos[random.randrange(0,118)], Elementos[random.randrange(0,118)], Elementos[random.randrange(0,118)], Elementos[random.randrange(0,118)]]
pontos = 0
chances = 4
Oescolhido = li[random.randrange(0,3)]
B1 = li[random.randrange(0,3)]
li.remove(B1)
B2 = li[random.randrange(0,2)]
li.remove(B2)
B3 = li[random.randrange(0,1)]
li.remove(B3)
B4 = li[0]
li.remove(B4)

Creditos = " \n Creditos: \n ESCOLA AYRTON SENNA \n A EQUIPE MAIS FODEROSA DA 118\n \n Diretor de arte: Yuri Guilherme Santos \n Equipe De Programadores: \n Yuri Guilherme Santos \n\n Linguagem: Python \n \n Participaçoes Especiais: \n \n Rafael \n Ana \n Gabriela\n \n Agradecimentos Especiais:\n Obg por comporem musicas legais \n Madeon \n Aurora \n Alan Walker\n \n \n \n "

    
janela.iconbitmap('icone.ico')
janela.title("Tabela periodica FIX")
janela.geometry("800x600+200+10")
janela["bg"] = "#3a3a3a"
tela(janela)
janela.mainloop()
