import unittest
from sort import sort

class TestSortFunction(unittest.TestCase):
    def test_standard_package(self):
        # Package is neither bulky nor heavy
        self.assertEqual(sort(30, 40, 50, 10), "STANDARD")
    
    def test_bulky_by_volume(self):
        # Package is bulky due to large volume
        self.assertEqual(sort(100, 100, 100, 15), "SPECIAL")
    
    def test_bulky_by_dimension(self):
        # Package is bulky because one dimension exceeds 150 cm
        self.assertEqual(sort(200, 50, 50, 10), "SPECIAL")
    
    def test_heavy_package(self):
        # Package is heavy but not bulky
        self.assertEqual(sort(50, 50, 50, 25), "SPECIAL")
    
    def test_rejected_package(self):
        # Package is both bulky and heavy
        self.assertEqual(sort(200, 200, 200, 25), "REJECTED")
    
    def test_edge_case_bulky_dimension(self):
        # Package has a dimension exactly at the bulky threshold
        self.assertEqual(sort(150, 50, 50, 10), "SPECIAL")
    
    def test_edge_case_bulky_volume(self):
        # Package has a volume exactly at the bulky threshold
        self.assertEqual(sort(100, 100, 100, 10), "SPECIAL")
    
    def test_edge_case_heavy(self):
        # Package has a mass exactly at the heavy threshold
        self.assertEqual(sort(50, 50, 50, 20), "SPECIAL")
    
    def test_just_below_bulky_volume(self):
        # Package volume is just below the bulky threshold
        self.assertEqual(sort(99, 100, 100, 10), "STANDARD")
    
    def test_just_below_heavy_mass(self):
        # Package mass is just below the heavy threshold
        self.assertEqual(sort(50, 50, 50, 19.99), "STANDARD")
    
    def test_large_dimension_small_mass(self):
        # Bulky due to dimension, light mass
        self.assertEqual(sort(160, 20, 20, 5), "SPECIAL")
    
    def test_small_dimension_heavy_mass(self):
        # Heavy due to mass, small dimensions
        self.assertEqual(sort(20, 20, 20, 22), "SPECIAL")
    
    def test_zero_dimension(self):
        # Edge case with zero dimensions (assuming zero dimensions are acceptable)
        self.assertEqual(sort(0, 50, 50, 10), "STANDARD")
        self.assertEqual(sort(50, 0, 50, 10), "STANDARD")
        self.assertEqual(sort(50, 50, 0, 10), "STANDARD")
    
    def test_zero_mass(self):
        # Edge case with zero mass (assuming zero mass is acceptable)
        self.assertEqual(sort(50, 50, 50, 0), "STANDARD")
    
    def test_negative_dimensions(self):
        # Negative dimensions should raise a ValueError
        with self.assertRaises(ValueError):
            sort(-100, 50, 50, 10)
        with self.assertRaises(ValueError):
            sort(50, -50, 50, 10)
        with self.assertRaises(ValueError):
            sort(50, 50, -50, 10)
    
    def test_negative_mass(self):
        # Negative mass should raise a ValueError
        with self.assertRaises(ValueError):
            sort(50, 50, 50, -10)

if __name__ == "__main__":
    unittest.main()