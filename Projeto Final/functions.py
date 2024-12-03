from tkinter import messagebox,simpledialog
from scrapping import scrapping_func
import json
import os
from deep_translator import GoogleTranslator
import menu_boxes

json_path = "xddd.json"
flag_path = "pt-br-flag.png"

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
        menu_boxes.custom_message_box(
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
        menu_boxes.custom_message_box(
            "Error","Algo deu errado com o arquivo, talvez voce nao tenha ele criado ainda. Por favor tente pegar conselhos e salvo-los antes."
            )

def delete_everything():
    if os.path.exists(json_path):
        os.remove(json_path)
        menu_boxes.custom_message_box(
            "Deletando conselhos" ,"Dando tchau pros conselhos passados"
            )
    else:
        menu_boxes.custom_message_box(
            "Erro" ,"Voce nao tem nenhum conselho salvo, entao como voce quer deleta-los?????"
            )

def translate_from_english_memory(data):
    formatted_advices_pt = "\n".join(
        [f"ID: {advices.id}, Conselho: '{GoogleTranslator('en','pt').translate(advices.advice)}'" for advices in data]
        )  
    menu_boxes.custom_message_box("Conselhos traduzidos" ,f"{formatted_advices_pt}",flag_path)
    
def translate_from_english_json():
    existing_data = retrieving_json_info()
    formatted_advices_pt = "\n".join(
        [f"ID: {advices["id"]}, Conselho: '{GoogleTranslator('en','pt').translate(advices['advice'])}'" for advices in existing_data]
        )  
    menu_boxes.custom_message_box("Conselhos traduzidos" ,f"{formatted_advices_pt}",flag_path)

def About():
    menu_boxes.custom_message_box("Info sobre este software" ,"Este programa foi feito usando por Marcelo Honorato Queiroga como Projeto Final da matéria de Introdução a Programa, ministrada pelo Professor Messias Batista, para o curso de Sistemas para Internet, turno Noite. Interface feita utilizando TkInter.")


    

if __name__ == "__main__":
    #testeeeee
    aaaaa = [
        {"id": 3, "advice": "Never set an alarm clock unless you know how to switch it off"},
        {"id": 1, "advice": "Always carry a notebook"},
        {"id": 2, "advice": "Smile more often"}
    ]
    json_file(aaaaa,'xddd.json')
    
