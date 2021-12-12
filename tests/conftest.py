import pytest 
import subprocess
import socket




@pytest.fixture
def run_test():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    server_process = subprocess.Popen(['iperf3', '-s', '-1'])
    with open('output.txt', 'w') as f:
        client_process = subprocess.Popen(['iperf3', '-c', local_ip], stdout=f, text=True) 
    server_process.wait()
    client_process.wait()

@pytest.fixture()
def read_file():
    with open('output.txt', 'r', encoding='utf8') as f:
        text = f.readlines()
        transfer = int(text[16][26:29])
        bitrate = int(text[16][39:43])
    print(f' Tansferis : {transfer}')
    print(f' Bitrate : {bitrate}')
    return transfer, bitrate
    
