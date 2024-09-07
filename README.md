# Chat Integration System

This repository provides a basic setup for sending and optionally receiving messages from a discord channel using webhooks and a discord bot.

## How to Use

1. **Send Messages:**
   - Make a POST request to `http://localhost:5000/send` with a JSON payload:
   
     ```json
     {
         "message": "Hello, Discord!"
     }
     ```

2. **Receive Messages (Optional):**
   - To receive messages from a Discord channel run the Discord bot script Make sure you have configured the bot token and channel ID correctly in the script.

## Notes

- Make sure you have your discord webhook url and bot token configured in the scripts

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
