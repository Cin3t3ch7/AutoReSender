from pyrogram import Client, filters

# Configuración de la aplicación
api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'
source_chat_id = 'SOURCE_CHAT_ID'  # ID del grupo de origen
target_chat_id ='TARGET_CHAT_ID'   # ID del grupo de destino

# Inicialización del cliente
app = Client("my_account", api_id=api_id, api_hash=api_hash)

@app.on_message(filters.chat(source_chat_id) & (filters.document | filters.video | filters.audio | filters.photo))
async def forward_files(client, message):
    await message.forward(target_chat_id)

if __name__ == "__main__":
    print("Bot is running...")
    app.run()
