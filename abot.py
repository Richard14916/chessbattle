import time
import chess
import copy
import numpy as np
from func_timeout import func_timeout, FunctionTimedOut

class evaluate_position:
    def __init__(self,board,side):
        self.board = board
    
