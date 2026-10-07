from pathlib import Path
import sys
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'_series2_support'))
from complete_runner import main
if __name__=='__main__': main(HERE)
