from tkinter import messagebox,simpledialog
from scrapping import scrapping_func
import json
import os
from deep_translator import GoogleTranslator

json_path = "xddd.json"

def get_advices():
    
    numb_advices = simpledialog.askinteger(
        "Quantidade de Conselhos",
        "Quantos conselhos você quer pegar?",
        minvalue=1,
        maxvalue=100 
    )
    if numb_advices:
       
        advices = scrapping_func(numb_quotes=numb_advices)
        formatted_advices = "\n".join([f"ID: {slip.id}, Advice: '{slip.advice}'" for slip in advices])
        messagebox.showinfo(
            "Conselhos Coletados",
            f"Pegamos {numb_advices} conselhos pra você!\n\n{formatted_advices}"
            )
    return advices
    

def json_file(data, file_path):
    
    if os.path.exists(file_path):
        with open(file_path,'r') as file:
            try:
                existing_data = json.load(file)
            except json.JSONDecodeError:
                existing_data = []
    else:
        existing_data = []

    json_data = [slip.to_dict() for slip in data]
    existing_data.extend(json_data)

    with open(file_path,'w') as file:
        json.dump(existing_data,file, indent=4)

def retrieving_json_info(file_path = json_path):
    try:
        with open(file_path,'r') as file:            
                existing_data = json.load(file)
                return existing_data    
    except (TypeError,FileNotFoundError):
        messagebox.showerror(
            "Error","Algo deu errado com o arquivo, talvez voce nao tenha ele criado ainda. Por favor tente pegar conselhos e salvo-los antes."
            )

def delete_everything():
    if os.path.exists(json_path):
        os.remove(json_path)
        messagebox.showinfo(
            "Deletando conselhos" ,"Dando tchau pros conselhos passados"
            )
    else:
        messagebox.showinfo(
            "Erro" ,"Voce nao tem nenhum conselho salvo, entao como voce quer deleta-los?????"
            )

def translate_from_english_memory(data):
    print("memory")
def translate_from_english_json():
    existing_data = retrieving_json_info()
    formatted_advices_pt = "\n".join(
        [f"ID: {advices["id"]}, Conselho: '{GoogleTranslator('en','pt').translate(advices['advice'])}'" for advices in existing_data]
        )  
    messagebox.showinfo("Conselhos traduzidos" ,f"{formatted_advices_pt}")



    

if __name__ == "__main__":
    #testeeeee
    aaaaa = [
        {"id": 3, "advice": "Never set an alarm clock unless you know how to switch it off"},
        {"id": 1, "advice": "Always carry a notebook"},
        {"id": 2, "advice": "Smile more often"}
    ]
    json_file(aaaaa,'xddd.json')
    
