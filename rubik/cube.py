
import itertools
from rubik.cubeColor import CubeColor
from rubik.cubelet import Cubelet
from rubik.cubeCode import CubeCode
from rubik.cubeFacePosition import CubeFacePosition
from rubik.faceRotationDirection import FaceRotationDirection

class Cube:
    '''
    Rubik's cube
    '''
    
    cubelets = {}
    
    FACE_CENTER_CUBELET_COORDS = [(1, 1, 0), (1, 1, 2), (0, 1, 1), (2, 1, 1), (1, 0, 1), (1, 2, 1)]

    def __init__(self, cubeCode):
        # make sure supplied param is a valid CubeCode
        assert (isinstance(cubeCode, CubeCode))
 
        self.size = cubeCode.CUBE_WIDTH
        self.faceArea = cubeCode.CUBE_WIDTH ** 2
               
        for i, j, k in itertools.product(*[range(cubeCode.CUBE_WIDTH)] * 3):
            self.cubelets[i, j, k] = Cubelet()
        
        codeIndex = 0
        for facePosition in cubeCode.FACE_POSITION_ORDER:
            for coords in cubeCode.FACE_COORD_MAPPINGS[facePosition]:
                color = CubeColor(cubeCode.text[codeIndex])
                self.cubelets[coords].setFaceColor(facePosition, color)
                
                codeIndex += 1
                
    def rotateFace(self, facePosition: CubeFacePosition, direction: FaceRotationDirection):
        # make sure supplied params are the right types
        assert (isinstance(facePosition, CubeFacePosition))
        assert (isinstance(direction, FaceRotationDirection))
                
    def toCode(self):
        
        codeText = ''
        
        for facePosition in CubeCode.FACE_POSITION_ORDER:
            for coords in CubeCode.FACE_COORD_MAPPINGS[facePosition]:
                color = self.cubelets[coords].faces[facePosition]
                codeText += color.value
                
        return CubeCode(codeText)            