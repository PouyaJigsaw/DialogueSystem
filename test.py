
#DIALOGUE


#_model
'''

class dialogue model

is wiping the dialogue based on buttons (so wait until pushing buttons?)

button attachments (if need buttons)

how much wait to wipe the dialogue?

dialogue state : "start_1" bla bla

multiple choices in dialogue content :true or false


send the dialogue to the dialogue manager 

a pointer to where the dialogue current word is (index)

if true, it should be chosen randomly



'''


#_controller
'''
dialogue controller

dialogue stack

dialogue to show (or words to show)


show the dialogue letter by letter:
    always check top of stack
    show the dialogue based on pointer
    

wipe the box:
if its button dependent then wait till button event
else wait based on time

'''


#_view
'''
dialogue view

location of dialoguebox
dimension of dialoguebox
dialoguebox background color
dialogue font color
dialogue content


update every 0.05 second ?

'''

#_test
'''
create a script that gets input with keyboard and puts dialogue in the stack
'''
#AVATAR

#_model
'''

abstract class avatar model:
    

    class reaction avatar:
        
        sprite image
        sprite_blink image

        time between blinks

        can we assign time for showing this? depend on dialogue time!!!



    class talking avatar
        sprite image
        sprite image_talking
        sprite image_blink

        time between opening and closing mouth
        time between blinks

        when does it end talking?
    
    class idle avatar
        sprite image
        sprite image_right
        sprite image_left
        sprite image_blink

        time between default and left/right

        time between left and right

        time between etc.
        
        does it need a pointer?


'''


#-controller
'''
class avatar controller
    avatar stack
    
    current sprite
    current avatar

    
    always check stack right?

    def idle_loop

    def action_loop

    def talking_loop


    update 0.05 for images based on current sprite

'''

#_view
'''
class avatar view
    location
    dimension
    current image

    update every folan second!

'''


#_test
'''
create a script that gets input with keyboard and puts dialogue in the stack
'''


#I should create two different tkinter projects in mac, start with dialogue, then with avatar

#then should figure out how to make the state machine