
from unittest import TestCase
import rubik.solve as solve

class SolveTest(TestCase):
    
    # solve - POSITIVE TESTS
    
    def test_solve_10010_ShouldReturnStatusOKForValidParams(self):
        
        result = solve._solve({
            'op': 'solve',
            'cube': 'wrobbobgygwrwrwgoybgorgwbggyboboywyrgywoygbbwyorrwyrro'
        })
        
        self.assertIn('status', result)
        self.assertEqual(result['status'], 'ok')
    
    # solve - NEGATIVE TESTS
    
    # supplying no cube param should result in error status
    def test_solve_20010_ShouldErrorOnMissingCube(self):
        result = solve._solve({'op': 'solve', 'dir': 'R'})
        
        self.assertIn('status', result)
        self.assertEqual(result['status'], solve.ERROR_MISSING_CUBE)
    
    # supplying non-string cube should result in error status
    def test_solve_20020_ShouldErrorOnNonStringCube(self):
        
        result = solve._solve({
            'op': 'solve',
            'cube': [1, 2, 3]
        })
        
        self.assertIn('status', result)
        self.assertEqual(result['status'], solve.ERROR_INVALID_CUBE)
    
    # supplying string cube not 54 chars long should result in error status
    def test_solve_20030_ShouldErrorOnCubeWithInvalidLength(self):
        
        result = solve._solve({
            'op': 'solve',
            'cube': 'bryogw'
        })
        
        self.assertIn('status', result)
        self.assertEqual(result['status'], solve.ERROR_INVALID_CUBE)
        
    # supplying a string cube not over the alphabet [brgoyw] should throw exception
    def test_solve_20040_ShouldErrorOnCubeContainingNonColorChars(self):
        
        result = solve._solve({
            'op': 'solve',
            'cube': 'gorbbgobbwgowrrwrbgwwygyyggr!rgowyybbrwwyrybgyyoowboor'
        })
        
        self.assertIn('status', result)
        self.assertEqual(result['status'], solve.ERROR_INVALID_CUBE)
    
    # supplying a string cube not containing every color code should throw exception
    def test_solve_20050_ShouldErrorOnCubeNotContainingEveryColor(self):
        
        result = solve._solve({
            'op': 'solve',
            'cube': 'ggwobgrrbrwgorrwggwwoggbrgggbrwobbrwggorgobobggowwbogg'
        })
        
        self.assertIn('status', result)
        self.assertEqual(result['status'], solve.ERROR_INVALID_CUBE)
            
    # supplying a string cube with an uneven distribution of colors should throw exception
    def test_solve_20060_ShouldErrorOnCubeWithUnevenColorDistribution(self):
        
        result = solve._solve({
            'op': 'solve',
            'cube': 'wobrbrrryyoowrwrggggyggwrrwgyroobobborwbyyggowwbowybyy'
        })
        
        self.assertIn('status', result)
        self.assertEqual(result['status'], solve.ERROR_INVALID_CUBE)
            
    # supplying a string cube with non-unique center cubelet face colors should throw exception
    def test_solve_20070_ShouldErrorOnCubeWithNonUniqueCenterFaceColors(self):
        
        result = solve._solve({
            'op': 'solve',
            'cube': 'gyyogroywgrygrorbwryyggbbwwbwowoboybrbgoywwooyggrwrbbr'
        })
        
        self.assertIn('status', result)
        self.assertEqual(result['status'], solve.ERROR_INVALID_CUBE)
        