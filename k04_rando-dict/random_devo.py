# Anastasia Lee
# peaches & mangoes
# SoftDev
# K04 -- Python dictionaries and random selection
# 2024-09-17
# time spent: 1 hour

import random
krewes = {
           4: [ 
                'DUA','TAWAB','EVA','JACK','VICTOR','EVAN','JASON','COLYI','IVAN','TANZEEM',
                'TAHMIM','STANLEY','LEON','NAOMI','NIA','ANASTASIA','JADY','BRIAN','JACOB',
                'ALEX','CHONGTIAN','DANNY','MARCO','ABIDUR','ANKITA','ANDY','ETHAN','AMANDA',
                'AIDAN','LINDA','QIANJUN','JIAYING','KISHI'
		      ],
           5: [ 
                'ADITYA','MARGIE','RACHEL','ALEXANDER','ZIYAD','DANNY','ENDRIT','CADEN',
                'VEDANT','SUHANA','KYLE','KEVIN','RAYMOND','CHRISTOPHER','JONATHAN','SASHA',
                'NAFIYU','TIM','WILL','DANIEL','BENJAMIN','CLAIRE','CHLOE','STELLA','TRACY',
                'JESSICA','JACKIE','WEN YUAN','YINWEI','TIFFANY','JAYDEN DANIEL','PRINCEDEN' 
              ]
         }

def random_devo(krewes):
    list = []
    for value in krewes.values():
        for devo in value:
            list.append(devo)
    print(random.choice(list))

random_devo(krewes)