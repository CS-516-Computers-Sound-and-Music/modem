# modem
Assignment 2: Designing a demodulator for a simplified Bell 103 Modem

1. I saved the wav file using `curl https://www.po8.org/modem-messages/shaned.wav --output message.wav`

The script `modem_decoder.py` is where all of my code is located. The assignment overall was fairly simple to implement and has 4 steps:

1. Read in the file using `scipy.io.wavfile`. For a sanity check, I also confirmed that the bits per sample is 160. With standard sample rate (48kHz) and Bell 103 Model Protocol of 300 baud (300 bps), each bit is represented by 160 samples. 

2. Tone-power function: the tone power function is implemented using a simple loop following the directions in `tone_power(...)`. I also normalize the samples as specified in the directions in the `normalize_samples(...)` function. 

3. `decode(...)` calls the tone-power function on 160-sample long sub arrays of the full sample. 

4. Finally, `decode_bits` is an array compilation that goes through discrete 10-bit chunks of the bitstring returned by `decode`, reverses the middle 8 bits, converts those 8 bits by casting to binary (`int(<chunk>, 2))`), and casts to a character (`chr(<binary_chunk>)`) and returns the 8-bit long bit strings. I also confirmed, seperately, that each little-endian string starts with a 0 and ends with a 1. 

The output message is `There will be big changes for you but you will be happy.` and is saved in `MESSAGE.txt`. Unfortunately, I don't like big changes, but this is very sweet and hopeful - thanks, Bart!

## Todo:
I have not done any of the extra work, nor do I assert that my sample rate is the standard that I would expect. If I were to read in a file that does not fit the expected sample rate. While everything is extrapolated out and I never hard-code the sample rate, I haven't confirmed it will still work. 

The first step in doing some of the extras may be to just download the song and see if it works. But, if it doesn't just work out of the box, I should probably find the start of each byte of the segment rather than assuming that each byte is aligned. 