starwars = ['Chewee', 'Hon Solo', 'Luke Skywaker', 'Yoda', 'Princess Lea', 'Lando', 'Ben Kanobee']
darkside = ['Darth Vadar', 'Darthmaul', 'Dark Sideous', 'Count Duku', 'Bobafet']

myFavoriteCharacter = input("Who is your favorite starwars character?")

challenge = input("Can you sort the following starwars characters in alphabetical order faster then me (yes or no)?")
print(starwars, " \n\n Ready set Go!! \n\n")

if myFavoriteCharacter in starwars:
    print("Your favorite starwars charater %s is a rebel." % myFavoriteCharacter)
elif myFavoriteCharacter in darkside:
    print("Your favorite starwars charater %s is on the dark side of the force." % myFavoriteCharacter)
else:
    print("Your favorite starwars charater %s is not in our rebel or dark side list." % myFavoriteCharacter)
    confirmAdd = input("Do you want to add your %s favorite character to the rebel list?" % myFavoriteCharacter)
    if confirmAdd == 'yes':
        starwars.append(myFavoriteCharacter)
        print(sorted(starwars))       
    else:
        confirmAdd = input("Do you want to add your %s favorite character to the dark side list?" % myFavoriteCharacter)
        if confirmAdd == 'yes':
            darkside.append(myFavoriteCharacter)
            print(sorted(darkside))

            