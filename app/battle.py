from app.knight import Knight


class Battle:
    fighters = {}

    @classmethod
    def hold_duel(cls, knight1: Knight, knight2: Knight) -> None:
        knight1.hp -= max(knight2.power - knight1.protection, 0)
        knight2.hp -= max(knight1.power - knight2.protection, 0)
        knight1.hp = max(knight1.hp, 0)
        knight2.hp = max(knight2.hp, 0)
        cls.fighters[knight1.name] = knight1.hp
        cls.fighters[knight2.name] = knight2.hp

    @classmethod
    def get_battle_results(cls) -> dict:
        return cls.fighters
