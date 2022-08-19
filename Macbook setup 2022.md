# Macbook Setup 2022

- Install brew package manager  
  `$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
- Install iTerm2  
  `$ brew install --cask iterm2`
- Raycast for window management, password generation  
  `$ brew install --cask raycast`
  - Password generator extension
    ```
    git clone git@github.com:productiveme/raycast-ext-passphrase-generator.git passphrase
    cd passphrase
    npm i && npm run dev
    ```
- Install node
  ```bash
  $ brew install nvm # follow instructions at the bottom of the output
  $ nvm install node
  ```    

- Terminal setup 
  - Install zsh with zinit and pure-prompt (requires node, see later on)
    ```bash
    $ chsh -s /bin/zsh
    $ bash -c "$(curl --fail --show-error --silent --location https://raw.githubusercontent.com/zdharma-continuum/zinit/HEAD/scripts/install.sh)" # then reload the shell
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
  - Some aliases in ~/.zprofile
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
- Install communication apps
  - `$ brew install --cask slack zoom`
- Install vpn
  - `$ brew install --cask tunnelblick`
- Install development apps
  - Install XCode  
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
    $ pyenv install 3.9.9
    $ pyenv global 3.9.9
    $ echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.zshrc
    ```
    
  - Install java. 
    `$ brew install --cask adoptopenjdk`
    
  - [Install Flutter](https://flutter.dev/docs/get-started/install/macos)
  ```bash
  brew install --cask flutter
  ```
 
  - Flutter dependencies  
    `$ brew install --cask android-studio google-chrome`  
    `$ sudo gem install cocoapods`
    
  - NodeJS helpers
    ```bash
    $ npm i -g chalet mup git-removed-branches jsoncalc
    $ curl https://install.meteor.com/ | sh
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
    
  - Handy tools for 
      - documentation 
        `$ brew install --cask workflowy licecap xmind`
      - security
        `$ brew install --cask bitwarden tunnelblick`
      - design
        `$ brew install --cask inkscape gimp`


