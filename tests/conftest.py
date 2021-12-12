import pytest 
import subprocess


@pytest.fixture
def run_test():
    server_process = subprocess.Popen(['iperf3', '-s', '-1'])
    with open('output.txt', 'w') as f:
        client_process = subprocess.Popen(['iperf3', '-c', '192.168.0.12'], stdout=f, text=True) 
    server_process.wait()
    client_process.wait()

@pytest.fixture(autouse=True)
def read_file():
    with open('output.txt', 'r', encoding='utf8') as f:
        text = f.readlines()
        transfer = int(text[16][26:29])
        bitrate = int(text[16][39:43])
    print(f' Tansferis : {transfer}')
    print(f' Bitrate : {bitrate}')
    return transfer, bitrate
    
