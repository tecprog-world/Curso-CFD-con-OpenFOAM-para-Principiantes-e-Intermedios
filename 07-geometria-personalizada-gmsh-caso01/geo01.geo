// Gmsh project created on Sun Dec 26 18:52:36 2021
SetFactory("OpenCASCADE");
//+
Circle(1) = {0, -2, 0, 0.5, 0, 2*Pi};
//+
Circle(2) = {0, 2, 0, 0.5, 0, 2*Pi};
//+
Ellipse(3) = {0, 0, 0, 0.5, 0.25, 0, 2*Pi};

