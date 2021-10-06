import pandas as pd
import os

class Data:
    '''
    class Data: Used to get complete dataset from the IMS Test 1, 2, and 3
    '''
    def __init__(self, indir):
        self.directory = indir
        
    def get_dataset_test1(self):
        '''
        This function is used to get dataset in a csv format 
        for Test 1 of IMS Dataset that contains 8 channels in
        each file.
        '''
        final_data = pd.DataFrame()
        for filename in os.listdir(self.directory):
            df=pd.read_csv(os.path.join(self.directory, filename), sep='\t', header=None)
            df['filename'] = os.path.basename(filename)
            df1= pd.DataFrame(df)
            df1.columns = ['bx1','by1','bx2','by2', 'bx3','by3','bx4','by4','Class']
            dfs=[final_data, df1]
            final_data = final_data.append(df1) 
        return final_data

    def get_dataset_test2(self):
        '''
        This function is used to get dataset in a csv format 
        for Test 2 of IMS Dataset that contains 4 channels in
        each file.
        '''
        final_data = pd.DataFrame()
        for filename in os.listdir(self.directory):
            df=pd.read_csv(os.path.join(self.directory, filename), sep='\t', header=None)
            df['filename'] = os.path.basename(filename)
            df1= pd.DataFrame(df)
            df1.columns = ['bx1','by1','bx2','by2','Class']
            dfs=[final_data, df1]
            final_data = final_data.append(df1) 
        return final_data

    def get_dataset_test3(self):
        '''
        This function is used to get dataset in a csv format 
        for Test 3 of IMS Dataset that contains 4 channels in
        each file.
        '''
        final_data = pd.DataFrame()
        for filename in os.listdir(self.directory):
            df = pd.read_csv(os.path.join(self.directory, filename), sep='\t', header=None)
            df['filename'] = os.path.basename(filename)
            df1= pd.DataFrame(df)
            df1.columns = ['bx1','by1','bx2','by2','Class']
            dfs=[final_data, df1]
            final_data = final_data.append(df1) 
        return final_data

