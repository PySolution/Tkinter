
#Módulos:

#Importa todas as funções do módulo tkinter:
import tkinter                          

#Cria as funções para os submenus:
def Novo_Arquivo():
    text_area.delete(1.0, "end")

def Salvar_Arquivo():
    conteudo = text_area.get(1.0, "end")
    file = open("notepad.txt", "w")
    file.write(conteudo)
    file.close()

def Abrir():
    file = open("notepad.txt", "r")
    conteudo = file.read()
    text_area.insert(1.0, conteudo)

#Cria uma função para o botão de atualizar o formato da fonte:
def AtualizarFonte():
    size = spin_font_size.get()
    font = spin_font_text.get()
    text_area.config(font="{} {}".format(font, size))


#Cria uma Janela:
window = tkinter.Tk()

#Insere um título na janela:
window.title("NotePad") 

#Tamanho mínimo da janela (Redimensionável manualmente somente para maior):
#window.minsize(width=1280, height=720)

#Informa o tamanho inicial da janela (Redimensionável para maior e menor): 
window.geometry("1280x720")             


#Cria um campo para escrita no tamanho da janela:
text_area = tkinter.Text(
    window, font = "Arial 20 bold", width=1280, height=720)

#Cria uma área (Barra Horizontal) dentro da janela para inserir algum objeto, com altura de 30px:
frame = tkinter.Frame(window, height=30)

#Empacota o frame dentro da janela e expande no eixo "x" conforme o tamanho da janela:
frame.pack(fill="x")

#Cria uma Label do lado esquerdo, dentro do frame, para indicar o tipo da fonte:
font_text = tkinter.Label(frame, text=" Fonte: ")
font_text.pack(side="left")

#Cria uma SpinBox dentro do frame para selecionar o tipo de Fonte:
spin_font_text = tkinter.Spinbox(frame, values=("Arial", "Verdana"))
spin_font_text.pack(side="left")

#Cria uma Label do lado esquerdo, dentro do frame, para indicar o tamanho da fonte:
text_size = tkinter.Label(frame, text=" Tamanho da Fonte: ")
text_size.pack(side="left")

#Cria uma SpinBox dentro do frame para selecionar o tamanho de Fonte:
spin_font_size = tkinter.Spinbox(frame, from_=10, to=60)
spin_font_size.pack(side="left")

#Cria um botão do lado esquerdo, dentro do frame, para atualizar o formato da fonte:
button_atualizar = tkinter.Button(frame, text="Atualizar", command=AtualizarFonte)
button_atualizar.pack(side="left")

#Empacota o widget dentro da janela:     
text_area.pack()                        

#Cria um menu principal na janela:
main_menu = tkinter.Menu(window) 

#Cria um submenu de opções dentro do menu principal(tearoff=0 Não permite deslocar o menu):
file_menu = tkinter.Menu(
    main_menu, tearoff=0)

#Cria os itens do submenu e suasrespectivas ações:
file_menu.add_command(
    label="Novo", command=Novo_Arquivo)                    
file_menu.add_command(
    label="Salvar", command=Salvar_Arquivo)                 
file_menu.add_command(
    label="Abrir", command=Abrir)                           
file_menu.add_command(
    label="Sair", command = window.quit)                    

#configura o menu principal no formato cascata, cria um nome e insere o submenu:
main_menu.add_cascade(
    label="Arquivo", menu=file_menu)

#Mostra o menu na janela:                       
window.config(menu = main_menu)           

#Mantém a janela ativa:
window.mainloop()                       
