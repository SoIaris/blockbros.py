# Blockbro-py

BlockBros-py makes it easier to interact with blockbros api
## Installation

```bash
pip install blockbros-py
```

# Usage
```
import blockbros

# Auth
login = blockbros.Auth.login(0000000000000000, "3a69a5643165d9be14ae63384df66c8d9e6a2046$sha1$btdFtx45MUf3mqPtfCCskU")
alt_login = blockbros.Auth.alt_login(000000, "CNptMSwG")

# Gamer
gamer = blockbros.Gamer(0000000000000000, "3AqQMSTEkdAmqq4F8eh5bkQeAs7qAHmx")

# search
searchGamer = gamer.search("DAIGO")

# follow /  unfollow
gamer.followGamer(0000000000000000)
gamer.unfollowGamer(0000000000000000)

# block / unblock
gamer.blockGamer(0000000000000000)
gamer.unblockGamer(0000000000000000)

# channel
gamer.setChannelUrl("/@MrBeast")
```

# links
- [github repository](https://github.com/SoIaris/blockbros.py)

## License

[MIT](https://choosealicense.com/licenses/mit/)

