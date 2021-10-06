import json
import numpy as np

class ComplexEncoder(json.JSONEncoder):
    '''
    This class is used if data is having complex numbers or is represented by ndarray so as to convert
    data into representable json format.
    '''
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        
        elif np.iscomplexobj(obj):
            return abs(obj)

        elif hasattr(obj,'reprJSON'):
            return obj.reprJSON()

        else:
            return json.JSONEncoder.default(self, obj)