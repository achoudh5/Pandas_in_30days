#import pandas as pd
import pandas as pd

#creating a data frame by reading the values
#of the .csv using the methid read_csv
data_frame1 = pd.read_csv(r'name_of_your_file1.csv')
data_frame2 = pd.read_csv(r'name_of_your_file2.csv')

dataframe_concat= pd.concat([data_frame1,data_frame2])

#printing the concatenated data-frames as a data frame
print (dataframe_concat)