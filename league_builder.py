import csv  #Need to import module to read csv.

#Have to make sure to use Dunder main in order to make sure that this file runs only when called, and not just because of import.

if __name__ == "__main__":

    #Setting up the arrays to gather information read from the csb and organize it accordingly.

    names = []
    heights = []
    experience = []
    parents = []
    sharks = []
    dragons = []
    raptors = []

    #Opening csv and taking the players names, heights, experiences, and parents out of the csv and into the arrays I created.

    with open('soccer_players.csv') as csvfile:
        soccer_players = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in soccer_players:
            names.append(row[0])
            heights.append(row[1])
            experience.append(row[2])
            parents.append(row[3])

    #Deleting the unnecessary titles for each row so that they don't appear in the teams.txt

    del names[0]
    del heights[0]
    del experience[0]
    del parents[0]

    #Zipping of all the arrays into a neat and clean little set for the sake of iteration

    zip_object = zip(names, heights, experience, parents)
    clean_set = set(zip_object)

    #Setting up variables to hold the team allocation.
    #Each number corresponds with a team: 1 is Sharks, 2 is Dragons, 3 is Raptors.
    #Two different sets of counts for experienced and unexperienced players.

    exp_count = 1
    count = 1

    #Iteration through the set to check for a: player has experience
    # b: to make sure each team gets the same amount of experienced players (IE 3 exp players and 3 unexp players per team)
    #This is done using the count variables to essentially limit the amount of experienced players per team (done via incremental placement)

    for player in clean_set:
        exp = player[2]
        if exp == "YES":
            if exp_count == 1:
                sharks.append(player)
            elif exp_count == 2:
                dragons.append(player)
            elif exp_count == 3:
                raptors.append(player)
            if exp_count == 3:
                exp_count = 1
            else:
                exp_count += 1
        else:
            if count == 1:
                sharks.append(player)
            elif count == 2:
                dragons.append(player)
            elif count == 3:
                raptors.append(player)
            if count == 3:
                count = 1
            else:
                count += 1

    #Creating a file and writing the necessary information to it via 3 FOR loops.
    #Ends with closing the file when done.

    file = open("teams.txt", "w")
    file.write("Sharks\n")
    for shark in sharks:
        shark_read = ", ".join(shark)
        file.write("\n")
        file.write(shark_read)
    file.write("\n\nDragons\n")
    for dragon in dragons:
        dragon_read = ", ".join(dragon)
        file.write("\n")
        file.write(dragon_read)
    file.write("\n\nRaptors\n")
    for raptor in raptors:
        raptor_read = ", ".join(raptor)
        file.write("\n")
        file.write(raptor_read)
    file.close
