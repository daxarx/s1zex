#!/bin/bash
print_center(){
    local x
    local y
    text="$*"
    x=$(( ($(tput cols) - ${#text}) / 2))
    echo -ne "\E[6n";read -sdR y; y=$(echo -ne "${y#*[}" | cut -d';' -f1)
    echo -ne "\033[${y};${x}f$*"
}

run_in_bg() {
    eval "$@" &>/dev/null & disown;
}

echo -e "\033[0;96mInstalling Adaptator... Just a Moment...\033[0m"

eval "cd ~/ &&
rm -rf Adaptator &&
git clone --branch Dev https://github.com/s1zexxx/Adaptator &&
cd Adaptator &&
pip install -U pip &&
pip install -r requirements.txt &&
echo '' > ~/../usr/etc/motd &&
echo 'clear && . <(wget -qO- https://github.com/s1zexxx/Adaptator/raw/main/assets/banner.sh) && cd ~/Adaptator && python3 -m s1zex --port 1242' > ~/.bash_profile"

echo -e "\033[0;96mStarting Adaptator...\033[0m"

run_in_bg "python3 -m s1zex --port 1242"
sleep 10

echo -ne "\\033[2J\033[3;1f"
print_center "
\033[95m| Adaptator Adaptator Adaptator Adaptator|033[0m
\033[95m| Adaptator Adaptator Adaptator Adaptator|033[0m
\033[95m| Adaptator Adaptator Adaptator Adaptator|033[0m
\033[95m| Adaptator Adaptator Adaptator Adaptator|033[0m
\033[95m| Adaptator Adaptator Adaptator Adaptator|033[0m

\033[95mAdaptator loaded successfully!\033[0m
\033[95mWeb url: http://localhost:1242\033[0m
"

eval "termux-open-url http://localhost:1242"


