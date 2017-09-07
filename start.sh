#!/bin/sh

while getopts "u:ht" opt; do
  case $opt in
    u)
      updatetime=$OPTARG
      export updatetime
      ;;
    t)
      openthread=true
      export openthread
      ;;
    h)
      echo "Use -u and a number to choose the interval in which the timer updates, use -t to open the thread (if it exists), and use -h for help."
      exit 0
      ;;
    \?)
      echo "Invalid option: -$OPTARG. Use radiocli -h for help."
      exit 1
      ;;
    :)
      echo "Option -$OPTARG requires an argument. Use radiocli -h for help."
      exit 1
      ;;
  esac
done

python3 radio.py
