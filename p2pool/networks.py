from p2pool.bitcoin import networks
from p2pool.util import math

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

nets = dict(
    ecocoin=math.Object(
        PARENT=networks.nets['ecocoin'],
        SHARE_PERIOD=120, # seconds
        CHAIN_LENGTH=12*60*60//120, # shares
        REAL_CHAIN_LENGTH=12*60*60//120, # shares
        TARGET_LOOKBEHIND=30, # shares
        SPREAD=36, # blocks
        IDENTIFIER='c138e5b9e7923514'.decode('hex'),
        PREFIX='d206c3a24ee749b4'.decode('hex'),
        P2P_PORT=1341,
        MIN_TARGET=4,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=False,
        WORKER_PORT=2233,
        BOOTSTRAP_ADDRS=' '.split(' '),
        ANNOUNCE_CHANNEL='#ecocoin-pool',
        VERSION_CHECK=lambda v: True,
    ),
)
for net_name, net in nets.iteritems():
    net.NAME = net_name
