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
As the BIOS screen loads you being to feel hungry.
Do you:
1) Wait until your system boots to it's desktop before getting a snack
2) Go grab a snack immediately
""")

choice_a = TreeNode (""" 
25 Minutes have passed but you have finally booted to your desktop.
Do you:
1)Get up and go get a snack
2)Cut your losses and start picking a game to play 
""")

choice_b = TreeNode ("""
Luckily you went to grab that snack, mechanical hard drives have never been slower! 
You come back just in time to boot into your desktop.
Do you:
1)Start picking a game to play
2)Turn on limewire to download some tunes
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



choice_a_3 = TreeNode("""
Your first ladder game in and your house phone rings.You still have dial up and now you have more disconnects than wins.
You decide to just switch to World of Warcraft. You login and spawn where you left off.
Where did you spawn?
1)The Barrens                      
2)Stormwind                     
""")

choice_a_4 = TreeNode("""
You enter the login Queue with 5,000 users ahead of you
1)Reformat your hard drive and reinstall windows, you know what you did                      
2)Ignore the files and go boot up a game, whats the worst that can happen?
""")

choice_a_1.add_child(choice_a_3)
choice_a_2.add_child(choice_a_4)













#TESTING AREA

print("It is 2005 and you have just finished the work week. Time to play some games... what could go wrong")


#user_input = input("What is your name?")
#print(user_input)

story_root.traverse()