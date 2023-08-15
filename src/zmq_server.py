import argparse

desc = 'A Python program that performs tasks for virtuoso.'
parser = argparse.ArgumentParser(description=desc)
parser.add_argument('port', type=int, help='socket port number.')
args = parser.parse_args()
port = args.port

# import zmq

# context = zmq.Context()
# socket = context.socket(zmq.REP)
# socket.bind(f"tcp://127.0.0.1:{port}")

# message = socket.recv_json()
# print("Received request: %s" % message)

# socket.close()
# context.term()

##########################################################

import os
import sys
from server import SkillServer
from zmqwrapper import ZMQRouter

def run_skill_server(port):
    """Run the BAG/Virtuoso server."""
    error_msg = ''
    server = None
    
    try:
        # attempt to open port and start server
        router = ZMQRouter(port=port)
        server = SkillServer(router, sys.stdout, sys.stdin, tmpdir=None)

    except Exception as ex:
        error_msg = 'bag server process error:\n%s\n' % str(ex)

    if not error_msg:
        try:
            sys.stdout.write('BAG skill server has started.  Yay!\n')
            sys.stdout.flush()
            server.run()
        except Exception as ex:
            error_msg = 'bag server process error:\n%s\n' % str(ex)

    if error_msg:
        sys.stderr.write(error_msg)
        sys.stderr.flush()

run_skill_server(port)
