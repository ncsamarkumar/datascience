from sklearn import tree

#height, weight, shoe size

x = [[180,70,10],[160,68,8],[179,65,9],[190,85,11],[130,50,6],[200,95,11],[110,45,5],[100,40,4],[210,100,12],[172,70,8],[122,40,7],[168,70,6],[140,60,6]]
y = ['male','male','male','male','female','male','female','female','male','female','female','female','female']

clf = tree.DecisionTreeClassifier()
clf = clf.fit(x,y)
prediction = clf.predict([[140,76,12]])
print(prediction)