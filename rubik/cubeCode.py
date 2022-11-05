
import re
from rubik.cubeColor import CubeColor
from rubik.cubeFacePosition import CubeFacePosition

class CubeCode:
    
    CODE_LENGTH = 54
    
    CUBE_WIDTH = 3
    
    FACE_POSITION_ORDER = [
        CubeFacePosition.FRONT,
        CubeFacePosition.RIGHT,
        CubeFacePosition.BACK,
        CubeFacePosition.LEFT,
        CubeFacePosition.UP,
        CubeFacePosition.DOWN,
    ]
    
    FACE_COORD_MAPPINGS = {
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
    
    FACE_CENTER_INDICES = [4, 13, 22, 31, 40, 49]
    
    def __init__(self, codeText):
        # make sure supplied param is a string
        assert (isinstance(codeText, str))
        
        # make sure "cube code" is 54 chars long
        assert (len(codeText) == self.CODE_LENGTH)
        
        # make sure is over alphabet [brgoyw]
        assert (not bool(re.search('[^brgoyw#]', codeText)))
        
        # make sure contains every color
        for color in CubeColor.getFaceColors():
            assert (codeText.__contains__(color.value))
            
        # make sure contains even distribution of colors
        colorDistributions = {c: 0 for c in CubeColor.getFaceColors()}
        
        for letter in codeText:
            color = CubeColor(letter)
            colorDistributions[color] += 1
        
        assert (len(set(colorDistributions.values())) == 1)
        
        # make sure there are no 2 center cubelet faces with same color
        centerColors = set(map(lambda index: CubeColor(codeText[index]), self.FACE_CENTER_INDICES))
        assert (len(centerColors) == len(CubeColor.getFaceColors()))
        
        self.text = codeText