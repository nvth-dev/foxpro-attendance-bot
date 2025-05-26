import discord
import requests
from data import *
from fox_request import *

# difine client
client = discord.Client(intents=discord.Intents.default())


init_db()  # Initialize the database if not already done

# logger
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

# Create a command to send an HTTP request
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('!h'):
        await message.channel.send("!c to checkin?\n!exit to checkout?\n!otp to send OTP to your email.\n!v <otp_code> to verify OTP.")

    if str(message.author.id) == get_your_discord_id():  # Replace with your Discord ID

        # Check if the message starts with '!c' to execute the command   
        if message.content.startswith('!c'):
            response_message = execute_command_in()
            await message.channel.send("checking in...")
            await message.channel.send(response_message)   

        # Check if the message starts with '!exit' to execute the command
        if message.content.startswith('!exit'):
            response_message = execute_command_out()
            await message.channel.send("checking out...")
            await message.channel.send(response_message)

        # Create a command to send an email
        if message.content.startswith('!otp'):
            sent_email()
            message.channel.send("OTP has been sent to your email. Please check your inbox.")
            await message.channel.send("Please enter the OTP code using !v <otp_code> command.")

        if message.content.startswith('!v'):
            otp = message.content[2:]  # get the OTP from the message content
            response_message = verify_otp(otp)
            await message.channel.send("Verifying OTP...")
            if response_message == True:
                await message.channel.send("OTP verified successfully!")
            #await message.channel.send(response_message)

    else: # If the user is not authorized, send a message
        await message.channel.send("You are not authorized to use this command.")
  

# Run the bot on Discord
client.run(get_bot_token())