from utils.make_data import Export
from utils.misc_opers import Misc
from services.mongodb.upload_data import CRUD
import time

def main():
    start_time=time.time()   
    
    #tO EXPORT THE DATA 
    #Export('datasets\\IMS', 3).export_data()
    
    # df = Misc('df', 'Class', 2).fetch_df()
    # features = Misc(df, 'Class', 2).features('by2')
    CRUD('results\\').insert()
    end_time = time.time()
    
    print('Executed in {} seconds'.format(end_time-start_time))

if __name__ == '__main__':
    main()