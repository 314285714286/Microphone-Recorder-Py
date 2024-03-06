import pyaudio
import wave

# Set up audio input
p = pyaudio.PyAudio()

stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)

# Set up wave file
wf = wave.open('output.wav', 'wb')
wf.setnchannels(1)
wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
wf.setframerate(44100)

# Record audio
print("Recording...")

while True:
    data = stream.read(1024)
    wf.writeframes(data)

# Stop recording and clean up
print("Finished recording.")

stream.stop_stream()
stream.close()

p.terminate()

wf.close()