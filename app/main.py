from app.knightProvider import get_knights_for_battle
from app.knight import Knight
from app.battle import Battle


def battle(knights: dict) -> dict:
    # BATTLE PREPARATIONS:

    # lancelot
    lancelot = Knight.get_knight(knights, "lancelot")
    lancelot.get_ready_for_fight()
    # arthur
    arthur = Knight.get_knight(knights, "arthur")
    arthur.get_ready_for_fight()

    # mordred
    mordred = Knight.get_knight(knights, "mordred")
    mordred.get_ready_for_fight()

    # red_knight
    red_knight = Knight.get_knight(knights, "red_knight")
    red_knight.get_ready_for_fight()

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    Battle.hold_duel(lancelot, mordred)

    # 2 Arthur vs Red Knight:
    Battle.hold_duel(arthur, red_knight)

    # Return battle results:
    return Battle.get_battle_results()


print(battle(get_knights_for_battle()))
