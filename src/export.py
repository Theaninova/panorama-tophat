#!/usr/bin/env python3
import cadquery as cq
from settings import Settings
from side import side
from front import front
from umbilical import umbilical
from corner import corner
from assembly import assembly
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

side_length = 200
extra_length = 120 + 2 * 20

for size in [250, 300, 350]:
    settings = Settings()
    settings.size = (size + extra_length, size + extra_length)
    settings.corner_size = (
        (size + extra_length - side_length) / 2,
        (size + extra_length - side_length) / 2,
    )

    result = corner(settings)
    cq.exporters.export(result, f"../STEPs/corner_{size}_x4.step")
    cq.exporters.export(result, f"../STLs/corner_{size}_x4.stl")

settings = Settings()
length = 300 + extra_length
settings.size = (length, length)
settings.corner_size = ((length - side_length) / 2, (length - side_length) / 2)

for count in range(2, 7):
    settings.umbilical_count = count
    result_umbilical = umbilical(settings).rotate((0, 0, 0), (1, 0, 0), -90)
    cq.exporters.export(result_umbilical, f"../STEPs/umbilical_{count}.step")
    cq.exporters.export(result_umbilical, f"../STLs/umbilical_{count}.stl")

result_side = side(settings, 1).rotate((0, 0, 0), (1, 0, 0), -90)
cq.exporters.export(result_side, "../STEPs/side_x2.step")
cq.exporters.export(result_side, "../STLs/side_x2.stl")

result_front = front(settings).rotate((0, 0, 0), (1, 0, 0), -90)
cq.exporters.export(result_front, "../STEPs/front.step")
cq.exporters.export(result_front, "../STLs/front.stl")

result_assembly = assembly(settings)
cq.exporters.export(
    result_assembly.toCompound()
    .rotate((0, 0, 0), (1, 0, 0), -90)
    .rotate((0, 0, 0), (0, 1, 0), 180)
    .translate((120, 0, 0)),
    "../media/assembly.svg",
    opt={
        "showAxes": False,
        "marginLeft": 100,
        "marginTop": 50,
        "strokeColor": (0xDB, 0x3F, 0x38),
    },
)
