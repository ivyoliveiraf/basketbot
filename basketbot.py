# Mini Bot de Perguntas sobre Python
print("Olá, eu sou o BasketBot!")
print("Digite 'sair' para encerrar a conversa.\n")

while True:
    pergunta = input("Você: ").strip().lower()

    if pergunta == "sair":
        print("BasketBot: Valeu! Até a próxima!")
        break

    elif "nba" in pergunta:
        print("A nova temporada da NBA começa em outubro. Os favoritos este ano são os Celtics, Nuggets e Bucks.")

    elif "jogadores" in pergunta or "jogador" in pergunta:
        print("Alguns dos melhores jogadores atualmente são Nikola Jokic, Giannis Antetokounmpo, Luka Doncic e Stephen Curry.")

    elif "times" in pergunta or "time" in pergunta:
        print("Times populares incluem o Los Angeles Lakers, Golden State Warriors, Boston Celtics e Miami Heat.")

    elif "estatísticas" in pergunta or "stats" in pergunta:
        print("Jokic teve médias de quase um triplo-duplo na última temporada, com mais de 26 pontos, 12 rebotes e 9 assistências por jogo.")

    elif "títulos" in pergunta or "campeonatos" in pergunta:
        print("Os Boston Celtics e os Los Angeles Lakers são os maiores campeões da NBA, com 17 títulos cada.")

    elif "história" in pergunta or "histórico" in pergunta:
        print("A NBA foi fundada em 1946. Lendas como Michael Jordan, Kobe Bryant e LeBron James marcaram gerações.")

    else:
        print("Hmmm... não entendi. Pergunte sobre NBA, jogadores, times, estatísticas, títulos ou história.")

