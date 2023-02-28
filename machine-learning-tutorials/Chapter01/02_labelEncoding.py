from sklearn import preprocessing

label_encoder = preprocessing.LabelEncoder()

input_classes = ['audi', 'ford', 'audi', 'toyota', 'ford', 'bmw']

# print classes
label_encoder.fit(input_classes)
print("class mapping...")
for i, item in enumerate(label_encoder.classes_):
    print(item, "--->", i)

# transform s set of classes
labels = ['toyota', 'ford', 'audi']
encoded_labels = label_encoder.transform(labels)
print("Labels =", labels)
print("Encoded labels =", list(encoded_labels))

# inverse transform
encoded_labels = [2,1,0,3,1]
decoded_labels = label_encoder.inverse_transform(encoded_labels)
print("Encoded labels =", encoded_labels)
print("Decoded Labels =", list(decoded_labels))