import argparse,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/'metrics'))
import adapters,run_metrics
import audited_receivers,audited_oracles
audited_receivers.install(adapters);audited_oracles.install(adapters)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',required=True);a=p.parse_args();run_metrics.main(a.output)
