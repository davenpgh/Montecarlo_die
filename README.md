Grace Davenport's Monte Carlo Simulator

Synopsis:
This package contains three classes: `die`, `game` and `analyzer`. On a command line, install package with `pip install -e .` once in package directory.  In python environment, import package by `import Package`. Now classes can be accessed by `Package.die` for example. To explictly import `montecarlo` module, type `from davenpgh_ds5100_montecarlo.Package import montecarlo`. 

Example:
Create a die of `die` class by `die1 = die(np.array([1,2,3,4,5,6]))`.
Change the weight of `die1` by `die1.change_weight([1],10)`.
Roll `die1` 100 times by `die1.roll_die(100)`.
View `die1` results by `die1.current_state()`. This will return a pandas dataframe. For more details, see docstring below.
Create a second die, `die2 = die(np.array([1,2,3,4,5,6]))`. This is a fair die.

Create a game of `game` class by `game1 = game([die1,die2])`.
Roll all die in list 5 times by `game1.play(5)`.
View `game1` results by `game1.results(style = 'wide')`. This will return a pandas dataframe. For more details, see docstring below. 

Create an analyzer of `analyzer` class by `analyzer1 = analyzer(game1)`.
View the number of jackpots rolled (when all die roll same face) `analyzer1.jackpot()`.
View `analyzer1` face counts by `analyzer1.face_count()`. This will return a pandas dataframe.
View `analyzer1` number of distinct combinations rolled by `analyzer1.combo_count()`.
View `analyzer1` number of distinct permutations rolled by `analyzer1.perm_count()`.


API Description:

class die:
    '''
    Come roll a die! *fun guarenteed*
    Customizable die with faces and weights; can be rolled one or more times to select a face.
    '''
    
    die(faces)
        '''
        Create your die!
        
        Input: faces (all letters or all numbers, categorical or numeric)
        Faces must be distinct and placed in a numpy array.
        Default weight = 1.0 for each face (fair die)
        '''
        
     die.change_weight(face_val, new_weight)
        '''
        Want to create an unfair die?
        
        Input: face you want to change
        Input: corresponding new weight
        
        Face must appear in previous numpy array. 
        Weight must be numeric (int or float) or castable to numeric. 
        '''
        
      die.roll_die(n_roll = 1)
          '''
          Roll your die!
        
          Input: number of rolls (integer). Default = 1 roll
          Return: list of faces rolled
          '''
          
       die.current_state()
          '''
          What does my die look like?
        
          Input: none
          Return: dataframe with faces (index) and their corresponding weights
          '''
          
          
class game:
    '''
    This game allows a used to roll one or more similar die, one or more times.
    Each die must have the same number of faces, but can be weighted differently.
    '''
    
    game(dice)
       '''
        Place one or more die into the game.
        
        Input: list of pre-instantiated dice
        ''' 
        
    game.play(n_roll)
        '''
        Roll your dice!
        
        Input: number of rolls (integer)
        '''
    
    game.results(style = 'wide')
        '''
        See your results!
        
        Input: style of dataframe containing dice results. Either 'wide' or 'narrow'. 
        Default = 'wide'
        Return: narrow dataframe with dice results. Multiindex of roll number 
        and die number with corresponding column of face results. 
        '''

class analyzer:
   '''
    Analyze game results! caution: fun may occur
    Input your results of a single game and compute descriptive statistics.
    '''
    
    analyzer(game):
       '''
        Place game into analyzer.
        
        Input: game object. Game must be of game class
        '''
        
    analyzer.jackpot()
       '''
        Compute jackpot (when all die roll same face)
        
        Input: none
        Return: number of jackpots (integer)
        '''
        
     analyzer.face_count()
        '''
        Compute the number of times a given face is rolled in each event.        
        
        Input: none
        Return: dataframe with roll number as index and face rolled as columns.
        Count values in cells. Fill value = 0.
        '''
        
     anaylzer.combo_count()
        '''
        Computes the distinct combinations of faces rolled, along with their counts.
        Combinations are order-independent and may contain repetitions.

        Input: none
        Return: dataframe with multindex of distinct combinations and corresponding count column.
        '''
        
     analyzer.perm_count()
        '''
        Computes the distinct permutations of faces rolled, along with their counts.
        Combinations are order-dependent and may contain repetitions.

        Input: none
        Return: dataframe with multindex of distinct permutations and corresponding count column.
        ''' 
    
