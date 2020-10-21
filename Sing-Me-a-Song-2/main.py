"""
Assignment 1 - Sing me a Song
"""
#Functions
#This is for Strip My Mind (Optioin 1)
def strip_my_mind():
    #print("***DEBUG*** Strip my Mind")
    strip_my_mind_full = [
        "Oh, yeah yeah", 
        "Wow, wow, wow, wow, yeah", 
        "Arthur J. did, indicate that", 
        "The boulevard will never be", 
        "So full of life and love again hey", 
        "(Aw, say goodbye to your boots, man)", 
        " ", 
        "Hot as Hades, early eighties", 
        "Sing another song", 
        "Make me feel like I'm in love again, hey", 
        "(You gotta lose to win)", 
        " ", 
        "Oh Yeah", 
        "Oh", 
        "Please don't strip my mind", 
        "Leave something behind", 
        "Please don't strip my mind", 
        " ", 
        "Oh, hey yeah, oh", 
        "Wow, wow, wow, wow, wow yeah", 
        "All in favor sign the waiver", 
        "Bloody Carolina", 
        "Won't you take another look inside, hey", 
        "(Aw, it will make me cry)", 
        " ", "Operator, co-creator", 
        "Come on Babt Ellie", 
        "Won't you blow another compensator, hey", 
        "(Ah, you only get what you bring)", 
        " ", 
        "Oh yeah", 
        "Oh", 
        "Please..."]
    strip_my_mind_chorus = [
        "Please don't strip my mind", 
        "Leave something behind", 
        "Please don't strip my mind",]
    
    full_song_length = len(strip_my_mind_full)
    chorus_length = len(strip_my_mind_chorus)
    index = 0
    #If user selected 1, the "if" statement will run
    if sectionChoice == 1:
        while index < full_song_length:
            print(strip_my_mind_full[index])
            index = index + 1
    #If user selected 2, the "else" statement will run
    elif sectionChoice == 2:
        #print("***DEBUG*** This Works!")
            while index < chorus_length:
                print(strip_my_mind_chorus[index])
                index = index + 1
    else:
        print("Please Choose a Valid Option")

#This is for The Wizard (Option 2)
def the_wizard():
    #print("***DEBUG*** The Wizard")
    the_wizard_full = [
        "Misty morning, clouds in the sky", 
        "Without warning, the wizard walks by", 
        "Casting his shadow, weaving his spell", 
        "Funny clothes, tinkling bell", 
        " ", 
        "Never talking", 
        "Just keeps walking", 
        "Spreading his magic", 
        " ", 
        "Evil power disappears", 
        "Demons worry when the wizard is near", 
        "He turns tears into joy", 
        "Everyone's happy when the wizard walks by", 
        " ", 
        "Never talking", 
        "Just keeps walking", 
        "Spreading his magic", 
        " ", 
        "Sun is shining, clouds have gone by", 
        "All the people give a happy sigh", 
        "He has passed by, giving his sign", 
        "Left all the people feeling so fine", 
        "Never talking", "Just keeps walking", 
        "Spreading his magic"]
    the_wizard_chorus = [
        "Never talking", 
        "Just keeps walking", 
        "Spreading his magic"]
    
    full_song_length = len(the_wizard_full)
    chorus_length = len(the_wizard_chorus)
    index = 0
    #If user selected 1, the "if" statement will run
    if sectionChoice == 1:
        while index < full_song_length:
            print(the_wizard_full[index])
            index = index + 1
    #If user selected 2, the "else" statement will run
    elif sectionChoice == 2:
        #print("***DEBUG*** This Works!")
            while index < chorus_length:
                print(the_wizard_chorus[index])
                index = index + 1
    else:
        print("Please Choose a Valid Option")

