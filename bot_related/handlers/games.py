from random import choice


def black_jack(day_balance, bet):
    pl_table = 0
    dil_table = 0
    pl_card = 0
    dil_card = 0
    fair=0
    def fair_checker():
        nonlocal fair
        if day_balance*0.3>bet:
            fair=1

    cards = [num for num in range(1, 12) for _ in range(4)]
    
    # ------------------------------------------------------------------------------
    def give_card(entity):
        # 1 - DIL / 0 - PL
        fair_checker()
        nonlocal cards
        if entity == 1:
            nonlocal dil_card, dil_table
            dil_card = choice(cards)
            while dil_table+dil_card>21:
                if fair==1:
                    break
                dil_card=choice(cards)
            cards.remove(dil_card)
            if dil_card==11 and dil_table+11>21:
                dil_table+=1
            else:
                dil_table += dil_card

            print("Диллеру выдана карта ", dil_card, " общая сумма ", dil_table)
        else:
            nonlocal pl_card, pl_table
            pl_card = choice(cards)
            while pl_table+pl_card==21:
                if fair==1:
                    break
                pl_card = choice(cards)
            cards.remove(pl_card)
            if pl_card==11 and dil_table+11>21:
                pl_table+=1
            else:
                pl_table += pl_card            
            print("Игроку выдана карта ", pl_card, " общая сумма ", pl_table)
        return
    # ------------------------------------------------------------------------------

    def checker(current_list, sum_cards):
        good = 0
        for i in current_list:
            if i + sum_cards < 21:
                good += 1
        return good / len(current_list)
    # ---------------------------------------------------------------------------------

    for x in range(2):
        if x == 1:
            give_card(1)
        give_card(0)
                
    answer = input("Вы хотите сделать дабл?\n")
    if answer == "Yes":
        # ПРОВЕРКА БАЛАНСА НА НАЛИЧИЕ ДЕНЕГ ДЛЯ ДАБЛА
        bet *= 2
        give_card(0)
        answer=None
        if pl_table > 21:
            print("У вас перебор")
            day_balance += bet
            return
    else:
        answer = input("Вы хотите взять еще 1 карту?\n")
    
    while answer == "Yes":
        give_card(0)
        if pl_table > 21:
            print("У вас перебор")
            day_balance += bet
            return
        answer = input("Вы хотите взять еще 1 карту?\n")
    
    while dil_table < pl_table and (pl_table!=dil_table and checker()<0.5 ):
        give_card(1)
        if dil_table > 21:
            print("У диллера перебор, вы выиграли ", bet*2)
            day_balance -= bet
            return
    if pl_table == dil_table:
        print("Ничья вы вернули ставку" )
        #НАДО В БД ВЕРНУТЬ СТАВКУ!!!!
    elif dil_table > pl_table:
        print("Вы проиграли ", bet)
    else:
        print("Вы выиграли ", bet * 2)
