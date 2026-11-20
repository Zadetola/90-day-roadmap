#!/bin/bash
echo "== Who and where =="
whoami
hostname
date
echo "== Disk =="
df -h
echo "== Lines in ps aux (includes header) =="
ps aux | wc -l
echo "== Network =="
hostname -I
echo "== OS =="
grep PRETTY_NAME /etc/os-release
echo "== Users =="
who
echo "== Connections =="
ss -tuln
