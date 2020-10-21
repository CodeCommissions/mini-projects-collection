import turtle


def get_players(total_players):
    players = [turtle.Turtle() for total_players in range(total_players)]
    colors = ["blue", "dark red", "violet", "orange"]
    coords = [[-150, 0], [150,0], [0, 150], [0, -150]]
    for i in range(total_players):
        player = players[i]
        player.penup()
        player.goto(coords[i][0], coords[i][1])
        player.pendown()
        player.color(colors[i])

    return players


players = get_players(2)
sam, alex = players[0], players[1]

# # # # # # Competition Zone # # # # # # :





turtle.mainloop()