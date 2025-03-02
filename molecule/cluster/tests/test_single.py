def test_service_is_running(host):
    service = host.service("consul")
    assert service.is_running
    assert service.is_enabled

def test_port_is_listning(host):
    socket1 = host.socket('tcp://0.0.0.0:8500')
    socket2 = host.socket('tcp://0.0.0.0:8501')
    assert socket1.is_listening
    assert socket2.is_listening
