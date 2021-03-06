| # install pyenv |                                                              |
| --------------- | ------------------------------------------------------------ |
|                 | git clone https://github.com/pyenv/pyenv.git ~/.pyenv        |
|                 | echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc         |
|                 | echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc      |
|                 | echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc |
|                 | source ~/.bashrc                                             |
|                 | pyenv install 3.6.7                                          |
|                 | pyenv global 3.6.7                                           |
|                 | pyenv rehash                                                 |
|                 |                                                              |
|                 |                                                              |
|                 | # install pyenv-virtualenv                                   |
|                 | git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv |
|                 | echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc        |
|                 | source ~/.bashrc                                             |
|                 |                                                              |
|                 |                                                              |
|                 | # etc                                                        |
|                 | python -V                                                    |
|                 | pip install -U pip                                           |
|                 | pip install flask                                            |
|                 | pip install requests                                         |
|                 | pip freeze > req.txt                                         |