
import itertools

from rubik.cubeColor import CubeColor
from rubik.cubelet import Cubelet
from rubik.cubeCode import CubeCode
from rubik.cubeFacePosition import CubeFacePosition
from rubik.faceRotationDirection import FaceRotationDirection
from rubik.cubeRotationDirection import CubeRotationDirection

class Cube:
    """Represents a 3x3x3 Rubik's cube"""
    
    """the 27 cubelets that make up the cube"""
    cubelets = {}
    
    """
    coordinates of the cubelets that make up each cube face,
    ordered by position in cube code
    """
    CUBELET_COORDS = {
        CubeFacePosition.FRONT: [
            (0, 0, 0), (1, 0, 0), (2, 0, 0),
            (0, 1, 0), (1, 1, 0), (2, 1, 0),
            (0, 2, 0), (1, 2, 0), (2, 2, 0),
        ],
        CubeFacePosition.RIGHT: [
            (2, 0, 0), (2, 0, 1), (2, 0, 2),
            (2, 1, 0), (2, 1, 1), (2, 1, 2),
            (2, 2, 0), (2, 2, 1), (2, 2, 2),
        ],
        CubeFacePosition.BACK: [
            (2, 0, 2), (1, 0, 2), (0, 0, 2),
            (2, 1, 2), (1, 1, 2), (0, 1, 2),
            (2, 2, 2), (1, 2, 2), (0, 2, 2),
        ],
        CubeFacePosition.LEFT: [
            (0, 0, 2), (0, 0, 1), (0, 0, 0),
            (0, 1, 2), (0, 1, 1), (0, 1, 0),
            (0, 2, 2), (0, 2, 1), (0, 2, 0),
        ],
        CubeFacePosition.UP: [
            (0, 0, 2), (1, 0, 2), (2, 0, 2),
            (0, 0, 1), (1, 0, 1), (2, 0, 1),
            (0, 0, 0), (1, 0, 0), (2, 0, 0),
        ],
        CubeFacePosition.DOWN: [
            (0, 2, 0), (1, 2, 0), (2, 2, 0),
            (0, 2, 1), (1, 2, 1), (2, 2, 1),
            (0, 2, 2), (1, 2, 2), (2, 2, 2),
        ],
    }
    
    """ how many cubelets make up each side """
    WIDTH = 3
    
    """ dimension of the cube (3D) """
    DIM = 3
    
    """ how many cubelets total make up each face """
    FACE_AREA = WIDTH ** 2
    
    """ how many cubelets total make up the cube """
    VOLUME = WIDTH ** DIM
    
    """coordinates of all of the center cubelets in each cube face"""
    FACE_CENTER_CUBELET_COORDS = {
        CubeFacePosition.FRONT: (1, 1, 0),
        CubeFacePosition.BACK: (1, 1, 2),
        CubeFacePosition.LEFT: (0, 1, 1),
        CubeFacePosition.RIGHT: (2, 1, 1),
        CubeFacePosition.UP: (1, 0, 1),
        CubeFacePosition.DOWN: (1, 2, 1)
    }

    def __init__(self, cubeCode: str | CubeCode):
        """initializes the cube from a cube code representing the initial state"""
        
        assert isinstance(cubeCode, (str, CubeCode))
        
        # if supplied a string, turn it into a CubeCode
        if isinstance(cubeCode, str):
            cubeCode = CubeCode(cubeCode)
        
        for i, j, k in itertools.product(*[range(self.WIDTH)] * self.DIM):
            self.cubelets[i, j, k] = Cubelet()
        
        codeIndex = 0
        for facePosition in cubeCode.FACE_POSITION_ORDER:
            for coords in Cube.CUBELET_COORDS[facePosition]:
                color = CubeColor(cubeCode.text[codeIndex])
                self.cubelets[coords].setFaceColor(facePosition, color)
                
                codeIndex += 1
    
    def rotateFace(self, facePosition: CubeFacePosition, direction: FaceRotationDirection):
        """Rotates one of the cube's faces either clockwise or counterclockwise"""
        
        assert (isinstance(facePosition, CubeFacePosition))
        assert (isinstance(direction, FaceRotationDirection))
        
        # determine which direction to rotate each cubelet
        
        if (
            facePosition is CubeFacePosition.FRONT and direction is FaceRotationDirection.CLOCKWISE
            or facePosition is CubeFacePosition.BACK and direction is FaceRotationDirection.COUNTERCLOCKWISE
        ):
            cubeletRotationDirection = CubeRotationDirection.FLIP_RIGHTWARD
        
        elif (
            facePosition is CubeFacePosition.FRONT and direction is FaceRotationDirection.COUNTERCLOCKWISE
            or facePosition is CubeFacePosition.BACK and direction is FaceRotationDirection.CLOCKWISE
        ):
            cubeletRotationDirection = CubeRotationDirection.FLIP_LEFTWARD
            
        elif (
            facePosition is CubeFacePosition.LEFT and direction is FaceRotationDirection.CLOCKWISE
            or facePosition is CubeFacePosition.RIGHT and direction is FaceRotationDirection.COUNTERCLOCKWISE
        ):
            cubeletRotationDirection = CubeRotationDirection.FLIP_FORWARD
        
        elif (
            facePosition is CubeFacePosition.LEFT and direction is FaceRotationDirection.COUNTERCLOCKWISE
            or facePosition is CubeFacePosition.RIGHT and direction is FaceRotationDirection.CLOCKWISE
        ):
            cubeletRotationDirection = CubeRotationDirection.FLIP_BACKWARD
            
        elif (
            facePosition is CubeFacePosition.UP and direction is FaceRotationDirection.CLOCKWISE
            or facePosition is CubeFacePosition.DOWN and direction is FaceRotationDirection.COUNTERCLOCKWISE
        ):
            cubeletRotationDirection = CubeRotationDirection.SPIN_LEFTWARD
        
        elif (
            facePosition is CubeFacePosition.UP and direction is FaceRotationDirection.COUNTERCLOCKWISE
            or facePosition is CubeFacePosition.DOWN and direction is FaceRotationDirection.CLOCKWISE
        ):
            cubeletRotationDirection = CubeRotationDirection.SPIN_RIGHTWARD
        
        # start tracking changes to the cube's cubelets
        alteredCubelets = {}
        
        # for each cubelet in up face
        for (x, y, z) in Cube.CUBELET_COORDS[facePosition]:
            
            # figure out where the cubelet will go to
            newCoord = self.rotateCoord((x, y, z), facePosition, direction)
            
            # update its position and rotate accordingly
            alteredCubelets[newCoord] = self.cubelets[x, y, z]
            alteredCubelets[newCoord].rotate(cubeletRotationDirection)
        
        # apply changes to the cubelets
        self.cubelets.update(alteredCubelets)
        
    def rotateCoord(self, coord, facePosition: CubeFacePosition, direction: FaceRotationDirection):
        """determines the new location of a cube coordinate if a specific face rotation was applied to the cube"""
        
        assert (isinstance(facePosition, CubeFacePosition))
        assert (isinstance(direction, FaceRotationDirection))
        
        # a coordinate not in the face being rotated is not affected
        if not coord in self.CUBELET_COORDS[facePosition]:
            return coord
        
        (x, y, z) = coord
        
        # determine the coordinate transform function to apply based on the manner of rotation specified
        
        if (
            facePosition is CubeFacePosition.FRONT and direction is FaceRotationDirection.CLOCKWISE
            or facePosition is CubeFacePosition.BACK and direction is FaceRotationDirection.COUNTERCLOCKWISE
        ):
            coordTransform = lambda x, y, z : (2 - y, x, z)
        
        elif (
            facePosition is CubeFacePosition.FRONT and direction is FaceRotationDirection.COUNTERCLOCKWISE
            or facePosition is CubeFacePosition.BACK and direction is FaceRotationDirection.CLOCKWISE
        ):
            coordTransform = lambda x, y, z : (y, 2 - x, z)
            
        elif (
            facePosition is CubeFacePosition.LEFT and direction is FaceRotationDirection.CLOCKWISE
            or facePosition is CubeFacePosition.RIGHT and direction is FaceRotationDirection.COUNTERCLOCKWISE
        ):
            coordTransform = lambda x, y, z : (x, 2 - z, y)
        
        elif (
            facePosition is CubeFacePosition.LEFT and direction is FaceRotationDirection.COUNTERCLOCKWISE
            or facePosition is CubeFacePosition.RIGHT and direction is FaceRotationDirection.CLOCKWISE
        ):
            coordTransform = lambda x, y, z : (x, z, 2 - y)
            
        elif (
            facePosition is CubeFacePosition.UP and direction is FaceRotationDirection.CLOCKWISE
            or facePosition is CubeFacePosition.DOWN and direction is FaceRotationDirection.COUNTERCLOCKWISE
        ):
            coordTransform = lambda x, y, z : (z, y, 2 - x)
        
        elif (
            facePosition is CubeFacePosition.UP and direction is FaceRotationDirection.COUNTERCLOCKWISE
            or facePosition is CubeFacePosition.DOWN and direction is FaceRotationDirection.CLOCKWISE
        ):
            coordTransform = lambda x, y, z : (2 - z, y, x)
        
        return coordTransform(x, y, z)
    
    def toCode(self):
        """Serializes the cube into a cube code"""
        
        codeText = ''
        
        for facePosition in CubeCode.FACE_POSITION_ORDER:
            for coords in Cube.CUBELET_COORDS[facePosition]:
                color = self.cubelets[coords].faces[facePosition]
                codeText += color.value
                
        cubeCode = CubeCode(codeText)
        return cubeCode.text
