

def test_iperf_speed(run_test ,read_file):
    print(read_file)
    assert(read_file)[0] > 5
    assert(read_file)[1] > 40

