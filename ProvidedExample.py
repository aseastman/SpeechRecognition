#This is essentially the example (with a few edits for funtionality) provided 
#by the dragonfly developers.

from dragonfly import Grammar, CompoundRule
import time
import pythoncom


# Voice command rule combining spoken form and recognition processing.
class ExampleRule(CompoundRule):
    spec = "do something computer"                  # Spoken form of command.
    def _process_recognition(self, node, extras):   # Callback when command is spoken.
        print "Voice command spoken."

# Create a grammar which contains and loads the command rule.
grammar = Grammar("example grammar")                # Create a grammar to contain the command rule.
grammar.add_rule(ExampleRule())                     # Add the command rule to the grammar.
grammar.load()                                      # Load the grammar.

#Added this to the given example
while True:
    pythoncom.PumpWaitingMessages()
    time.sleep(0.1)