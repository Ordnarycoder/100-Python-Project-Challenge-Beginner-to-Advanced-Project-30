def guess_rainbow_colors():
    points = 0

    colors = {
        1 : "red",
        2 : "orange",
        3 : "yellow",
        4 : "green",
        5 : "blue",
        6 : "indigo",
        7 : "violet"
    }
    print("Please enter colors with order!")
    first_color = input("Please enter first color: ")
    second_color = input("Please enter second color: ")
    third_color = input("Please enter third color: ")
    fourth_color = input("Please enter fourth color: ")
    fifth_color = input("Please enter fifth color: ")
    sixth_color = input("Please enter sixth color: ")
    seventh_color = input("Please enter seventh color: ")
    if first_color == colors[1] and second_color == colors[2] and third_color == colors[3] and fourth_color == colors[4] and fifth_color == colors[5] and sixth_color == colors[6] and seventh_color == colors[7]:
        points += 7
    
    if points == 7:
        print("Congratulations!\nYou guessed all color right!")
    else:
        print("I think something's wrong with your colors!")
        
guess_rainbow_colors()
    