#This is for Some Minds (Option 3)
def some_minds():
    #print("***DEBUG*** Some Minds")
    some_minds_full = [
        " "
        "In our home all day I waited for the change",
        "Something warm that I could say",
        "But I admit it won't come",
        "Somehow I don't care",              
        "Though I love the clothes she wears",
        "And I love her body bare (bare)",
        " ",
        "So, I pray, I pray that it won't feel the same, and",
        "Don't think that I can't see it in your eyes",     
        "Darling yeah, we both knew it from the start",
        "Some minds are better kept apart",
        " ",
        "Ohh, oh oh",
        "Oh oh, oh oh",
        "Oh oh oh",
        "Oh oh oh oh",
        " ",
        "Here I pass the day in a most peculiar way",
        "Watching ships out in the bay",
        "And I swallow so hard",
        "Am I too weak to fight?",
        "As the day becomes the night",
        "And I don't want to be right (right)",
        "So, I pray, I pray that it won't feel the same, and",
        "Don't think that I can't see it in your eyes",
        "Darling yeah, we both knew it from the start", 
        "Some minds are better kept apart", 
        "I pray that it won't feel the same, and", 
        "Don't think that I can't see it in your eyes", 
        "Darling yeah, we both knew it from the start", 
        "Some minds are better kept apart"]
    some_minds_chorus = [
        "I pray that it won't feel the same, and", 
        "Don't think that I can't see it in your eyes", 
        "Darling yeah, we both knew it from the start", 
        "Some minds are better kept apart"]
    
    full_song_length = len(some_minds_full)
    chorus_length = len(some_minds_chorus)
    index = 0
    #If user selected 1, the "if" statement will run
    if sectionChoice == 1:
        while index < full_song_length:
            print(some_minds_full[index])
            index = index + 1
    #If user selected 2, the "else" statement will run
    elif sectionChoice == 2:
        #print("***DEBUG*** This Works!")
            while index < chorus_length:
                print(some_minds_chorus[index])
                index = index + 1
    else:
        print("Please Choose a Valid Option")

#I feel like the song functions could be more effiecient 

#Song Options
song_array = ["1) Strip my Mind - RHCP", "2) The Wizard - Black Sabbath", "3) Some Minds - Flume"]
index = 0

song_list = len(song_array)

#While Loop to print the song options
while index < song_list:
    print(song_array[index])
    #print("***DEBUG***: index loop " + str(song_index))
    index = index + 1

#User Input for song choice
songChoice = int(input("Type: 1, 2, or 3 ")) 

choice_array = ["Please Select a Valid Option", "Strip My Mind", "The Wizard", "Some Minds"]
#print("***DEBUG***: Song Choice is: " + choice_array[songChoice])
print("Song Choice is: " + choice_array[songChoice])

sectionChoice = int(input("Press 1 for full song or 2 for just the chorus "))

if songChoice == 1:
    #print("***DEBUG*** Choices are 1 & 1")
    strip_my_mind()
elif songChoice == 2:
    #print("***DEBUG*** Choices are 2 & 1")
    the_wizard()
elif songChoice == 3:
    #print("***DEBUG*** Choices are 3 & 1")
    some_minds()
else:
    print("Please Select a Valid Option")  


