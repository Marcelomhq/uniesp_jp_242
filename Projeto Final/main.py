import scrapping
import functions
import tkinter as tk
from tkinter import messagebox,simpledialog
import os
import lib_classes
import menu_boxes


app = tk.Tk()
app.title("Seu Zé: Conselhos Digitais para um Negócio Arretado!")
app.geometry("650x350")
button_width = 50
extra_menu_button_width = 35

icon_image = tk.PhotoImage(file="Logo.png")
app.iconphoto(False,icon_image)

label = tk.Label(app, text="© Made by MarceloHQ", font=("Arial", 10), fg="black")
label.place(relx=1.0, rely=1.0, anchor="se")

advices_data = None

def fetch_advices():
    global advices_data
    try:
        advices_data = functions.get_advices()
    except Exception:
        messagebox.showinfo("Erro")

def save_advices():
    global advices_data
    if advices_data:
        functions.json_file(advices_data,'xddd.json')
        menu_boxes.custom_message_box("Salvar Conselhos", "Seus conselhos foram salvos com sucesso!")
        advices_data = None
    else:
        messagebox.showerror(
            "Erro", "Voce precisa primeiro pegar conselhos antes de salvá-los!"
            )

def retrieve_advices():
    global advices_data

    if advices_data:
        messagebox.showinfo(
            "Voce ja tem conselhos salvos na memoria, por genteliza salve-os antes de pegar os conselhos salvos"
            )
    else:
        advices_data = functions.retrieving_json_info()
        if advices_data:
            formatted_advices = "\n".join(
                [f"ID: {advices["id"]}, Advice: '{advices["advice"]}'" for advices in advices_data]
                )        
            messagebox.showinfo(
                "Mostrando conselhos salvos anteriormente" ,f"{formatted_advices}"
                )
            #colocando isso aqui so pq tava dando bug com chamava opcao 3 e dps a 2. futuramente vou resolver
            advices_data = None

def retrieve_advices_translate():
    if advices_data:
        functions.translate_from_english_memory(advices_data)
    else:
        messagebox.showerror(
            "Erro", "Voce nao tem conselhos na memoria entao como quer traduzi-los???? Va pegar conselho omii!!!!"
            )

def saved_advices_translate():
    if os.path.exists(functions.json_path):
        functions.translate_from_english_json()
    else:
        messagebox.showerror(
            "Erro", "Voce nao tem conselhos salvos nesse computador entao como quer traduzi-los???? Va pegar conselho e depois salvar-los antes de vir aqui omii!!!!"
            )


def exit_app():
    app.destroy()

def extra_menu():
    extra_menu = tk.Toplevel(app)
    extra_menu.title("Menu de traducao")
    extra_menu.geometry('400x300')

    extra_menu.transient(app)
    extra_menu.grab_set()

    tk.Label(
        extra_menu, text="Funcionalidades de traducao", font=("Arial",16)
        ).pack(pady=10)

    tk.Button(
        extra_menu, text="1. Traduzir que estao na memoria",width=extra_menu_button_width, command=retrieve_advices_translate
        ).pack(pady=5)
    tk.Button(
        extra_menu, text="2. Traduzir conselhos ja salvos",width=extra_menu_button_width, command=saved_advices_translate
        ).pack(pady=5)
    tk.Button(
        extra_menu, text="3. Voltar ao menu principal",width=extra_menu_button_width, command=extra_menu.destroy
        ).pack(pady=5)


tk.Label(
    app, text=" Bem-Vindo a Missão Secreta da Cachaçaria do Seu Zé:\nConselhos Digitais para um Negócio Arretado!", font=("Arial", 16)
    ).pack(pady=10)
tk.Button(
    app, text="1. Pegue novos conselhos aqui!!",width=button_width, command=fetch_advices
    ).pack(pady=5)
tk.Button(
    app, text="2. Salvar conselhos para o futuro!!",width=button_width, command=save_advices
    ).pack(pady=5)
tk.Button(
    app, text="3. Ler conselhos do passado!!",width=button_width, command=retrieve_advices
    ).pack(pady=5)
tk.Button(
    app, text="4. Deletar todos os conselhos salvos e comecar do zero!!",width=button_width, command=functions.delete_everything
    ).pack(pady=5)
tk.Button(
    app, text="5. Traduzir conselhos do ingles, caso voce nao saiba ingles",width=button_width, command=extra_menu
    ).pack(pady=5)
tk.Button(
    app, text="6. Sair",width=button_width, command=exit_app
    ).pack(pady=5)

if __name__ == "__main__":
    app.mainloop()


