from sklearn.preprocessing import LabelEncoder
#Label encoding across multiple columns in scikit-learn
from collections import defaultdict
d = defaultdict(LabelEncoder)
#With this, you now retain all columns LabelEncoder as dictionary.

# Encoding the variable
fit = df.apply(lambda x: d[x.name].fit_transform(x))

# Inverse the encoded
fit.apply(lambda x: d[x.name].inverse_transform(x))

# Using the dictionary to label future data
df.apply(lambda x: d[x.name].transform(x))

#Saving and loading a dictonary
import pickle
a = {'hello': 'world'}
with open('filename.pickle', 'wb') as handle:
    pickle.dump(a, handle, protocol=pickle.HIGHEST_PROTOCOL)
with open('filename.pickle', 'rb') as handle:
    b = pickle.load(handle)
print a == b
