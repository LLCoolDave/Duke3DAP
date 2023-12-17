from BaseClasses import Region

from ..base_classes import D3DLevel


class E3L5(D3DLevel):
    name = "Movie Set"
    levelnum = 4
    volumenum = 2
    keys = ["Blue", "Red", "Yellow"]
    location_defs = [
        {"id": 0, "name": "Control Room Night Vision Goggles", "type": "sprite"},
        {"id": 9, "name": "Moon Landing Atomic Health", "type": "sprite"},
        {"id": 24, "name": "Vending Machine Night Vision Goggles", "type": "sprite"},
        {"id": 39, "name": "Spacecraft Night Vision Goggles", "type": "sprite"},
        {"id": 40, "name": "Earth Vent Atomic Health", "type": "sprite"},
        {"id": 41, "name": "Earth Jetpack", "type": "sprite"},
        {"id": 43, "name": "3DRealms Freezethrower", "type": "sprite"},
        {"id": 47, "name": "Subway Medkit", "type": "sprite"},
        {"id": 51, "name": "3DRealms Atomic Health", "type": "sprite"},
        {"id": 61, "name": "Studio Medkit", "type": "sprite"},
        {"id": 71, "name": "Yellow Key Card", "type": "sprite"},
        {"id": 80, "name": "Crate Atomic Health", "type": "sprite"},
        {"id": 81, "name": "Crate Devastator", "type": "sprite"},
        {"id": 105, "name": "Red Key Card", "type": "sprite"},
        {"id": 170, "name": "Moon Landing Chaingun", "type": "sprite"},
        {
            "id": 257,
            "name": "Beta Armor",
            "type": "sprite",
        },  # unreachable development room
        {"id": 258, "name": "Blue Key Card", "type": "sprite"},
        {
            "id": 261,
            "name": "Beta Holo Duke",
            "type": "sprite",
        },  # unreachable development room
        {"id": 267, "name": "Subway Shotgun", "type": "sprite"},
        {"id": 268, "name": "Booth Medkit", "type": "sprite"},
        {"id": 364, "name": "Spacecraft Wall Atomic Health", "type": "sprite"},
        {"id": 367, "name": "Spacecraft RPG", "type": "sprite"},
        {"id": 371, "name": "Crash Site Steroids", "type": "sprite"},
        {"id": 380, "name": "Studio Pipebombs", "type": "sprite"},
        {"id": 415, "name": "Streets Pipebombs", "type": "sprite"},
        {"id": 416, "name": "Control Room Tripmine 1", "type": "sprite"},
        {"id": 417, "name": "Control Room Tripmine 2", "type": "sprite"},
        {"id": 418, "name": "Earth Shrinker", "type": "sprite"},
        {"id": 424, "name": "Vending Machine Atomic Health 1", "type": "sprite"},
        {"id": 425, "name": "Vending Machine Atomic Health 2", "type": "sprite"},
        {"id": 426, "name": "Vending Machine Atomic Health 3", "type": "sprite"},
        {"id": 480, "name": "Moon Landing Jetpack", "type": "sprite"},
        {"id": 487, "name": "Subway Chaingun", "type": "sprite"},
        {"id": 88, "name": "Secret Earth Screen", "type": "sector"},
        {"id": 149, "name": "Secret Crate", "type": "sector"},
        {"id": 183, "name": "Secret Vending Machine", "type": "sector"},
        {"id": 195, "name": "Secret 3DRealms", "type": "sector"},
        {"id": 0, "name": "Exit", "type": "exit"},
        {"id": 10, "name": "Secret Exit", "type": "exit"},
    ]
    events = ["Gate Control"]

    def main_region(self) -> Region:
        r = self.rules
        ret = self.region(
            self.name,
            [
                "Blue Key Card",
                "Subway Shotgun",
                "Streets Pipebombs",
                "Crash Site Steroids",
            ],
        )

        subway_entrance = self.region(
            "Subway Entrance", ["Exit", "Subway Medkit", "Subway Chaingun"]
        )
        # This is so easy I refuse to classify it as glitched
        self.connect(
            ret,
            subway_entrance,
            self.event("Gate Control")
            | (r.can_crouch & r.jump)
            | (r.jetpack(50) & r.can_crouch & r.difficulty("medium")),
        )

        start_ledges = self.region(
            "Outside Ledges",
            [
                "Booth Medkit",
                "Vending Machine Night Vision Goggles",
                "Secret 3DRealms",
                "3DRealms Freezethrower",
                "3DRealms Atomic Health",
                "Secret Vending Machine",
                "Vending Machine Atomic Health 1",
                "Vending Machine Atomic Health 2",
                "Vending Machine Atomic Health 3",
            ],
        )
        self.connect(ret, start_ledges, r.jump)

        studio_floor = self.region(
            "Studio Floor",
            [
                "Yellow Key Card",
                "Moon Landing Chaingun",
                "Moon Landing Jetpack",
                "Studio Pipebombs",
                "Studio Medkit",
                "Secret Exit",
            ],
        )
        # might be possible to do without steroids
        self.connect(
            ret,
            studio_floor,
            self.blue_key
            | (
                r.glitched
                & r.difficulty("medium")
                & r.steroids
                & r.can_sprint
                & r.can_crouch
            )
            | (
                r.glitched
                & r.difficulty("extreme")
                & r.steroids
                & r.can_sprint
                & r.can_jump
                & r.tripmine
            ),
        )

        studio_ledges = self.region(
            "Studio Ledges",
            [
                "Moon Landing Atomic Health",
                "Crate Atomic Health",
                "Secret Crate",
                "Crate Devastator",
            ],
        )
        self.connect(studio_floor, studio_ledges, r.jump)

        space_craft = self.region(
            "Spacecraft Studio",
            [
                "Spacecraft Wall Atomic Health",
                "Spacecraft RPG",
                "Red Key Card",
                "Spacecraft Night Vision Goggles",
            ],
        )
        self.connect(
            studio_floor,
            space_craft,
            self.yellow_key
            | (
                r.glitched
                & r.difficulty("extreme")
                & r.steroids
                & r.can_sprint
                & r.can_jump
                & r.tripmine
            ),
        )

        earth_secret = self.region(
            "Behind the Earth Screen",
            [
                "Secret Earth Screen",
                "Earth Jetpack",
                "Earth Shrinker",
                "Earth Vent Atomic Health",
            ],
        )
        self.connect(space_craft, earth_secret, r.jump)
        self.restrict(
            "Earth Vent Atomic Health", r.can_jump & r.jetpack(50)
        )  # This has weird clipping stuff

        control_room = self.region("Subway Control Room", ["Gate Control"])
        self.connect(studio_floor, control_room, self.red_key)

        control_room_ledge = self.region(
            "Subway Control Room Ledge",
            [
                "Control Room Tripmine 1",
                "Control Room Tripmine 2",
                "Control Room Night Vision Goggles",
            ],
        )
        self.connect(control_room, control_room_ledge, r.jump)
        return ret
