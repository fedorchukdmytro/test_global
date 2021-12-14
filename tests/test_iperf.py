import json


def test_iperf_speed(run_server, run_client):
    with open('output.json', 'r') as data_file:
        data = json.load(data_file)
    assert (data['end']['streams'][0]['receiver']['bytes'] / 1000000) > 40
    assert (data['end']['streams'][0]['receiver']['bits_per_second'] / 1000000) > 5
