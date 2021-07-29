import csv
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB

from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.naive_bayes import BernoulliNB
from sklearn.linear_model import LogisticRegression


class Game:
    conditions = []
    move = 0
    
    def __init__(self, conditions, move):
        super().__init__()
        self.conditions = conditions
        self.move = move        

class Machine:
    games = []
    clf = SVC(kernel='linear')
    #clf_svm_auto = make_pipeline(StandardScaler(), SVC(gamma='auto'))
    

    def __init__(self, model='support_vector_machine'):
        super().__init__()
        self.games = []

        print(model)

        if model == 'decision_tree_classifier':
            self.clf = DecisionTreeClassifier()
        elif model == 'gaussian_nb':
            self.clf = GaussianNB()
        elif model == 'random_forest_classifier':
            self.clf = RandomForestClassifier(random_state=0)
        elif model == 'gradient_boosting_classifier':
            self.clf = GradientBoostingClassifier(random_state=0)
        elif model == 'ada_boost_classifier':
            self.clf = AdaBoostClassifier(random_state=0)
        elif model == 'bernoulli_nb':
            self.clf = BernoulliNB()
        elif model == 'logistic_regression':
            self.clf = LogisticRegression(random_state=0)
                
        with open('moves_2.csv','r') as c:
            print("Loading training games")
            o = csv.reader(c)
            #print("The contents of the above file is as follows:")
            for r in o:
                lst = list(map(int,r))
                g = Game(lst[1:11], lst[11])
                self.games.append(g)
    
    def fit(self):
        training, test = train_test_split(self.games, test_size=1, random_state=42)
        train_x = [x.conditions for x in training]
        train_y = [x.move for x in training]
        test_x = [x.conditions for x in test]
        test_y = [x.move for x in test]
        
        self.clf.fit(train_x, train_y)
    
    def predict(self, currentBoardConditions):
        return self.clf.predict([currentBoardConditions])