import cadquery as cq
from settings import Settings


def side(settings: Settings, axis) -> cq.Workplane:
    length = settings.size[axis] - settings.corner_size[axis] * 2
    return (
        cq.Workplane("XY")
        .box(length, settings.extrusion_thickness, settings.thickness)
        .faces("<Z")
        .workplane()
        .rect(length - (settings.holder_padding * 2), 6.2)
        .extrude(1, taper=45)
        .faces(">Z")
        .workplane()
        .rect(length - settings.bore_padding * 2, 0)
        .vertices()
        .cboreHole(3.5, 5.9, 3.1)
        .faces(">Z")
        .workplane()
        .center(0, -7.2 / 2)
        .box(
            length - (settings.holder_padding * 2),
            10 + (7.2 / 2),
            settings.top_thickness,
            centered=(True, False, False),
        )
        .edges(">Z")
        .edges("|Y")
        .chamfer(7, settings.fillet)
        .edges(">Z")
        .edges("<Y")
        .fillet(settings.fillet)
        .faces(">Y")
        .fillet(settings.fillet)
    )
