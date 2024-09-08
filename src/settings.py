from dataclasses import dataclass


@dataclass
class Settings:
    size = (420, 420)
    corner_size = (100, 100)

    thickness = 10
    top_thickness = 10

    extrusion_thickness = 20
    holder_padding = 30
    bore_padding = holder_padding / 2

    fillet = 2

    ptfe_d = 3
    ptfe_cd = 9.5
    ptfe_cz = 6
    ptfe_safe_cut = (3, 10)

    can_thickness = 5.5

    umbilical_padding = 1
    umbilical_spacing = 4
    umbilical_count = 4

    umbilical_width = ptfe_cd + umbilical_padding + can_thickness

    logo_scale = 0.04
    logo_emboss = 1
