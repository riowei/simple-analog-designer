import argparse

desc = 'A Python program that performs tasks for virtuoso.'
parser = argparse.ArgumentParser(description=desc)
parser.add_argument('port', type=int, help='socket port number.')
parser.add_argument('message', type=str, help='send cmd.')
args = parser.parse_args()
port = args.port
message = args.message

# import zmq
# import json

# context = zmq.Context()
# socket = context.socket(zmq.REQ)
# socket.connect(f"tcp://127.0.0.1:{port}")

# sentMessage = {
#     "Name": "Ibrahim",
#     "Age": 27,
#     "Country": "Lebanon"
# }

# sentMessageJson = json.dumps(sentMessage)    
# socket.send_json(sentMessageJson)

# socket.close()
# context.term()

###############################################

from zmqwrapper import ZMQDealer

dealer = ZMQDealer(port=port)

def eval_skill(expr, input_files=None, out_file=None):
        request = dict(
            type='skill',
            expr=expr,
            input_files=input_files,
            out_file=out_file,
        )
        dealer.send_obj(request)
        reply = dealer.recv_obj()
        return reply

for i in range(10):
    print(eval_skill(message))


