import math
import argparse

def train_steps(flags):
    # Roughly until the learning rate becomes 1e-5
    decay_count = math.log(1e-5 / flags.lr, 0.1) # How many times decay has to be applied to reach 1e-5.
    return math.ceil(flags.lr_decay_steps * decay_count / flags.test_every)

def default_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-N', type=int,
            help="How many training examples to use.", default=60000)
    parser.add_argument('--name', type=str, required=True,
            help="What to call the experiment. Determines the directory where results are dumped.")
    parser.add_argument('--lr-decay-steps', type=int, default=50000,
            help="The program uses exponential learning rate decay with 0.1 decay every lr-decay-steps.")
    parser.add_argument('--test-every', type=int, default=5000,
            help="How often to evaluate the test accuracy. Unit optimization iterations.")
    parser.add_argument('--test-size', type=int, default=10000)
    parser.add_argument('--num-samples', type=int, default=10)
    parser.add_argument('--log-dir', type=str, default='results',
            help="Directory to write the results to.")
    parser.add_argument('--lr', type=float, default=0.01)
    parser.add_argument('--batch-size', type=int, default=128,
            help="Minibatch size to use in optimization.")
    parser.add_argument('--optimizer', type=str, default='Adam',
            help="Either Adam or NatGrad")

    parser.add_argument('-M', type=str, default='64',
            help="How many inducing points to use at each layer.")
    parser.add_argument('--feature-maps', type=str, default='1')
    parser.add_argument('--filter-sizes', type=str, default='5,5')
    parser.add_argument('--strides', type=str, default='1,1')
    parser.add_argument('--base-kernel', type=str, default='rbf')
    parser.add_argument('--white', action='store_true', default=False)

    parser.add_argument('--last-kernel', type=str, default='add')

    parser.add_argument('--gamma', type=float, default=1.0,
            help="Gamma parameter to start with for natgrad.")

    parser.add_argument('--load-model', action='store_true')
    return parser

