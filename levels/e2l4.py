from BaseClasses import Region

from ..base_classes import D3DLevel


class E2L4(D3DLevel):
    name = "Fusion Station"
    levelnum = 3
    volumenum = 1
    keys = ["Red"]
    location_defs = [
        {"id": 3, "name": "3 Freezethrower", "type": "sprite"},
        {"id": 13, "name": "13 Armor", "type": "sprite"},
        {"id": 18, "name": "18 Night Vision Goggles", "type": "sprite"},
        {"id": 19, "name": "19 Night Vision Goggles", "type": "sprite"},
        {"id": 20, "name": "20 Night Vision Goggles", "type": "sprite"},
        {"id": 46, "name": "46 Chaingun", "type": "sprite"},
        {"id": 54, "mp": True, "name": "MP 54 Holo Duke", "type": "sprite"},
        {"id": 111, "name": "111 Atomic Health", "type": "sprite"},
        {"id": 135, "name": "135 Tripbomb", "type": "sprite"},
        {"id": 136, "name": "136 Tripbomb", "type": "sprite"},
        {"id": 139, "name": "139 Protective Boots", "type": "sprite"},
        {"id": 142, "name": "142 Atomic Health", "type": "sprite"},
        {"id": 143, "name": "143 Atomic Health", "type": "sprite"},
        {"id": 158, "name": "158 Devastator", "type": "sprite"},
        {"id": 159, "name": "159 Atomic Health", "type": "sprite"},
        {"id": 167, "name": "167 Medkit", "type": "sprite"},
        {"id": 210, "name": "210 Armor", "type": "sprite"},
        {"id": 253, "name": "253 Jetpack", "type": "sprite"},
        {"id": 696, "name": "696 Atomic Health", "type": "sprite"},
        {"id": 715, "name": "715 Shotgun", "type": "sprite"},
        {"id": 718, "name": "718 Medkit", "type": "sprite"},
        {"id": 720, "name": "720 Tripbomb", "type": "sprite"},
        {"id": 721, "name": "721 Night Vision Goggles", "type": "sprite"},
        {"id": 722, "name": "722 Chaingun", "type": "sprite"},
        {"id": 739, "name": "739 Shrinker", "type": "sprite"},
        {"id": 750, "name": "750 Pipebombs", "type": "sprite"},
        {"id": 751, "name": "751 Pipebombs", "type": "sprite"},
        {"id": 756, "name": "756 RPG", "type": "sprite"},
        {"id": 759, "mp": True, "name": "MP 759 Jetpack", "type": "sprite"},
        {"id": 760, "mp": True, "name": "MP 760 Jetpack", "type": "sprite"},
        {"id": 761, "mp": True, "name": "MP 761 Jetpack", "type": "sprite"},
        {"id": 762, "mp": True, "name": "MP 762 Jetpack", "type": "sprite"},
        {"id": 790, "name": "790 Atomic Health", "type": "sprite"},
        {"id": 791, "name": "791 Atomic Health", "type": "sprite"},
        {"id": 792, "name": "792 Pipebombs", "type": "sprite"},
        {"id": 793, "name": "793 Pipebombs", "type": "sprite"},
        {"id": 835, "name": "835 Shotgun", "type": "sprite"},
        {"id": 836, "mp": True, "name": "MP 836 RPG", "type": "sprite"},
        {"id": 837, "mp": True, "name": "MP 837 Devastator", "type": "sprite"},
        {"id": 838, "name": "838 Tripbomb", "type": "sprite"},
        {"id": 839, "name": "839 Tripbomb", "type": "sprite"},
        {"id": 867, "mp": True, "name": "MP 867 Pipebombs", "type": "sprite"},
        {"id": 870, "mp": True, "name": "MP 870 Protective Boots", "type": "sprite"},
        {"id": 871, "mp": True, "name": "MP 871 Protective Boots", "type": "sprite"},
        {"id": 872, "mp": True, "name": "MP 872 Protective Boots", "type": "sprite"},
        {"id": 873, "mp": True, "name": "MP 873 Protective Boots", "type": "sprite"},
        {"id": 874, "name": "874 Steroids", "type": "sprite"},
        {"id": 875, "name": "875 Steroids", "type": "sprite"},
        {"id": 317, "name": "Secret 1", "type": "sector"},
        {"id": 374, "name": "Secret 2", "type": "sector"},
        {"id": 378, "name": "Secret 3", "type": "sector"},
        {"id": 384, "name": "Secret 4", "type": "sector"},
        {"id": 405, "name": "Secret 5", "type": "sector"},
        {"id": 409, "name": "Secret 6", "type": "sector"},
        {"id": 416, "name": "Secret 7", "type": "sector"},
        {"id": 0, "name": "Exit", "type": "exit"},
    ]