import subprocess
import json

def run_server():
    server_process = subprocess.Popen(['iperf3', '-s', '-1'])
    # server_process.wait()
run_server()


def run_client():  
    with open('output.json', 'w') as f:
        client_process = subprocess.Popen(['iperf3', '-c', '127.0.0.1', '-J'], stdout=f,) 
        client_process.wait()
run_client()


def test_iperf_speed():
    with open('output.json', 'r') as data_file:
        data = json.load(data_file)
    print(data['end']['streams'][0]['receiver']['bytes']/100000)
    print(data['end']['streams'][0]['receiver']['bits_per_second']/1000000)
test_iperf_speed()    

				