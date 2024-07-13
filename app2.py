import flet as ft
from cadastrar_usuario import cadastrar_usuario

def main(page: ft.Page):

    page.window_width = 600

    campo_nome = ft.TextField(
        label='Digite seu nome: ',
        width=500,
        border_color=ft.colors.DEEP_ORANGE_700,
        )
    
    campo_email = ft.TextField(
        label='Digite seu email: ',
        width=500,
        border_color=ft.colors.DEEP_ORANGE_700
    )
    
    campo_senha = ft.TextField(
        label='Digite sua senha: ',
        width=500,
        border_color=ft.colors.DEEP_ORANGE_700,
        password = True
    )

    def executar_cadastro(e):
        try:
            nome = cadastrar_usuario(e, campo_nome, campo_email, campo_senha)
        except ValueError:
            page.open(ft.AlertDialog(title=ft.Text(f'Email inválido. Campo email deve conter @.')))
        except NameError:
            page.open(ft.AlertDialog(title=ft.Text(f'Email já cadastrado.')))
        else:
            page.update()
            page.open(ft.AlertDialog(title=ft.Text(f'Usuário {nome} cadastrado com sucesso!')))


    botao = ft.ElevatedButton(text="Cadastrar", on_click=executar_cadastro)

    linha_1 = ft.Row(
        controls=[campo_nome],
        alignment=ft.MainAxisAlignment.CENTER
    )

    linha_2 = ft.Row(
        controls=[campo_email],
        alignment=ft.MainAxisAlignment.CENTER
    )

    linha_3 = ft.Row(
        controls = [campo_senha],
        alignment=ft.MainAxisAlignment.CENTER
    )

    linha_4 = ft.Row(controls=[botao],
                     alignment=ft.MainAxisAlignment.CENTER)
    page.add(linha_1, linha_2, linha_3, linha_4)



    ...

ft.app(target=main)