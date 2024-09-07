import cadquery as cq
from settings import Settings
from side import side


def umbilical(settings: Settings) -> cq.Workplane:
    return (
        side(settings, 0)
        .faces("<Y")
        .workplane()
        .center(
            settings.umbilical_width / 2
            - (settings.ptfe_cd + settings.umbilical_padding) / 2,
            -5,
        )
        .rarray(
            settings.umbilical_spacing + settings.umbilical_width,
            1,
            settings.umbilical_count,
            1,
        )
        .cboreHole(settings.ptfe_d, settings.ptfe_cd, settings.ptfe_cz)
        .faces(">Y")
        .workplane()
        .sketch()
        .rarray(
            settings.umbilical_spacing + settings.umbilical_width,
            1,
            settings.umbilical_count,
            1,
        )
        .circle(settings.ptfe_cd / 2)
        .finalize()
        .cutBlind(-settings.ptfe_cz)
        .faces("<Y[1]")
        .workplane()
        .sketch()
        .rarray(
            settings.umbilical_spacing + settings.umbilical_width,
            1,
            settings.umbilical_count,
            1,
        )
        .circle(settings.ptfe_cd / 2)
        .finalize()
        .cutBlind(-settings.ptfe_cz, taper=45)
        .faces("<Y")
        .workplane()
        .center(
            -(
                settings.ptfe_cd / 2
                + settings.umbilical_padding
                + settings.can_thickness / 2
            ),
            -settings.thickness / 2 + settings.can_thickness / 2,
        )
        .sketch()
        .rarray(
            settings.umbilical_spacing + settings.umbilical_width,
            1,
            settings.umbilical_count,
            1,
        )
        .circle(settings.can_thickness / 2)
        .finalize()
        .cutThruAll()
        .center(0, -settings.can_thickness / 2)
        .sketch()
        .rarray(
            settings.umbilical_spacing + settings.umbilical_width,
            1,
            settings.umbilical_count,
            1,
        )
        .rect(settings.can_thickness, settings.can_thickness)
        .finalize()
        .cutThruAll()
    )
