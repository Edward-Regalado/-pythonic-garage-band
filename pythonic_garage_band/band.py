class Band:
    bands = []
    def __init__(self, name, members=None):
        self.name = name
        self.members = members
        Band.bands.append(self)

    def __str__(self):
        return f"The band {self.name}"

    def __repr__(self):
        return f"Band instance. name={self.name}, members={self.members}"
    
    def play_solos(self):
        solos = []
        for player in self.members:
            solos.append(player.play_solo())
        return solos

    @classmethod
    def to_list(cls):
        return cls.bands


class Musician:
    def __init__(self, name, type, instrument):
        self.name = name
        self.type = type
        self.instrument = instrument
    
    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return f"{self.type} instance. Name = {self.name}"

class Guitarist(Musician):
    def __init__(self, name):
      super().__init__(name, "Guitarist", "guitar")
    
    def play_solo():
      pass

class Bassist(Musician):
    def __init__(self, name):
      super().__init__(name, "Bassist", "bass")
    
    def play_solo():
        pass

class Drummer(Musician):
    def __init__(self, name):
        super().__init__(name, "Drummer", "drums")
    
    def play_solo():
        pass