# *** This was my second attempt after making a messy program that did half the job: ***
"""
#Functions

def strip_my_mind_lyrics():
    #print ("*** DEBUG *** Strip my Mind")
    index = 0
    array_length = len(strip_my_mind)
    section_choice = int(input("Press 1 for Chorus or 2 for Full song "))
    if section_choice == 1:
        #Chorus
        #print("***DEBUG*** Strip my mind Chorus")
        while index > array_length:
            print(strip_my_mind[index])
            print("***DEBUG***")
            index = index + 1
    elif section_choice == 2:
        #Full song
        #print("***DEBUG*** Strip my mind Full Song")
        print(strip_my_mind)
    else:
        print("Please select a valid option")

def the_wizard_lyrics():
    #print ("*** DEBUG *** The Wizard")
    section_choice = int(input("Press 1 for Chorus or 2 for Full song "))
    if section_choice == 1:
        #Chorus
        print("***DEBUG*** The Wizard Chorus")
    elif section_choice == 2:
        #Full song        
        print("***DEBUG*** The Wizard Full Song")
    else:
        print("Please select a valid option")

def some_minds_lyrics():
    #print ("*** DEBUG *** Some Minds")
    section_choice = int(input("Press 1 for Chorus or 2 for Full song "))
    if section_choice == 1:
        #Chorus
        print("***DEBUG*** Some Minds Chorus")
    elif section_choice == 2:
        #Full song        
        print("***DEBUG*** Some Minds Full Song")
    else:
        print("Please select a valid option")
#Strip my mind chorus elements are: 15, 18, and 19

strip_my_mind = ["Oh, yeah yeah", "Wow, wow, wow, wow, yeah", "Arthur J. did, indicate that", "The boulevard will never be", "So full of life and love again hey", "(Aw, say goodbye to your boots, man)", " ", "Hot as Hades, early eighties", "Sing another song", "Make me feel like I'm in love again, hey", "(You gotta lose to win)", " ", "Oh Yeah", "Oh", "Please don't strip my mind", "Leave something behind", "Please don't strip my mind", " ", "Oh, hey yeah, oh", "Wow, wow, wow, wow, wow yeah", "All in favor sign the waiver", "Bloody Carolina", "Won't you take another look inside, hey", "(Aw, it will make me cry)", " ", "Operator, co-creator", "Come on Babt Ellie", "Won't you blow another compensator, hey", "(Ah, you only get what you bring)", " ", "Oh yeah", "Oh", "Please..."]
#array_length = len(strip_my_mind)

index = 0
array_length = len(strip_my_mind)
while index > array_length:
    print(strip_my_mind[index])
    print("***DEBUG***")
    index = index + 1

"""
"""
#Strip my mind chorus elements are: 15, 18, and 19
strip_my_mind = ["Oh, yeah yeah", "Wow, wow, wow, wow, yeah", "Arthur J. did, indicate that", "The boulevard will never be", "So full of life and love again hey", "(Aw, say goodbye to your boots, man)", " ", "Hot as Hades, early eighties", "Sing another song", "Make me feel like I'm in love again, hey", "(You gotta lose to win)", " ", "Oh Yeah", "Oh", "Please don't strip my mind", "Leave something behind", "Please don't strip my mind", " ", "Oh, hey yeah, oh", "Wow, wow, wow, wow, wow yeah", "All in favor sign the waiver", "Bloody Carolina", "Won't you take another look inside, hey", "(Aw, it will make me cry)", " ", "Operator, co-creator", "Come on Babt Ellie", "Won't you blow another compensator, hey", "(Ah, you only get what you bring)", " ", "Oh yeah", "Oh", "Please..."]
"""
"""
    #This Plays the full song of the songChoice
def showFullSong(songChoice):
    print("***DEBUG*** (Full Song) Song Choice is: " + songChoice)
    #This Plays just the chorus of the songChoice
def showChorus(songChoice):
    print("***DEBUG*** (Chorus) Song Choice is: " + songChoice)


def showChorus(choice_array):
    print("***DEBUG*** (Chorus) Song Choice is: " + choice_array[songChoice]) #This Returned a 't'... ??? Still not sure why after fixing

print("What song would you like to see the lyrics for?")
"""
"""
#Song Options
song_array = ["1) Strip my Mind - RHCP", "2) The Wizard - Black Sabbath", "3) Some Minds - Flume"]
song_index = 0

#Song Variables
 
#Used this to test that my user input was working - it Worked
strip_my_mind = str("Strip my Mind")
the_wizard = str("The Wizard")
some_minds = str("Some Minds")


song_list = len(song_array)

#While Loop to print the song options
while song_index < song_list:
    print(song_array[song_index])
    #print("***DEBUG***: index loop " + str(song_index))
    song_index = song_index + 1

#User Input for song choice
songChoice = int(input("Type: 1, 2, or 3 ")) 
choice_array = ["Please Select a Valid Option", "Strip My Mind", "The Wizard", "Some Minds"]
#print("***DEBUG***: Song Choice is: " + choice_array[songChoice])
print("Song Choice is: " + choice_array[songChoice])

if songChoice == 1:
    strip_my_mind_lyrics()
elif songChoice == 2:
    the_wizard_lyrics()
elif songChoice == 3:
    some_minds_lyrics()
else:
    print("Please select a valid option")


sectionChoice = int(input("Press 1 for full song or 2 for just the chorus "))

if sectionChoice == 1:
    showFullSong(choice_array[songChoice])
elif sectionChoice == 2:
    showChorus(choice_array[songChoice])
else:
    print("Please select a valid option")
"""
"""
finalChoice = songChoice + sectionChoice

print("***DEBUG***: Final Choice = " + finalChoice)

#### DEBUG ###
if finalChoice == 11:
    print("It Worked!")
else:
    print("It did not work :(")

"""
"""
songChoice = int(input("Type: 1, 2, or 3 "))

if songChoice == 1:
    sectionChoice = int(input("Type '1' for just the chrous or '2' for the full song"))
if songChoice == 2:
    sectionChoice = int(input("Type '1' for just the chrous or '2' for the full song"))
if songChoice == 3:
    sectionChoice = int(input("Type '1' for just the chrous or '2' for the full song"))
else:
    print("Invalid Option")

finalChoice = songChoice + sectionChoice

print(finalChoice)
"""