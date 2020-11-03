#! /bin/bash

# printf "Available hosts\n\n" >> scan_results.txt

for i in {1..254}
do 
    echo "Scanning: 192.168.1.${i}"
    ping -c 1 192.168.1.${i} | grep "bytes from"  | cut -d " " -f 4 | sed 's/.$//' >> scan_results.txt
done

echo "Scan complete, check 'scan_results.txt' for live hosts."
echo "Use command 'namp -iL scan_results.txt' to scan live hosts."