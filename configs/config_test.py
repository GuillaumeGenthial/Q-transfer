EXP_NAME = "test"
ENV = 'MountainCar-v0'
TARGET_NAMES = [
"time",
]
SOURCE_NAMES = [
"bumps",
"standard"
]
VERBOSE = False
EXPLORATION_PROBA_START = 0.2
EXPLORATION_PROBA_END = 0.1
MAX_ITER = 1000
NUM_TRIALS_SOURCES = 100
NUM_TRIALS_TARGETS = [100]
NUM_TRIALS_EVAL = 100
RELOAD_WEIGHTS = False
DISCOUNT = 1.
ELIGIBILITY = False
TRAIN = True
DEEP_MODES = [1]
RELOAD_FREQ = 200
EXPERIENCE_REPLAY_SIZE = 10000
AVERAGE_TIMES = 1
LR_ENSEMBLE = 0.001
LR_DEEP = 0.001
