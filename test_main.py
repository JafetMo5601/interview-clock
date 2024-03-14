from main import Clock


def test_default_clock():
    """
    Test default behavior of the clock.
    """
    clock = Clock(duration_hours=0.00055555556)  # Simulate a very short duration for testing
    clock.run()  # Start the clock
    assert clock.tick_message == "tick"
    assert clock.tock_message == "tock"
    assert clock.bong_message == "bong"


def test_message_update():
    """
    Test updating messages during the clock simulation.
    """
    clock = Clock(duration_hours=0.00055555556)  # Simulate a very short duration for testing
    # Simulate user input to update messages
    clock.tick_message = "new tick"
    clock.tock_message = "new tock"
    clock.bong_message = "new bong"
    clock.run()  # Start the clock
    assert clock.tick_message == "new tick"
    assert clock.tock_message == "new tock"
    assert clock.bong_message == "new bong"


def test_custom_duration():
    """
    Test the clock with a custom duration.
    """
    clock = Clock(duration_hours=0.1)  # Simulate a very short duration for testing
    clock.run()  # Start the clock
    assert not clock.running  # Check if the clock stops after the specified duration
