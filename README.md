# Play Music (actual notes) through a Piezo Buzzer (Speaker) -- PWM

This script let's you play the Tetris Theme A through a Buzzer (Piezo) style speaker.
Feel free to add more songs, a description on how to is in the commentary.

Make sure to select the correct GPIO Pin, I've used #12, since it's one of the two Hardware PWM's pf the RPi 3.
Every other Pin will work aswell, but it'll be software emulated and may result in inaccurate results and high CPU load.

### Notes

You'll find the frequencies on this page `https://pages.mtu.edu/~suits/notefreqs.html`
