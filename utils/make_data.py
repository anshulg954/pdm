import os
from services.data.get_data import Data
class Export:
    '''
    This class exports the dataset to csv format
    '''
    def __init__(self, directory, type):
        self.directory =  directory
        self.type = type
        
    def export_data(self):
        '''
        Export the data to csv
        '''
        
        data_dir = self.directory
        if self.type == 1:
            data_dir = data_dir+'\\1st_test'
            df = Data(data_dir).get_dataset_test1()
            df.to_csv('datasets\\IMScsv\\test1.csv', index=False)
        
        elif self.type == 2:
            data_dir = data_dir+'\\2nd_test'
            df = Data(data_dir).get_dataset_test2()
            df.to_csv('datasets\\IMScsv\\test2.csv', index=False)
        
        elif self.type == 3:
            data_dir = data_dir+'\\3rd_test'
            df = Data(data_dir).get_dataset_test3()
            df.to_csv('datasets\\IMScsv\\test3.csv', index=False)

        else:
            return 'Invalid Type Input!'

