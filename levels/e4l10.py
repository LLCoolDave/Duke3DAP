from BaseClasses import Region

from ..base_classes import D3DLevel


class E4L10(D3DLevel):
    name = "The Queen"
    levelnum = 9
    volumenum = 3
    keys = ["Red", "Blue", "Yellow"]
    location_defs = [
        {"id": 29, "name": "R-Side Dive Jetpack", "type": "sprite"},
        {"id": 150, "name": "DukeTag R-Side Protective Boots", "type": "sprite"},
        {"id": 151, "name": "DukeTag L-Side Protective Boots", "type": "sprite"},
        {"id": 260, "name": "Yellow Dive Atomic Health 1", "type": "sprite"},
        {"id": 297, "mp": True, "name": "MP Start Shotgun 1", "type": "sprite"},
        {"id": 298, "mp": True, "name": "MP Start Shotgun 2", "type": "sprite"},
        {"id": 299, "mp": True, "name": "MP Start Shotgun 3", "type": "sprite"},
        {"id": 300, "mp": True, "name": "MP Start Shotgun 4", "type": "sprite"},
        {"id": 312, "name": "L-Side Vent Pipebombs", "type": "sprite"},
        {"id": 315, "name": "Center Pipebombs 1", "type": "sprite"},
        {"id": 316, "name": "Center Pipebombs 2", "type": "sprite"},
        {"id": 331, "name": "Queen Medkit", "type": "sprite"},
        {"id": 332, "name": "Queen Atomic Health", "type": "sprite"},
        {"id": 333, "name": "Queen Armor", "type": "sprite"},
        {"id": 337, "name": "L-Side Scuba Gear", "type": "sprite"},
        {"id": 338, "name": "R-Side Protective Boots", "type": "sprite"},
        {"id": 374, "name": "L-Side Dive Armor", "type": "sprite"},
        {"id": 375, "name": "L-Side Dive Atomic Health", "type": "sprite"},
        {"id": 388, "mp": True, "name": "MP Center Devastator 1", "type": "sprite"},
        {"id": 424, "name": "Red Medkit", "type": "sprite"},
        {"id": 453, "name": "R-Side RPG", "type": "sprite"},
        {"id": 561, "name": "DukeTag R-Side Jetpack", "type": "sprite"},
        {"id": 579, "name": "L-Side RPG", "type": "sprite"},
        {"id": 613, "mp": True, "name": "MP Lobby Shotgun 4", "type": "sprite"},
        {"id": 614, "mp": True, "name": "MP Lobby Shotgun 1", "type": "sprite"},
        {"id": 615, "name": "Lobby Shotgun Shotgun 1", "type": "sprite"},
        {"id": 616, "mp": True, "name": "MP Lobby Shotgun 3", "type": "sprite"},
        {"id": 624, "name": "DukeTag L-Side Jetpack", "type": "sprite"},
        {"id": 669, "mp": True, "name": "MP Center Devastator 2", "type": "sprite"},
        {"id": 686, "name": "Lobby Pipebombs 1", "type": "sprite"},
        {"id": 701, "mp": True, "name": "MP Lobby Shotgun 5", "type": "sprite"},
        {"id": 702, "mp": True, "name": "MP Lobby Shotgun 2", "type": "sprite"},
        {"id": 776, "name": "Blue Medkit", "type": "sprite"},
        {"id": 789, "name": "Blue Key Card", "type": "sprite"},
        {"id": 823, "name": "Red Key Card", "type": "sprite"},
        {"id": 824, "name": "R-Side Dive Atomic Health", "type": "sprite"},
        {"id": 825, "name": "R-Side Dive Armor", "type": "sprite"},
        {"id": 840, "name": "L-Side Armor", "type": "sprite"},
        {"id": 841, "name": "R-Side Armor", "type": "sprite"},
        {"id": 842, "name": "Yellow Key Card", "type": "sprite"},
        {"id": 844, "name": "Yellow Steroids", "type": "sprite"},
        {"id": 852, "name": "Yellow Dive Atomic Health 2", "type": "sprite"},
        {"id": 859, "mp": True, "name": "MP Pillar 1 Chaingun", "type": "sprite"},
        {"id": 860, "mp": True, "name": "MP Pillar 3 Chaingun", "type": "sprite"},
        {"id": 861, "mp": True, "name": "MP Pillar 4 Chaingun", "type": "sprite"},
        {"id": 862, "mp": True, "name": "MP Pillar 2 Chaingun", "type": "sprite"},
        {"id": 891, "name": "Lobby Pipebombs 4", "type": "sprite"},
        {"id": 892, "name": "Lobby Pipebombs 2", "type": "sprite"},
        {"id": 893, "name": "Lobby Pipebombs 3", "type": "sprite"},
        {"id": 894, "mp": True, "name": "MP Lobby Chaingun 2", "type": "sprite"},
        {"id": 895, "mp": True, "name": "MP Lobby Chaingun 1", "type": "sprite"},
        {"id": 896, "name": "Lobby Chaingun 1", "type": "sprite"},
        {"id": 897, "name": "Lobby Chaingun 2", "type": "sprite"},
        {"id": 903, "name": "L-Side Devastator", "type": "sprite"},
        {"id": 904, "name": "R-Side Devastator", "type": "sprite"},
        {"id": 933, "name": "DukeTag RPG 1", "type": "sprite"},
        {"id": 934, "name": "DukeTag RPG 2", "type": "sprite"},
        {"id": 964, "name": "R-Side Vent Pipebombs", "type": "sprite"},
        {"id": 65, "name": "Secret Pillar 1", "type": "sector"},
        {"id": 67, "name": "Secret Pillar 2", "type": "sector"},
        {"id": 70, "name": "Secret Pillar 3", "type": "sector"},
        {"id": 72, "name": "Secret Pillar 4", "type": "sector"},
        {"id": 197, "name": "Secret L-Side Vent", "type": "sector"},
        {"id": 357, "name": "Secret R-Side Vent", "type": "sector"},
        {"id": 630, "name": "Secret Queens Chamber", "type": "sector"},
        {"id": 0, "name": "Exit", "type": "exit"},
    ]
    events = ["Red Switch", "Blue Switch"]
    must_dive = True
    has_boss = True

    def main_region(self) -> Region:
        r = self.rules
        ret = self.region(
            self.name,
            [
                "MP Start Shotgun 1",
                "MP Start Shotgun 2",
                "MP Start Shotgun 3",
                "MP Start Shotgun 4",
                "MP Lobby Shotgun 1",
                "MP Lobby Shotgun 2",
                "MP Lobby Shotgun 3",
                "MP Lobby Shotgun 4",
                "MP Lobby Shotgun 5",
                "Lobby Pipebombs 1",
                "Lobby Pipebombs 2",
                "Lobby Pipebombs 3",
                "Lobby Pipebombs 4",
                "Lobby Chaingun 1",
                "Lobby Chaingun 2",
                "MP Lobby Chaingun 1",
                "MP Lobby Chaingun 2",
                "Lobby Shotgun Shotgun 1",
                "Center Pipebombs 1",
                "Center Pipebombs 2",
                "MP Center Devastator 1",
                "MP Center Devastator 2",
                "L-Side Scuba Gear",
                "L-Side RPG",
                "L-Side Devastator",
            ],
        )

        lside_upper = self.region(
            "L-Side Upper",
            [
                "L-Side Vent Pipebombs",
                "Secret L-Side Vent",
                "L-Side Armor",
            ],
        )
        self.connect(ret, lside_upper, r.jump)

        lside_dive = self.region(
            "L-Side Dive",
            [
                "L-Side Dive Armor",
                "L-Side Dive Atomic Health",
                "Blue Key Card",
            ],
        )
        self.connect(ret, lside_dive, r.jump & r.can_dive)

        blue_key_room = self.region(
            "Blue Key Room",
            [
                "Blue Medkit",
                "Blue Switch",
            ],
        )
        self.connect(ret, blue_key_room, r.jump & self.blue_key)

        rside = self.region(
            "Right Side",
            [
                "R-Side Protective Boots",
                "R-Side RPG",
                "R-Side Devastator",
            ],
        )
        # 22 jetpack until here minimum
        self.connect(blue_key_room, rside)
        # Can enter right side by pushing buttons through wall cover, hard for obscurity
        self.connect(ret, rside, r.difficulty("hard"))

        rside_upper = self.region(
            "Right Side Upper",
            [
                "R-Side Armor",
                "Secret R-Side Vent",
                "R-Side Vent Pipebombs",
            ],
        )
        self.connect(rside, rside_upper, r.jump)

        pillar_secrets = self.region(
            "Pillar Secrets",
            [
                "Secret Pillar 1",
                "MP Pillar 1 Chaingun",
                "Secret Pillar 2",
                "MP Pillar 2 Chaingun",
                "Secret Pillar 3",
                "MP Pillar 3 Chaingun",
                "Secret Pillar 4",
                "MP Pillar 4 Chaingun",
            ],
        )
        # 50 might also be enough but very tight
        self.connect(
            ret, pillar_secrets, r.jetpack(75) | (r.difficulty("hard") & r.can_jump)
        )

        red_key_room = self.region(
            "Red Key Room",
            [
                "Red Medkit",
                "Yellow Key Card",
                "Red Switch",
            ],
        )
        # 33 jetpack to here
        self.connect(rside, red_key_room, r.jump & self.red_key)

        rside_dive = self.region(
            "Red Dive",
            [
                "R-Side Dive Jetpack",
                "Red Key Card",
                "R-Side Dive Atomic Health",
                "R-Side Dive Armor",
            ],
        )
        self.connect(rside, rside_dive, r.jump & r.can_dive)

        yellow_key_room = self.region(
            "Yellow Key Room",
            [
                "Yellow Steroids",
            ],
        )
        # 44 jetpack to here minimum on a no jump route
        self.connect(
            red_key_room,
            yellow_key_room,
            (
                self.yellow_key
                & (
                    r.can_jump
                    | r.jetpack(300)
                    | (r.can_sprint & r.jetpack(250))
                    | (r.difficulty("hard") & r.jetpack(200))
                    | (r.difficulty("hard") & r.can_sprint & r.jetpack(150))
                )
                | (r.crouch_jump & r.steroids)
            )
            & self.event("Red Switch")
            & self.event("Blue Switch"),
        )

        yellow_dive = self.region(
            "Yellow Dive",
            [
                "Yellow Dive Atomic Health 1",
                "Yellow Dive Atomic Health 2",
                "Secret Queens Chamber",
                "Queen Medkit",
                "Queen Atomic Health",
                "Queen Armor",
                "Exit",
            ],
        )
        # Don't need to touch water before getting here
        self.connect(yellow_key_room, yellow_dive, r.can_dive)
        self.restrict("Exit", r.can_kill_boss_4)
        # Unreachable DukeTag MP Locations at the Start:
        # {"id": 933, "name": "DukeTag RPG 1", "type": "sprite"},
        # {"id": 934, "name": "DukeTag RPG 2", "type": "sprite"},
        # R-Side MP Only {"id": 150, "name": "DukeTag R-Side Protective Boots", "type": "sprite"},
        # R-Side MP Only {"id": 561, "name": "DukeTag R-Side Jetpack", "type": "sprite"},
        # L-Side MP Only {"id": 151, "name": "DukeTag L-Side Protective Boots", "type": "sprite"},
        # L-Side MP Only {"id": 624, "name": "DukeTag L-Side Jetpack", "type": "sprite"},
        return ret
