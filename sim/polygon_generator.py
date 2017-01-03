from ode import TriMeshData

def make_polygon(vertices):
    meshdata = TriMeshData()
    faces = [[0, i, i+1] for i in range(1,len(vertices)-1)]
    meshdata.build(vertices, faces)
    return meshdata
