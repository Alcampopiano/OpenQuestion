# from hypothesize.measuring_associations import *
import os

# alpha=.05
# nboot=100
# tr=.2
# beta=.2

try:
    os.chdir('OpenQuestion/tests')
except:
    pass

def test_wincor():

    # np.random.seed(42)
    # df = create_example_data(2)
    # results = wincor(df.cell_1, df.cell_2)
    # expected = pickle.load(open("test_data/wincor.pkl", "rb"))

    assert 1 == 2
