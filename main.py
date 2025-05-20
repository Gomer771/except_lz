
from cod import Mistake

def execute_analysis():

    inspector = Mistake('var6.csv')
    inspector.analyze_data()

if __name__ == "__main__":
    execute_analysis()