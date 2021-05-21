# Macbook Setup 2021
- Install brew package manager  
  `$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
- Install iTerm2  
  `$ brew install --cask iterm2`
- Hammerspoon for window management, password generation  
  `$ brew install --cask hammerspoon`
  - Config
    ```lua
    -- https://github.com/peterklijn/hammerspoon-shiftit/raw/master/Spoons/ShiftIt.spoon.zip
    hs.loadSpoon("ShiftIt")
    spoon.ShiftIt:bindHotkeys({})
    -- https://github.com/Hammerspoon/Spoons/raw/master/Spoons/PasswordGenerator.spoon.zip
    hs.loadSpoon("PasswordGenerator")
    spoon.PasswordGenerator.password_style="xkcd"
    spoon.PasswordGenerator.word_count=4
    spoon.PasswordGenerator.word_leet=2
    spoon.PasswordGenerator:bindHotkeys({
      copy = { { "ctrl", "cmd", "alt" }, "p" }
    })
    hs.hotkey.bind({"cmd", "alt", "ctrl", "shift"}, "I", function()
      hs.caffeinate.set("displayIdle", true, true)
      hs.caffeinate.set("systemIdle", true, true)
      hs.caffeinate.set("system", true, true)
      hs.alert.show("Preventing Sleep")
    end)
    hs.hotkey.bind({"cmd", "alt", "ctrl", "shift"}, "O", function()
      hs.caffeinate.set("displayIdle", false, true)
      hs.caffeinate.set("systemIdle", false, true)
      hs.caffeinate.set("system", false, true)
      hs.alert.show("Allowing Sleep")
    end)
    ```
- Terminal setup
  - Install zsh with zinit and pure-prompt
    ```bash
    $ chsh -s /bin/zsh
    $ sh -c "$(curl -fsSL https://raw.githubusercontent.com/zdharma/zinit/master/doc/install.sh)"
    $ zinit self-update
    $ npm install --global pure-prompt
    $ cat >> ~/.zshrc
    ```
  - Paste the following (Ctrl-D when you've pasted to finalize the file)
    ```bash
    zinit ice compile'(pure|async).zsh' pick'async.zsh' src'pure.zsh'
    zinit light sindresorhus/pure
    zinit wait lucid for \
     atinit"ZINIT[COMPINIT_OPTS]=-C; zicompinit; zicdreplay" \
        zdharma/fast-syntax-highlighting \
     blockf \
        zsh-users/zsh-completions \
     atload"!_zsh_autosuggest_start" \
        zsh-users/zsh-autosuggestions
    HISTSIZE=1000
    HISTFILE=~/.zsh_history
    SAVEHIST=200
    setopt appendhistory
    setopt sharehistory
    setopt incappendhistory
    # Key bindings: (find the codes with `cat` and pressing key)
    # alt-right-arrow
    bindkey "^[^[[C" forward-word
    # alt-left-arrow
    bindkey "^[^[[D" backward-word 
    # delete-key
    bindkey "^[[3~" delete-char
    # home-key
    bindkey "^[[H" beginning-of-line
    # end-key
    bindkey "^[[F" end-of-line"
    ```
  - Some aliases in ~/.zprofile -- **NOTE: replace with your own ~/project path**
    ```bash
    alias flushdns='sudo dscacheutil -flushcache;sudo killall -HUP mDNSResponder;'
    alias gf='function _goldfinger(){ (cd ~/project; sh goldfinger.sh $1 $2) }; _goldfinger'
    alias pwdenv='read -sr OS_PWD && export OS_PWD'
    alias scpb='scp -i ~/.ssh/bolt_id_rsa'
    alias sshb='ssh -i ~/.ssh/bolt_id_rsa'
    alias typora='open -a typora'
    ```
  - Git aliases  
    ```bash
    $ git config --global alias.up "push -u origin HEAD"
    $ git config --global alias.graph "log --graph --abbrev-commit --decorate --format=format:'%C(bold blue)%h%C(reset) - %C(bold green)(%ar)%C(reset) %C(white)%s%C(reset) %C(dim white)- %an%C(reset)%C(bold yellow)%d%C(reset)' --all"
    ```
- Install communication apps
  - `$ brew install --cask slack zoom discord`
- Install vpn
  - `$ brew install --cask tunnelblick`
- Install development apps
  - Install XCode 12.4 (for Catalina) or latest (for Big Sur)  
    > Download at: https://developer.apple.com/xcode/download/  
    > Or install Xcode via the App Store (https://apps.apple.com/za/app/xcode/id497799835?mt=12)  
    > Once installed, run:  
    > `$ sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer`   
    > `$ sudo xcodebuild -runFirstLaunch`
  - IDE and tools  
    `$ brew install --cask visual-studio-code azure-data-studio postman`
  - Install python 3
    ```bash
    $ brew install pyenv
    $ pyenv install 3.7.3
    $ pyenv global 3.7.3
    $ echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.zshrc
    ```
  - Install java. 
    `$ brew install --cask adoptopenjdk`
  - [Install Flutter](https://flutter.dev/docs/get-started/install/macos)
  - Flutter dependencies  
    `$ brew install --cask android-studio google-chrome`  
    `$ sudo gem install cocoapods`
  - NodeJS and helpers
    ```bash
    $ brew install node
    $ npm i -g chalet mup
    $ curl https://install.meteor.com/ | sh
    $ npm install -g git-removed-branches
    ```
  - npm custom registry
    ```bash
    $ npm login --scope=@productiveme --always-auth --registry http://nexus.productive.me/repository/npm
    $ npm config set @productiveme:registry http://nexus.productive.me/repository/npm
    ```
  - Docker
    ```bash
    $ brew install docker
    $ brew install --cask docker
    ```
    Handy for documentation and mindmapping  
    `$ brew install --cask typora workflowy`
  - Browser for developers - comparing devices  
    `$ brew install --cask blisk`
