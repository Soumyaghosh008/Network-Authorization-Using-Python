#!/usr/bin/env python
from scapy.all import ARP, Ether, srp
from python_telegram_bot import TelegramBot

def get_connected_devices(ip_range):
    arp_request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip_range)
    result = srp(arp_request, timeout=3, verbose=0)[0]
    return [({"ip": packet[1].psrc, "mac": packet[1].hwsrc}) for packet in result]

def send_telegram_message(bot_token, chat_id, message):
    bot = TelegramBot(bot_token)
    bot.send_message(chat_id, message)

def main():
    # Configure your network details
    your_wifi_ip_range = "192.168.1.1/24"  # Adjust this to match your network's IP range
    telegram_bot_token = "YOUR_TELEGRAM_BOT_TOKEN"
    telegram_chat_id = "YOUR_TELEGRAM_CHAT_ID"

    connected_devices = get_connected_devices(your_wifi_ip_range)

    if connected_devices:
        message = "New device connected to your WiFi:\n"
        for device in connected_devices:
            message += f"IP: {device['ip']}, MAC: {device['mac']}\n"

        send_telegram_message(telegram_bot_token, telegram_chat_id, message)

if __name__ == "__main__":
    main()