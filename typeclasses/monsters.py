from typeclasses.objects import Object

class Monster(Object):
    """
    Base monster class.
    """

    def move_around(self):
        print(f"{self.key} is moving around!")


class Drake(Monster):
    """
    A drake, mutated dragon style monster.
    """
    def move_around(self):
        super().move_around()
        print(f"{self.key} ambles across the ground on massive claws.")

    def toxicbreath(self):
        """
        Drakes breathes toxins.
        """
        print(f"{self.key} spews forth a cloud of toxic gas!")