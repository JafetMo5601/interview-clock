# Clock Application

The Clock Application simulates a clock with customizable messages for different time intervals. It allows users to specify the duration of the clock and customize messages for each second, minute, and hour.

## Features

- Displays messages for each second, minute, and hour.
- Allows users to customize messages interactively.
- Stops running after the specified duration.

## Requirements

- Python 3.x
- No additional Python packages required

## Usage

1. Clone the repository:
git clone https://github.com/JafetMo5601/interview-clock.git


2. Navigate to the project directory:
cd interview-clock

3. Run the application:
python main.py

4. Follow the on-screen instructions to customize messages if desired.

## Configuration

The following configuration options are available:

- `duration_hours`: Duration of the clock in hours (default is 3 hours).
- `tick_message`: Message for each second (default is "tick").
- `tock_message`: Message for each minute (default is "tock").
- `bong_message`: Message for each hour (default is "bong").

You can adjust these options directly in the `main.py` file or provide them as arguments when creating an instance of the `Clock` class.

## Testing
To run tests, execute the following command:
python test_clock.py


## Contributing
Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a pull request
