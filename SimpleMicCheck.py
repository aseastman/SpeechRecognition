#In order to make this work, you need Windows Speech Recognition and dragonfly.
#Dragonfly has a bunch of pre-requisites as well that you can find on their Github page. 

from dragonfly import Grammar, MappingRule, Text, Dictation
import pythoncom
import time

test_com = MappingRule(\
name="test",\
mapping = {"write <text>": Text("%(text)s")},\
extras=[Dictation("text"),],)

grammar = Grammar("test grammar")
grammar.add_rule(test_com)
grammar.load()

#Keeps the program running to execute the commands
while True:
    pythoncom.PumpWaitingMessages()
    time.sleep(0.1)
    
    but annathe house sits on a hillran unattained of the many many many within