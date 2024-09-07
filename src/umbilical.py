from settings import Settings
from side import side


def umbilical(settings: Settings):
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
        .rarray(
            settings.umbilical_spacing + settings.umbilical_width,
            1,
            settings.umbilical_count,
            1,
        )
        .cboreHole(settings.ptfe_d, settings.ptfe_cd, settings.ptfe_cz)
        .faces("<Y")
        .workplane()
        .center(
            -(
                settings.ptfe_cd / 2
                + settings.umbilical_padding
                + settings.can_thickness / 2
            ),
            0,
        )
        .rarray(
            settings.umbilical_spacing + settings.umbilical_width,
            1,
            settings.umbilical_count,
            1,
        )
        .hole(settings.can_thickness)
    )
