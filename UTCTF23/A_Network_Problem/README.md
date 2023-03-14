## A Network Problem - Part 1

<details>
  <summary>Description</summary>
  
  > There are some interesting ports open on betta.utctf.live, particularly port 8080. <br>
  > By Robert Hill (@Rob H on discord) <br>
  > `betta.utctf.live:8080`
  
</details>

We can establish a network connection by using netcat then sending data through that connection. In this context, the command will establish a connection to the host `betta.utctf.live` on port `8080`, which is a server or service that can receive connections to perform certain network interactions.

```
$ nc betta.utctf.live 8080
Hi Wade! I am using socat to broadcast this message. Pretty nifty right? --jwalker utflag{meh-netcats-cooler}
```

After the connection is successfully established, we will receive response data from the host in the form of text and also a flag.

<details>
  <summary>Flag</summary>
  
  > `utflag{meh-netcats-cooler}`
  
</details>

<br>

## A Network Problem - Part 2

<details>
  <summary>Description</summary>
  
  > betta.utctf.live has other interesting ports. Lets look at 445 this time. <br>
  > By Robert Hill (@Rob H on discord) <br>
  > `betta.utctf.live:445`
  
</details>

We can use the command `enum4linux -a betta.utctf.live` to run the enum4linux program in the terminal and perform enumeration on the host betta.utctf.live.

`enum4linux` is a tool used to examine Windows and Samba systems in order to search for information about users, user lists, group information, security policy information, and information about running services. In this context, the command will attempt to perform enumeration on the `betta.utctf.live` host with the `-a` option that allows searching for more detailed information, such as searching for Samba shares, user information, and other information.

In general, the enum4linux program is used to scan and gather information on systems connected to a network in order to evaluate the security of those systems, including searching for potential vulnerabilities and security holes that attackers can exploit.

```bash
$ enum4linux -a betta.utctf.live
===============================( Share Enumeration on betta.utctf.live )===============================
        Sharename       Type      Comment
        ---------       ----      -------
        WorkShares      Disk      Sharing of work files
        BackUps         Disk      File Backups.
        IPC$            IPC       IPC Service (Samba Server)
SMB1 disabled -- no workgroup available

[+] Attempting to map shares on betta.utctf.live

//betta.utctf.live/WorkShares   Mapping: OK Listing: OK Writing: N/A
//betta.utctf.live/BackUps      Mapping: DENIED Listing: N/A Writing: N/A

[E] Can't understand response:

NT_STATUS_CONNECTION_REFUSED listing \*
//betta.utctf.live/IPC$ Mapping: N/A Listing: N/A Writing: N/A
```

We have discovered SMB share `WorkShares`. It will useful for us to find more files we can work with.

Let’s enumerate SMB using `smbclient` tool. Upon password prompt hit Enter and we will be logged in `WorkShares` smb share.

```bash
$ smbclient //betta.utctf.live/WorkShares
Password for [WORKGROUP\nopedawn]:
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Thu Mar  9 02:45:05 2023
  ..                                  D        0  Thu Mar  9 02:45:05 2023
  shares                              D        0  Thu Mar  9 02:45:05 2023

                9974088 blocks of size 1024. 6101912 blocks available
smb: \> cd shares\
smb: \shares\> ls
  .                                   D        0  Thu Mar  9 02:45:05 2023
  ..                                  D        0  Thu Mar  9 02:45:05 2023
  Advertising                         D        0  Thu Mar  9 02:45:05 2023
  OfficeFun                           D        0  Thu Mar  9 02:45:05 2023
  IT                                  D        0  Thu Mar  9 02:45:05 2023

                9974088 blocks of size 1024. 6101884 blocks available
smb: \shares\> cd IT\
smb: \shares\IT\> ls
  .                                   D        0  Thu Mar  9 02:45:05 2023
  ..                                  D        0  Thu Mar  9 02:45:05 2023
  Itstuff                             D        0  Thu Mar  9 02:45:05 2023

                9974088 blocks of size 1024. 6101660 blocks available
smb: \shares\IT\> cd Itstuff\
smb: \shares\IT\Itstuff\> ls
  .                                   D        0  Thu Mar  9 02:45:05 2023
  ..                                  D        0  Thu Mar  9 02:45:05 2023
  notetoIT                            N      380  Thu Mar  9 02:45:05 2023

                9974088 blocks of size 1024. 6101632 blocks available
smb: \shares\IT\Itstuff\>more notetoIT
I don't understand the fasination with the magic phrase "abracadabra", but too many people are using them as passwords. Crystal Ball, Wade Coldwater, Jay Walker, and Holly Wood all basically have the same password. Can you please reach out to them and get them to change thier passwords or at least get them append a special character?

-- Arty F.

utflag{out-of-c0ntrol-access}
 ```
 
 <details>
  <summary>Flag</summary>
  
  > `utflag{out-of-c0ntrol-access}`
  
</details>
