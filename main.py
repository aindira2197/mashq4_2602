from abc import ABC, abstractmethod


class Hayvon(ABC):
    @abstractmethod
    def ovoz(self):
        pass


class It(Hayvon):
    def ovoz(self):
        print("Vov Vov")


hayvon = It()
hayvon.ovoz()
