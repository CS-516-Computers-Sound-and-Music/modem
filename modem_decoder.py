from scipy.io import wavfile as wf
import matplotlib.pyplot as plt
import numpy as np

sample_rate, y = wf.read("message.wav")
bits_per_s = 300
samp_per_bit = sample_rate//bits_per_s

def tone_power(samples, f, sample_rate):
    I = 0
    Q = 0
    ac = 2*np.pi*(f/sample_rate)

    for n in range(samples.shape[0]):
        angle = ac * n
        I = I + samples[n] * np.cos(angle)
        Q = Q + samples[n] * np.sin(angle)

    return I**2 + Q**2

def normalize_samples(samples):
    return 2*(samples/np.max(samples))-1

def decode(samples, spb, sr):
    """ Convert to array of 0s and 1s in message_bits """
    message_bits = ""
    for i in range(0,samples.shape[0],spb):
        mark_resp = tone_power(samples[i:i+spb], 2225, sr)
        space_resp = tone_power(samples[i:i+spb], 2025, sr)

        message_bits += "1" if mark_resp>space_resp else "0"
    return message_bits

def decode_bits(bitstring):
    return [chr(int(message_bits[start+8:start:-1],2)) for start in range(0,len(message_bits), 10)]

y = normalize_samples(y)

message_bits = decode(y,samp_per_bit,sample_rate)

""" Convert message bits to an array of letters 
    Each valid bitstring is 10 bits long, 
        starting with a space bit (0)
        ending with a mark bit (1)
        with 8 bits of data, 8-Bit ASCII, little endian
"""
message = "".join(decode_bits(message_bits))
print(message)