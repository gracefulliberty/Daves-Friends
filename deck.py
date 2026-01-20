from dataclasses import dataclass

class Color:
    RED = 0
    YELLOW = 1
    BLUE = 2
    GREEN = 3
    
class Deck:
    cards = []
    
    def __init__(self):
        self.cards = []
        
    def add_default_cards(self):
        colors = [Color.RED, Color.YELLOW, Color.BLUE, Color.GREEN]
        
        self.cards = []
        
        for color in colors:
            for i in range(0, 10):
                self.cards.append(Number(color, i))
                if i != 0:
                    self.cards.append(Number(color, i))
    
            for i in range(0, 2):
                self.cards.append(Skip(color))
                self.cards.append(DrawTwo(color))
                self.cards.append(Reverse(color))
    
    
        for i in range(0, 4):
            self.cards.append(Wild())
            self.cards.append(DrawFourWild())
            
    
@dataclass
class Number:
    color: Color
    number: int
    
@dataclass
class Wild:
    color: Color | None = None
    
@dataclass
class DrawFourWild:
    color: Color | None = None
    
@dataclass
class Skip:
    color: Color
    
@dataclass
class DrawTwo:
    color: Color
    
@dataclass
class Reverse:
    color: Color
    
Card = Number | Wild | DrawFourWild | Reverse | Skip | DrawTwo

def can_play_card(top: Card, playing: Card) -> bool:
    if playing == Wild or playing == DrawFourWild:
        return True

    match top:
        case Number(color, number):
            return color == playing.color or number == playing.number
        case Reverse(color) | Skip(color) | DrawTwo(color):
            return color == playing.color
        case Wild(color) | DrawFourWild(color):
            return color == playing.color
            
    return False
    
