import json

def limpar_campos(elementos):
    for elemento in elementos:
        elemento.value = ''

def validar_email(elemento):
    if '@' not in elemento.value:
        raise ValueError
    
def validar_email_ja_existente(elemento):
    with open('banco_app.json','r') as file:
        banco = json.load(file)
        banco['emails']
        
    if  elemento.value in banco['emails']:
        raise NameError