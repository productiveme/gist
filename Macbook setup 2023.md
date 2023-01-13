# Macbook Setup 2023
- Install brew package manager  
    `$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
- Install iTerm2  
    `$ brew install --cask iterm2`
- Raycast for window management, password generation  
    `$ brew install --cask raycast`
- NodeJS and helpers
    ```bash
    $ brew install nvm
    $ nvm install node
    ```
- Password generator extension for raycast
    ```
    git clone git@github.com:productiveme/raycast-ext-passphrase-generator.git passphrase
    cd passphrase
    npm i && npm run dev
    ```

- Terminal setup 
  - Install zsh with zinit 
    ```bash
    $ sh -c "$(curl -fsSL https://raw.githubusercontent.com/zdharma/zinit/master/doc/install.sh)"
    $ zinit self-update

    $ cat >> ~/.zshrc
    ```
  - Paste the following (Ctrl-D when you've pasted to finalize the file)
    ```bash
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
    alias pwdenv='read -sr OS_PWD && export OS_PWD'
    alias rosetta='function _rosetta(){ arch -x86_64 $@ }; _rosetta'
    alias jsonc='function _jsonc(){ (for i in $@; do :; done; code $i && jsoncalc $@) }; _jsonc'
    ```
  - Git aliases  
    ```bash
    $ git config --global alias.up "push -u origin HEAD"
    $ git config --global alias.graph "log --graph --abbrev-commit --decorate --format=format:'%C(bold blue)%h%C(reset) - %C(bold green)(%ar)%C(reset) %C(white)%s%C(reset) %C(dim white)- %an%C(reset)%C(bold yellow)%d%C(reset)' --all"
    ```
- Install some npm global tools
    ```bash
    $ npm i -g git-removed-branches jsoncalc meteor
    ```
- Install communication apps
  - `$ brew install --cask slack`
- Install development apps
  - Install XCode  
    > Download at: https://developer.apple.com/xcode/download/  
    > Or install Xcode via the App Store (https://apps.apple.com/za/app/xcode/id497799835?mt=12)  
    > Once installed, run:  
    > `$ sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer`   
    > `$ sudo xcodebuild -runFirstLaunch`
  - IDE and tools  
    `$ brew install --cask visual-studio-code azure-data-studio`
  - Install python 3
    ```bash
    $ brew install pyenv
    $ pyenv install 3.7.3
    $ pyenv global 3.7.3
    $ echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.zshrc
    ```
  - Install java. 
    `$ brew install --cask temurin8`
  - [Install Flutter](https://flutter.dev/docs/get-started/install/macos)
  - Flutter dependencies  
    `$ brew install --cask android-studio google-chrome`  
    `$ sudo gem install cocoapods`
    
  - npm custom registry
    ```bash
    $ npm login --scope=@productiveme --always-auth --registry http://nexus.productive.me/repository/npm
    $ npm config set @productiveme:registry http://nexus.productive.me/repository/npm
    ```
  - Docker
    ```bash
    $ brew install --cask docker
    ```
  - Handy tools for 
      - documentation 
        `$ brew install --cask workflowy licecap`
      - security
        `$ brew install --cask bitwarden`
        `$ brew install wireguard-tools` or install from [App Store](https://itunes.apple.com/us/app/wireguard/id1451685025?ls=1&mt=12)
      - design
        `$ brew install --cask inkscape gimp`

