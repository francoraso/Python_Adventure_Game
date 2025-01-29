#TREENODE CLASS

class TreeNode:

    def __init__(self, story_piece):
        self.story_piece = story_piece
        self.choices = []

    def add_child(self, node):
        self.choices.append(node)

    def traverse(self):
        story_node = self
        print(story_node.story_piece)
        while len(story_node.choices) > 0:
            choice = input("Enter 1 or 2 to continue the story: ")
            if choice not in ["1", "2"]:
                print("Invalid choice. Try again.")
            else:
                chosen_index = int(choice)
                chosen_index -= 1
                chosen_child = story_node.choices[chosen_index]
                print(chosen_child.story_piece)
                story_node = chosen_child






#VARIABLES FOR TREE


story_root = TreeNode (""" 
You hop on your trusty Pentium 4 Rig and hit the power button.
As the BIOS screen beeps to show you its alive you begin to feel hungry.
Do you:
1) Wait until your system boots to it's desktop before getting a snack
2) Go grab a snack immediately
""")

choice_a = TreeNode ("""""
Murphy's Law has unfortunately decided to make an appearance.
Your system is stuck on the windows xp loading screen and you didn't notice it for a solid 10 minutes
and now you have to hit the physical reset button (please oh please do not corrupt my Windows Installation)
Do you:
1)Get up and go get a snack while your computer restarts
2)Cut your losses and start picking a game to play as soon as you get into your desktop
""")

choice_b = TreeNode ("""
Luckily you went to grab that snack, that 5400RPM harddrive is trustworthy but it is slow. 
You come back just in time to boot into your desktop.
Do you:
1)Start picking a game to play
2)Turn on limewire to download some music while you play
""")

story_root.add_child(choice_a)
story_root.add_child(choice_b)

choice_a_1 = TreeNode("""
After returning with your snack you have a quick look at your desktop icons, you see that you have only two games installed on your 40gb hard drive.
What game do you play:
1)Starcraft Broodwar                      
2)World of Warcraft                     
""")

choice_a_2 = TreeNode("""
You only have 2 games installed.
What game do you play:
1)You don't like the games you have installed. You hop off your PC and go play E.T on your Atari                      
2)Age of Empires                   
""")

choice_a.add_child(choice_a_1)
choice_a.add_child(choice_a_2)


choice_b_1 = TreeNode("""
After a quick look at your desktop icons, you see that you have only two games installed on your 40gb hard drive.
Do you play:
1)Warcraft 3                      
2)Halo:Combat Evolved                     
""")

choice_b_2 = TreeNode("""
You boot up limewire and notice a few completed files with no file extensions.
Do you:
1)Reformat your hard drive and reinstall windows, you know what you did                      
2)Ignore the files and go boot up a game, whats the worst that can happen?                     
""")

choice_b.add_child(choice_b_1)
choice_b.add_child(choice_b_2)


choice_b_7 = TreeNode("""
You reinstalled windows and are slowly but surely individually installing every driver. 
Your games are slowly installing by 700mb CD-ROM and all you have is minesweeper for now.

Gamenight is ruined...but it could have been worse :)

You lose. Please try again.
""")

choice_b_8 = TreeNode("""
You double click the icon for Counter Strike Source but nothing is happening.
All of a sudden your cd-drive starts opening and closing on its own and a message appears on your screen;

  "ALL YOUR BASE ARE BELONG TO US" before shutting down your computer.

   Dennis Ritchie would not be proud.

Gaming night is ruined.

You lose.

Please try again.
  
""")

choice_b_2.add_child(choice_b_7)
choice_b_2.add_child(choice_b_8)

choice_b_3 = TreeNode("""
You login to Warcraft 3 and it somehow time warps you into the future. 
Blizzard Entertainment is not recognizable and your copy of Warcraft 3 was force updated to Warcraft 3:Reforged.
The game is glitchy and unplayable so you turn it off. You have have some newly installed games in the future but 
they are not on your PC..... You lift up this touch screen device in your hand that has a sim card in it and you see a game
title that looks familiar but it can't be....not on a phone...It can't be an april fools joke, were out of season.
1)Risk it and open the game                     
2)Remove the game from your phone and look for other new games. The future must have something better.                  
""")

choice_b_5 = TreeNode("""

It is as horrible as you thought. Somehow the future brought an action RPG to a mobile device 
with no plans on being played on PC. Diablo:Immortal loads up and just as fast as your mobile device can thermal throttle
you shut the game right down. Your mobile device rings, an unknown caller from the future has a message for you. 
You pickup the phone and the caller says "Do you guys not have phones".

You cast the phone into the fire. The future is not what you thought it would be, gaming will never be the same.

The future of gaming is ruined.

You lose. 

Please try again.
""")


