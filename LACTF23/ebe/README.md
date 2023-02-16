## misc/ebe

<details>
  <summary>Description</summary>
  
  > I was trying to send a flag to my friend over UDP, one character at a time, but it got corrupted! I think someone else was messing around with me and sent extra bytes, though it seems like they actually abided by RFC 3514 for once. Can you get the flag? <br> [EBE.pcap](./EBE.pcap)

</details>

Given the packet capture file we can use wireshark to analyze it

After we check the `Statistics > Protocol Hierarchy`  it just show UDP packet and that has 1 byte of each packet bytes

Now check the UDP Stream `Right Click on 1 packet > Follow > UDP Stream`, and we got this some string

```
Lpy5lUKeaVcg3XTtQVftv{Vx_wk4T7ZMKLaaydWM3AO6R8V_1gvLuT6fqeuvxb_sd8ZnqNGSMSu8T8}JDeO8wXQU1ZeJ7_pZE3gCWx}MhJMf1YWVra}SDW8_PBUhXlgYJKcTN767REmwM6wtO4Z6R7QPiV9qJ7In_1UAC45V0wNv6OW{_hDnyXV}lS4w04_m7HQcqt2ZvfcV3qFAd1iWo_LMWQOvE1NOd_HqnZf2uXF9gfEkY51DVcUDQuNduX4RP{J30}czrL8U0s9PuNgF0}0j5063aA4mLdSFm7e08j4c7gUqZb4}
```

By the challenge descripttion that gives some hint `RFC 3514`. After some googling stuff, those are known as Evil Bit - [The Security Flag in the IPv4 Header](https://www.ietf.org/rfc/rfc3514.txt)

```
The bit field is laid out as follows:

             0
            +-+
            |E|
            +-+

   Currently-assigned values are defined as follows:

   0x0  If the bit is set to 0, the packet has no evil intent.  Hosts,
        network elements, etc., SHOULD assume that the packet is
        harmless, and SHOULD NOT take any defensive measures.  (We note
        that this part of the spec is already implemented by many common
        desktop operating systems.)

   0x1  If the bit is set to 1, the packet has evil intent.  Secure
        systems SHOULD try to defend themselves against such packets.
        Insecure systems MAY chose to crash, be penetrated, etc.
```

We can assume that each packet that we have to check does not contain packet `0x01` or 1 bit, and must be 0 bit.. then we can filter packets on wireshark with the following keywords `ip.flags.rb != 1` or `ip .flags.rb == 0`

Then check every single packet that we have filtered, then assemble it to get the flag

<details>
  <summary>FLAG</summary>
  
  > `lactf{3V1L_817_3xf1l7R4710N_4_7H3_W1N_51D43c8000034d0c}`

</details>
