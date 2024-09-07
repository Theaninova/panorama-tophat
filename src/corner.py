import cadquery as cq
from settings import Settings


def corner(settings: Settings):
    return (
        cq.Workplane("XY")
        .box(settings.corner_size[0], settings.corner_size[1], settings.thickness)
        .faces(">Z")
        .workplane()
        .pushPoints(
            [
                (
                    (settings.corner_size[0] - settings.extrusion_thickness) / 2,
                    -settings.corner_size[1] / 2 + settings.bore_padding,
                ),
                (
                    -settings.corner_size[0] / 2 + settings.bore_padding,
                    (settings.corner_size[1] - settings.extrusion_thickness) / 2,
                ),
            ]
        )
        .cboreHole(3.5, 5.9, 3.1)
        .center(settings.holder_padding / 2, settings.holder_padding / 2)
        .rect(
            settings.corner_size[0] - settings.holder_padding,
            settings.corner_size[1] - settings.holder_padding,
        )
        .extrude(settings.top_thickness)
        .center(
            (settings.holder_padding + settings.extrusion_thickness) / -2,
            (settings.holder_padding + settings.extrusion_thickness) / -2,
        )
        .rect(
            settings.corner_size[0] - settings.extrusion_thickness,
            settings.corner_size[1] - settings.extrusion_thickness,
        )
        .cutThruAll()
        .faces(">Z")
        .workplane()
        .center(7.2, 7.2)
        .rect(
            settings.corner_size[0] - settings.extrusion_thickness,
            settings.corner_size[1] - settings.extrusion_thickness,
        )
        .cutBlind(-settings.top_thickness)
        .edges(">Z")
        .edges("<Y")
        .chamfer(settings.fillet, 7)
        .edges(">Z")
        .edges("<X")
        .chamfer(settings.fillet, 7)
        .edges(">Y or >X")
        .fillet(settings.fillet)
        .edges(">Z")
        .edges(">>Y[1] or >>X[1]")
        .fillet(settings.fillet)
    )