choice_b_6 = TreeNode("""
You search through your computer desktop for more games and stumble upon some trade macro's installed for
some game called Path of Exile. You open the game and are wonderstruck by the endless creativity
for builds, endgame content, consistant seasonal updates and microtransactions that are solely for qualify of life
and cosmetic all for Free. You buy all the stash tab variations you can because supporting these devs is the 
last hope games have in the future.

Gaming is forever saved. They really know what they are doing in New Zealand.

You win!!

There are four paths to victory and you found path 4/4.
                      
If you are reading this you may be considering me for the Dev Degree program at Shopify. I hope
you enjoyed my text based adventure and more so I hope that it was able to bring some nostalgia and
laughs to those who reached any of the end paths regardless of victory or defeat. I have been forever learning since I was old 
enough to get my hands on a computer and I never plan to stop growing in a field that means so much to me.
                      
I really hope that we can work together in the future as I continue to achieve new goals and reach new heights.
                      
                      THANK YOU FOR PLAYING!!
""")


choice_b_3.add_child(choice_b_5)
choice_b_3.add_child(choice_b_6)

choice_b_4 = TreeNode("""
You just joined into a 16 person lobby on Blood Gulch and you are absolutely shredding the leader boards all night.
Pizza is ordered and the crew wants to have a LAN party.

Gamenight is saved.

You win!!

There are four paths to victory and you found path 3/4.

If you are reading this you may be considering me for the Dev Degree program at Shopify. I hope
you enjoyed my text based adventure and more so I hope that it was able to bring some nostalgia and
laughs to those who reached any of the end paths regardless of victory or defeat. I have been forever learning since I was old 
enough to get my hands on a computer and I never plan to stop growing in a field that means so much to me.
                      
I really hope that we can work together in the future as I continue to achieve new goals and reach new heights.
                      
                      THANK YOU FOR PLAYING!!

""")








choice_b_1.add_child(choice_b_3)
choice_b_1.add_child(choice_b_4)


choice_a_3 = TreeNode("""
Your first ladder game in and your house phone rings.You still have dial up and now you have more disconnects than wins.
You decide to just switch to World of Warcraft. You login and spawn where you left off.
Where did you spawn?
1)The Barrens                      
2)Stormwind                     
""")

choice_a_4 = TreeNode("""
You are in Queue to login but are in position 22,000
You don't get to play that night.

Your game night is ruined. 
Please try again.
""")

choice_a_1.add_child(choice_a_3)
choice_a_1.add_child(choice_a_4)


choice_a_5 = TreeNode("""
You spawned in the Barrens and the chat was so toxic your PC blue screened and is stuck in a boot loop.

Your game night is ruined. 
Please try again.                     
""")


choice_a_6 = TreeNode("""
You spawn in Stormwind. The realization that you made a Character on the alliance suddenly hits 
and you reroll a character on Horde. 

Gamenight is saved.

You win!!

There are four paths to victory and you found path 2/4.

If you are reading this you may be considering me for the Dev Degree program at Shopify. I hope
you enjoyed my text based adventure and more so I hope that it was able to bring some nostalgia and
laughs to those who reached any of the end paths regardless of victory or defeat. I have been forever learning since I was old 
enough to get my hands on a computer and I never plan to stop growing in a field that means so much to me.
                      
I really hope that we can work together in the future as I continue to achieve new goals and reach new heights.
                      
                      THANK YOU FOR PLAYING!!

""")

choice_a_3.add_child(choice_a_5)
choice_a_3.add_child(choice_a_6)



choice_a_7 = TreeNode("""
E.T for Atari was the worst game ever made and you happen to own the last copy. 
You receive a call from the Environmental Authority in New Mexico. 
As the last person on Earth with a copy of the game you are legally bound to dig up 
every last unsold and buried cartridge of E.T in the New Mexico Landfill.

Your game night is ruined and now you have to figure out what to do with all this junk.
Please try again.
""")

choice_a_8 = TreeNode("""
Age of Empires boots right up and with its basic graphic requirements you are able to run it using your onboard graphics perfectly
You decide to play offline since your 3web dial up service is about as effective as sending data packets by pidgeon.
Luckily the AI oppenents offer a competitive match and you can always type in "how do you turn this on" for some fun.

Gamenight is saved.

You win!!

There are three paths to victory and you found path 1/4.


If you are reading this you may be considering me for the Dev Degree program at Shopify. I hope
you enjoyed my text based adventure and more so I hope that it was able to bring some nostalgia and
laughs to those who reached any of the end paths regardless of victory or defeat. I have been forever learning since I was old 
enough to get my hands on a computer and I never plan to stop growing in a field that means so much to me.
                      
I really hope that we can work together in the future as I continue to achieve new goals and reach new heights.
                      
                      THANK YOU FOR PLAYING!!

""")


choice_a_2.add_child(choice_a_7)
choice_a_2.add_child(choice_a_8)







#TESTING AREA

print("It is the year 2005 and you have just finished the school/work week. Time to fire up some amazing games")
print("What could go wrong...")

user_input = input("What is your name adventurer?")
print (user_input) 
print ("let your gaming adventure begin")

story_root.traverse()