<div style="display:flex; justify-content:center;">
<img src="./legwork-logo.png" alt="legwork">
</div>

## Contributing [![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/dwyl/esta/issues) 

An event driven backtesting engine written in Python3 for algorithmic trading. You will be able to write algorithms in Python, which will be able to interface with the engine seamlessly.

### Backtester Setup
Make sure you have `docker` installed.

#### Run with Docker
```bash
sh ./setup.sh
```

#### Example run configuration
```bash
python3 main.py --dir "Daily" --start-time "2016-12-15" --end-time "2018-12-17"
```

