/*---------------------------------------------------------------------------*\
  =========                 |
  \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox
   \\    /   O peration     | Website:  https://openfoam.org
    \\  /    A nd           | Copyright (C) YEAR OpenFOAM Foundation
     \\/     M anipulation  |
-------------------------------------------------------------------------------
License
    This file is part of OpenFOAM.

    OpenFOAM is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    OpenFOAM is distributed in the hope that it will be useful, but WITHOUT
    ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
    FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
    for more details.

    You should have received a copy of the GNU General Public License
    along with OpenFOAM.  If not, see <http://www.gnu.org/licenses/>.

Description
    Template for use with codeStream.

\*---------------------------------------------------------------------------*/

#include "dictionary.H"
#include "Ostream.H"
#include "Pstream.H"
#include "unitConversion.H"

//{{{ begin codeInclude
#line 36 "/opt/openfoam9/tutorials/resources/blockMesh/angledDuct/#codeStream"
#include "pointField.H"
        #include "transformField.H"
//}}} end codeInclude

// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

namespace Foam
{

// * * * * * * * * * * * * * * * Local Functions * * * * * * * * * * * * * * //

//{{{ begin localCode

//}}} end localCode


// * * * * * * * * * * * * * * * Global Functions  * * * * * * * * * * * * * //

extern "C"
{
    void codeStream_e4d1a7bc617c19f981e9c7f57e5704d685cd9640
    (
        Ostream& os,
        const dictionary& dict
    )
    {
//{{{ begin code
        #line 42 "/opt/openfoam9/tutorials/resources/blockMesh/angledDuct/#codeStream"
const scalar halfWidth = (50)/2.0;

        // Length between the bend and outlet
        const scalar distOutlet = 100 + 100;

        pointField points
        ({
            point(0,          0,      -halfWidth), // pt 0
            point(100,   0,      -halfWidth), // pt 1
            point(distOutlet, 0,      -halfWidth), // pt 2
            point(0,          50, -halfWidth), // pt 3
            point(100,   50, -halfWidth), // pt 4
            point(distOutlet, 50, -halfWidth)  // pt 5
        });

        // Rotate points around z-axis
        points = transform(Rz(degToRad(45)), points);

        // Append points 6 and 7
        points.append(points[0]);  // pt 6
        points.append(points[3]);  // pt 7

        points[6].x() = -150;
        points[7].x() = -150;

        // Duplicate z points
        points.append(cmptMultiply(points, vector(1, 1, -1)));

        os  << points;
//}}} end code
    }
}


// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

} // End namespace Foam

// ************************************************************************* //

