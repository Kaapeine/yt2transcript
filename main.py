from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
from punctuator import Punctuator

def getTranscript(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id)

    formatter = TextFormatter()
    text_formatted = formatter.format_transcript(transcript)

    return text_formatted

if __name__ == "__main__":
    video_id = input("Enter Video ID: ")
    text = getTranscript(video_id)
    text = text.replace("\n", " ")
    p = Punctuator('model.pcl')
    text = p.punctuate(text)
    print(text)
    filename = video_id + ".txt"
    f = open(filename, "x")
    f.write(text)
    f.close()
    print("Written to " + filename)



