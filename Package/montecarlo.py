import pandas as pd
import numpy as np

class die:
    '''
    Come roll a die! *fun guarenteed*
    Customizable die with faces and weights; can be rolled one or more times to select a face.
    '''
    
    def __init__(self, faces):
        '''
        Create your die!
        
        Input: faces (all letters or all numbers; categorical or numeric)
        Faces must be distinct and placed in a numpy array.
        Default weight = 1.0 for each face (fair die)
        '''
        self.faces = faces
        self.__df = pd.DataFrame({'faces':faces,
                     'weights':[1.0 for f in faces]}).set_index('faces')
        
        #are faces in an array?
        if not isinstance(faces, np.ndarray):
            raise TypeError("Faces not an array")
        
        #are faces distinct?
        if len(np.unique(faces)) != len(faces):
            raise ValueError("Values not distinct")
            
    def change_weight(self, face_val, new_weight):
        '''
        Want to create an unfair die?
        
        Input: faces you want to change in a list
        Input: corresponding new weight
        
        Face must appear in previous numpy array. 
        Weight must be numeric (int or float) or castable to numeric. 
        '''
        self.face_val = face_val
        self.new_weight = new_weight
        
        #is face on die?
        for val in face_val:
            if val not in self.faces:
                raise IndexError("Face not on die")
        
        self.__df.loc[face_val] = new_weight
      
        #is weight numeric?
        if not isinstance(new_weight, (int,float)):
            raise TypeError("Weight not numeric")
        
        #can weight be cast to int?
        try:
            new_weight = int(new_weight)
        except:
            raise TypeError("Weight not numeric")

        #can weight be cast to float?
        try:
            new_weight = float(new_weight)
        except:
            raise TypeError("Weight not numeric")
        
    def roll_die(self, n_roll = 1):
        '''
        Roll your die!
        
        Input: number of rolls (integer). Default = 1 roll
        Return: list of faces rolled
        '''
        return self.__df.sample(n_roll, weights=self.__df.weights, replace=True).index.to_list()
        
    def current_state(self):
        '''
        What does my die look like?
        
        Input: none
        Return: dataframe with faces (index) and their corresponding weights
        '''
        return self.__df.copy()
    

class game:
    '''
    This game allows a used to roll one or more similar die, one or more times.
    Each die must have the same number of faces, but can be weighted differently.
    '''
    
    def __init__(self, dice):
        '''
        Place one or more die into the game.
        
        Input: list of pre-instantiated dice
        '''
        self.dice = dice
        
    def play(self, n_roll):
        '''
        Roll your dice!
        
        Input: number of rolls (integer)
        '''
        self.n_roll = n_roll
        self.__df = pd.DataFrame({'Roll_number': range(n_roll)}).set_index("Roll_number")
        
        for die in self.dice:
            new_roll = pd.DataFrame({die: die.roll_die(n_roll)})
            self.__df = pd.concat([self.__df, new_roll], axis = 1, ignore_index = True)
            
        self.__df = self.__df.rename_axis(index= "Roll Number", columns = 'Die Number')
        
    def results(self, style = 'wide'):
        '''
        See your results!
        
        Input: style of dataframe containing dice results. Either 'wide' or 'narrow'. 
        Default = 'wide'
        Return: narrow dataframe with dice results. Multiindex of roll number 
        and die number with corresponding column of face results. 
        '''
        self.style = style
        if style == 'narrow':
            return self.__df.copy()
        elif style == 'wide':
            return self.__df.copy().stack().reset_index().set_index(["Roll Number", "Die Number"]).rename({0:'Face Rolled'}, axis=1)
        else:
            raise ValueError ("Try 'wide' or 'narrow'") 


class analyzer:
    '''
    Analyze game results! caution: fun may occur
    Input your results of a single game and compute descriptive statistics.
    '''
    def __init__(self, game):
        '''
        Place game into analyzer.
        
        Input: game object. Game must be of game class
        '''
        self.game = game
        if game.__class__.__name__ != 'game':
            raise ValueError("Object must be of game class")
            
    def jackpot(self):
        '''
        Compute jackpot (when all die roll same face)
        
        Input: none
        Return: number of jackpots (integer)
        '''
        df = self.game.results().unstack()
        results = sum(df.eq(df.iloc[:, 0], axis=0).all(1))
        return results
    
    def face_count(self):
        '''
        Compute the number of times a given face is rolled in each event.        
        
        Input: none
        Return: dataframe with roll number as index and face rolled as columns.
        Count values in cells. Fill value = 0.
        '''
        df = self.game.results()
        result_df = df.pivot_table(index='Roll Number', columns='Face Rolled', aggfunc='size', fill_value=0)
        result_df = result_df.reindex(columns=self.game.dice[0].faces, fill_value=0)
        return result_df
    
    def combo_count(self):
        '''
        Computes the distinct combinations of faces rolled, along with their counts.
        Combinations are order-independent and may contain repetitions.

        Input: none
        Return: dataframe with multindex of distinct combinations and corresponding count column.
        '''
        df = self.game.results().unstack()
        results = pd.DataFrame(np.sort(df.values, axis=1), columns=df.columns).value_counts()
        return pd.DataFrame(results)

    def perm_count(self):
        '''
        Computes the distinct permutations of faces rolled, along with their counts.
        Combinations are order-dependent and may contain repetitions.

        Input: none
        Return: dataframe with multindex of distinct permutations and corresponding count column.
        '''
        df = self.game.results().unstack()
        results = df.value_counts().to_frame()
        return results