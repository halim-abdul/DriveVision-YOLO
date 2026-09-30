import argparse
from . import __version__

def build_parser():
    p=argparse.ArgumentParser(prog="drivevision",description="Autonomous-driving perception research framework")
    p.add_argument("--version",action="version",version=__version__)
    sub=p.add_subparsers(dest="command")
    sub.add_parser("doctor",help="check runtime environment")
    sub.add_parser("benchmark",help="run benchmark suite")
    return p

def main():
    args=build_parser().parse_args()
    if args.command=="doctor":
        import torch
        print({"version":__version__,"torch":torch.__version__,"cuda":torch.cuda.is_available()})
    elif args.command=="benchmark": print("Use scripts/run_benchmarks.py")

if __name__=="__main__":main()
