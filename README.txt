4820 Project 1

Repository Link: https://github.com/sbeck4/4820Project1

Contributions
- Shannon Beck: knobs.py, video content for the vertical screen
- Wade: receive.py and partially VideoPlayer.py and knob.py. In VideoPlayer, implemented scrubVideo() and get_time(), animations and images for knobs.py, 
- Josh: VideoPlayer.py:  chooseVideo(), build(), and all other Class definitions/imports
        Knobs.py:        onKnob(), most of on_token_placed(), some of TeiKnobApp: build() function

How to Run
1. Download the files from this github
2. Find the ip address of the receiver computer
3. Assign that ip address to the "ip" variable in knobs.py
4. Run the video player (vertical screen) by typing kivy video.py into the command line 
5. Run the knobs file (horizontal screen) by typing kivy knobs.py into the command line
6. Place a tangible on the knobs on the horizontal screen to play a video on the vertical screen

Platforms
- Any computer with python and kivy

Tangibles
- Use with any three pronged tangible that creates a triangle on the screen
