def winner(drag1_time,drag2_time):    

    drag1_speed = dist/drag1_time
    drag2_speed = dist/drag2_time

    if drag1_speed > drag2_speed:
        winner = "Dragao 1"
        return winner
    elif drag2_speed > drag1_speed:
        winner = "Dragao 2"
        return winner
    else:
        winner = "Dragao 1 e Dragao 2, pois tem a mesma velocidade"
        return winner
    
if __name__ == "__main__":
    dist = 1000
    print("VAMOS AGORA DECIDIR O VENCEDOR DA PARTIDA!!")
    drag1_time = float(input("Em quantas horas o dragao 1 percorreu nosso percurso? "))    
    drag2_time = float(input("Em quantas horas o dragao 2 percorreu nosso percurso? "))
    drag_winner = winner(drag1_time, drag2_time)
    print(f"O vencedor da corrida de dragao foi o: {drag_winner}!!")
   