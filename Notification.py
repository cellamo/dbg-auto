from pushbullet import Pushbullet

pb = Pushbullet('o.60Jhc5XyskyW0vb1AKS7a4jz7wFTMkz5')  # Replace with your access token

# Function to send notification
def send_notification(title, body):
    pb.push_note(title, body)