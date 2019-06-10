"""
speech 模块
控制电脑模块
"""
import speech as sp


while True:
    phrase = sp.input(prompt=None)
    sp.say("You said %s" % phrase)
    if phrase == 'turn off':
        break

