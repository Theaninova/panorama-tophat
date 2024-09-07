import cadquery as cq
from settings import Settings
from side import side


def umbilical(settings: Settings) -> cq.Workplane:
    arr = (
        settings.umbilical_spacing + settings.umbilical_width,
        1,
        settings.umbilical_count,
        1,
    )

    return (
        side(settings, 0)
        .faces("<Y")
        .workplane()
        .center(
            settings.umbilical_width / 2
            - (settings.ptfe_cd + settings.umbilical_padding) / 2,
            -5,
        )
        .sketch()
        .rarray(*arr)
        .rect(settings.ptfe_safe_cut[0], settings.ptfe_safe_cut[1])
        .circle(settings.ptfe_cd / 2)
        .clean()
        .finalize()
        .cutBlind(-settings.ptfe_cz)
        .faces("<Y")
        .workplane()
        .sketch()
        .rarray(*arr)
        .circle(settings.ptfe_d / 2)
        .clean()
        .finalize()
        .cutThruAll()
        .faces(">Y")
        .workplane()
        .sketch()
        .rarray(*arr)
        .rect(settings.ptfe_safe_cut[0], settings.ptfe_safe_cut[1])
        .circle(settings.ptfe_cd / 2)
        .clean()
        .finalize()
        .cutBlind(-settings.ptfe_cz)
        .faces("<Y[1]")
        .workplane()
        .sketch()
        .rarray(*arr)
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
        .rarray(*arr)
        .circle(settings.can_thickness / 2)
        .finalize()
        .cutThruAll()
        .center(0, -settings.can_thickness / 2)
        .sketch()
        .rarray(*arr)
        .rect(settings.can_thickness, settings.can_thickness)
        .finalize()
        .cutThruAll()
    )
