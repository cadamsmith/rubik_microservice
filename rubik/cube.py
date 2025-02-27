
import itertools

from rubik.cubeColor import CubeColor
from rubik.cubelet import Cubelet
from rubik.cubeCode import CubeCode
from rubik.cubeFacePosition import CubeFacePosition
from rubik.faceRotationDirection import FaceRotationDirection
from rubik.cubeRotationDirection import CubeRotationDirection
from rubik.faceCubeletPosition import FaceCubeletPosition

class Cube:
    """Represents a 3x3x3 Rubik's cube"""
    
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
    
    """ coordinates of all of the center cubelets in each cube face """
    FACE_CENTER_CUBELET_COORDS = {
        CubeFacePosition.FRONT: (1, 1, 0),
        CubeFacePosition.BACK: (1, 1, 2),
        CubeFacePosition.LEFT: (0, 1, 1),
        CubeFacePosition.RIGHT: (2, 1, 1),
        CubeFacePosition.UP: (1, 0, 1),
        CubeFacePosition.DOWN: (1, 2, 1)
    }
    
    """
    orientation coords of the vertical faces, useful for CubeSolver algorithms
    
    they describe an orientation for a cube face as if it were pointing toward you,
    and that orientation is obtained by spinning the cube rightward to look at each cube face
    """
    FACE_ORIENTATION_COORDS = {
        CubeFacePosition.FRONT: {
            FaceCubeletPosition.UP_LEFT: (0, 0, 0),
            FaceCubeletPosition.UP_RIGHT: (2, 0, 0),
            FaceCubeletPosition.DOWN_LEFT: (0, 2, 0),
            FaceCubeletPosition.DOWN_RIGHT: (2, 2, 0),
            
            FaceCubeletPosition.UP: (1, 0, 0),
            FaceCubeletPosition.LEFT: (0, 1, 0),
            FaceCubeletPosition.RIGHT: (2, 1, 0)
        },
        CubeFacePosition.LEFT: {
            FaceCubeletPosition.UP_LEFT: (0, 0, 2),
            FaceCubeletPosition.UP_RIGHT: (0, 0, 0),
            FaceCubeletPosition.DOWN_LEFT: (0, 2, 2),
            FaceCubeletPosition.DOWN_RIGHT: (0, 2, 0),
            
            FaceCubeletPosition.UP: (0, 0, 1),
            FaceCubeletPosition.LEFT: (0, 1, 2),
            FaceCubeletPosition.RIGHT: (0, 1, 0)
        },
        CubeFacePosition.BACK: {
            FaceCubeletPosition.UP_LEFT: (2, 0, 2),
            FaceCubeletPosition.UP_RIGHT: (0, 0, 2),
            FaceCubeletPosition.DOWN_LEFT: (2, 2, 2),
            FaceCubeletPosition.DOWN_RIGHT: (0, 2, 2),
            
            FaceCubeletPosition.UP: (1, 0, 2),
            FaceCubeletPosition.LEFT: (2, 1, 2),
            FaceCubeletPosition.RIGHT: (0, 1, 2)
        },
        CubeFacePosition.RIGHT: {
            FaceCubeletPosition.UP_LEFT: (2, 0, 0),
            FaceCubeletPosition.UP_RIGHT: (2, 0, 2),
            FaceCubeletPosition.DOWN_LEFT: (2, 2, 0),
            FaceCubeletPosition.DOWN_RIGHT: (2, 2, 2),
            
            FaceCubeletPosition.UP: (2, 0, 1),
            FaceCubeletPosition.LEFT: (2, 1, 0),
            FaceCubeletPosition.RIGHT: (2, 1, 2)
        }
    }

    def __init__(self, cubeCode: str | CubeCode):
        """ initializes the cube from a cube code representing the initial state """
        
        assert isinstance(cubeCode, (str, CubeCode))
        
        # if supplied a string, turn it into a CubeCode
        if isinstance(cubeCode, str):
            cubeCode = CubeCode(cubeCode)
        
        # initialize all 27 cubelets without color
        self._cubelets = {}
        for i, j, k in itertools.product(*[range(self.WIDTH)] * self.DIM):
            self[i, j, k] = Cubelet()
        
        # iterate thru cube code, coloring cubelets accordingly
        codeIndex = 0
        for facePosition in cubeCode.FACE_POSITION_ORDER:
            for coords in Cube.CUBELET_COORDS[facePosition]:
                color = CubeColor(cubeCode.text[codeIndex])
                self[coords][facePosition] = color
                
                codeIndex += 1
    
    def __getitem__(self, coord: tuple[int]):
        """ accessor for the cubelets that make up the cube """
        
        # ensure coord is integer tuple (x, y, z), where x, y, z ∈ [0, 2]
        assert isinstance(coord, tuple)
        assert len(coord) == 3
        
        for num in coord:
            assert isinstance(num, int)
            assert 0 <= num and num <= 2
        
        # congrats, it's a valid index
        return self._cubelets[coord]
    
    def __setitem__(self, coord, value):
        """ mutator for the cubelets that make up the cube """
        
        # ensure coord is integer tuple (x, y, z), where x, y, z ∈ [0, 2]
        assert isinstance(coord, tuple)
        assert len(coord) == 3
        
        for num in coord:
            assert isinstance(num, int)
            assert 0 <= num and num <= 2
        
        # ensure value is Cubelet
        assert isinstance(value, Cubelet)
        
        # congrats, it's a valid assignment
        self._cubelets[coord] = value
    
    def rotateFace(self, facePosition: CubeFacePosition, direction: FaceRotationDirection):
        """ rotates one of the cube's faces either clockwise or counterclockwise """
        
        # ensure params are the right types
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
            alteredCubelets[newCoord] = self[x, y, z]
            alteredCubelets[newCoord].rotate(cubeletRotationDirection)
        
        # apply changes to the cubelets
        self._cubelets.update(alteredCubelets)
    
    def rotateCoord(self, coord, facePosition: CubeFacePosition, direction: FaceRotationDirection):
        """ 
        determines the new location of a cube coordinate if a specific face rotation was 
        applied to the cube
        """
        
        # ensure params are correct types
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
    
    def getFaceColor(self, facePosition: CubeFacePosition) -> CubeColor:
        """ get the color of a cube face, i.e. the color of the center tile on that face """
        
        # ensure params are right types
        assert isinstance(facePosition, CubeFacePosition)
        
        centerCoord = self.FACE_CENTER_CUBELET_COORDS[facePosition]
        faceColor = self[centerCoord][facePosition]
        
        return faceColor
    
    def toCode(self):
        """ serializes the cube into a cube code """
        
        codeText = ''
        
        for facePosition in CubeCode.FACE_POSITION_ORDER:
            for coords in Cube.CUBELET_COORDS[facePosition]:
                color = self[coords][facePosition]
                codeText += color.value
        
        cubeCode = CubeCode(codeText)
        return cubeCode.text
    
    '''
    methods for determining whether the cube satisfies certain conditions
    that are useful to check for in cube solver algorithms
    '''
    
    def hasUpDaisy(self):
        """ determines whether the cube has a daisy centered on the up face """
        
        # center coordinate of up face
        (centerX, centerY, centerZ) = self.FACE_CENTER_CUBELET_COORDS[CubeFacePosition.UP]
        
        # down color, also the colors the daisy petals should be
        downColor = self.getFaceColor(CubeFacePosition.DOWN)
        
        # coordinates of each petal cubelet
        petalCoords = [
            (centerX - 1, centerY, centerZ),
            (centerX, centerY, centerZ - 1),
            (centerX + 1, centerY, centerZ),
            (centerX, centerY, centerZ + 1)
        ]
        
        # check all petal cubelet coords
        for coord in petalCoords:
            
            # determine whether the up face color is the _cube's down color
            color = self[coord][CubeFacePosition.UP]
            
            if color != downColor:
                return False
        
        return True
    
    def hasDownCross(self):
        """ determines whether the cube has a cross centered on the down face """
        
        # center coordinate of down face
        (centerX, centerY, centerZ) = self.FACE_CENTER_CUBELET_COORDS[CubeFacePosition.DOWN]
        
        # down color, also the color that the plus sign of the down cross should be
        downColor = self.getFaceColor(CubeFacePosition.DOWN)
        
        # coordinates of each petal cubelet around the cross
        petalCoords = [
            (centerX - 1, centerY, centerZ),
            (centerX, centerY, centerZ - 1),
            (centerX + 1, centerY, centerZ),
            (centerX, centerY, centerZ + 1)
        ]
        
        # check all petal cubelet coords
        for coord in petalCoords:
            
            # determine whether its down face color is the cube's down color
            color = self[coord][CubeFacePosition.DOWN]
            
            if color != downColor:
                return False
        
        # need to check a pair of cubelet faces on all vertical side face positions of the cube
        otherFacesToCheck = [CubeFacePosition.FRONT, CubeFacePosition.LEFT, CubeFacePosition.BACK, CubeFacePosition.RIGHT]
        
        # go thru each face position
        for facePosition in otherFacesToCheck:
            
            # pair to check is center cubelet and cubelet below it
            (centerX, centerY, centerZ) = self.FACE_CENTER_CUBELET_COORDS[facePosition]
            (belowX, belowY, belowZ) = (centerX, centerY + 1, centerZ)
            
            # determine whether their color is the same
            faceColor = self[(centerX, centerY, centerZ)][facePosition]
            belowColor = self[(belowX, belowY, belowZ)][facePosition]
            
            if faceColor != belowColor:
                return False
        
        return True
    
    def isDownLayerSolved(self):
        """ determines whether the cube's down layer is solved """
        
        # down color, also the color that every tile on down face should be
        downColor = self.getFaceColor(CubeFacePosition.DOWN)
        
        # check all colors on down face
        for coord in self.CUBELET_COORDS[CubeFacePosition.DOWN]:
             
            # determine whether each is the right color
            color = self[coord][CubeFacePosition.DOWN]
            
            if color != downColor:
                return False
        
        # need to check more colors on each of the 4 vertical side face positions of the cube
        otherFacePositionsToCheck = [CubeFacePosition.FRONT, CubeFacePosition.LEFT, CubeFacePosition.BACK, CubeFacePosition.RIGHT]
        
        # check that the center tile and lower 3 tiles are the same color on each face
        lowerCoords = [(0, 2, 0), (1, 2, 0), (2, 2, 0)]
        
        for facePosition in otherFacePositionsToCheck:
            
            # center color
            faceColor = self.getFaceColor(facePosition)
            
            # determine whether all 3 lower colors are the same
            lowerColors = list(map(lambda coord : self[coord][facePosition], lowerCoords))
            
            if any(color != faceColor for color in lowerColors):
                return False
            
            # get next 3 lower coords
            lowerCoords = list(map(
                lambda coord : self.rotateCoord(coord, CubeFacePosition.DOWN, FaceRotationDirection.COUNTERCLOCKWISE),
                lowerCoords
            ))
        
        return True
    
    def isMiddleLayerSolved(self):
        """ determines whether the cube's middle layer is solved """
        
        # face positions that need to be inspected
        verticalFacePositions = [
            CubeFacePosition.FRONT, CubeFacePosition.LEFT, CubeFacePosition.BACK, CubeFacePosition.RIGHT
        ]
        
        # check that the all 3 middle layer cubelet face colors are the same for each vertical cube face
        for facePosition in verticalFacePositions:
            
            # center color
            faceColor = self.getFaceColor(facePosition)
            
            # these are the cubelets to the left and right of the center cubelet
            middleCoords = [
                self.FACE_ORIENTATION_COORDS[facePosition][FaceCubeletPosition.LEFT],
                self.FACE_ORIENTATION_COORDS[facePosition][FaceCubeletPosition.RIGHT]
            ]
            
            # determine whether the 2 middle coords have same color as face
            middleColors = list(map(lambda coord : self[coord][facePosition], middleCoords))
            
            if any(color != faceColor for color in middleColors):
                return False
        
        return True
    
    def hasUpCross(self):
        """ determines whether an up cross is present on the cube """
        
        # center coordinate of down face
        (centerX, centerY, centerZ) = self.FACE_CENTER_CUBELET_COORDS[CubeFacePosition.UP]
        upColor = self.getFaceColor(CubeFacePosition.UP)
        
        # coordinates of each cubelet on petals of the cross
        petalCoords = [
            (centerX - 1, centerY, centerZ),
            (centerX, centerY, centerZ - 1),
            (centerX + 1, centerY, centerZ),
            (centerX, centerY, centerZ + 1)
        ]
        
        # check all petal cubelet coords
        for coord in petalCoords:
            
            # determine whether its down face color is the cube's down color
            color = self[coord][CubeFacePosition.UP]
            
            if color != upColor:
                return False
        
        return True
    
    def isUpFaceSolved(self):
        """ determines whether the cube's up face is solved """
        
        # up color, also the color that every tile on up face should be
        upColor = self.getFaceColor(CubeFacePosition.UP)
        
        # check all colors on up face
        for coord in self.CUBELET_COORDS[CubeFacePosition.UP]:
             
            # determine whether each is the right color
            color = self[coord][CubeFacePosition.UP]
            
            if color != upColor:
                return False
        
        return True
    
    def isUpEdgesSolved(self):
        """ determines whether the faces on the vertical edges of the up layer are solved """
        
        # need to check more colors on each of the 4 vertical side face positions of the cube
        verticalFacePositions = [CubeFacePosition.FRONT, CubeFacePosition.LEFT, CubeFacePosition.BACK, CubeFacePosition.RIGHT]
        
        # check that the center tile and upper 3 tiles are the same color on each face
        for facePosition in verticalFacePositions:
            upLayerCoords = [
                self.FACE_ORIENTATION_COORDS[facePosition][FaceCubeletPosition.UP_LEFT],
                self.FACE_ORIENTATION_COORDS[facePosition][FaceCubeletPosition.UP],
                self.FACE_ORIENTATION_COORDS[facePosition][FaceCubeletPosition.UP_RIGHT],
            ]
            
            # center color
            faceColor = self.getFaceColor(facePosition)
            
            # determine whether all 3 lower colors are the same
            upLayerColors = list(map(lambda coord : self[coord][facePosition], upLayerCoords))
            
            if any(color != faceColor for color in upLayerColors):
                return False
        
        return True
    
    def isUpCornersSolved(self):
        """ determines whether the cube's up layer corners are solved """
        
        # first check whether up layer is solved
        if not self.isUpFaceSolved():
            return False
        
        # need to check more colors on each of the 4 vertical side face positions of the cube
        otherFacePositionsToCheck = [CubeFacePosition.FRONT, CubeFacePosition.LEFT, CubeFacePosition.BACK, CubeFacePosition.RIGHT]
        
        # check that the center tile and up corners are the same color on each face
        for facePosition in otherFacePositionsToCheck:
            upCornerCoords = [
                self.FACE_ORIENTATION_COORDS[facePosition][FaceCubeletPosition.UP_LEFT],
                self.FACE_ORIENTATION_COORDS[facePosition][FaceCubeletPosition.UP_RIGHT]
            ]
            
            # center color
            faceColor = self.getFaceColor(facePosition)
            
            # determine whether all 3 lower colors are the same
            upLayerColors = list(map(lambda coord : self[coord][facePosition], upCornerCoords))
            
            if any(color != faceColor for color in upLayerColors):
                return False
        
        return True
    
    def isUpLayerSolved(self):
        """ determines whether the cube's up layer is solved """
        
        # first check whether up face is solved
        if not self.isUpFaceSolved():
            return False
        
        # next check the up face edges
        if not self.isUpEdgesSolved():
            return False
        
        return True
    