import sys
import pandas as pd

path = './CIC-IDS2017/MachineLearningCVE/'

csv_data = pd.read_csv(path+'Wednesday-workingHours.pcap_ISCX.csv')  # Read data



labels_values_counts = csv_data[' Label'].value_counts()
labels_values = labels_values_counts.index

path1 = './CIC-IDS2017/Wednesday_'

n = 5000      # Extract data

for labels_value in labels_values:
    df_sample = csv_data[csv_data[' Label'] == labels_value]
    sample_count = df_sample[' Label'].value_counts()
    if sample_count[0] >= 5000:
        df_sample = df_sample.sample(n)
        filepath = path1 + labels_value + '_extract'+str(n)+'.csv'  # input
    else:
        print("Insufficient data"+str(n))
        filepath = path1 + labels_value + '_extract' + str(sample_count[0]) + '.csv'  # input
    df_columns = pd.DataFrame([list(csv_data.columns)])
    df_columns.to_csv(filepath, mode='w', header=False, index=0)
    df_sample.to_csv(filepath, mode='a', header=False, index=0)

# labels = csv_data['Label'].value_counts()
#
# print(labels)
