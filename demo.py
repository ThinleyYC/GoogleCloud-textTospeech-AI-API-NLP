import os
from google.cloud import texttospeech
from google.cloud import texttospeech_v1

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'demoServiceAccount.json'

client = texttospeech_v1.TextToSpeechClient()

text = 'Every action in Google Cloud requires certain permissions. When someone tries to perform an action in Google Cloud—for example, create a VM instance or view a dataset—IAM first checks to see if they have the required permissions. If they do, then IAM prevents them from performing the action.'

synthesis_input = texttospeech_v1.SynthesisInput(text=text)

"""
method #1
"""
voice1 = texttospeech_v1.VoiceSelectionParams(
        language_code='en-in', 
        ssml_gender=texttospeech_v1.SsmlVoiceGender.MALE
)

 
"""
method #2
"""

voice2 =  texttospeech_v1.VoiceSelectionParams(
    name = 'vi-VN-Wavenet-D',
    language_code= 'vi-VN'
)

"""
Output file config
"""
audio_config = texttospeech_v1.AudioConfig(
    audio_encoding= texttospeech_v1.AudioEncoding.MP3
)

response1 = client.synthesize_speech(
    input=synthesis_input,
    voice=voice1,
    audio_config=audio_config

)
response2= client.synthesize_speech(
    input=synthesis_input,
    voice=voice2,
    audio_config=audio_config
)

with open ('audio file1.mp3', 'wb') as output1:
    output1.write(response1.audio_content)   

with open ('audio file2.mp3', 'wb') as output1:
    output1.write(response2.audio_content) 