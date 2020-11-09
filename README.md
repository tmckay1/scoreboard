# scoreboard
This program is used to light up a message board powered by a Raspberry Pi 3.

## Assumptions
When writing this program I assumed:
- You are running Raspberry Pi OS (Raspbian) on the Raspberry Pi 3 or Raspberry Pi Zero W
- You have already setup the hardware and circuit
- You are using hardware supported by the Software Requirements below

## Software Requirements
In order to use the program you will need the following:
- Python 3 installed
- <a href="https://github.com/ManiacalLabs/BiblioPixel">BiblioPixel</a> Installed (any any dependency it requires like <a href="https://github.com/jgarff/rpi_ws281x">the rpi_ws281x driver</a>)

## Setup

- You can clone/download the project to any directory you want to keep the files.
- Run <code>sudo pip3 install -r requirements.txt</code>
- Install Bibliopixel requirement <a href="https://github.com/jgarff/rpi_ws281x">rpi_ws281x</a>
- Run <code>sudo python3 drawScoreBoard.py</code> to see the scoreboard

## How It Works
The file <code>drawScoreboard.py</code> is a sample script that executes the program. You can follow this as a template for writing you're own implementation. All animations, algorithms, character sets, and parsers can be subclassed to fit the needs of your specific setup. For example if you are using an 8x48 message board, you will need to create a character set for that. Here's the basic idea for writing a message to your board:
- Create a custom animation class inheriting the <code>BaseAnim</code> class from BiblioPixel and override the <code>step()</code> function. OR use the <code>MessageBoardAnimation</code> class provided, which does this.
- Customize the animation to accept the arguments you need.
- Create a BiblioPixel driver for the LED model strip you have
- Create the character set you will use and initialize the parser with the character set
- Create the color algorithm you will use and initialize the message algorithm with the color algorithm
- Initialize the custom animation and run
