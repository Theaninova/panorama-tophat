from side import side
from settings import Settings
from util import transform
import cadquery as cq


def front(settings: Settings):
    return (
        side(settings, 0)
        .faces(">Y")
        .cut(
            transform(
                cq.importers.importDXF("../assets/Stealthchanger_logo.dxf"),
                cq.Matrix(
                    [
                        [settings.logo_scale, 0, 0, 0],
                        [0, settings.logo_scale, 0, 0],
                        [0, 0, settings.logo_scale, 0],
                        [0, 0, 0, 1],
                    ]
                ),
            )
            .wires()
            .toPending()
            .extrude(settings.logo_emboss)
            .rotate((1, 0, 0), (0, 0, 0), 90)
            .rotate((0, 0, 1), (0, 0, 0), 180)
            .translate((0, 10, settings.top_thickness / 2))
        )
    )
