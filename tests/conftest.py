import pytest
import subprocess


@pytest.fixture
def run_server():
    server_process = subprocess.Popen(['iperf3', '-s', '-1'])


@pytest.fixture
def run_client():
    with open('/Users/dmytrofedorchuk/glob/test_global/tests/output.json', 'w') as f:
        client_process = subprocess.Popen(['iperf3', '-c', '127.0.0.1', '-J'], stdout=f,)
    client_process.wait()
