from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parent.parent/'_series2_support'))
from complete_runner import main
main(Path(__file__).resolve().parent)
