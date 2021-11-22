def main():
    
    infile = open('WorldSeriesWinners.txt', 'r')

    winnerslist = infile.read().splitlines()

    infile.close()

    teamname = input('Enter a team name: ')
    
    numberofwins = 0

    for name in winnerslist:
        if name.casefold() == teamname.casefold():
            numberofwins = numberofwins + 1

    if numberofwins == 1:
            print(teamname, 'has won the world series', numberofwins, 'time.')
            
    elif numberofwins > 1:
            print(teamname, 'has won the world series', numberofwins, 'time.')

    else:
        print(teamname, 'has never won the world series.')
main()
