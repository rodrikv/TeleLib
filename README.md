# TeleLib

A Telegram Wrapper.

## NodeJS

install NodeJS version Via `npm` or `yarn`

```bash
yarn add @telelib/telelib
# or
npm i --save @telelib/telelib
```

create a .js or a .ts file
install the package using npm or yarn

import the package:

```typescript
import {
    Bot,
    types, // since it's typescript, import Types as well
} from '@telelib/telelib'

// create an instance:
const TelegramBot = new Bot({
 telegram: {
  token: '[TOKEN]',
 },
 debug: true // provide to enable debug mode.
})

// create a listener on 'Message' Type:
TelegramBot.client.on(
 'message',
 (msg: types.Message) => {
  if (msg.text) {
   return msg.reply(`your message was:\n${msg.text}`)
  }
  msg.reply('i only understand text messages')
 }
)

// then start the loop to fetch updates from telegram.
TelegramBot.start()
```

- replace `[TOKEN]` with your telegram bot token


## Python

being worked on ...

## more info

- for more examples visit [examples](/examples)
- for better and more detailed documentation visit [docs](/docs)

## issues / bugs / suggestions ?

there's no template for now, just open an issue or fix it and do a Pull request, your name will be here as a contributor. :)

## contributors

- [ReloadLife](https://github.com/reloadlife) - Maintainer

## todo list

- [ ] Write Full Documentation
- [ ] add Helper methods
- [ ] Add More examples
- [ ] Write Interfaces for all Message types, classes, methods.
- [ ] Add Support for Webhooks
- [ ] Implement TelegramPassport related methods
- [ ] Add MTProto and TDLib Wrapper.
- [ ] Clean up and optimize the code.

## Supported Languages

- [x] TypeScript
- [ ] Python
- [ ] PHP
- [ ] Lua
- [ ] Ruby
- [ ] Go
- [ ] Perl
- [ ] Julia
