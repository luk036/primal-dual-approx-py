from random import randint

from pldl.netlist import Netlist, create_random_graph
from pldl.netlist_algo import min_maximal_matching
import matplotlib.pyplot as plt
import networkx as nx
import argparse
import logging
import sys

from pldl import __version__

__author__ = "Wai-Shing Luk"
__copyright__ = "Wai-Shing Luk"
__license__ = "mit"

_logger = logging.getLogger(__name__)


def run_MMM(H: Netlist):
    mincost = 100000000000
    minpart = []
    randseq = [randint(0, 1) for _ in range(H.number_of_modules())]

    if isinstance(H.modules, range):
        part = randseq
    elif isinstance(H.modules, list):
        part = {v: k for v, k in zip(H.modules, randseq)}
    else:
        raise NotImplementedError

    minpart = part.copy()
    return mincost, minpart


def plot(H: Netlist, p, solnset):
    N = H.number_of_modules()
    M = H.number_of_nets()
    pos = nx.spring_layout(H.G)
    nx.draw_networkx_edges(H.G, pos=pos, width=1)
    nx.draw_networkx_nodes(H.G,
                           nodelist=range(N, N + M),
                           node_color='y',
                           node_size=40,
                           pos=pos)
    nx.draw_networkx_nodes(H.G,
                           nodelist=list(p.keys()),
                           node_size=list(p.values()),
                           node_color=list(p.values()),
                           cmap=plt.cm.Reds_r,
                           pos=pos)
    nx.draw_networkx_nodes(H.G,
                           nodelist=solnset,
                           node_size=40,
                           node_color='c',
                           pos=pos)
    plt.show()


def parse_args(args):
    """Parse command line parameters

    Args:
      args ([str]): command line parameters as list of strings

    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace
    """
    parser = argparse.ArgumentParser(
        description="Multilevel Circuit Partition demonstration")
    parser.add_argument("--version",
                        action="version",
                        version="pldl {ver}".format(ver=__version__))
    parser.add_argument(dest="N",
                        help="number of modules",
                        type=int,
                        metavar="INT")
    parser.add_argument(dest="M",
                        help="number of nets",
                        type=int,
                        metavar="INT")
    parser.add_argument(dest="eta",
                        help="ratio of nets and pins",
                        type=float,
                        metavar="FLOAT")
    parser.add_argument("-v",
                        "--verbose",
                        dest="loglevel",
                        help="set loglevel to INFO",
                        action="store_const",
                        const=logging.INFO)
    parser.add_argument("-vv",
                        "--very-verbose",
                        dest="loglevel",
                        help="set loglevel to DEBUG",
                        action="store_const",
                        const=logging.DEBUG)
    parser.add_argument("-p",
                        "--plot",
                        dest="plot",
                        help="plot the result graphically",
                        action="store_const",
                        const=True)
    return parser.parse_args(args)


def setup_logging(loglevel):
    """Setup basic logging

    Args:
      loglevel (int): minimum loglevel for emitting messages
    """
    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    logging.basicConfig(level=loglevel,
                        stream=sys.stdout,
                        format=logformat,
                        datefmt="%Y-%m-%d %H:%M:%S")


def main(args):
    """Main entry point allowing external calls

    Args:
      args ([str]): command line parameter list
    """
    args = parse_args(args)
    setup_logging(args.loglevel)
    _logger.debug("Starting crazy calculations...")
    # print("The {}-th Fibonacci number is {}".format(args.n, fib(args.n)))

    if args.eta >= 1:
        _logger.error("eta value {} is too big".format(args.eta))
        return
    if args.eta > 0.3:
        _logger.warning("eta value {} may be too big".format(args.eta))

    H = create_random_graph(args.N, args.M, args.eta)
    p = dict()
    for v in H.modules:
        p[v] = randint(50, 100)
    weight = dict()
    for net in H.nets:
        weight[net] = sum(p[v] for v in H.G[net])

    solnset = set()
    depset = set()
    totalcost = min_maximal_matching(H, weight, solnset, depset)
    print("total cost = {}".format(totalcost))

    if args.plot:
        plot(H, p, solnset)
    _logger.info("Script ends here")


def run():
    """Entry point for console_scripts
    """
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
