import json
from validacoes import limpar_campos, validar_email, validar_email_ja_existente
 
def cadastrar_usuario(e, campo_nome, campo_email, campo_senha):
        with open('banco_app.json','r') as file:
            dicionario = json.load(file)

        nome = campo_nome.value
        email = campo_email.value 
        senha = campo_senha.value
        try:
            campos_texto = [campo_nome, campo_email, campo_senha]
            validar_email(campo_email)
            validar_email_ja_existente(campo_email)
        except ValueError:
            print('Email inválido. Campo email deve conter @.')
            raise ValueError
        except NameError:
            print('Email já cadastrado.') 
            raise NameError
        else:
        
            dicionario['nomes'].append(nome)
            dicionario['emails'].append(email)
            dicionario['senhas'].append(senha)

            with open('banco_app.json','w') as file:
                file.write(json.dumps(dicionario, indent=4))
        
            limpar_campos(campos_texto)

        return nome