# -*- coding: utf-8 -*-
"""
The problem that I chose to solve is the boredom that students experience when studying.
Because it's designed for studying students I decided the program can't be too time consuming for the user
To accomplish this I decided to make a simple text based rpg 
"""
import random

def job_selection():
    """
    Takes user input to return stats values according to chosen class
    """
    print ("Warrior - High health but low attack")
    print ("Adventurer - Balanced stats")
    print ("Rogue - High attack but low health")
    job = input("Choose one of the jobs above: ")

    if job == "Warrior":
        max_health = 45
        attack = 3
    elif job == "Adventurer":
        max_health = 35
        attack = 5
    elif job == "Rogue":
        max_health = 25
        attack = 7
    return max_health, attack

def exploration_tutorial():
    """
    Explains to the user what each the choices given during the exploration phase does
    """
    print ("\nExplore - Look for one of your targets")
    print ("Rest - Heal up to max health but remaining enemies increase by 1")
    print ("Town - Heal to max health and restock potions but remaining enemies increase by 2\n")
    
def combat_tutorial():
    """
    Explains to the user what each the choices given during the combat phase does
    """
    print ("\nAttack - attack the enemy (damage done will be a random roll from 0-4 plus your attack stat")
    print ("\tNote that enemy attack will be calculated the same way")
    print ("Potion - heals you by 20, will not heal more than max health (You only have 3 so use them wisely)") 
    print ("Escape - Try to run away (35% chance to succeed)\n") 

    
def player_damage(attack,enemy_health,enemy_name):
    """
    Gets player attack stat, enemy health and the name of the monster
    returns the value of enemy health after damage calculation
    """
    damage = random.randint(0,4) + attack
    enemy_health -= damage
    print("You dealt ",damage, " damage to the "+enemy_name)
    return enemy_health
    
def enemy_damage(enemy_attack,health,enemy_name):
    """
    Gets enemy attack stat, player health and the name of the monster
    returns the value of player health after damage calculation
    """

    damage = random.randint(0,4) + enemy_attack
    health -= damage
    print (enemy_name+" dealt ",damage, " damage to you")
    return health

def chose_potion(potions,health,max_health):
    """
    Gets number of potions and player health
    Returns new values of potions and player health if condition is true, else informs player that there are no potions remaining.
    """
    if potions > 0:
        health += 20
        if health > max_health:
            health = max_health
        potions -= 1
        print ("Remaining potions: ", potions)
    else:
        print("No potions remaining, enemy attacks while you're looking in your bag")
    return potions,health

def chose_escape():
    """
    Uses a randome value from 0 to 100 to decide if the excape succeeds
    Returns true if value is greater than 50 (50% chance), false if otherwise
    """
    is_successful = False
    escape_roll = random.randint(0,100)
    if escape_roll > 65:
        is_successful = True
    return is_successful
        
if __name__ == "__main__":
    
    #Assigns stats according to job selected
    max_health,attack = job_selection()
    health = max_health
    is_alive = True
    potions = 3
    
    print ("\nYou head to the adventurer's guild to take a job and see two requests posted.")
    print ("The first is hunting 10 goblins and the second is hunting 3 orcs")
    print ("Goblins are weak but will take longer to hunt, Orcs are powerful but will be a quicker hunt")

    player_choice = input("Will you take the request to hunt Goblins or Orcs? ")

    #Assigns enemy stats and number of enemies according to selected quest
    if player_choice == "Goblins":
        enemy_max_health = 15
        enemy_attack = 3
        enemies = 10
        enemy_name = "goblin"

    elif player_choice == "Orcs":
        enemy_max_health = 30
        enemy_attack = 4
        enemies = 3
        enemy_name = "orc"
    
    #assigns health to enemy for first battle
    enemy_health = enemy_max_health

    #Gives player quick tutorial on what each choice does 
    print ("\nExploration Tutorial:")
    exploration_tutorial()
    print ("\nCombat Tutorial:")
    combat_tutorial()
    
    print ("\nYou prepare your equipment and enter the forest")
    #Exploration loop continues until the player dies or completes the quest
    while is_alive and enemies > 0:
        
        #Provides the user with important information at the start of every exploration phase 
        print ("Enemies remaining: ",enemies)
        print ("Current health: ",health)
        print ("Remaing potions: ",potions)
        
        player_choice = input ("Explore, Rest or Town? (type help if you forgot what these actions do) ")
    
        if player_choice == "Explore":
            print ("After exploring for a while you encounter a lone "+enemy_name)
            #Combat loop will continue until either the player or the enemy is slain
            while enemy_health > 0 and health > 0:
                print ("Enemy health: ",enemy_health)
                print ("Your health: ",health)
                
                player_choice = input("Attack, Potion or Escape? (Type Help if you forgot these actions) ")
                
                #Calls on the function that corresponds with user input
                if player_choice == "Attack":
                    enemy_health = player_damage(attack, enemy_health, enemy_name)
                elif player_choice == "Potion":
                    potions,health = chose_potion(potions, health,max_health)
                elif player_choice == "Escape":
                    #If escape is successful program exits battle loop, else the loop continues
                    if chose_escape():
                        print("Escaped successfully")
                        break
                    else:
                        print("Failed to escape, the "+enemy_name+" attacks while your back is turned")   
                elif player_choice == "Help":
                    combat_tutorial()
                #If enemy survives after player's turn, enemy will attack player
                if enemy_health > 0:
                    health = enemy_damage(enemy_attack, health,enemy_name)
                
            #If enemy is defeated player is informed, number of enemies is updated 
            if enemy_health <= 0:
                print("You have defeated the " + enemy_name,"\n")
                enemies -= 1   
            #Resets enemy health value after battle ends
            enemy_health = enemy_max_health
            
            if health >= 0:
                is_alive = False
            
        #If player chooses Rest, fully restore health and increase remainging enemies by 1
        elif player_choice == "Rest":
            health = max_health
            enemies += 1
        #If player chooses Town, fully restore health and potions, then increase remaining enemies by 2
        elif player_choice == "Town":
            health = max_health
            potions = 3
            enemies += 2
        elif player_choice == "Help":
            exploration_tutorial()
    #Congratulates player if they are alive at the end, if otherwise displays defeat message
    if is_alive:
        print("Congratulations, you succeeded with your quest!")
    else:
        print("Unfortunately you died during your quest, rest in peace.")
        
        
        
    
