import pywhatkit
import pandas as pd
import re

import datetime

# Get the current date and time
current_datetime = datetime.datetime.now()

# Extract the current hours and minutes
current_hour = current_datetime.hour
current_minute = current_datetime.minute

df = pd.read_excel("Paper_Presentation_as_on(06-09-2023).xlsx",
                   usecols=["Name", "Phone Number"], skiprows=13)

for index, row in df.iterrows():
    if index <= 82:
        continue
    name = row["Name"]
    ph = row["Phone Number"]
    message = f"""
Hi *{name}* 👋,

We hope this message finds you well! 🌟 We would like to express our sincere gratitude for your participation in Technovista Paper Presentation. Your enthusiasm and interest in this event have been greatly appreciated. 🚀

To enhance your experience and keep the discussions going, we have created a dedicated WhatsApp group exclusively for participants in the *Computing Domain*. Joining this group will give you the opportunity to connect with fellow participants, exchange ideas 💡, and stay updated. 📌

📌 *WhatsApp Group Link: https://chat.whatsapp.com/F3K2OslNCLIHaqC1vt12gs*

We look forward to having you onboard. 🤝

If you have any questions or need assistance with anything related to the group, please feel free to reach out to us. Let's make this group a hub of knowledge and collaboration! 🤓

Thank you once again for being a part of Technovista Paper Presentation. We can't wait to see you in the group! 🎉

Best regards,
Paper Presentation - CSE 🙌
Technovista 🌐
    """
    pywhatkit.sendwhatmsg(f"+91{ph}", message,
                          current_hour, current_minute+index % 82, 15, True)
    print(f"{index} Sent to {name} {ph}")
