import json

from aiogram import types, F
from aiogram.types import FSInputFile, InputMediaPhoto
from loguru import logger

from keyboards.user_keyboards import selection_goods_keyboard
from system.dispatcher import bot
from system.dispatcher import dp
from system.dispatcher import router


def load_bot_info_services_and_prices():
    with open("messages/goods_redemption_service_messages.json", 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data


@router.callback_query(F.data == "warranty_service")
async def goods_redemption_service_handlers(callback_query: types.CallbackQuery):
    logger.debug(callback_query)
    logger.debug(callback_query.message.message_id)
    main_menu_key = selection_goods_keyboard()

    data = load_bot_info_services_and_prices()
    document = FSInputFile('messages/image/4.png')
    media = InputMediaPhoto(media=document, caption=data)

    await bot.edit_message_media(media=media,
                                 chat_id=callback_query.message.chat.id,
                                 message_id=callback_query.message.message_id,
                                 reply_markup=main_menu_key
                                 )


def goods_redemption_service_handlers_register_message_handler():
    """Регистрируем handlers для бота"""
    dp.message.register(goods_redemption_service_handlers)