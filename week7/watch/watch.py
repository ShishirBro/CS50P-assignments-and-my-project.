import re
def main():
    a= input("HTML: ")
    b=parse(a)
    print(b)
def parse(s):
    match =re.search(r'<iframe[^>]*src="https?://(?:www\.)?youtube\.com/embed/([^"]+)"[^>]*>',s)
    if match:
        video_id = match.group(1)
        youtube_url = f"https://youtu.be/{video_id}"
        return youtube_url
    else:
        return None
if __name__ == "__main__":
    main()
