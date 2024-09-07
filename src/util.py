import cadquery as cq


def transform(workplane: cq.Workplane, m: cq.Matrix) -> cq.Workplane:
    return workplane.newObject(
        [
            o.transformGeometry(m) if isinstance(o, cq.Shape) else o
            for o in workplane.objects
        ]
    )
