import cadquery as cq
from settings import Settings
from corner import corner
from front import front
from side import side
from umbilical import umbilical


def assembly(settings: Settings) -> cq.Assembly:
    return (
        cq.Assembly()
        .add(
            side(settings, 1).rotate((0, 0, 0), (0, 0, 1), -90),
            loc=cq.Location(cq.Vector(settings.size[0] / 2 - 10, 0, 0)),
            name="Side Right",
        )
        .add(
            side(settings, 1).rotate((0, 0, 0), (0, 0, 1), 90),
            loc=cq.Location(cq.Vector(-settings.size[0] / 2 + 10, 0, 0)),
            name="Side Left",
        )
        .add(
            front(settings),
            loc=cq.Location(cq.Vector(0, settings.size[1] / 2 - 10, 0)),
            name="Side Front",
        )
        .add(
            umbilical(settings).rotate((0, 0, 0), (0, 0, 1), 180),
            loc=cq.Location(cq.Vector(0, -settings.size[1] / 2 + 10, 0)),
            name="Side Back",
        )
        .add(
            corner(settings),
            loc=cq.Location(
                cq.Vector(
                    (settings.size[0] - settings.corner_size[0]) / 2,
                    (settings.size[1] - settings.corner_size[1]) / 2,
                    0,
                )
            ),
            name="Corner Front Left",
        )
        .add(
            corner(settings).rotate((0, 0, 0), (0, 0, 1), 90),
            loc=cq.Location(
                cq.Vector(
                    (settings.size[0] - settings.corner_size[0]) / -2,
                    (settings.size[1] - settings.corner_size[1]) / 2,
                    0,
                )
            ),
            name="Corner Front Right",
        )
        .add(
            corner(settings).rotate((0, 0, 0), (0, 0, 1), -90),
            loc=cq.Location(
                cq.Vector(
                    (settings.size[0] - settings.corner_size[0]) / 2,
                    (settings.size[1] - settings.corner_size[1]) / -2,
                    0,
                )
            ),
            name="Corner Back Left",
        )
        .add(
            corner(settings).rotate((0, 0, 0), (0, 0, 1), 180),
            loc=cq.Location(
                cq.Vector(
                    (settings.size[0] - settings.corner_size[0]) / -2,
                    (settings.size[1] - settings.corner_size[1]) / -2,
                    0,
                )
            ),
            name="Corner Back Right",
        )
    )
