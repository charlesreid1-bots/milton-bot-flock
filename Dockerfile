FROM rainbowmindmachine/rainbowmindmachine:v23
MAINTAINER charles@charlesreid1.com

RUN git clone https://git.charlesreid1.com/bots/b-milton.git /milton
WORKDIR "/milton/bot"
CMD ["/usr/bin/env","python","MiltonBotFlock.py"]

