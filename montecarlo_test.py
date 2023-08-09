from combined import die, game, analyzer
import unittest
import pandas as pd
import numpy as np

class combinedTestSuite(unittest.TestCase):
    
    def test_1_die(self):
        die1 = die(np.array([1,2,3,4,5,6]))
        message = "die is not array"
        self.assertTrue(isinstance(die1.faces, np.ndarray), message)
        
    def test_2_die(self):
        die1 = die(np.array([1,2,3,4,5,6]))
        die1.change_weight([1],10)
        message = "weight is not numeric"
        self.assertTrue(isinstance(die1.new_weight, (int,float)), message)
        
    def test_3_die(self):
        die1 = die(np.array([1,2,3,4,5,6]))
        message = "return is not a list"
        self.assertTrue(isinstance(die1.roll_die(), list), message)
        
    def test_4_die(self):
        die1 = die(np.array([1,2,3,4,5,6]))
        message = "return is not a dataframe"
        self.assertTrue(isinstance(die1.current_state(), pd.DataFrame), message)

#####
    def test_1_game(self):
        die1 = die(np.array([1,2,3,4,5,6]))
        die2 = die(np.array([1,2,3,4,5,6]))
        die2.change_weight([1],10)
        game1 = game([die1,die2])
        message = "Dice are not in list form"
        self.assertTrue(isinstance(game1.dice, list), message)
        
    def test_2_game(self):
        die1 = die(np.array([1,2,3,4,5,6]))
        die2 = die(np.array([1,2,3,4,5,6]))
        die2.change_weight([1],10)
        game1 = game([die1,die2])
        game1.play(5)
        expected = 5
        self.assertEqual(game1.n_roll, expected)
        
    def test_3_game(self):
        die1 = die(np.array([1,2,3,4,5,6]))
        die2 = die(np.array([1,2,3,4,5,6]))
        die2.change_weight([1],10)
        game1 = game([die1,die2])
        game1.play(5)
        game1.results('wide')
        expected = 'wide'
        self.assertEqual(game1.style, expected)

    def test_1_analyzer(self):
        die1 = die(np.array([1,2,3,4,5,6]))
        die2 = die(np.array([1,2,3,4,5,6]))
        die2.change_weight([1],10)
        game1 = game([die1,die2])
        game1.play(5)
        
        analyzer1 = analyzer(game1)
        message = "game is not of game class"
        self.assertTrue(game1.__class__.__name__ == 'game', message)
        
    def test_2_analyzer(self):
        die1 = die(np.array([1,2,3,4,5,6]))
        die2 = die(np.array([1,2,3,4,5,6]))
        die2.change_weight([1],10)
        game1 = game([die1,die2])
        game1.play(5)
        
        analyzer1 = analyzer(game1)
        message = "output is not an integer"
        self.assertTrue(isinstance(analyzer1.jackpot(), int), message)
        
    def test_3_analyzer(self):
        die1 = die(np.array([1,2,3,4,5,6]))
        die2 = die(np.array([1,2,3,4,5,6]))
        die2.change_weight([1],10)
        game1 = game([die1,die2])
        game1.play(5)
        
        analyzer1 = analyzer(game1)
        message = "return is not a dataframe"
        self.assertTrue(isinstance(analyzer1.face_count(), pd.DataFrame), message)
        
    def test_4_analyzer(self):
        die1 = die(np.array([1,2,3,4,5,6]))
        die2 = die(np.array([1,2,3,4,5,6]))
        die2.change_weight([1],10)
        game1 = game([die1,die2])
        game1.play(5)
        
        analyzer1 = analyzer(game1)
        message = "return is not a dataframe"
        self.assertTrue(isinstance(analyzer1.combo_count(), pd.DataFrame), message)
    
    def test_5_analyzer(self):
        die1 = die(np.array([1,2,3,4,5,6]))
        die2 = die(np.array([1,2,3,4,5,6]))
        die2.change_weight([1],10)
        game1 = game([die1,die2])
        game1.play(5)
        
        analyzer1 = analyzer(game1)
        message = "return is not a dataframe"
        self.assertTrue(isinstance(analyzer1.perm_count(), pd.DataFrame), message)

if __name__ == '__main__':
    unittest.main(verbosity=2)