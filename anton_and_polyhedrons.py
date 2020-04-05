'''

Anton's favourite geometric figures are regular polyhedrons. Note that there are five kinds of regular polyhedrons:

Tetrahedron. Tetrahedron has 4 triangular faces.
Cube. Cube has 6 square faces.
Octahedron. Octahedron has 8 triangular faces.
Dodecahedron. Dodecahedron has 12 pentagonal faces.
Icosahedron. Icosahedron has 20 triangular faces.
All five kinds of polyhedrons are shown on the picture below:

'''
my_dict = {}
shape = []
my_dict["Tetrahedron"] = 4

my_dict["Cube"] = 6

my_dict["Octahedron"] = 8

my_dict["Dodecahedron"] = 12

my_dict["Icosahedron"] = 20

sum = 0

n = int(input())

for i in range(n):
    shape.append(input())

for j in range(n):
    sum = sum + my_dict[shape[j]]

print(sum)
    