import PySimpleGUI as sg
from hashids import Hashids

def criar_tela_login():
    sg.theme("DarkGrey11")
    opcoes = ["Hash", "ID"]

    layout = [
        [sg.Text("Configurações", size=(30,2), justification='center')],
        [sg.Text("Salt:           "),sg.Input(key="salt", size=(20,1),default_text='admin')],
        [sg.Text("Alphabet:    "),sg.Input(key="alphabet", size=(20,1),default_text='01234567890ABCDEFGHIJKLMNOPQRSTWUVXYZ')],
        [sg.Text("Min length : "),sg.Input(key="min_lenght", size=(20,1),default_text='6')],
        [sg.Text("")],
        [sg.Text("Escolha a ação: ")],
        [sg.Column([[sg.Text("Gerar:  "),sg.Combo(opcoes,default_value="Hash",key="checkbox")]],justification='center')],
        [sg.Column([[sg.Text("Hash/ID: "),sg.Input(key="hash_id", size=(10,1), default_text='')]],justification='center')],
        [sg.Column([[sg.Button("OK", key="ok", size=(5,1))]], justification='center')],
        [sg.Column([[sg.Text("Resultado: ",),sg.Input("", key="resultado", size=(20,1)) ]], justification='center')]
    ]
    window = sg.Window("Gerador HASH/ID", layout)
    monitorar_eventos(window)

# Monitorar eventos da tela
def monitorar_eventos(window):
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            window.close()
            break
        if event == "ok":
            valor_salt = values["salt"]
            valor_alphabet = values["alphabet"]
            valor_min_lenght = values["min_lenght"]
            checkbox = values["checkbox"]
            hashid = values["hash_id"]
            gerou_erro = verificar_configuracoes_hash(valor_alphabet, valor_min_lenght, hashid, checkbox)
            if gerou_erro is False:
                hashids = Hashids(salt=valor_salt, alphabet=valor_alphabet, min_length=valor_min_lenght)
                if checkbox == "Hash":
                    resultado = hashids.encode(int(hashid))
                    window["resultado"].update(resultado)
                if checkbox == "ID":
                    resultado = hashids.decode(hashid)
                    resultado = str(resultado).replace("(","").replace(")","").replace(",","")
                    if resultado == "":
                        criar_tela_erro(mensagem_erro="Não foi possivel gerar ID a partir dessa Hash com as configurações definidas \n Verifique a Hash inserida")
                    else:
                        window["resultado"].update(resultado)               

def verificar_configuracoes_hash(valor_alphabet, valor_min_lenght, hashid, checkbox, gerou_erro = False):
    global valor_alphabet_corrigido
    mensagem_erro = "Erro(s): \n"
    if valor_alphabet:
        valor_alphabet = set(valor_alphabet)
        total_caracteres = len(valor_alphabet)
        if total_caracteres < 16:
            gerou_erro = True
            mensagem_erro += "-Preencha o campo Alphabet com no minimo 16 caracteres diferentes \n"  
    else:
        gerou_erro = True
        mensagem_erro += "-Preencha o campo Alphabet \n"
    
    try:
        teste = int(valor_min_lenght)
    except ValueError:
        gerou_erro = True
        mensagem_erro += "-O valor do Min Lenght deve conter um número inteiro \n"

    if checkbox == 'Hash':
        try:
            teste = int(hashid)
        except ValueError:
            gerou_erro = True
            mensagem_erro += "-O valor do campo Hash/ID deve ser um número inteiro \n"  
    
    if hashid == '':
        gerou_erro = True
        mensagem_erro += "-Por favor preencha o campo Hash/Id \n"  

    if gerou_erro:
        criar_tela_erro(mensagem_erro)
    else:
        return gerou_erro

def criar_tela_erro(mensagem_erro):
    sg.theme("DarkGrey11")
    layout_erro = [
        [sg.Text(mensagem_erro, auto_size_text=True, justification='center')],
        [sg.Column([[sg.Button("OK", key="ok_erro", size=(5,1))]], justification='center')]
    ]
    window_erro = sg.Window("Erro", layout_erro)
    while True:
        event_erro = window_erro.read()
        if event_erro == sg.WIN_CLOSED or "ok_erro":
            window_erro.close()
            break
    
criar_tela_login()