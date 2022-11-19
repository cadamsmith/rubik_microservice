
from unittest import TestCase

from rubik.cubeSolver import CubeSolver
from rubik.cubeFacePosition import CubeFacePosition
from rubik.faceRotationDirection import FaceRotationDirection
from rubik.solveStage import SolveStage
from rubik.cube import Cube

class CubeSolverTest(TestCase):
    
    ''' CubeSolver.__init__ -- NEGATIVE TESTS '''
    
    def test_cubeSolver_init_10010_ShouldThrowExceptionForNonSuppliedCube(self):
        """ supplying no cube should throw exception """
        
        with self.assertRaises(Exception):
            CubeSolver()
    
    def test_cubeSolver_init_10020_ShouldThrowExceptionForCubeOfInvalidType(self):
        """ supplying cube of invalid type should throw exception """
        
        with self.assertRaises(Exception):
            CubeSolver('not a cube')
    
    ''' CubeSolver.__init__ -- POSITIVE TESTS '''
    
    def test_cubeSolver_init_20010_ShouldInstantiateCubeSolverForValidCubeCode(self):
        """ supplying valid cube should instantiate cube solver """
        
        solver = CubeSolver('oboybbrrggrborywwroogggbygrooyyorbobygwwygbrwwwrywbywg')
        
        self.assertIsInstance(solver, CubeSolver)
    
    def test_cubeSolver_init_20020_ShouldNotModifyInputCube(self):
        """ the cube supplied to the cube solver should not be modified """
        
        code = 'rbgobbogbwyboroywwyggwgrbbyroywogogwwyoyyrgyobrrwwbgrr'
        cube = Cube(code)
        
        CubeSolver(cube)
        self.assertEqual(cube.toCode(), code)
    
    ''' CubeSolver.__init__ -- Solve Down Cross -- POSITIVE TESTS '''
    
    def test_cubeSolver_init_30010_ASolvedCubeShouldYieldNoDirectionsToSolveDownCross(self):
        """ an already solved cube should give no solve directions """
        
        solver = CubeSolver(
            'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww',
            SolveStage.DOWN_CROSS
        )
        solution = solver.getSolution()
        
        self.assertEqual(len(solution), 0)
    
    def test_cubeSolver_init_30011_ACubeWithDownCrossShouldYieldNoDirectionsToSolveDownCross(self):
        """ a cube with a down cross should give no solve directions """
        
        solver = CubeSolver(
            'bowybbybrrgwrrgbrooywygbggwbrooorrorobggyoyybgwywwwgwy',
            SolveStage.DOWN_CROSS
        )
        solution = solver.getSolution()
        
        self.assertEqual(len(solution), 0)
    
    def test_cubeSolver_init_30030_ACubeWithUpDaisyShouldYieldCorrectDirectionsToSolveDownCross(self):
        """ a cube with an up daisy should yield correct solve directions """
        
        cube = Cube('wryrbobgbgbybrgwbrogyrgyyogborrobogwrwbwywgworyoowywyg')
        
        solver = CubeSolver(cube, SolveStage.DOWN_CROSS)
        solution = solver.getSolution()
        
        # execute all of the solution rotations
        for (facePosition, direction) in solution:
            cube.rotateFace(facePosition, direction)
        
        # check whether it actually solved down cross
        self.assertTrue(cube.hasDownCross())
    
    def test_cubeSolver_init_30031_AnotherCubeWithUpDaisyShouldYieldCorrectDirectionsToSolveDownCross(self):
        """ another cube with an up daisy should yield correct solve directions """
        
        cube = Cube('wbyrbybgwrgyorbryrgooygrwowbrgyogorrywowywowgyogbwgbbb')
        
        solver = CubeSolver(cube, SolveStage.DOWN_CROSS)
        solution = solver.getSolution()
        
        # execute all of the solution rotations
        for (facePosition, direction) in solution:
            cube.rotateFace(facePosition, direction)
        
        # check whether it actually solved down cross
        self.assertTrue(cube.hasDownCross())
    
    def test_cubeSolver_init_30032_YetAnotherCubeWithUpDaisyShouldYieldCorrectDirectionsToSolveDownCross(self):
        """ yet another cube with an up daisy should yield correct solve directions """
        
        cube = Cube('ybgobgbbbrrgyrgoyoogwrggwowbogooybyrowywywrwwyryrwbrbg')
        
        solver = CubeSolver(cube, SolveStage.DOWN_CROSS)
        solution = solver.getSolution()
        
        # execute all of the solution rotations
        for (facePosition, direction) in solution:
            cube.rotateFace(facePosition, direction)
        
        # check whether it actually solved down cross
        self.assertTrue(cube.hasDownCross())
    
    def test_cubeSolver_init_30040_ACubeWithoutUpDaisyShouldYieldCorrectDirectionsToSolveDownCross(self):
        """ a cube without an up daisy should yield correct solve directions """
        
        cube = Cube('owrwbwybyyywrrybygggorgbygwgbboogborwrrryowobgwogwbryo')
        
        solver = CubeSolver(cube, SolveStage.DOWN_CROSS)
        solution = solver.getSolution()
        
        # execute all of the solution rotations
        for (facePosition, direction) in solution:
            cube.rotateFace(facePosition, direction)
        
        # check whether it actually solved down cross
        self.assertTrue(cube.hasDownCross())
    
    def test_cubeSolver_init_30041_AnotherCubeWithoutUpDaisyShouldYieldCorrectDirectionsToSolveDownCross(self):
        """ another cube without an up daisy should yield correct solve directions """
        
        cube = Cube('yogrbyyoowobgrgbbrrygrgowgorybwowgbrwrybybogogywwwrywb')
        
        solver = CubeSolver(cube, SolveStage.DOWN_CROSS)
        solution = solver.getSolution()
        
        # execute all of the solution rotations
        for (facePosition, direction) in solution:
            cube.rotateFace(facePosition, direction)
        
        # check whether it actually solved down cross
        self.assertTrue(cube.hasDownCross())
    
    def test_cubeSolver_init_30042_YetAnotherCubeWithoutUpDaisyShouldYieldCorrectDirectionsToSolveDownCross(self):
        """ yet another cube without an up daisy should yield correct solve directions """
        
        cube = Cube('owyobygwwowyrrorygbgbbggrrbwwgroywywroroyrybbogggwboby')
        
        solver = CubeSolver(cube, SolveStage.DOWN_CROSS)
        solution = solver.getSolution()
        
        # execute all of the solution rotations
        for (facePosition, direction) in solution:
            cube.rotateFace(facePosition, direction)
        
        # check whether it actually solved down cross
        self.assertTrue(cube.hasDownCross())
        
    ''' CubeSolver.__init__ -- Solve Down Layer -- POSITIVE TESTS '''

    def test_cubeSolver_init_40010_ASolvedCubeShouldYieldNoDirectionsToSolveDownLayer(self):
        """ an already solved cube should give no solve directions """
        
        solver = CubeSolver(
            'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww',
            SolveStage.DOWN_LAYER
        )
        solution = solver.getSolution()
        
        self.assertEqual(len(solution), 0)
        
    def test_cubeSolver_init_40011_ACubeWithASolvedDownLayerShouldYieldNoDirectionsToSolveDownLayer(self):
        """ a cube with a solved down layer should give no solve directions """
        
        solver = CubeSolver(
            'yryybgbbbgybrryrrrygyogrgggrorbobooogoobygbyowwwwwwwww',
            SolveStage.DOWN_LAYER
        )
        solution = solver.getSolution()
        
        self.assertEqual(len(solution), 0)
    
    def test_cubeSolver_init_40020_ACubeWithUpDaisyShouldYieldCorrectDirectionsToSolveDownLayer(self):
        """ a cube with an up daisy should yield correct solve directions """
        
        cube = Cube('wryrbobgbgbybrgwbrogyrgyyogborrobogwrwbwywgworyoowywyg')
        
        solver = CubeSolver(cube, SolveStage.DOWN_LAYER)
        solution = solver.getSolution()
        
        # execute all of the solution rotations
        for (facePosition, direction) in solution:
            cube.rotateFace(facePosition, direction)
        
        # check whether it actually solved down layer
        self.assertTrue(cube.isDownLayerSolved())
    
    def test_cubeSolver_init_40021_AnotherCubeWithUpDaisyShouldYieldCorrectDirectionsToSolveDownLayer(self):
        """ another cube with an up daisy should yield correct solve directions """
        
        cube = Cube('wbyrbybgwrgyorbryrgooygrwowbrgyogorrywowywowgyogbwgbbb')
        
        solver = CubeSolver(cube, SolveStage.DOWN_LAYER)
        solution = solver.getSolution()
        
        # execute all of the solution rotations
        for (facePosition, direction) in solution:
            cube.rotateFace(facePosition, direction)
        
        # check whether it actually solved down layer
        self.assertTrue(cube.isDownLayerSolved())
    
    def test_cubeSolver_init_40022_YetAnotherCubeWithUpDaisyShouldYieldCorrectDirectionsToSolveDownLayer(self):
        """ yet another cube with an up daisy should yield correct solve directions """
        
        cube = Cube('ybgobgbbbrrgyrgoyoogwrggwowbogooybyrowywywrwwyryrwbrbg')
        
        solver = CubeSolver(cube, SolveStage.DOWN_LAYER)
        solution = solver.getSolution()
        
        # execute all of the solution rotations
        for (facePosition, direction) in solution:
            cube.rotateFace(facePosition, direction)
        
        # check whether it actually solved down layer
        self.assertTrue(cube.isDownLayerSolved())
    
    def test_cubeSolver_init_40030_ACubeWithoutUpDaisyShouldYieldCorrectDirectionsToSolveDownLayer(self):
        """ a cube without an up daisy should yield correct solve directions """
        
        cube = Cube('owrwbwybyyywrrybygggorgbygwgbboogborwrrryowobgwogwbryo')
        
        solver = CubeSolver(cube, SolveStage.DOWN_LAYER)
        solution = solver.getSolution()
        
        # execute all of the solution rotations
        for (facePosition, direction) in solution:
            cube.rotateFace(facePosition, direction)
        
        # check whether it actually solved down layer
        self.assertTrue(cube.isDownLayerSolved())
    
    def test_cubeSolver_init_40031_AnotherCubeWithoutUpDaisyShouldYieldCorrectDirectionsToSolveDownLayer(self):
        """ another cube without an up daisy should yield correct solve directions """
        
        cube = Cube('yogrbyyoowobgrgbbrrygrgowgorybwowgbrwrybybogogywwwrywb')
        
        solver = CubeSolver(cube, SolveStage.DOWN_LAYER)
        solution = solver.getSolution()
        
        # execute all of the solution rotations
        for (facePosition, direction) in solution:
            cube.rotateFace(facePosition, direction)
        
        # check whether it actually solved down layer
        self.assertTrue(cube.isDownLayerSolved())
    
    def test_cubeSolver_init_40032_YetAnotherCubeWithoutUpDaisyShouldYieldCorrectDirectionsToSolveDownLayer(self):
        """ yet another cube without an up daisy should yield correct solve directions """
        
        cube = Cube('owyobygwwowyrrorygbgbbggrrbwwgroywywroroyrybbogggwboby')
        
        solver = CubeSolver(cube, SolveStage.DOWN_LAYER)
        solution = solver.getSolution()
        
        # execute all of the solution rotations
        for (facePosition, direction) in solution:
            cube.rotateFace(facePosition, direction)
        
        # check whether it actually solved down layer
        self.assertTrue(cube.isDownLayerSolved())
    
    ''' CubeSolver.__init__ -- Solve Down and Middle Layers -- POSITIVE TESTS '''
    
    def test_cubeSolver_init_50010_ASolvedCubeShouldYieldNoRotationsToSolveDownAndMiddleLayers(self):
        """ a solved cube should give no rotations to solve down and middle layers """
        
        solver = CubeSolver(
            'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww',
            SolveStage.DOWN_AND_MIDDLE_LAYERS
        )
        solution = solver.getSolution()
        
        self.assertEqual(len(solution), 0)
        
    def test_cubeSolver_init_50011_ACubeWithSolvedDownAndMiddleLayersShouldYieldNoRotationsToSolveThoseTwoLayers(self):
        """ a cube with solved down, mid layers should give no directions to solve down, mid layers """
        
        solver = CubeSolver(
            'ygrbbbbbbyoyrrrrrrgryggggggrbboooooogyoyyyoybwwwwwwwww',
            SolveStage.DOWN_AND_MIDDLE_LAYERS
        )
        solution = solver.getSolution()
        
        self.assertEqual(len(solution), 0)
    
    def test_cubeSolver_init_50020_AnCubeWithoutAnyProgressShouldYieldCorrectRotationsToSolveDownAndMiddleLayers(self):
        """ a cube with down cross should yield correct rotations to solve down and middle layers """
        
        cube = Cube('rorwbrrgwwgrbrygwoyogoggbgyoywworbygywbbyobbgyrorwboyw')
        
        solver = CubeSolver(cube, SolveStage.DOWN_AND_MIDDLE_LAYERS)
        solution = solver.getSolution()
        
        # execute all of the solution rotations
        for (facePosition, direction) in solution:
            cube.rotateFace(facePosition, direction)
        
        # check whether it actually solved down and middle layers
        self.assertTrue(cube.isDownLayerSolved())
        self.assertTrue(cube.isMiddleLayerSolved())
    
    def test_cubeSolver_init_50030_ACubeWithUpDaisyShouldYieldCorrectRotationsToSolveDownAndMiddleLayers(self):
        """ a cube with down cross should yield correct rotations to solve down and middle layers """
        
        cube = Cube('brogbbbowggryrgbrywoyrgroyorbwbooyorgwgwywowwyyrbwybgg')
        
        solver = CubeSolver(cube, SolveStage.DOWN_AND_MIDDLE_LAYERS)
        solution = solver.getSolution()
        
        # execute all of the solution rotations
        for (facePosition, direction) in solution:
            cube.rotateFace(facePosition, direction)
        
        # check whether it actually solved down and middle layers
        self.assertTrue(cube.isDownLayerSolved())
        self.assertTrue(cube.isMiddleLayerSolved())
    
    def test_cubeSolver_init_50040_ACubeWithDownCrossShouldYieldCorrectRotationsToSolveDownAndMiddleLayers(self):
        """ a cube with down cross should yield correct rotations to solve down and middle layers """
        
        cube = Cube('rggbbggbyrrbrrygrboygbgyogbwywgooyooorwoybbowywrwwwrwy')
        
        solver = CubeSolver(cube, SolveStage.DOWN_AND_MIDDLE_LAYERS)
        solution = solver.getSolution()
        
        # execute all of the solution rotations
        for (facePosition, direction) in solution:
            cube.rotateFace(facePosition, direction)
        
        # check whether it actually solved down and middle layers
        self.assertTrue(cube.isDownLayerSolved())
        self.assertTrue(cube.isMiddleLayerSolved())
    
    def test_cubeSolver_init_50050_ACubeWithSolvedDownLayerShouldYieldCorrectRotationsToSolveDownAndMiddleLayers(self):
        """ a cube with solved down layer should yield correct rotations to solve down and middle layers """
        
        cube = Cube('gorybybbbyoybrrrrroggbgygggobrrogoooyrboyyygbwwwwwwwww')
        
        solver = CubeSolver(cube, SolveStage.DOWN_AND_MIDDLE_LAYERS)
        solution = solver.getSolution()
        
        # execute all of the solution rotations
        for (facePosition, direction) in solution:
            cube.rotateFace(facePosition, direction)
        
        # check whether it actually solved down and middle layers
        self.assertTrue(cube.isDownLayerSolved())
        self.assertTrue(cube.isMiddleLayerSolved())
    
    def test_cubeSolver_init_50051_AnotherCubeWithSolvedDownLayerShouldYieldCorrectRotationsToSolveDownAndMiddleLayers(self):
        """ another cube with solved down layer should yield correct rotations to solve down and middle layers """
        
        cube = Cube('roggbybbboorrrbrrryyorgbgggbgyooroooybbyyyggywwwwwwwww')
        
        solver = CubeSolver(cube, SolveStage.DOWN_AND_MIDDLE_LAYERS)
        solution = solver.getSolution()
        
        # execute all of the solution rotations
        for (facePosition, direction) in solution:
            cube.rotateFace(facePosition, direction)
        
        # check whether it actually solved down and middle layers
        self.assertTrue(cube.isDownLayerSolved())
        self.assertTrue(cube.isMiddleLayerSolved())
    
    ''' CubeSolver.__init__ -- Solve Down, Middle Layers and Up Face -- POSITIVE TESTS '''
    
    def test_cubeSolver_init_60040_ASolvedCubeShouldYieldNoRotationsToSolveDownAndMiddleLayersAndUpCross(self):
        """ a solved cube should give no rotations to solve down and middle layers """
        
        solver = CubeSolver('bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww', SolveStage.DOWN_MID_LAYERS_AND_UP_CROSS)
        expected = []
        
        self.assertEqual(solver.getSolution(), expected)
        
    def test_cubeSolver_init_60041_ACubeWithSolvedDownAndMiddleLayersAndUpCrossShouldYieldNoRotationsToSolveThose(self):
        """ a cube with solved down, mid layers and up cross should give no directions to solve down, mid layers and up cross """
        
        solver = CubeSolver('ygrbbbbbbyoyrrrrrrgryggggggrbboooooogyoyyyoybwwwwwwwww', SolveStage.DOWN_MID_LAYERS_AND_UP_CROSS)
        expected = []
        
        self.assertEqual(solver.getSolution(), expected)
        
    def test_cubeSolver_init_60050_ACubeWithSolvedDownAndMiddleLayersShouldYieldCorrectDirectionsToSolveDownMidLayersAndUpCross(self):
        """ a cube with solved down, mid layers should give correct directions to solve down, mid layers and up cross """
        
        solver = CubeSolver(
            'gbgbbbbbbyyyrrrrrrbobggggggyyyoooooooyrrygoyrwwwwwwwww',
            SolveStage.DOWN_MID_LAYERS_AND_UP_CROSS
        )
        
        expected = [
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.FRONT, FaceRotationDirection.COUNTERCLOCKWISE),
            
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.FRONT, FaceRotationDirection.COUNTERCLOCKWISE)
        ]
        
        self.assertEqual(solver.getSolution(), expected)
        
    def test_cubeSolver_init_60060_ACubeWithSolvedDownLayerShouldYieldCorrectDirectionsToSolveDownMidLayersAndUpCross(self):
        
        solver = CubeSolver(
            'gyyobgbbbbborryrrrybobgggggbrryogoooyogyyryorwwwwwwwww',
            SolveStage.DOWN_MID_LAYERS_AND_UP_CROSS
        )
        
        expected = [
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.LEFT, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.FRONT, FaceRotationDirection.COUNTERCLOCKWISE),
            
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.COUNTERCLOCKWISE),
            
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.FRONT, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.LEFT, FaceRotationDirection.COUNTERCLOCKWISE),
            
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.BACK, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.RIGHT, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.BACK, FaceRotationDirection.COUNTERCLOCKWISE),
            
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.FRONT, FaceRotationDirection.COUNTERCLOCKWISE),
            
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.FRONT, FaceRotationDirection.COUNTERCLOCKWISE)
        ]
        
        self.assertEqual(solver.getSolution(), expected)
    
    ''' CubeSolver.getSolution -- POSITIVE TESTS '''
    
    def test_cubeSolver_getSolution_20010_ShouldReturnValidDirections(self):
        """ should return list of type (CubeFacePosition, FaceRotationDirection) """
        
        solver = CubeSolver('gbogbobwowboyroyrygbrggrrwywwyyoygrwgowbyyorbrgbwwgrob')
        
        rotations = solver.getSolution()
        
        # make sure directions is a list
        self.assertIsInstance(rotations, list)
        
        for rotation in rotations:
            # make sure each direction is a tuple
            self.assertIsInstance(rotation, tuple)
            
            # make sure each direction tuple has 2 items each
            self.assertEqual(len(rotation), 2)
            
            # make sure each direction is of type (CubeFacePosition, FaceRotationDirection)
            (facePosition, rotationDirection) = rotation
            
            self.assertIsInstance(facePosition, CubeFacePosition)
            self.assertIsInstance(rotationDirection, FaceRotationDirection)
    
    