from typing import List

from telelib.bot import DefaultType

from telelib.bot import DefaultMethod


class Integer(int):
    ...


class String(str):
    ...


class Float(float):
    ...


Boolean = bool


class Update(DefaultType):

    @property
    def update_id(
        self
    ) -> "Integer":
        return self._d["update_id"]

    @property
    def message(
        self
    ) -> "Message" | "None":
        return self._d["message"]

    @property
    def edited_message(
        self
    ) -> "Message" | "None":
        return self._d["edited_message"]

    @property
    def channel_post(
        self
    ) -> "Message" | "None":
        return self._d["channel_post"]

    @property
    def edited_channel_post(
        self
    ) -> "Message" | "None":
        return self._d["edited_channel_post"]

    @property
    def inline_query(
        self
    ) -> "InlineQuery" | "None":
        return self._d["inline_query"]

    @property
    def chosen_inline_result(
        self
    ) -> "ChosenInlineResult" | "None":
        return self._d["chosen_inline_result"]

    @property
    def callback_query(
        self
    ) -> "CallbackQuery" | "None":
        return self._d["callback_query"]

    @property
    def shipping_query(
        self
    ) -> "ShippingQuery" | "None":
        return self._d["shipping_query"]

    @property
    def pre_checkout_query(
        self
    ) -> "PreCheckoutQuery" | "None":
        return self._d["pre_checkout_query"]

    @property
    def poll(
        self
    ) -> "Poll" | "None":
        return self._d["poll"]

    @property
    def poll_answer(
        self
    ) -> "PollAnswer" | "None":
        return self._d["poll_answer"]

    @property
    def my_chat_member(
        self
    ) -> "ChatMemberUpdated" | "None":
        return self._d["my_chat_member"]

    @property
    def chat_member(
        self
    ) -> "ChatMemberUpdated" | "None":
        return self._d["chat_member"]

    @property
    def chat_join_request(
        self
    ) -> "ChatJoinRequest" | "None":
        return self._d["chat_join_request"]


class WebhookInfo(DefaultType):

    @property
    def url(
        self
    ) -> "String":
        return self._d["url"]

    @property
    def has_custom_certificate(
        self
    ) -> "Boolean":
        return self._d["has_custom_certificate"]

    @property
    def pending_update_count(
        self
    ) -> "Integer":
        return self._d["pending_update_count"]

    @property
    def ip_address(
        self
    ) -> "String" | "None":
        return self._d["ip_address"]

    @property
    def last_error_date(
        self
    ) -> "Integer" | "None":
        return self._d["last_error_date"]

    @property
    def last_error_message(
        self
    ) -> "String" | "None":
        return self._d["last_error_message"]

    @property
    def last_synchronization_error_date(
        self
    ) -> "Integer" | "None":
        return self._d["last_synchronization_error_date"]

    @property
    def max_connections(
        self
    ) -> "Integer" | "None":
        return self._d["max_connections"]

    @property
    def allowed_updates(
        self
    ) -> "List[String]" | "None":
        return self._d["allowed_updates"]


class User(DefaultType):

    @property
    def id(
        self
    ) -> "Integer":
        return self._d["id"]

    @property
    def is_bot(
        self
    ) -> "Boolean":
        return self._d["is_bot"]

    @property
    def first_name(
        self
    ) -> "String":
        return self._d["first_name"]

    @property
    def last_name(
        self
    ) -> "String" | "None":
        return self._d["last_name"]

    @property
    def username(
        self
    ) -> "String" | "None":
        return self._d["username"]

    @property
    def language_code(
        self
    ) -> "String" | "None":
        return self._d["language_code"]

    @property
    def is_premium(
        self
    ) -> "Boolean" | "None":
        return self._d["is_premium"]

    @property
    def added_to_attachment_menu(
        self
    ) -> "Boolean" | "None":
        return self._d["added_to_attachment_menu"]

    @property
    def can_join_groups(
        self
    ) -> "Boolean" | "None":
        return self._d["can_join_groups"]

    @property
    def can_read_all_group_messages(
        self
    ) -> "Boolean" | "None":
        return self._d["can_read_all_group_messages"]

    @property
    def supports_inline_queries(
        self
    ) -> "Boolean" | "None":
        return self._d["supports_inline_queries"]


class Chat(DefaultType):

    @property
    def id(
        self
    ) -> "Integer":
        return self._d["id"]

    @property
    def type(
        self
    ) -> "String":
        return self._d["type"]

    @property
    def title(
        self
    ) -> "String" | "None":
        return self._d["title"]

    @property
    def username(
        self
    ) -> "String" | "None":
        return self._d["username"]

    @property
    def first_name(
        self
    ) -> "String" | "None":
        return self._d["first_name"]

    @property
    def last_name(
        self
    ) -> "String" | "None":
        return self._d["last_name"]

    @property
    def photo(
        self
    ) -> "ChatPhoto" | "None":
        return self._d["photo"]

    @property
    def bio(
        self
    ) -> "String" | "None":
        return self._d["bio"]

    @property
    def has_private_forwards(
        self
    ) -> "Boolean" | "None":
        return self._d["has_private_forwards"]

    @property
    def join_to_send_messages(
        self
    ) -> "Boolean" | "None":
        return self._d["join_to_send_messages"]

    @property
    def join_by_request(
        self
    ) -> "Boolean" | "None":
        return self._d["join_by_request"]

    @property
    def description(
        self
    ) -> "String" | "None":
        return self._d["description"]

    @property
    def invite_link(
        self
    ) -> "String" | "None":
        return self._d["invite_link"]

    @property
    def pinned_message(
        self
    ) -> "Message" | "None":
        return self._d["pinned_message"]

    @property
    def permissions(
        self
    ) -> "ChatPermissions" | "None":
        return self._d["permissions"]

    @property
    def slow_mode_delay(
        self
    ) -> "Integer" | "None":
        return self._d["slow_mode_delay"]

    @property
    def message_auto_delete_time(
        self
    ) -> "Integer" | "None":
        return self._d["message_auto_delete_time"]

    @property
    def has_protected_content(
        self
    ) -> "Boolean" | "None":
        return self._d["has_protected_content"]

    @property
    def sticker_set_name(
        self
    ) -> "String" | "None":
        return self._d["sticker_set_name"]

    @property
    def can_set_sticker_set(
        self
    ) -> "Boolean" | "None":
        return self._d["can_set_sticker_set"]

    @property
    def linked_chat_id(
        self
    ) -> "Integer" | "None":
        return self._d["linked_chat_id"]

    @property
    def location(
        self
    ) -> "ChatLocation" | "None":
        return self._d["location"]


class Message(DefaultType):

    @property
    def message_id(
        self
    ) -> "Integer":
        return self._d["message_id"]

    @property
    def from_(
        self
    ) -> "User" | "None":
        return self._d["from"]

    @property
    def sender_chat(
        self
    ) -> "Chat" | "None":
        return self._d["sender_chat"]

    @property
    def date(
        self
    ) -> "Integer":
        return self._d["date"]

    @property
    def chat(
        self
    ) -> "Chat":
        return self._d["chat"]

    @property
    def forward_from_(
        self
    ) -> "User" | "None":
        return self._d["forward_from"]

    @property
    def forward_from__chat(
        self
    ) -> "Chat" | "None":
        return self._d["forward_from_chat"]

    @property
    def forward_from__message_id(
        self
    ) -> "Integer" | "None":
        return self._d["forward_from_message_id"]

    @property
    def forward_signature(
        self
    ) -> "String" | "None":
        return self._d["forward_signature"]

    @property
    def forward_sender_name(
        self
    ) -> "String" | "None":
        return self._d["forward_sender_name"]

    @property
    def forward_date(
        self
    ) -> "Integer" | "None":
        return self._d["forward_date"]

    @property
    def is_automatic_forward(
        self
    ) -> "Boolean" | "None":
        return self._d["is_automatic_forward"]

    @property
    def reply_to_message(
        self
    ) -> "Message" | "None":
        return self._d["reply_to_message"]

    @property
    def via_bot(
        self
    ) -> "User" | "None":
        return self._d["via_bot"]

    @property
    def edit_date(
        self
    ) -> "Integer" | "None":
        return self._d["edit_date"]

    @property
    def has_protected_content(
        self
    ) -> "Boolean" | "None":
        return self._d["has_protected_content"]

    @property
    def media_group_id(
        self
    ) -> "String" | "None":
        return self._d["media_group_id"]

    @property
    def author_signature(
        self
    ) -> "String" | "None":
        return self._d["author_signature"]

    @property
    def text(
        self
    ) -> "String" | "None":
        return self._d["text"]

    @property
    def entities(
        self
    ) -> "List[MessageEntity]" | "None":
        return self._d["entities"]

    @property
    def animation(
        self
    ) -> "Animation" | "None":
        return self._d["animation"]

    @property
    def audio(
        self
    ) -> "Audio" | "None":
        return self._d["audio"]

    @property
    def document(
        self
    ) -> "Document" | "None":
        return self._d["document"]

    @property
    def photo(
        self
    ) -> "List[PhotoSize]" | "None":
        return self._d["photo"]

    @property
    def sticker(
        self
    ) -> "Sticker" | "None":
        return self._d["sticker"]

    @property
    def video(
        self
    ) -> "Video" | "None":
        return self._d["video"]

    @property
    def video_note(
        self
    ) -> "VideoNote" | "None":
        return self._d["video_note"]

    @property
    def voice(
        self
    ) -> "Voice" | "None":
        return self._d["voice"]

    @property
    def caption(
        self
    ) -> "String" | "None":
        return self._d["caption"]

    @property
    def caption_entities(
        self
    ) -> "List[MessageEntity]" | "None":
        return self._d["caption_entities"]

    @property
    def contact(
        self
    ) -> "Contact" | "None":
        return self._d["contact"]

    @property
    def dice(
        self
    ) -> "Dice" | "None":
        return self._d["dice"]

    @property
    def game(
        self
    ) -> "Game" | "None":
        return self._d["game"]

    @property
    def poll(
        self
    ) -> "Poll" | "None":
        return self._d["poll"]

    @property
    def venue(
        self
    ) -> "Venue" | "None":
        return self._d["venue"]

    @property
    def location(
        self
    ) -> "Location" | "None":
        return self._d["location"]

    @property
    def new_chat_members(
        self
    ) -> "List[User]" | "None":
        return self._d["new_chat_members"]

    @property
    def left_chat_member(
        self
    ) -> "User" | "None":
        return self._d["left_chat_member"]

    @property
    def new_chat_title(
        self
    ) -> "String" | "None":
        return self._d["new_chat_title"]

    @property
    def new_chat_photo(
        self
    ) -> "List[PhotoSize]" | "None":
        return self._d["new_chat_photo"]

    @property
    def delete_chat_photo(
        self
    ) -> "Boolean" | "None":
        return self._d["delete_chat_photo"]

    @property
    def group_chat_created(
        self
    ) -> "Boolean" | "None":
        return self._d["group_chat_created"]

    @property
    def supergroup_chat_created(
        self
    ) -> "Boolean" | "None":
        return self._d["supergroup_chat_created"]

    @property
    def channel_chat_created(
        self
    ) -> "Boolean" | "None":
        return self._d["channel_chat_created"]

    @property
    def message_auto_delete_timer_changed(
        self
    ) -> "MessageAutoDeleteTimerChanged" | "None":
        return self._d["message_auto_delete_timer_changed"]

    @property
    def migrate_to_chat_id(
        self
    ) -> "Integer" | "None":
        return self._d["migrate_to_chat_id"]

    @property
    def migrate_from__chat_id(
        self
    ) -> "Integer" | "None":
        return self._d["migrate_from_chat_id"]

    @property
    def pinned_message(
        self
    ) -> "Message" | "None":
        return self._d["pinned_message"]

    @property
    def invoice(
        self
    ) -> "Invoice" | "None":
        return self._d["invoice"]

    @property
    def successful_payment(
        self
    ) -> "SuccessfulPayment" | "None":
        return self._d["successful_payment"]

    @property
    def connected_website(
        self
    ) -> "String" | "None":
        return self._d["connected_website"]

    @property
    def passport_data(
        self
    ) -> "PassportData" | "None":
        return self._d["passport_data"]

    @property
    def proximity_alert_triggered(
        self
    ) -> "ProximityAlertTriggered" | "None":
        return self._d["proximity_alert_triggered"]

    @property
    def video_chat_scheduled(
        self
    ) -> "VideoChatScheduled" | "None":
        return self._d["video_chat_scheduled"]

    @property
    def video_chat_started(
        self
    ) -> "VideoChatStarted" | "None":
        return self._d["video_chat_started"]

    @property
    def video_chat_ended(
        self
    ) -> "VideoChatEnded" | "None":
        return self._d["video_chat_ended"]

    @property
    def video_chat_participants_invited(
        self
    ) -> "VideoChatParticipantsInvited" | "None":
        return self._d["video_chat_participants_invited"]

    @property
    def web_app_data(
        self
    ) -> "WebAppData" | "None":
        return self._d["web_app_data"]

    @property
    def reply_markup(
        self
    ) -> "InlineKeyboardMarkup" | "None":
        return self._d["reply_markup"]


class MessageId(DefaultType):

    @property
    def message_id(
        self
    ) -> "Integer":
        return self._d["message_id"]


class MessageEntity(DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return self._d["type"]

    @property
    def offset(
        self
    ) -> "Integer":
        return self._d["offset"]

    @property
    def length(
        self
    ) -> "Integer":
        return self._d["length"]

    @property
    def url(
        self
    ) -> "String" | "None":
        return self._d["url"]

    @property
    def user(
        self
    ) -> "User" | "None":
        return self._d["user"]

    @property
    def language(
        self
    ) -> "String" | "None":
        return self._d["language"]


class PhotoSize(DefaultType):

    @property
    def file_id(
        self
    ) -> "String":
        return self._d["file_id"]

    @property
    def file_unique_id(
        self
    ) -> "String":
        return self._d["file_unique_id"]

    @property
    def width(
        self
    ) -> "Integer":
        return self._d["width"]

    @property
    def height(
        self
    ) -> "Integer":
        return self._d["height"]

    @property
    def file_size(
        self
    ) -> "Integer" | "None":
        return self._d["file_size"]


class Animation(DefaultType):

    @property
    def file_id(
        self
    ) -> "String":
        return self._d["file_id"]

    @property
    def file_unique_id(
        self
    ) -> "String":
        return self._d["file_unique_id"]

    @property
    def width(
        self
    ) -> "Integer":
        return self._d["width"]

    @property
    def height(
        self
    ) -> "Integer":
        return self._d["height"]

    @property
    def duration(
        self
    ) -> "Integer":
        return self._d["duration"]

    @property
    def thumb(
        self
    ) -> "PhotoSize" | "None":
        return self._d["thumb"]

    @property
    def file_name(
        self
    ) -> "String" | "None":
        return self._d["file_name"]

    @property
    def mime_type(
        self
    ) -> "String" | "None":
        return self._d["mime_type"]

    @property
    def file_size(
        self
    ) -> "Integer" | "None":
        return self._d["file_size"]


class Audio(DefaultType):

    @property
    def file_id(
        self
    ) -> "String":
        return self._d["file_id"]

    @property
    def file_unique_id(
        self
    ) -> "String":
        return self._d["file_unique_id"]

    @property
    def duration(
        self
    ) -> "Integer":
        return self._d["duration"]

    @property
    def performer(
        self
    ) -> "String" | "None":
        return self._d["performer"]

    @property
    def title(
        self
    ) -> "String" | "None":
        return self._d["title"]

    @property
    def file_name(
        self
    ) -> "String" | "None":
        return self._d["file_name"]

    @property
    def mime_type(
        self
    ) -> "String" | "None":
        return self._d["mime_type"]

    @property
    def file_size(
        self
    ) -> "Integer" | "None":
        return self._d["file_size"]

    @property
    def thumb(
        self
    ) -> "PhotoSize" | "None":
        return self._d["thumb"]


class Document(DefaultType):

    @property
    def file_id(
        self
    ) -> "String":
        return self._d["file_id"]

    @property
    def file_unique_id(
        self
    ) -> "String":
        return self._d["file_unique_id"]

    @property
    def thumb(
        self
    ) -> "PhotoSize" | "None":
        return self._d["thumb"]

    @property
    def file_name(
        self
    ) -> "String" | "None":
        return self._d["file_name"]

    @property
    def mime_type(
        self
    ) -> "String" | "None":
        return self._d["mime_type"]

    @property
    def file_size(
        self
    ) -> "Integer" | "None":
        return self._d["file_size"]


class Video(DefaultType):

    @property
    def file_id(
        self
    ) -> "String":
        return self._d["file_id"]

    @property
    def file_unique_id(
        self
    ) -> "String":
        return self._d["file_unique_id"]

    @property
    def width(
        self
    ) -> "Integer":
        return self._d["width"]

    @property
    def height(
        self
    ) -> "Integer":
        return self._d["height"]

    @property
    def duration(
        self
    ) -> "Integer":
        return self._d["duration"]

    @property
    def thumb(
        self
    ) -> "PhotoSize" | "None":
        return self._d["thumb"]

    @property
    def file_name(
        self
    ) -> "String" | "None":
        return self._d["file_name"]

    @property
    def mime_type(
        self
    ) -> "String" | "None":
        return self._d["mime_type"]

    @property
    def file_size(
        self
    ) -> "Integer" | "None":
        return self._d["file_size"]


class VideoNote(DefaultType):

    @property
    def file_id(
        self
    ) -> "String":
        return self._d["file_id"]

    @property
    def file_unique_id(
        self
    ) -> "String":
        return self._d["file_unique_id"]

    @property
    def length(
        self
    ) -> "Integer":
        return self._d["length"]

    @property
    def duration(
        self
    ) -> "Integer":
        return self._d["duration"]

    @property
    def thumb(
        self
    ) -> "PhotoSize" | "None":
        return self._d["thumb"]

    @property
    def file_size(
        self
    ) -> "Integer" | "None":
        return self._d["file_size"]


class Voice(DefaultType):

    @property
    def file_id(
        self
    ) -> "String":
        return self._d["file_id"]

    @property
    def file_unique_id(
        self
    ) -> "String":
        return self._d["file_unique_id"]

    @property
    def duration(
        self
    ) -> "Integer":
        return self._d["duration"]

    @property
    def mime_type(
        self
    ) -> "String" | "None":
        return self._d["mime_type"]

    @property
    def file_size(
        self
    ) -> "Integer" | "None":
        return self._d["file_size"]


class Contact(DefaultType):

    @property
    def phone_number(
        self
    ) -> "String":
        return self._d["phone_number"]

    @property
    def first_name(
        self
    ) -> "String":
        return self._d["first_name"]

    @property
    def last_name(
        self
    ) -> "String" | "None":
        return self._d["last_name"]

    @property
    def user_id(
        self
    ) -> "Integer" | "None":
        return self._d["user_id"]

    @property
    def vcard(
        self
    ) -> "String" | "None":
        return self._d["vcard"]


class Dice(DefaultType):

    @property
    def emoji(
        self
    ) -> "String":
        return self._d["emoji"]

    @property
    def value(
        self
    ) -> "Integer":
        return self._d["value"]


class PollOption(DefaultType):

    @property
    def text(
        self
    ) -> "String":
        return self._d["text"]

    @property
    def voter_count(
        self
    ) -> "Integer":
        return self._d["voter_count"]


class PollAnswer(DefaultType):

    @property
    def poll_id(
        self
    ) -> "String":
        return self._d["poll_id"]

    @property
    def user(
        self
    ) -> "User":
        return self._d["user"]

    @property
    def option_ids(
        self
    ) -> "List[Integer]":
        return self._d["option_ids"]


class Poll(DefaultType):

    @property
    def id(
        self
    ) -> "String":
        return self._d["id"]

    @property
    def question(
        self
    ) -> "String":
        return self._d["question"]

    @property
    def options(
        self
    ) -> "List[PollOption]":
        return self._d["options"]

    @property
    def total_voter_count(
        self
    ) -> "Integer":
        return self._d["total_voter_count"]

    @property
    def is_closed(
        self
    ) -> "Boolean":
        return self._d["is_closed"]

    @property
    def is_anonymous(
        self
    ) -> "Boolean":
        return self._d["is_anonymous"]

    @property
    def type(
        self
    ) -> "String":
        return self._d["type"]

    @property
    def allows_multiple_answers(
        self
    ) -> "Boolean":
        return self._d["allows_multiple_answers"]

    @property
    def correct_option_id(
        self
    ) -> "Integer" | "None":
        return self._d["correct_option_id"]

    @property
    def explanation(
        self
    ) -> "String" | "None":
        return self._d["explanation"]

    @property
    def explanation_entities(
        self
    ) -> "List[MessageEntity]" | "None":
        return self._d["explanation_entities"]

    @property
    def open_period(
        self
    ) -> "Integer" | "None":
        return self._d["open_period"]

    @property
    def close_date(
        self
    ) -> "Integer" | "None":
        return self._d["close_date"]


class Location(DefaultType):

    @property
    def longitude(
        self
    ) -> "Float":
        return self._d["longitude"]

    @property
    def latitude(
        self
    ) -> "Float":
        return self._d["latitude"]

    @property
    def horizontal_accuracy(
        self
    ) -> "Float" | "None":
        return self._d["horizontal_accuracy"]

    @property
    def live_period(
        self
    ) -> "Integer" | "None":
        return self._d["live_period"]

    @property
    def heading(
        self
    ) -> "Integer" | "None":
        return self._d["heading"]

    @property
    def proximity_alert_radius(
        self
    ) -> "Integer" | "None":
        return self._d["proximity_alert_radius"]


class Venue(DefaultType):

    @property
    def location(
        self
    ) -> "Location":
        return self._d["location"]

    @property
    def title(
        self
    ) -> "String":
        return self._d["title"]

    @property
    def address(
        self
    ) -> "String":
        return self._d["address"]

    @property
    def foursquare_id(
        self
    ) -> "String" | "None":
        return self._d["foursquare_id"]

    @property
    def foursquare_type(
        self
    ) -> "String" | "None":
        return self._d["foursquare_type"]

    @property
    def google_place_id(
        self
    ) -> "String" | "None":
        return self._d["google_place_id"]

    @property
    def google_place_type(
        self
    ) -> "String" | "None":
        return self._d["google_place_type"]


class WebAppData(DefaultType):

    @property
    def data(
        self
    ) -> "String":
        return self._d["data"]

    @property
    def button_text(
        self
    ) -> "String":
        return self._d["button_text"]


class ProximityAlertTriggered(DefaultType):

    @property
    def traveler(
        self
    ) -> "User":
        return self._d["traveler"]

    @property
    def watcher(
        self
    ) -> "User":
        return self._d["watcher"]

    @property
    def distance(
        self
    ) -> "Integer":
        return self._d["distance"]


class MessageAutoDeleteTimerChanged(DefaultType):

    @property
    def message_auto_delete_time(
        self
    ) -> "Integer":
        return self._d["message_auto_delete_time"]


class VideoChatScheduled(DefaultType):

    @property
    def start_date(
        self
    ) -> "Integer":
        return self._d["start_date"]


class VideoChatStarted(DefaultType):
    ...


class VideoChatEnded(DefaultType):

    @property
    def duration(
        self
    ) -> "Integer":
        return self._d["duration"]


class VideoChatParticipantsInvited(DefaultType):

    @property
    def users(
        self
    ) -> "List[User]":
        return self._d["users"]


class UserProfilePhotos(DefaultType):

    @property
    def total_count(
        self
    ) -> "Integer":
        return self._d["total_count"]

    @property
    def photos(
        self
    ) -> "List[List[PhotoSize]]":
        return self._d["photos"]


class File(DefaultType):

    @property
    def file_id(
        self
    ) -> "String":
        return self._d["file_id"]

    @property
    def file_unique_id(
        self
    ) -> "String":
        return self._d["file_unique_id"]

    @property
    def file_size(
        self
    ) -> "Integer" | "None":
        return self._d["file_size"]

    @property
    def file_path(
        self
    ) -> "String" | "None":
        return self._d["file_path"]


class WebAppInfo(DefaultType):

    @property
    def url(
        self
    ) -> "String":
        return self._d["url"]


class ReplyKeyboardMarkup(DefaultType):

    @property
    def keyboard(
        self
    ) -> "List[List[KeyboardButton]]":
        return self._d["keyboard"]

    @property
    def resize_keyboard(
        self
    ) -> "Boolean" | "None":
        return self._d["resize_keyboard"]

    @property
    def one_time_keyboard(
        self
    ) -> "Boolean" | "None":
        return self._d["one_time_keyboard"]

    @property
    def input_field_placeholder(
        self
    ) -> "String" | "None":
        return self._d["input_field_placeholder"]

    @property
    def selective(
        self
    ) -> "Boolean" | "None":
        return self._d["selective"]


class KeyboardButton(DefaultType):

    @property
    def text(
        self
    ) -> "String":
        return self._d["text"]

    @property
    def request_contact(
        self
    ) -> "Boolean" | "None":
        return self._d["request_contact"]

    @property
    def request_location(
        self
    ) -> "Boolean" | "None":
        return self._d["request_location"]

    @property
    def request_poll(
        self
    ) -> "KeyboardButtonPollType" | "None":
        return self._d["request_poll"]

    @property
    def web_app(
        self
    ) -> "WebAppInfo" | "None":
        return self._d["web_app"]


class KeyboardButtonPollType(DefaultType):

    @property
    def type(
        self
    ) -> "String" | "None":
        return self._d["type"]


class ReplyKeyboardRemove(DefaultType):

    @property
    def remove_keyboard(
        self
    ) -> "Boolean":
        return self._d["remove_keyboard"]

    @property
    def selective(
        self
    ) -> "Boolean" | "None":
        return self._d["selective"]


class InlineKeyboardMarkup(DefaultType):

    @property
    def inline_keyboard(
        self
    ) -> "List[List[InlineKeyboardButton]]":
        return self._d["inline_keyboard"]


class InlineKeyboardButton(DefaultType):

    @property
    def text(
        self
    ) -> "String":
        return self._d["text"]

    @property
    def url(
        self
    ) -> "String" | "None":
        return self._d["url"]

    @property
    def callback_data(
        self
    ) -> "String" | "None":
        return self._d["callback_data"]

    @property
    def web_app(
        self
    ) -> "WebAppInfo" | "None":
        return self._d["web_app"]

    @property
    def login_url(
        self
    ) -> "LoginUrl" | "None":
        return self._d["login_url"]

    @property
    def switch_inline_query(
        self
    ) -> "String" | "None":
        return self._d["switch_inline_query"]

    @property
    def switch_inline_query_current_chat(
        self
    ) -> "String" | "None":
        return self._d["switch_inline_query_current_chat"]

    @property
    def callback_game(
        self
    ) -> "CallbackGame" | "None":
        return self._d["callback_game"]

    @property
    def pay(
        self
    ) -> "Boolean" | "None":
        return self._d["pay"]


class LoginUrl(DefaultType):

    @property
    def url(
        self
    ) -> "String":
        return self._d["url"]

    @property
    def forward_text(
        self
    ) -> "String" | "None":
        return self._d["forward_text"]

    @property
    def bot_username(
        self
    ) -> "String" | "None":
        return self._d["bot_username"]

    @property
    def request_write_access(
        self
    ) -> "Boolean" | "None":
        return self._d["request_write_access"]


class CallbackQuery(DefaultType):

    @property
    def id(
        self
    ) -> "String":
        return self._d["id"]

    @property
    def from_(
        self
    ) -> "User":
        return self._d["from"]

    @property
    def message(
        self
    ) -> "Message" | "None":
        return self._d["message"]

    @property
    def inline_message_id(
        self
    ) -> "String" | "None":
        return self._d["inline_message_id"]

    @property
    def chat_instance(
        self
    ) -> "String":
        return self._d["chat_instance"]

    @property
    def data(
        self
    ) -> "String" | "None":
        return self._d["data"]

    @property
    def game_short_name(
        self
    ) -> "String" | "None":
        return self._d["game_short_name"]


class ForceReply(DefaultType):

    @property
    def force_reply(
        self
    ) -> "Boolean":
        return self._d["force_reply"]

    @property
    def input_field_placeholder(
        self
    ) -> "String" | "None":
        return self._d["input_field_placeholder"]

    @property
    def selective(
        self
    ) -> "Boolean" | "None":
        return self._d["selective"]


class ChatPhoto(DefaultType):

    @property
    def small_file_id(
        self
    ) -> "String":
        return self._d["small_file_id"]

    @property
    def small_file_unique_id(
        self
    ) -> "String":
        return self._d["small_file_unique_id"]

    @property
    def big_file_id(
        self
    ) -> "String":
        return self._d["big_file_id"]

    @property
    def big_file_unique_id(
        self
    ) -> "String":
        return self._d["big_file_unique_id"]


class ChatInviteLink(DefaultType):

    @property
    def invite_link(
        self
    ) -> "String":
        return self._d["invite_link"]

    @property
    def creator(
        self
    ) -> "User":
        return self._d["creator"]

    @property
    def creates_join_request(
        self
    ) -> "Boolean":
        return self._d["creates_join_request"]

    @property
    def is_primary(
        self
    ) -> "Boolean":
        return self._d["is_primary"]

    @property
    def is_revoked(
        self
    ) -> "Boolean":
        return self._d["is_revoked"]

    @property
    def name(
        self
    ) -> "String" | "None":
        return self._d["name"]

    @property
    def expire_date(
        self
    ) -> "Integer" | "None":
        return self._d["expire_date"]

    @property
    def member_limit(
        self
    ) -> "Integer" | "None":
        return self._d["member_limit"]

    @property
    def pending_join_request_count(
        self
    ) -> "Integer" | "None":
        return self._d["pending_join_request_count"]


class ChatAdministratorRights(DefaultType):

    @property
    def is_anonymous(
        self
    ) -> "Boolean":
        return self._d["is_anonymous"]

    @property
    def can_manage_chat(
        self
    ) -> "Boolean":
        return self._d["can_manage_chat"]

    @property
    def can_delete_messages(
        self
    ) -> "Boolean":
        return self._d["can_delete_messages"]

    @property
    def can_manage_video_chats(
        self
    ) -> "Boolean":
        return self._d["can_manage_video_chats"]

    @property
    def can_restrict_members(
        self
    ) -> "Boolean":
        return self._d["can_restrict_members"]

    @property
    def can_promote_members(
        self
    ) -> "Boolean":
        return self._d["can_promote_members"]

    @property
    def can_change_info(
        self
    ) -> "Boolean":
        return self._d["can_change_info"]

    @property
    def can_invite_users(
        self
    ) -> "Boolean":
        return self._d["can_invite_users"]

    @property
    def can_post_messages(
        self
    ) -> "Boolean" | "None":
        return self._d["can_post_messages"]

    @property
    def can_edit_messages(
        self
    ) -> "Boolean" | "None":
        return self._d["can_edit_messages"]

    @property
    def can_pin_messages(
        self
    ) -> "Boolean" | "None":
        return self._d["can_pin_messages"]


class ChatMember(DefaultType):
    ...


class ChatMemberOwner(DefaultType):

    @property
    def status(
        self
    ) -> "String":
        return self._d["status"]

    @property
    def user(
        self
    ) -> "User":
        return self._d["user"]

    @property
    def is_anonymous(
        self
    ) -> "Boolean":
        return self._d["is_anonymous"]

    @property
    def custom_title(
        self
    ) -> "String" | "None":
        return self._d["custom_title"]


class ChatMemberAdministrator(DefaultType):

    @property
    def status(
        self
    ) -> "String":
        return self._d["status"]

    @property
    def user(
        self
    ) -> "User":
        return self._d["user"]

    @property
    def can_be_edited(
        self
    ) -> "Boolean":
        return self._d["can_be_edited"]

    @property
    def is_anonymous(
        self
    ) -> "Boolean":
        return self._d["is_anonymous"]

    @property
    def can_manage_chat(
        self
    ) -> "Boolean":
        return self._d["can_manage_chat"]

    @property
    def can_delete_messages(
        self
    ) -> "Boolean":
        return self._d["can_delete_messages"]

    @property
    def can_manage_video_chats(
        self
    ) -> "Boolean":
        return self._d["can_manage_video_chats"]

    @property
    def can_restrict_members(
        self
    ) -> "Boolean":
        return self._d["can_restrict_members"]

    @property
    def can_promote_members(
        self
    ) -> "Boolean":
        return self._d["can_promote_members"]

    @property
    def can_change_info(
        self
    ) -> "Boolean":
        return self._d["can_change_info"]

    @property
    def can_invite_users(
        self
    ) -> "Boolean":
        return self._d["can_invite_users"]

    @property
    def can_post_messages(
        self
    ) -> "Boolean" | "None":
        return self._d["can_post_messages"]

    @property
    def can_edit_messages(
        self
    ) -> "Boolean" | "None":
        return self._d["can_edit_messages"]

    @property
    def can_pin_messages(
        self
    ) -> "Boolean" | "None":
        return self._d["can_pin_messages"]

    @property
    def custom_title(
        self
    ) -> "String" | "None":
        return self._d["custom_title"]


class ChatMemberMember(DefaultType):

    @property
    def status(
        self
    ) -> "String":
        return self._d["status"]

    @property
    def user(
        self
    ) -> "User":
        return self._d["user"]


class ChatMemberRestricted(DefaultType):

    @property
    def status(
        self
    ) -> "String":
        return self._d["status"]

    @property
    def user(
        self
    ) -> "User":
        return self._d["user"]

    @property
    def is_member(
        self
    ) -> "Boolean":
        return self._d["is_member"]

    @property
    def can_change_info(
        self
    ) -> "Boolean":
        return self._d["can_change_info"]

    @property
    def can_invite_users(
        self
    ) -> "Boolean":
        return self._d["can_invite_users"]

    @property
    def can_pin_messages(
        self
    ) -> "Boolean":
        return self._d["can_pin_messages"]

    @property
    def can_send_messages(
        self
    ) -> "Boolean":
        return self._d["can_send_messages"]

    @property
    def can_send_media_messages(
        self
    ) -> "Boolean":
        return self._d["can_send_media_messages"]

    @property
    def can_send_polls(
        self
    ) -> "Boolean":
        return self._d["can_send_polls"]

    @property
    def can_send_other_messages(
        self
    ) -> "Boolean":
        return self._d["can_send_other_messages"]

    @property
    def can_add_web_page_previews(
        self
    ) -> "Boolean":
        return self._d["can_add_web_page_previews"]

    @property
    def until_date(
        self
    ) -> "Integer":
        return self._d["until_date"]


class ChatMemberLeft(DefaultType):

    @property
    def status(
        self
    ) -> "String":
        return self._d["status"]

    @property
    def user(
        self
    ) -> "User":
        return self._d["user"]


class ChatMemberBanned(DefaultType):

    @property
    def status(
        self
    ) -> "String":
        return self._d["status"]

    @property
    def user(
        self
    ) -> "User":
        return self._d["user"]

    @property
    def until_date(
        self
    ) -> "Integer":
        return self._d["until_date"]


class ChatMemberUpdated(DefaultType):

    @property
    def chat(
        self
    ) -> "Chat":
        return self._d["chat"]

    @property
    def from_(
        self
    ) -> "User":
        return self._d["from"]

    @property
    def date(
        self
    ) -> "Integer":
        return self._d["date"]

    @property
    def old_chat_member(
        self
    ) -> "ChatMember":
        return self._d["old_chat_member"]

    @property
    def new_chat_member(
        self
    ) -> "ChatMember":
        return self._d["new_chat_member"]

    @property
    def invite_link(
        self
    ) -> "ChatInviteLink" | "None":
        return self._d["invite_link"]


class ChatJoinRequest(DefaultType):

    @property
    def chat(
        self
    ) -> "Chat":
        return self._d["chat"]

    @property
    def from_(
        self
    ) -> "User":
        return self._d["from"]

    @property
    def date(
        self
    ) -> "Integer":
        return self._d["date"]

    @property
    def bio(
        self
    ) -> "String" | "None":
        return self._d["bio"]

    @property
    def invite_link(
        self
    ) -> "ChatInviteLink" | "None":
        return self._d["invite_link"]


class ChatPermissions(DefaultType):

    @property
    def can_send_messages(
        self
    ) -> "Boolean" | "None":
        return self._d["can_send_messages"]

    @property
    def can_send_media_messages(
        self
    ) -> "Boolean" | "None":
        return self._d["can_send_media_messages"]

    @property
    def can_send_polls(
        self
    ) -> "Boolean" | "None":
        return self._d["can_send_polls"]

    @property
    def can_send_other_messages(
        self
    ) -> "Boolean" | "None":
        return self._d["can_send_other_messages"]

    @property
    def can_add_web_page_previews(
        self
    ) -> "Boolean" | "None":
        return self._d["can_add_web_page_previews"]

    @property
    def can_change_info(
        self
    ) -> "Boolean" | "None":
        return self._d["can_change_info"]

    @property
    def can_invite_users(
        self
    ) -> "Boolean" | "None":
        return self._d["can_invite_users"]

    @property
    def can_pin_messages(
        self
    ) -> "Boolean" | "None":
        return self._d["can_pin_messages"]


class ChatLocation(DefaultType):

    @property
    def location(
        self
    ) -> "Location":
        return self._d["location"]

    @property
    def address(
        self
    ) -> "String":
        return self._d["address"]


class BotCommand(DefaultType):

    @property
    def command(
        self
    ) -> "String":
        return self._d["command"]

    @property
    def description(
        self
    ) -> "String":
        return self._d["description"]


class BotCommandScope(DefaultType):
    ...


class BotCommandScopeDefault(DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return self._d["type"]


class BotCommandScopeAllPrivateChats(DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return self._d["type"]


class BotCommandScopeAllGroupChats(DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return self._d["type"]


class BotCommandScopeAllChatAdministrators(DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return self._d["type"]


class BotCommandScopeChat(DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return self._d["type"]

    @property
    def chat_id(
        self
    ) -> "Integer" | "String":
        return self._d["chat_id"]


class BotCommandScopeChatAdministrators(DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return self._d["type"]

    @property
    def chat_id(
        self
    ) -> "Integer" | "String":
        return self._d["chat_id"]


class BotCommandScopeChatMember(DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return self._d["type"]

    @property
    def chat_id(
        self
    ) -> "Integer" | "String":
        return self._d["chat_id"]

    @property
    def user_id(
        self
    ) -> "Integer":
        return self._d["user_id"]


class MenuButton(DefaultType):
    ...


class MenuButtonCommands(DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return self._d["type"]


class MenuButtonWebApp(DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return self._d["type"]

    @property
    def text(
        self
    ) -> "String":
        return self._d["text"]

    @property
    def web_app(
        self
    ) -> "WebAppInfo":
        return self._d["web_app"]


class MenuButtonDefault(DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return self._d["type"]


class ResponseParameters(DefaultType):

    @property
    def migrate_to_chat_id(
        self
    ) -> "Integer" | "None":
        return self._d["migrate_to_chat_id"]

    @property
    def retry_after(
        self
    ) -> "Integer" | "None":
        return self._d["retry_after"]


class InputMedia(DefaultType):
    ...


class InputMediaPhoto(DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return self._d["type"]

    @property
    def media(
        self
    ) -> "String":
        return self._d["media"]

    @property
    def caption(
        self
    ) -> "String" | "None":
        return self._d["caption"]

    @property
    def parse_mode(
        self
    ) -> "String" | "None":
        return self._d["parse_mode"]

    @property
    def caption_entities(
        self
    ) -> "List[MessageEntity]" | "None":
        return self._d["caption_entities"]


class InputMediaVideo(DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return self._d["type"]

    @property
    def media(
        self
    ) -> "String":
        return self._d["media"]

    @property
    def thumb(
        self
    ) -> "InputFile" | "String" | "None":
        return self._d["thumb"]

    @property
    def caption(
        self
    ) -> "String" | "None":
        return self._d["caption"]

    @property
    def parse_mode(
        self
    ) -> "String" | "None":
        return self._d["parse_mode"]

    @property
    def caption_entities(
        self
    ) -> "List[MessageEntity]" | "None":
        return self._d["caption_entities"]

    @property
    def width(
        self
    ) -> "Integer" | "None":
        return self._d["width"]

    @property
    def height(
        self
    ) -> "Integer" | "None":
        return self._d["height"]

    @property
    def duration(
        self
    ) -> "Integer" | "None":
        return self._d["duration"]

    @property
    def supports_streaming(
        self
    ) -> "Boolean" | "None":
        return self._d["supports_streaming"]


class InputMediaAnimation(DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return self._d["type"]

    @property
    def media(
        self
    ) -> "String":
        return self._d["media"]

    @property
    def thumb(
        self
    ) -> "InputFile" | "String" | "None":
        return self._d["thumb"]

    @property
    def caption(
        self
    ) -> "String" | "None":
        return self._d["caption"]

    @property
    def parse_mode(
        self
    ) -> "String" | "None":
        return self._d["parse_mode"]

    @property
    def caption_entities(
        self
    ) -> "List[MessageEntity]" | "None":
        return self._d["caption_entities"]

    @property
    def width(
        self
    ) -> "Integer" | "None":
        return self._d["width"]

    @property
    def height(
        self
    ) -> "Integer" | "None":
        return self._d["height"]

    @property
    def duration(
        self
    ) -> "Integer" | "None":
        return self._d["duration"]


class InputMediaAudio(DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return self._d["type"]

    @property
    def media(
        self
    ) -> "String":
        return self._d["media"]

    @property
    def thumb(
        self
    ) -> "InputFile" | "String" | "None":
        return self._d["thumb"]

    @property
    def caption(
        self
    ) -> "String" | "None":
        return self._d["caption"]

    @property
    def parse_mode(
        self
    ) -> "String" | "None":
        return self._d["parse_mode"]

    @property
    def caption_entities(
        self
    ) -> "List[MessageEntity]" | "None":
        return self._d["caption_entities"]

    @property
    def duration(
        self
    ) -> "Integer" | "None":
        return self._d["duration"]

    @property
    def performer(
        self
    ) -> "String" | "None":
        return self._d["performer"]

    @property
    def title(
        self
    ) -> "String" | "None":
        return self._d["title"]


class InputMediaDocument(DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return self._d["type"]

    @property
    def media(
        self
    ) -> "String":
        return self._d["media"]

    @property
    def thumb(
        self
    ) -> "InputFile" | "String" | "None":
        return self._d["thumb"]

    @property
    def caption(
        self
    ) -> "String" | "None":
        return self._d["caption"]

    @property
    def parse_mode(
        self
    ) -> "String" | "None":
        return self._d["parse_mode"]

    @property
    def caption_entities(
        self
    ) -> "List[MessageEntity]" | "None":
        return self._d["caption_entities"]

    @property
    def disable_content_type_detection(
        self
    ) -> "Boolean" | "None":
        return self._d["disable_content_type_detection"]


class InputFile(DefaultType):
    ...


class Sticker(DefaultType):

    @property
    def file_id(
        self
    ) -> "String":
        return self._d["file_id"]

    @property
    def file_unique_id(
        self
    ) -> "String":
        return self._d["file_unique_id"]

    @property
    def width(
        self
    ) -> "Integer":
        return self._d["width"]

    @property
    def height(
        self
    ) -> "Integer":
        return self._d["height"]

    @property
    def is_animated(
        self
    ) -> "Boolean":
        return self._d["is_animated"]

    @property
    def is_video(
        self
    ) -> "Boolean":
        return self._d["is_video"]

    @property
    def thumb(
        self
    ) -> "PhotoSize" | "None":
        return self._d["thumb"]

    @property
    def emoji(
        self
    ) -> "String" | "None":
        return self._d["emoji"]

    @property
    def set_name(
        self
    ) -> "String" | "None":
        return self._d["set_name"]

    @property
    def premium_animation(
        self
    ) -> "File" | "None":
        return self._d["premium_animation"]

    @property
    def mask_position(
        self
    ) -> "MaskPosition" | "None":
        return self._d["mask_position"]

    @property
    def file_size(
        self
    ) -> "Integer" | "None":
        return self._d["file_size"]


class StickerSet(DefaultType):

    @property
    def name(
        self
    ) -> "String":
        return self._d["name"]

    @property
    def title(
        self
    ) -> "String":
        return self._d["title"]

    @property
    def is_animated(
        self
    ) -> "Boolean":
        return self._d["is_animated"]

    @property
    def is_video(
        self
    ) -> "Boolean":
        return self._d["is_video"]

    @property
    def contains_masks(
        self
    ) -> "Boolean":
        return self._d["contains_masks"]

    @property
    def stickers(
        self
    ) -> "List[Sticker]":
        return self._d["stickers"]

    @property
    def thumb(
        self
    ) -> "PhotoSize" | "None":
        return self._d["thumb"]


class MaskPosition(DefaultType):

    @property
    def point(
        self
    ) -> "String":
        return self._d["point"]

    @property
    def x_shift(
        self
    ) -> "Float":
        return self._d["x_shift"]

    @property
    def y_shift(
        self
    ) -> "Float":
        return self._d["y_shift"]

    @property
    def scale(
        self
    ) -> "Float":
        return self._d["scale"]


class InlineQuery(DefaultType):

    @property
    def id(
        self
    ) -> "String":
        return self._d["id"]

    @property
    def from_(
        self
    ) -> "User":
        return self._d["from"]

    @property
    def query(
        self
    ) -> "String":
        return self._d["query"]

    @property
    def offset(
        self
    ) -> "String":
        return self._d["offset"]

    @property
    def chat_type(
        self
    ) -> "String" | "None":
        return self._d["chat_type"]

    @property
    def location(
        self
    ) -> "Location" | "None":
        return self._d["location"]


class InlineQueryResult(DefaultType):
    ...


class InlineQueryResultArticle(DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return self._d["type"]

    @property
    def id(
        self
    ) -> "String":
        return self._d["id"]

    @property
    def title(
        self
    ) -> "String":
        return self._d["title"]

    @property
    def input_message_content(
        self
    ) -> "InputMessageContent":
        return self._d["input_message_content"]

    @property
    def reply_markup(
        self
    ) -> "InlineKeyboardMarkup" | "None":
        return self._d["reply_markup"]

    @property
    def url(
        self
    ) -> "String" | "None":
        return self._d["url"]

    @property
    def hide_url(
        self
    ) -> "Boolean" | "None":
        return self._d["hide_url"]

    @property
    def description(
        self
    ) -> "String" | "None":
        return self._d["description"]

    @property
    def thumb_url(
        self
    ) -> "String" | "None":
        return self._d["thumb_url"]

    @property
    def thumb_width(
        self
    ) -> "Integer" | "None":
        return self._d["thumb_width"]

    @property
    def thumb_height(
        self
    ) -> "Integer" | "None":
        return self._d["thumb_height"]


class InlineQueryResultPhoto(DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return self._d["type"]

    @property
    def id(
        self
    ) -> "String":
        return self._d["id"]

    @property
    def photo_url(
        self
    ) -> "String":
        return self._d["photo_url"]

    @property
    def thumb_url(
        self
    ) -> "String":
        return self._d["thumb_url"]

    @property
    def photo_width(
        self
    ) -> "Integer" | "None":
        return self._d["photo_width"]

    @property
    def photo_height(
        self
    ) -> "Integer" | "None":
        return self._d["photo_height"]

    @property
    def title(
        self
    ) -> "String" | "None":
        return self._d["title"]

    @property
    def description(
        self
    ) -> "String" | "None":
        return self._d["description"]

    @property
    def caption(
        self
    ) -> "String" | "None":
        return self._d["caption"]

    @property
    def parse_mode(
        self
    ) -> "String" | "None":
        return self._d["parse_mode"]

    @property
    def caption_entities(
        self
    ) -> "List[MessageEntity]" | "None":
        return self._d["caption_entities"]

    @property
    def reply_markup(
        self
    ) -> "InlineKeyboardMarkup" | "None":
        return self._d["reply_markup"]

    @property
    def input_message_content(
        self
    ) -> "InputMessageContent" | "None":
        return self._d["input_message_content"]


class InlineQueryResultGif(DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return self._d["type"]

    @property
    def id(
        self
    ) -> "String":
        return self._d["id"]

    @property
    def gif_url(
        self
    ) -> "String":
        return self._d["gif_url"]

    @property
    def gif_width(
        self
    ) -> "Integer" | "None":
        return self._d["gif_width"]

    @property
    def gif_height(
        self
    ) -> "Integer" | "None":
        return self._d["gif_height"]

    @property
    def gif_duration(
        self
    ) -> "Integer" | "None":
        return self._d["gif_duration"]

    @property
    def thumb_url(
        self
    ) -> "String":
        return self._d["thumb_url"]

    @property
    def thumb_mime_type(
        self
    ) -> "String" | "None":
        return self._d["thumb_mime_type"]

    @property
    def title(
        self
    ) -> "String" | "None":
        return self._d["title"]

    @property
    def caption(
        self
    ) -> "String" | "None":
        return self._d["caption"]

    @property
    def parse_mode(
        self
    ) -> "String" | "None":
        return self._d["parse_mode"]

    @property
    def caption_entities(
        self
    ) -> "List[MessageEntity]" | "None":
        return self._d["caption_entities"]

    @property
    def reply_markup(
        self
    ) -> "InlineKeyboardMarkup" | "None":
        return self._d["reply_markup"]

    @property
    def input_message_content(
        self
    ) -> "InputMessageContent" | "None":
        return self._d["input_message_content"]


class InlineQueryResultMpeg4Gif(DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return self._d["type"]

    @property
    def id(
        self
    ) -> "String":
        return self._d["id"]

    @property
    def mpeg4_url(
        self
    ) -> "String":
        return self._d["mpeg4_url"]

    @property
    def mpeg4_width(
        self
    ) -> "Integer" | "None":
        return self._d["mpeg4_width"]

    @property
    def mpeg4_height(
        self
    ) -> "Integer" | "None":
        return self._d["mpeg4_height"]

    @property
    def mpeg4_duration(
        self
    ) -> "Integer" | "None":
        return self._d["mpeg4_duration"]

    @property
    def thumb_url(
        self
    ) -> "String":
        return self._d["thumb_url"]

    @property
    def thumb_mime_type(
        self
    ) -> "String" | "None":
        return self._d["thumb_mime_type"]

    @property
    def title(
        self
    ) -> "String" | "None":
        return self._d["title"]

    @property
    def caption(
        self
    ) -> "String" | "None":
        return self._d["caption"]

    @property
    def parse_mode(
        self
    ) -> "String" | "None":
        return self._d["parse_mode"]

    @property
    def caption_entities(
        self
    ) -> "List[MessageEntity]" | "None":
        return self._d["caption_entities"]

    @property
    def reply_markup(
        self
    ) -> "InlineKeyboardMarkup" | "None":
        return self._d["reply_markup"]

    @property
    def input_message_content(
        self
    ) -> "InputMessageContent" | "None":
        return self._d["input_message_content"]


class InlineQueryResultVideo(DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return self._d["type"]

    @property
    def id(
        self
    ) -> "String":
        return self._d["id"]

    @property
    def video_url(
        self
    ) -> "String":
        return self._d["video_url"]

    @property
    def mime_type(
        self
    ) -> "String":
        return self._d["mime_type"]

    @property
    def thumb_url(
        self
    ) -> "String":
        return self._d["thumb_url"]

    @property
    def title(
        self
    ) -> "String":
        return self._d["title"]

    @property
    def caption(
        self
    ) -> "String" | "None":
        return self._d["caption"]

    @property
    def parse_mode(
        self
    ) -> "String" | "None":
        return self._d["parse_mode"]

    @property
    def caption_entities(
        self
    ) -> "List[MessageEntity]" | "None":
        return self._d["caption_entities"]

    @property
    def video_width(
        self
    ) -> "Integer" | "None":
        return self._d["video_width"]

    @property
    def video_height(
        self
    ) -> "Integer" | "None":
        return self._d["video_height"]

    @property
    def video_duration(
        self
    ) -> "Integer" | "None":
        return self._d["video_duration"]

    @property
    def description(
        self
    ) -> "String" | "None":
        return self._d["description"]

    @property
    def reply_markup(
        self
    ) -> "InlineKeyboardMarkup" | "None":
        return self._d["reply_markup"]

    @property
    def input_message_content(
        self
    ) -> "InputMessageContent" | "None":
        return self._d["input_message_content"]


class InlineQueryResultAudio(DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return self._d["type"]

    @property
    def id(
        self
    ) -> "String":
        return self._d["id"]

    @property
    def audio_url(
        self
    ) -> "String":
        return self._d["audio_url"]

    @property
    def title(
        self
    ) -> "String":
        return self._d["title"]

    @property
    def caption(
        self
    ) -> "String" | "None":
        return self._d["caption"]

    @property
    def parse_mode(
        self
    ) -> "String" | "None":
        return self._d["parse_mode"]

    @property
    def caption_entities(
        self
    ) -> "List[MessageEntity]" | "None":
        return self._d["caption_entities"]

    @property
    def performer(
        self
    ) -> "String" | "None":
        return self._d["performer"]

    @property
    def audio_duration(
        self
    ) -> "Integer" | "None":
        return self._d["audio_duration"]

    @property
    def reply_markup(
        self
    ) -> "InlineKeyboardMarkup" | "None":
        return self._d["reply_markup"]

    @property
    def input_message_content(
        self
    ) -> "InputMessageContent" | "None":
        return self._d["input_message_content"]


class InlineQueryResultVoice(DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return self._d["type"]

    @property
    def id(
        self
    ) -> "String":
        return self._d["id"]

    @property
    def voice_url(
        self
    ) -> "String":
        return self._d["voice_url"]

    @property
    def title(
        self
    ) -> "String":
        return self._d["title"]

    @property
    def caption(
        self
    ) -> "String" | "None":
        return self._d["caption"]

    @property
    def parse_mode(
        self
    ) -> "String" | "None":
        return self._d["parse_mode"]

    @property
    def caption_entities(
        self
    ) -> "List[MessageEntity]" | "None":
        return self._d["caption_entities"]

    @property
    def voice_duration(
        self
    ) -> "Integer" | "None":
        return self._d["voice_duration"]

    @property
    def reply_markup(
        self
    ) -> "InlineKeyboardMarkup" | "None":
        return self._d["reply_markup"]

    @property
    def input_message_content(
        self
    ) -> "InputMessageContent" | "None":
        return self._d["input_message_content"]


class InlineQueryResultDocument(DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return self._d["type"]

    @property
    def id(
        self
    ) -> "String":
        return self._d["id"]

    @property
    def title(
        self
    ) -> "String":
        return self._d["title"]

    @property
    def caption(
        self
    ) -> "String" | "None":
        return self._d["caption"]

    @property
    def parse_mode(
        self
    ) -> "String" | "None":
        return self._d["parse_mode"]

    @property
    def caption_entities(
        self
    ) -> "List[MessageEntity]" | "None":
        return self._d["caption_entities"]

    @property
    def document_url(
        self
    ) -> "String":
        return self._d["document_url"]

    @property
    def mime_type(
        self
    ) -> "String":
        return self._d["mime_type"]

    @property
    def description(
        self
    ) -> "String" | "None":
        return self._d["description"]

    @property
    def reply_markup(
        self
    ) -> "InlineKeyboardMarkup" | "None":
        return self._d["reply_markup"]

    @property
    def input_message_content(
        self
    ) -> "InputMessageContent" | "None":
        return self._d["input_message_content"]

    @property
    def thumb_url(
        self
    ) -> "String" | "None":
        return self._d["thumb_url"]

    @property
    def thumb_width(
        self
    ) -> "Integer" | "None":
        return self._d["thumb_width"]

    @property
    def thumb_height(
        self
    ) -> "Integer" | "None":
        return self._d["thumb_height"]


class InlineQueryResultLocation(DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return self._d["type"]

    @property
    def id(
        self
    ) -> "String":
        return self._d["id"]

    @property
    def latitude(
        self
    ) -> "Float":
        return self._d["latitude"]

    @property
    def longitude(
        self
    ) -> "Float":
        return self._d["longitude"]

    @property
    def title(
        self
    ) -> "String":
        return self._d["title"]

    @property
    def horizontal_accuracy(
        self
    ) -> "Float" | "None":
        return self._d["horizontal_accuracy"]

    @property
    def live_period(
        self
    ) -> "Integer" | "None":
        return self._d["live_period"]

    @property
    def heading(
        self
    ) -> "Integer" | "None":
        return self._d["heading"]

    @property
    def proximity_alert_radius(
        self
    ) -> "Integer" | "None":
        return self._d["proximity_alert_radius"]

    @property
    def reply_markup(
        self
    ) -> "InlineKeyboardMarkup" | "None":
        return self._d["reply_markup"]

    @property
    def input_message_content(
        self
    ) -> "InputMessageContent" | "None":
        return self._d["input_message_content"]

    @property
    def thumb_url(
        self
    ) -> "String" | "None":
        return self._d["thumb_url"]

    @property
    def thumb_width(
        self
    ) -> "Integer" | "None":
        return self._d["thumb_width"]

    @property
    def thumb_height(
        self
    ) -> "Integer" | "None":
        return self._d["thumb_height"]


class InlineQueryResultVenue(DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return self._d["type"]

    @property
    def id(
        self
    ) -> "String":
        return self._d["id"]

    @property
    def latitude(
        self
    ) -> "Float":
        return self._d["latitude"]

    @property
    def longitude(
        self
    ) -> "Float":
        return self._d["longitude"]

    @property
    def title(
        self
    ) -> "String":
        return self._d["title"]

    @property
    def address(
        self
    ) -> "String":
        return self._d["address"]

    @property
    def foursquare_id(
        self
    ) -> "String" | "None":
        return self._d["foursquare_id"]

    @property
    def foursquare_type(
        self
    ) -> "String" | "None":
        return self._d["foursquare_type"]

    @property
    def google_place_id(
        self
    ) -> "String" | "None":
        return self._d["google_place_id"]

    @property
    def google_place_type(
        self
    ) -> "String" | "None":
        return self._d["google_place_type"]

    @property
    def reply_markup(
        self
    ) -> "InlineKeyboardMarkup" | "None":
        return self._d["reply_markup"]

    @property
    def input_message_content(
        self
    ) -> "InputMessageContent" | "None":
        return self._d["input_message_content"]

    @property
    def thumb_url(
        self
    ) -> "String" | "None":
        return self._d["thumb_url"]

    @property
    def thumb_width(
        self
    ) -> "Integer" | "None":
        return self._d["thumb_width"]

    @property
    def thumb_height(
        self
    ) -> "Integer" | "None":
        return self._d["thumb_height"]


class InlineQueryResultContact(DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return self._d["type"]

    @property
    def id(
        self
    ) -> "String":
        return self._d["id"]

    @property
    def phone_number(
        self
    ) -> "String":
        return self._d["phone_number"]

    @property
    def first_name(
        self
    ) -> "String":
        return self._d["first_name"]

    @property
    def last_name(
        self
    ) -> "String" | "None":
        return self._d["last_name"]

    @property
    def vcard(
        self
    ) -> "String" | "None":
        return self._d["vcard"]

    @property
    def reply_markup(
        self
    ) -> "InlineKeyboardMarkup" | "None":
        return self._d["reply_markup"]

    @property
    def input_message_content(
        self
    ) -> "InputMessageContent" | "None":
        return self._d["input_message_content"]

    @property
    def thumb_url(
        self
    ) -> "String" | "None":
        return self._d["thumb_url"]

    @property
    def thumb_width(
        self
    ) -> "Integer" | "None":
        return self._d["thumb_width"]

    @property
    def thumb_height(
        self
    ) -> "Integer" | "None":
        return self._d["thumb_height"]


class InlineQueryResultGame(DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return self._d["type"]

    @property
    def id(
        self
    ) -> "String":
        return self._d["id"]

    @property
    def game_short_name(
        self
    ) -> "String":
        return self._d["game_short_name"]

    @property
    def reply_markup(
        self
    ) -> "InlineKeyboardMarkup" | "None":
        return self._d["reply_markup"]


class InlineQueryResultCachedPhoto(DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return self._d["type"]

    @property
    def id(
        self
    ) -> "String":
        return self._d["id"]

    @property
    def photo_file_id(
        self
    ) -> "String":
        return self._d["photo_file_id"]

    @property
    def title(
        self
    ) -> "String" | "None":
        return self._d["title"]

    @property
    def description(
        self
    ) -> "String" | "None":
        return self._d["description"]

    @property
    def caption(
        self
    ) -> "String" | "None":
        return self._d["caption"]

    @property
    def parse_mode(
        self
    ) -> "String" | "None":
        return self._d["parse_mode"]

    @property
    def caption_entities(
        self
    ) -> "List[MessageEntity]" | "None":
        return self._d["caption_entities"]

    @property
    def reply_markup(
        self
    ) -> "InlineKeyboardMarkup" | "None":
        return self._d["reply_markup"]

    @property
    def input_message_content(
        self
    ) -> "InputMessageContent" | "None":
        return self._d["input_message_content"]


class InlineQueryResultCachedGif(DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return self._d["type"]

    @property
    def id(
        self
    ) -> "String":
        return self._d["id"]

    @property
    def gif_file_id(
        self
    ) -> "String":
        return self._d["gif_file_id"]

    @property
    def title(
        self
    ) -> "String" | "None":
        return self._d["title"]

    @property
    def caption(
        self
    ) -> "String" | "None":
        return self._d["caption"]

    @property
    def parse_mode(
        self
    ) -> "String" | "None":
        return self._d["parse_mode"]

    @property
    def caption_entities(
        self
    ) -> "List[MessageEntity]" | "None":
        return self._d["caption_entities"]

    @property
    def reply_markup(
        self
    ) -> "InlineKeyboardMarkup" | "None":
        return self._d["reply_markup"]

    @property
    def input_message_content(
        self
    ) -> "InputMessageContent" | "None":
        return self._d["input_message_content"]


class InlineQueryResultCachedMpeg4Gif(DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return self._d["type"]

    @property
    def id(
        self
    ) -> "String":
        return self._d["id"]

    @property
    def mpeg4_file_id(
        self
    ) -> "String":
        return self._d["mpeg4_file_id"]

    @property
    def title(
        self
    ) -> "String" | "None":
        return self._d["title"]

    @property
    def caption(
        self
    ) -> "String" | "None":
        return self._d["caption"]

    @property
    def parse_mode(
        self
    ) -> "String" | "None":
        return self._d["parse_mode"]

    @property
    def caption_entities(
        self
    ) -> "List[MessageEntity]" | "None":
        return self._d["caption_entities"]

    @property
    def reply_markup(
        self
    ) -> "InlineKeyboardMarkup" | "None":
        return self._d["reply_markup"]

    @property
    def input_message_content(
        self
    ) -> "InputMessageContent" | "None":
        return self._d["input_message_content"]


class InlineQueryResultCachedSticker(DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return self._d["type"]

    @property
    def id(
        self
    ) -> "String":
        return self._d["id"]

    @property
    def sticker_file_id(
        self
    ) -> "String":
        return self._d["sticker_file_id"]

    @property
    def reply_markup(
        self
    ) -> "InlineKeyboardMarkup" | "None":
        return self._d["reply_markup"]

    @property
    def input_message_content(
        self
    ) -> "InputMessageContent" | "None":
        return self._d["input_message_content"]


class InlineQueryResultCachedDocument(DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return self._d["type"]

    @property
    def id(
        self
    ) -> "String":
        return self._d["id"]

    @property
    def title(
        self
    ) -> "String":
        return self._d["title"]

    @property
    def document_file_id(
        self
    ) -> "String":
        return self._d["document_file_id"]

    @property
    def description(
        self
    ) -> "String" | "None":
        return self._d["description"]

    @property
    def caption(
        self
    ) -> "String" | "None":
        return self._d["caption"]

    @property
    def parse_mode(
        self
    ) -> "String" | "None":
        return self._d["parse_mode"]

    @property
    def caption_entities(
        self
    ) -> "List[MessageEntity]" | "None":
        return self._d["caption_entities"]

    @property
    def reply_markup(
        self
    ) -> "InlineKeyboardMarkup" | "None":
        return self._d["reply_markup"]

    @property
    def input_message_content(
        self
    ) -> "InputMessageContent" | "None":
        return self._d["input_message_content"]


class InlineQueryResultCachedVideo(DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return self._d["type"]

    @property
    def id(
        self
    ) -> "String":
        return self._d["id"]

    @property
    def video_file_id(
        self
    ) -> "String":
        return self._d["video_file_id"]

    @property
    def title(
        self
    ) -> "String":
        return self._d["title"]

    @property
    def description(
        self
    ) -> "String" | "None":
        return self._d["description"]

    @property
    def caption(
        self
    ) -> "String" | "None":
        return self._d["caption"]

    @property
    def parse_mode(
        self
    ) -> "String" | "None":
        return self._d["parse_mode"]

    @property
    def caption_entities(
        self
    ) -> "List[MessageEntity]" | "None":
        return self._d["caption_entities"]

    @property
    def reply_markup(
        self
    ) -> "InlineKeyboardMarkup" | "None":
        return self._d["reply_markup"]

    @property
    def input_message_content(
        self
    ) -> "InputMessageContent" | "None":
        return self._d["input_message_content"]


class InlineQueryResultCachedVoice(DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return self._d["type"]

    @property
    def id(
        self
    ) -> "String":
        return self._d["id"]

    @property
    def voice_file_id(
        self
    ) -> "String":
        return self._d["voice_file_id"]

    @property
    def title(
        self
    ) -> "String":
        return self._d["title"]

    @property
    def caption(
        self
    ) -> "String" | "None":
        return self._d["caption"]

    @property
    def parse_mode(
        self
    ) -> "String" | "None":
        return self._d["parse_mode"]

    @property
    def caption_entities(
        self
    ) -> "List[MessageEntity]" | "None":
        return self._d["caption_entities"]

    @property
    def reply_markup(
        self
    ) -> "InlineKeyboardMarkup" | "None":
        return self._d["reply_markup"]

    @property
    def input_message_content(
        self
    ) -> "InputMessageContent" | "None":
        return self._d["input_message_content"]


class InlineQueryResultCachedAudio(DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return self._d["type"]

    @property
    def id(
        self
    ) -> "String":
        return self._d["id"]

    @property
    def audio_file_id(
        self
    ) -> "String":
        return self._d["audio_file_id"]

    @property
    def caption(
        self
    ) -> "String" | "None":
        return self._d["caption"]

    @property
    def parse_mode(
        self
    ) -> "String" | "None":
        return self._d["parse_mode"]

    @property
    def caption_entities(
        self
    ) -> "List[MessageEntity]" | "None":
        return self._d["caption_entities"]

    @property
    def reply_markup(
        self
    ) -> "InlineKeyboardMarkup" | "None":
        return self._d["reply_markup"]

    @property
    def input_message_content(
        self
    ) -> "InputMessageContent" | "None":
        return self._d["input_message_content"]


class InputMessageContent(DefaultType):
    ...


class InputTextMessageContent(DefaultType):

    @property
    def message_text(
        self
    ) -> "String":
        return self._d["message_text"]

    @property
    def parse_mode(
        self
    ) -> "String" | "None":
        return self._d["parse_mode"]

    @property
    def entities(
        self
    ) -> "List[MessageEntity]" | "None":
        return self._d["entities"]

    @property
    def disable_web_page_preview(
        self
    ) -> "Boolean" | "None":
        return self._d["disable_web_page_preview"]


class InputLocationMessageContent(DefaultType):

    @property
    def latitude(
        self
    ) -> "Float":
        return self._d["latitude"]

    @property
    def longitude(
        self
    ) -> "Float":
        return self._d["longitude"]

    @property
    def horizontal_accuracy(
        self
    ) -> "Float" | "None":
        return self._d["horizontal_accuracy"]

    @property
    def live_period(
        self
    ) -> "Integer" | "None":
        return self._d["live_period"]

    @property
    def heading(
        self
    ) -> "Integer" | "None":
        return self._d["heading"]

    @property
    def proximity_alert_radius(
        self
    ) -> "Integer" | "None":
        return self._d["proximity_alert_radius"]


class InputVenueMessageContent(DefaultType):

    @property
    def latitude(
        self
    ) -> "Float":
        return self._d["latitude"]

    @property
    def longitude(
        self
    ) -> "Float":
        return self._d["longitude"]

    @property
    def title(
        self
    ) -> "String":
        return self._d["title"]

    @property
    def address(
        self
    ) -> "String":
        return self._d["address"]

    @property
    def foursquare_id(
        self
    ) -> "String" | "None":
        return self._d["foursquare_id"]

    @property
    def foursquare_type(
        self
    ) -> "String" | "None":
        return self._d["foursquare_type"]

    @property
    def google_place_id(
        self
    ) -> "String" | "None":
        return self._d["google_place_id"]

    @property
    def google_place_type(
        self
    ) -> "String" | "None":
        return self._d["google_place_type"]


class InputContactMessageContent(DefaultType):

    @property
    def phone_number(
        self
    ) -> "String":
        return self._d["phone_number"]

    @property
    def first_name(
        self
    ) -> "String":
        return self._d["first_name"]

    @property
    def last_name(
        self
    ) -> "String" | "None":
        return self._d["last_name"]

    @property
    def vcard(
        self
    ) -> "String" | "None":
        return self._d["vcard"]


class InputInvoiceMessageContent(DefaultType):

    @property
    def title(
        self
    ) -> "String":
        return self._d["title"]

    @property
    def description(
        self
    ) -> "String":
        return self._d["description"]

    @property
    def payload(
        self
    ) -> "String":
        return self._d["payload"]

    @property
    def provider_token(
        self
    ) -> "String":
        return self._d["provider_token"]

    @property
    def currency(
        self
    ) -> "String":
        return self._d["currency"]

    @property
    def prices(
        self
    ) -> "List[LabeledPrice]":
        return self._d["prices"]

    @property
    def max_tip_amount(
        self
    ) -> "Integer" | "None":
        return self._d["max_tip_amount"]

    @property
    def suggested_tip_amounts(
        self
    ) -> "List[Integer]" | "None":
        return self._d["suggested_tip_amounts"]

    @property
    def provider_data(
        self
    ) -> "String" | "None":
        return self._d["provider_data"]

    @property
    def photo_url(
        self
    ) -> "String" | "None":
        return self._d["photo_url"]

    @property
    def photo_size(
        self
    ) -> "Integer" | "None":
        return self._d["photo_size"]

    @property
    def photo_width(
        self
    ) -> "Integer" | "None":
        return self._d["photo_width"]

    @property
    def photo_height(
        self
    ) -> "Integer" | "None":
        return self._d["photo_height"]

    @property
    def need_name(
        self
    ) -> "Boolean" | "None":
        return self._d["need_name"]

    @property
    def need_phone_number(
        self
    ) -> "Boolean" | "None":
        return self._d["need_phone_number"]

    @property
    def need_email(
        self
    ) -> "Boolean" | "None":
        return self._d["need_email"]

    @property
    def need_shipping_address(
        self
    ) -> "Boolean" | "None":
        return self._d["need_shipping_address"]

    @property
    def send_phone_number_to_provider(
        self
    ) -> "Boolean" | "None":
        return self._d["send_phone_number_to_provider"]

    @property
    def send_email_to_provider(
        self
    ) -> "Boolean" | "None":
        return self._d["send_email_to_provider"]

    @property
    def is_flexible(
        self
    ) -> "Boolean" | "None":
        return self._d["is_flexible"]


class ChosenInlineResult(DefaultType):

    @property
    def result_id(
        self
    ) -> "String":
        return self._d["result_id"]

    @property
    def from_(
        self
    ) -> "User":
        return self._d["from"]

    @property
    def location(
        self
    ) -> "Location" | "None":
        return self._d["location"]

    @property
    def inline_message_id(
        self
    ) -> "String" | "None":
        return self._d["inline_message_id"]

    @property
    def query(
        self
    ) -> "String":
        return self._d["query"]


class SentWebAppMessage(DefaultType):

    @property
    def inline_message_id(
        self
    ) -> "String" | "None":
        return self._d["inline_message_id"]


class LabeledPrice(DefaultType):

    @property
    def label(
        self
    ) -> "String":
        return self._d["label"]

    @property
    def amount(
        self
    ) -> "Integer":
        return self._d["amount"]


class Invoice(DefaultType):

    @property
    def title(
        self
    ) -> "String":
        return self._d["title"]

    @property
    def description(
        self
    ) -> "String":
        return self._d["description"]

    @property
    def start_parameter(
        self
    ) -> "String":
        return self._d["start_parameter"]

    @property
    def currency(
        self
    ) -> "String":
        return self._d["currency"]

    @property
    def total_amount(
        self
    ) -> "Integer":
        return self._d["total_amount"]


class ShippingAddress(DefaultType):

    @property
    def country_code(
        self
    ) -> "String":
        return self._d["country_code"]

    @property
    def state(
        self
    ) -> "String":
        return self._d["state"]

    @property
    def city(
        self
    ) -> "String":
        return self._d["city"]

    @property
    def street_line1(
        self
    ) -> "String":
        return self._d["street_line1"]

    @property
    def street_line2(
        self
    ) -> "String":
        return self._d["street_line2"]

    @property
    def post_code(
        self
    ) -> "String":
        return self._d["post_code"]


class OrderInfo(DefaultType):

    @property
    def name(
        self
    ) -> "String" | "None":
        return self._d["name"]

    @property
    def phone_number(
        self
    ) -> "String" | "None":
        return self._d["phone_number"]

    @property
    def email(
        self
    ) -> "String" | "None":
        return self._d["email"]

    @property
    def shipping_address(
        self
    ) -> "ShippingAddress" | "None":
        return self._d["shipping_address"]


class ShippingOption(DefaultType):

    @property
    def id(
        self
    ) -> "String":
        return self._d["id"]

    @property
    def title(
        self
    ) -> "String":
        return self._d["title"]

    @property
    def prices(
        self
    ) -> "List[LabeledPrice]":
        return self._d["prices"]


class SuccessfulPayment(DefaultType):

    @property
    def currency(
        self
    ) -> "String":
        return self._d["currency"]

    @property
    def total_amount(
        self
    ) -> "Integer":
        return self._d["total_amount"]

    @property
    def invoice_payload(
        self
    ) -> "String":
        return self._d["invoice_payload"]

    @property
    def shipping_option_id(
        self
    ) -> "String" | "None":
        return self._d["shipping_option_id"]

    @property
    def order_info(
        self
    ) -> "OrderInfo" | "None":
        return self._d["order_info"]

    @property
    def telegram_payment_charge_id(
        self
    ) -> "String":
        return self._d["telegram_payment_charge_id"]

    @property
    def provider_payment_charge_id(
        self
    ) -> "String":
        return self._d["provider_payment_charge_id"]


class ShippingQuery(DefaultType):

    @property
    def id(
        self
    ) -> "String":
        return self._d["id"]

    @property
    def from_(
        self
    ) -> "User":
        return self._d["from"]

    @property
    def invoice_payload(
        self
    ) -> "String":
        return self._d["invoice_payload"]

    @property
    def shipping_address(
        self
    ) -> "ShippingAddress":
        return self._d["shipping_address"]


class PreCheckoutQuery(DefaultType):

    @property
    def id(
        self
    ) -> "String":
        return self._d["id"]

    @property
    def from_(
        self
    ) -> "User":
        return self._d["from"]

    @property
    def currency(
        self
    ) -> "String":
        return self._d["currency"]

    @property
    def total_amount(
        self
    ) -> "Integer":
        return self._d["total_amount"]

    @property
    def invoice_payload(
        self
    ) -> "String":
        return self._d["invoice_payload"]

    @property
    def shipping_option_id(
        self
    ) -> "String" | "None":
        return self._d["shipping_option_id"]

    @property
    def order_info(
        self
    ) -> "OrderInfo" | "None":
        return self._d["order_info"]


class PassportData(DefaultType):

    @property
    def data(
        self
    ) -> "List[EncryptedPassportElement]":
        return self._d["data"]

    @property
    def credentials(
        self
    ) -> "EncryptedCredentials":
        return self._d["credentials"]


class PassportFile(DefaultType):

    @property
    def file_id(
        self
    ) -> "String":
        return self._d["file_id"]

    @property
    def file_unique_id(
        self
    ) -> "String":
        return self._d["file_unique_id"]

    @property
    def file_size(
        self
    ) -> "Integer":
        return self._d["file_size"]

    @property
    def file_date(
        self
    ) -> "Integer":
        return self._d["file_date"]


class EncryptedPassportElement(DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return self._d["type"]

    @property
    def data(
        self
    ) -> "String" | "None":
        return self._d["data"]

    @property
    def phone_number(
        self
    ) -> "String" | "None":
        return self._d["phone_number"]

    @property
    def email(
        self
    ) -> "String" | "None":
        return self._d["email"]

    @property
    def files(
        self
    ) -> "List[PassportFile]" | "None":
        return self._d["files"]

    @property
    def front_side(
        self
    ) -> "PassportFile" | "None":
        return self._d["front_side"]

    @property
    def reverse_side(
        self
    ) -> "PassportFile" | "None":
        return self._d["reverse_side"]

    @property
    def selfie(
        self
    ) -> "PassportFile" | "None":
        return self._d["selfie"]

    @property
    def translation(
        self
    ) -> "List[PassportFile]" | "None":
        return self._d["translation"]

    @property
    def hash(
        self
    ) -> "String":
        return self._d["hash"]


class EncryptedCredentials(DefaultType):

    @property
    def data(
        self
    ) -> "String":
        return self._d["data"]

    @property
    def hash(
        self
    ) -> "String":
        return self._d["hash"]

    @property
    def secret(
        self
    ) -> "String":
        return self._d["secret"]


class PassportElementError(DefaultType):
    ...


class PassportElementErrorDataField(DefaultType):

    @property
    def source(
        self
    ) -> "String":
        return self._d["source"]

    @property
    def type(
        self
    ) -> "String":
        return self._d["type"]

    @property
    def field_name(
        self
    ) -> "String":
        return self._d["field_name"]

    @property
    def data_hash(
        self
    ) -> "String":
        return self._d["data_hash"]

    @property
    def message(
        self
    ) -> "String":
        return self._d["message"]


class PassportElementErrorFrontSide(DefaultType):

    @property
    def source(
        self
    ) -> "String":
        return self._d["source"]

    @property
    def type(
        self
    ) -> "String":
        return self._d["type"]

    @property
    def file_hash(
        self
    ) -> "String":
        return self._d["file_hash"]

    @property
    def message(
        self
    ) -> "String":
        return self._d["message"]


class PassportElementErrorReverseSide(DefaultType):

    @property
    def source(
        self
    ) -> "String":
        return self._d["source"]

    @property
    def type(
        self
    ) -> "String":
        return self._d["type"]

    @property
    def file_hash(
        self
    ) -> "String":
        return self._d["file_hash"]

    @property
    def message(
        self
    ) -> "String":
        return self._d["message"]


class PassportElementErrorSelfie(DefaultType):

    @property
    def source(
        self
    ) -> "String":
        return self._d["source"]

    @property
    def type(
        self
    ) -> "String":
        return self._d["type"]

    @property
    def file_hash(
        self
    ) -> "String":
        return self._d["file_hash"]

    @property
    def message(
        self
    ) -> "String":
        return self._d["message"]


class PassportElementErrorFile(DefaultType):

    @property
    def source(
        self
    ) -> "String":
        return self._d["source"]

    @property
    def type(
        self
    ) -> "String":
        return self._d["type"]

    @property
    def file_hash(
        self
    ) -> "String":
        return self._d["file_hash"]

    @property
    def message(
        self
    ) -> "String":
        return self._d["message"]


class PassportElementErrorFiles(DefaultType):

    @property
    def source(
        self
    ) -> "String":
        return self._d["source"]

    @property
    def type(
        self
    ) -> "String":
        return self._d["type"]

    @property
    def file_hashes(
        self
    ) -> "List[String]":
        return self._d["file_hashes"]

    @property
    def message(
        self
    ) -> "String":
        return self._d["message"]


class PassportElementErrorTranslationFile(DefaultType):

    @property
    def source(
        self
    ) -> "String":
        return self._d["source"]

    @property
    def type(
        self
    ) -> "String":
        return self._d["type"]

    @property
    def file_hash(
        self
    ) -> "String":
        return self._d["file_hash"]

    @property
    def message(
        self
    ) -> "String":
        return self._d["message"]


class PassportElementErrorTranslationFiles(DefaultType):

    @property
    def source(
        self
    ) -> "String":
        return self._d["source"]

    @property
    def type(
        self
    ) -> "String":
        return self._d["type"]

    @property
    def file_hashes(
        self
    ) -> "List[String]":
        return self._d["file_hashes"]

    @property
    def message(
        self
    ) -> "String":
        return self._d["message"]


class PassportElementErrorUnspecified(DefaultType):

    @property
    def source(
        self
    ) -> "String":
        return self._d["source"]

    @property
    def type(
        self
    ) -> "String":
        return self._d["type"]

    @property
    def element_hash(
        self
    ) -> "String":
        return self._d["element_hash"]

    @property
    def message(
        self
    ) -> "String":
        return self._d["message"]


class Game(DefaultType):

    @property
    def title(
        self
    ) -> "String":
        return self._d["title"]

    @property
    def description(
        self
    ) -> "String":
        return self._d["description"]

    @property
    def photo(
        self
    ) -> "List[PhotoSize]":
        return self._d["photo"]

    @property
    def text(
        self
    ) -> "String" | "None":
        return self._d["text"]

    @property
    def text_entities(
        self
    ) -> "List[MessageEntity]" | "None":
        return self._d["text_entities"]

    @property
    def animation(
        self
    ) -> "Animation" | "None":
        return self._d["animation"]


class CallbackGame(DefaultType):
    ...


class GameHighScore(DefaultType):

    @property
    def position(
        self
    ) -> "Integer":
        return self._d["position"]

    @property
    def user(
        self
    ) -> "User":
        return self._d["user"]

    @property
    def score(
        self
    ) -> "Integer":
        return self._d["score"]


class getUpdates(DefaultMethod):

    def __init__(
        self,
        offset: "Integer" = None,
                limit: "Integer" = None,
                timeout: "Integer" = None,
                allowed_updates: "List[String]" = None,
    ):
        self._method = "getUpdates"
        self._res_type = "List[Update]"
        self._args = {}
        self._args['offset'] = offset
        self._args['limit'] = limit
        self._args['timeout'] = timeout
        self._args['allowed_updates'] = allowed_updates

    def result(self) -> "List[Update]":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class setWebhook(DefaultMethod):

    def __init__(
        self,
        url: "String",
        certificate: "InputFile" = None,
        ip_address: "String" = None,
        max_connections: "Integer" = None,
        allowed_updates: "List[String]" = None,
        drop_pending_updates: "Boolean" = None,
        secret_token: "String" = None,
    ):
        self._method = "setWebhook"
        self._res_type = "Boolean"
        self._args = {}
        self._args['url'] = url
        self._args['certificate'] = certificate
        self._args['ip_address'] = ip_address
        self._args['max_connections'] = max_connections
        self._args['allowed_updates'] = allowed_updates
        self._args['drop_pending_updates'] = drop_pending_updates
        self._args['secret_token'] = secret_token

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class deleteWebhook(DefaultMethod):

    def __init__(
        self,
        drop_pending_updates: "Boolean" = None,
    ):
        self._method = "deleteWebhook"
        self._res_type = "Boolean"
        self._args = {}
        self._args['drop_pending_updates'] = drop_pending_updates

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class getWebhookInfo(DefaultMethod):

    def __init__(
        self,

    ):
        self._method = "getWebhookInfo"
        self._res_type = "WebhookInfo"
        self._args = {}

    def result(self) -> "WebhookInfo":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class getMe(DefaultMethod):

    def __init__(
        self,

    ):
        self._method = "getMe"
        self._res_type = "User"
        self._args = {}

    def result(self) -> "User":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class logOut(DefaultMethod):

    def __init__(
        self,

    ):
        self._method = "logOut"
        self._res_type = "Boolean"
        self._args = {}

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class close(DefaultMethod):

    def __init__(
        self,

    ):
        self._method = "close"
        self._res_type = "Boolean"
        self._args = {}

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class sendMessage(DefaultMethod):

    def __init__(
        self,
        text: "String",
        chat_id: "Integer" | "String",
        parse_mode: "String" = None,
        entities: "List[MessageEntity]" = None,
        disable_web_page_preview: "Boolean" = None,
        disable_notification: "Boolean" = None,
        protect_content: "Boolean" = None,
        reply_to_message_id: "Integer" = None,
        allow_sending_without_reply: "Boolean" = None,
        reply_markup: "InlineKeyboardMarkup" | "ReplyKeyboardMarkup" | "ReplyKeyboardRemove" | "ForceReply" = None,
    ):
        self._method = "sendMessage"
        self._res_type = "Message"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['text'] = text
        self._args['parse_mode'] = parse_mode
        self._args['entities'] = entities
        self._args['disable_web_page_preview'] = disable_web_page_preview
        self._args['disable_notification'] = disable_notification
        self._args['protect_content'] = protect_content
        self._args['reply_to_message_id'] = reply_to_message_id
        self._args['allow_sending_without_reply'] = allow_sending_without_reply
        self._args['reply_markup'] = reply_markup

    def result(self) -> "Message":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class forwardMessage(DefaultMethod):

    def __init__(
        self,
        message_id: "Integer",
        from__chat_id: "Integer" | "String",
        chat_id: "Integer" | "String",
        disable_notification: "Boolean" = None,
        protect_content: "Boolean" = None,
    ):
        self._method = "forwardMessage"
        self._res_type = "Message"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['from_chat_id'] = from__chat_id
        self._args['disable_notification'] = disable_notification
        self._args['protect_content'] = protect_content
        self._args['message_id'] = message_id

    def result(self) -> "Message":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class copyMessage(DefaultMethod):

    def __init__(
        self,
        message_id: "Integer",
        from__chat_id: "Integer" | "String",
        chat_id: "Integer" | "String",
        caption: "String" = None,
        parse_mode: "String" = None,
        caption_entities: "List[MessageEntity]" = None,
        disable_notification: "Boolean" = None,
        protect_content: "Boolean" = None,
        reply_to_message_id: "Integer" = None,
        allow_sending_without_reply: "Boolean" = None,
        reply_markup: "InlineKeyboardMarkup" | "ReplyKeyboardMarkup" | "ReplyKeyboardRemove" | "ForceReply" = None,
    ):
        self._method = "copyMessage"
        self._res_type = "MessageId"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['from_chat_id'] = from__chat_id
        self._args['message_id'] = message_id
        self._args['caption'] = caption
        self._args['parse_mode'] = parse_mode
        self._args['caption_entities'] = caption_entities
        self._args['disable_notification'] = disable_notification
        self._args['protect_content'] = protect_content
        self._args['reply_to_message_id'] = reply_to_message_id
        self._args['allow_sending_without_reply'] = allow_sending_without_reply
        self._args['reply_markup'] = reply_markup

    def result(self) -> "MessageId":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class sendPhoto(DefaultMethod):

    def __init__(
        self,
        photo: "InputFile" | "String",
        chat_id: "Integer" | "String",
        caption: "String" = None,
        parse_mode: "String" = None,
        caption_entities: "List[MessageEntity]" = None,
        disable_notification: "Boolean" = None,
        protect_content: "Boolean" = None,
        reply_to_message_id: "Integer" = None,
        allow_sending_without_reply: "Boolean" = None,
        reply_markup: "InlineKeyboardMarkup" | "ReplyKeyboardMarkup" | "ReplyKeyboardRemove" | "ForceReply" = None,
    ):
        self._method = "sendPhoto"
        self._res_type = "Message"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['photo'] = photo
        self._args['caption'] = caption
        self._args['parse_mode'] = parse_mode
        self._args['caption_entities'] = caption_entities
        self._args['disable_notification'] = disable_notification
        self._args['protect_content'] = protect_content
        self._args['reply_to_message_id'] = reply_to_message_id
        self._args['allow_sending_without_reply'] = allow_sending_without_reply
        self._args['reply_markup'] = reply_markup

    def result(self) -> "Message":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class sendAudio(DefaultMethod):

    def __init__(
        self,
        audio: "InputFile" | "String",
        chat_id: "Integer" | "String",
        caption: "String" = None,
        parse_mode: "String" = None,
        caption_entities: "List[MessageEntity]" = None,
        duration: "Integer" = None,
        performer: "String" = None,
        title: "String" = None,
        thumb: "InputFile" | "String" = None,
        disable_notification: "Boolean" = None,
        protect_content: "Boolean" = None,
        reply_to_message_id: "Integer" = None,
        allow_sending_without_reply: "Boolean" = None,
        reply_markup: "InlineKeyboardMarkup" | "ReplyKeyboardMarkup" | "ReplyKeyboardRemove" | "ForceReply" = None,
    ):
        self._method = "sendAudio"
        self._res_type = "Message"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['audio'] = audio
        self._args['caption'] = caption
        self._args['parse_mode'] = parse_mode
        self._args['caption_entities'] = caption_entities
        self._args['duration'] = duration
        self._args['performer'] = performer
        self._args['title'] = title
        self._args['thumb'] = thumb
        self._args['disable_notification'] = disable_notification
        self._args['protect_content'] = protect_content
        self._args['reply_to_message_id'] = reply_to_message_id
        self._args['allow_sending_without_reply'] = allow_sending_without_reply
        self._args['reply_markup'] = reply_markup

    def result(self) -> "Message":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class sendDocument(DefaultMethod):

    def __init__(
        self,
        document: "InputFile" | "String",
        chat_id: "Integer" | "String",
        thumb: "InputFile" | "String" = None,
        caption: "String" = None,
        parse_mode: "String" = None,
        caption_entities: "List[MessageEntity]" = None,
        disable_content_type_detection: "Boolean" = None,
        disable_notification: "Boolean" = None,
        protect_content: "Boolean" = None,
        reply_to_message_id: "Integer" = None,
        allow_sending_without_reply: "Boolean" = None,
        reply_markup: "InlineKeyboardMarkup" | "ReplyKeyboardMarkup" | "ReplyKeyboardRemove" | "ForceReply" = None,
    ):
        self._method = "sendDocument"
        self._res_type = "Message"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['document'] = document
        self._args['thumb'] = thumb
        self._args['caption'] = caption
        self._args['parse_mode'] = parse_mode
        self._args['caption_entities'] = caption_entities
        self._args['disable_content_type_detection'] = disable_content_type_detection
        self._args['disable_notification'] = disable_notification
        self._args['protect_content'] = protect_content
        self._args['reply_to_message_id'] = reply_to_message_id
        self._args['allow_sending_without_reply'] = allow_sending_without_reply
        self._args['reply_markup'] = reply_markup

    def result(self) -> "Message":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class sendVideo(DefaultMethod):

    def __init__(
        self,
        video: "InputFile" | "String",
        chat_id: "Integer" | "String",
        duration: "Integer" = None,
        width: "Integer" = None,
        height: "Integer" = None,
        thumb: "InputFile" | "String" = None,
        caption: "String" = None,
        parse_mode: "String" = None,
        caption_entities: "List[MessageEntity]" = None,
        supports_streaming: "Boolean" = None,
        disable_notification: "Boolean" = None,
        protect_content: "Boolean" = None,
        reply_to_message_id: "Integer" = None,
        allow_sending_without_reply: "Boolean" = None,
        reply_markup: "InlineKeyboardMarkup" | "ReplyKeyboardMarkup" | "ReplyKeyboardRemove" | "ForceReply" = None,
    ):
        self._method = "sendVideo"
        self._res_type = "Message"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['video'] = video
        self._args['duration'] = duration
        self._args['width'] = width
        self._args['height'] = height
        self._args['thumb'] = thumb
        self._args['caption'] = caption
        self._args['parse_mode'] = parse_mode
        self._args['caption_entities'] = caption_entities
        self._args['supports_streaming'] = supports_streaming
        self._args['disable_notification'] = disable_notification
        self._args['protect_content'] = protect_content
        self._args['reply_to_message_id'] = reply_to_message_id
        self._args['allow_sending_without_reply'] = allow_sending_without_reply
        self._args['reply_markup'] = reply_markup

    def result(self) -> "Message":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class sendAnimation(DefaultMethod):

    def __init__(
        self,
        animation: "InputFile" | "String",
        chat_id: "Integer" | "String",
        duration: "Integer" = None,
        width: "Integer" = None,
        height: "Integer" = None,
        thumb: "InputFile" | "String" = None,
        caption: "String" = None,
        parse_mode: "String" = None,
        caption_entities: "List[MessageEntity]" = None,
        disable_notification: "Boolean" = None,
        protect_content: "Boolean" = None,
        reply_to_message_id: "Integer" = None,
        allow_sending_without_reply: "Boolean" = None,
        reply_markup: "InlineKeyboardMarkup" | "ReplyKeyboardMarkup" | "ReplyKeyboardRemove" | "ForceReply" = None,
    ):
        self._method = "sendAnimation"
        self._res_type = "Message"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['animation'] = animation
        self._args['duration'] = duration
        self._args['width'] = width
        self._args['height'] = height
        self._args['thumb'] = thumb
        self._args['caption'] = caption
        self._args['parse_mode'] = parse_mode
        self._args['caption_entities'] = caption_entities
        self._args['disable_notification'] = disable_notification
        self._args['protect_content'] = protect_content
        self._args['reply_to_message_id'] = reply_to_message_id
        self._args['allow_sending_without_reply'] = allow_sending_without_reply
        self._args['reply_markup'] = reply_markup

    def result(self) -> "Message":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class sendVoice(DefaultMethod):

    def __init__(
        self,
        voice: "InputFile" | "String",
        chat_id: "Integer" | "String",
        caption: "String" = None,
        parse_mode: "String" = None,
        caption_entities: "List[MessageEntity]" = None,
        duration: "Integer" = None,
        disable_notification: "Boolean" = None,
        protect_content: "Boolean" = None,
        reply_to_message_id: "Integer" = None,
        allow_sending_without_reply: "Boolean" = None,
        reply_markup: "InlineKeyboardMarkup" | "ReplyKeyboardMarkup" | "ReplyKeyboardRemove" | "ForceReply" = None,
    ):
        self._method = "sendVoice"
        self._res_type = "Message"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['voice'] = voice
        self._args['caption'] = caption
        self._args['parse_mode'] = parse_mode
        self._args['caption_entities'] = caption_entities
        self._args['duration'] = duration
        self._args['disable_notification'] = disable_notification
        self._args['protect_content'] = protect_content
        self._args['reply_to_message_id'] = reply_to_message_id
        self._args['allow_sending_without_reply'] = allow_sending_without_reply
        self._args['reply_markup'] = reply_markup

    def result(self) -> "Message":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class sendVideoNote(DefaultMethod):

    def __init__(
        self,
        video_note: "InputFile" | "String",
        chat_id: "Integer" | "String",
        duration: "Integer" = None,
        length: "Integer" = None,
        thumb: "InputFile" | "String" = None,
        disable_notification: "Boolean" = None,
        protect_content: "Boolean" = None,
        reply_to_message_id: "Integer" = None,
        allow_sending_without_reply: "Boolean" = None,
        reply_markup: "InlineKeyboardMarkup" | "ReplyKeyboardMarkup" | "ReplyKeyboardRemove" | "ForceReply" = None,
    ):
        self._method = "sendVideoNote"
        self._res_type = "Message"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['video_note'] = video_note
        self._args['duration'] = duration
        self._args['length'] = length
        self._args['thumb'] = thumb
        self._args['disable_notification'] = disable_notification
        self._args['protect_content'] = protect_content
        self._args['reply_to_message_id'] = reply_to_message_id
        self._args['allow_sending_without_reply'] = allow_sending_without_reply
        self._args['reply_markup'] = reply_markup

    def result(self) -> "Message":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class sendMediaGroup(DefaultMethod):

    def __init__(
        self,
        media: "List[InputMediaAudio]" | "List[InputMediaDocument]" | "List[InputMediaPhoto]" | "List[InputMediaVideo]",
        chat_id: "Integer" | "String",
        disable_notification: "Boolean" = None,
        protect_content: "Boolean" = None,
        reply_to_message_id: "Integer" = None,
        allow_sending_without_reply: "Boolean" = None,
    ):
        self._method = "sendMediaGroup"
        self._res_type = "List[Message]"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['media'] = media
        self._args['disable_notification'] = disable_notification
        self._args['protect_content'] = protect_content
        self._args['reply_to_message_id'] = reply_to_message_id
        self._args['allow_sending_without_reply'] = allow_sending_without_reply

    def result(self) -> "List[Message]":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class sendLocation(DefaultMethod):

    def __init__(
        self,
        longitude: "Float",
        latitude: "Float",
        chat_id: "Integer" | "String",
        horizontal_accuracy: "Float" = None,
        live_period: "Integer" = None,
        heading: "Integer" = None,
        proximity_alert_radius: "Integer" = None,
        disable_notification: "Boolean" = None,
        protect_content: "Boolean" = None,
        reply_to_message_id: "Integer" = None,
        allow_sending_without_reply: "Boolean" = None,
        reply_markup: "InlineKeyboardMarkup" | "ReplyKeyboardMarkup" | "ReplyKeyboardRemove" | "ForceReply" = None,
    ):
        self._method = "sendLocation"
        self._res_type = "Message"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['latitude'] = latitude
        self._args['longitude'] = longitude
        self._args['horizontal_accuracy'] = horizontal_accuracy
        self._args['live_period'] = live_period
        self._args['heading'] = heading
        self._args['proximity_alert_radius'] = proximity_alert_radius
        self._args['disable_notification'] = disable_notification
        self._args['protect_content'] = protect_content
        self._args['reply_to_message_id'] = reply_to_message_id
        self._args['allow_sending_without_reply'] = allow_sending_without_reply
        self._args['reply_markup'] = reply_markup

    def result(self) -> "Message":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class editMessageLiveLocation(DefaultMethod):

    def __init__(
        self,
        longitude: "Float",
        latitude: "Float",
        chat_id: "Integer" | "String" = None,
        message_id: "Integer" = None,
        inline_message_id: "String" = None,
        horizontal_accuracy: "Float" = None,
        heading: "Integer" = None,
        proximity_alert_radius: "Integer" = None,
        reply_markup: "InlineKeyboardMarkup" = None,
    ):
        self._method = "editMessageLiveLocation"
        self._res_type = "Message"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['message_id'] = message_id
        self._args['inline_message_id'] = inline_message_id
        self._args['latitude'] = latitude
        self._args['longitude'] = longitude
        self._args['horizontal_accuracy'] = horizontal_accuracy
        self._args['heading'] = heading
        self._args['proximity_alert_radius'] = proximity_alert_radius
        self._args['reply_markup'] = reply_markup

    def result(self) -> "Message":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class stopMessageLiveLocation(DefaultMethod):

    def __init__(
        self,
        chat_id: "Integer" | "String" = None,
        message_id: "Integer" = None,
        inline_message_id: "String" = None,
        reply_markup: "InlineKeyboardMarkup" = None,
    ):
        self._method = "stopMessageLiveLocation"
        self._res_type = "Message"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['message_id'] = message_id
        self._args['inline_message_id'] = inline_message_id
        self._args['reply_markup'] = reply_markup

    def result(self) -> "Message":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class sendVenue(DefaultMethod):

    def __init__(
        self,
        address: "String",
        title: "String",
        longitude: "Float",
        latitude: "Float",
        chat_id: "Integer" | "String",
        foursquare_id: "String" = None,
        foursquare_type: "String" = None,
        google_place_id: "String" = None,
        google_place_type: "String" = None,
        disable_notification: "Boolean" = None,
        protect_content: "Boolean" = None,
        reply_to_message_id: "Integer" = None,
        allow_sending_without_reply: "Boolean" = None,
        reply_markup: "InlineKeyboardMarkup" | "ReplyKeyboardMarkup" | "ReplyKeyboardRemove" | "ForceReply" = None,
    ):
        self._method = "sendVenue"
        self._res_type = "Message"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['latitude'] = latitude
        self._args['longitude'] = longitude
        self._args['title'] = title
        self._args['address'] = address
        self._args['foursquare_id'] = foursquare_id
        self._args['foursquare_type'] = foursquare_type
        self._args['google_place_id'] = google_place_id
        self._args['google_place_type'] = google_place_type
        self._args['disable_notification'] = disable_notification
        self._args['protect_content'] = protect_content
        self._args['reply_to_message_id'] = reply_to_message_id
        self._args['allow_sending_without_reply'] = allow_sending_without_reply
        self._args['reply_markup'] = reply_markup

    def result(self) -> "Message":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class sendContact(DefaultMethod):

    def __init__(
        self,
        first_name: "String",
        phone_number: "String",
        chat_id: "Integer" | "String",
        last_name: "String" = None,
        vcard: "String" = None,
        disable_notification: "Boolean" = None,
        protect_content: "Boolean" = None,
        reply_to_message_id: "Integer" = None,
        allow_sending_without_reply: "Boolean" = None,
        reply_markup: "InlineKeyboardMarkup" | "ReplyKeyboardMarkup" | "ReplyKeyboardRemove" | "ForceReply" = None,
    ):
        self._method = "sendContact"
        self._res_type = "Message"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['phone_number'] = phone_number
        self._args['first_name'] = first_name
        self._args['last_name'] = last_name
        self._args['vcard'] = vcard
        self._args['disable_notification'] = disable_notification
        self._args['protect_content'] = protect_content
        self._args['reply_to_message_id'] = reply_to_message_id
        self._args['allow_sending_without_reply'] = allow_sending_without_reply
        self._args['reply_markup'] = reply_markup

    def result(self) -> "Message":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class sendPoll(DefaultMethod):

    def __init__(
        self,
        options: "List[String]",
        question: "String",
        chat_id: "Integer" | "String",
        is_anonymous: "Boolean" = None,
        type: "String" = None,
        allows_multiple_answers: "Boolean" = None,
        correct_option_id: "Integer" = None,
        explanation: "String" = None,
        explanation_parse_mode: "String" = None,
        explanation_entities: "List[MessageEntity]" = None,
        open_period: "Integer" = None,
        close_date: "Integer" = None,
        is_closed: "Boolean" = None,
        disable_notification: "Boolean" = None,
        protect_content: "Boolean" = None,
        reply_to_message_id: "Integer" = None,
        allow_sending_without_reply: "Boolean" = None,
        reply_markup: "InlineKeyboardMarkup" | "ReplyKeyboardMarkup" | "ReplyKeyboardRemove" | "ForceReply" = None,
    ):
        self._method = "sendPoll"
        self._res_type = "Message"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['question'] = question
        self._args['options'] = options
        self._args['is_anonymous'] = is_anonymous
        self._args['type'] = type
        self._args['allows_multiple_answers'] = allows_multiple_answers
        self._args['correct_option_id'] = correct_option_id
        self._args['explanation'] = explanation
        self._args['explanation_parse_mode'] = explanation_parse_mode
        self._args['explanation_entities'] = explanation_entities
        self._args['open_period'] = open_period
        self._args['close_date'] = close_date
        self._args['is_closed'] = is_closed
        self._args['disable_notification'] = disable_notification
        self._args['protect_content'] = protect_content
        self._args['reply_to_message_id'] = reply_to_message_id
        self._args['allow_sending_without_reply'] = allow_sending_without_reply
        self._args['reply_markup'] = reply_markup

    def result(self) -> "Message":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class sendDice(DefaultMethod):

    def __init__(
        self,
        chat_id: "Integer" | "String",
        emoji: "String" = None,
        disable_notification: "Boolean" = None,
        protect_content: "Boolean" = None,
        reply_to_message_id: "Integer" = None,
        allow_sending_without_reply: "Boolean" = None,
        reply_markup: "InlineKeyboardMarkup" | "ReplyKeyboardMarkup" | "ReplyKeyboardRemove" | "ForceReply" = None,
    ):
        self._method = "sendDice"
        self._res_type = "Message"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['emoji'] = emoji
        self._args['disable_notification'] = disable_notification
        self._args['protect_content'] = protect_content
        self._args['reply_to_message_id'] = reply_to_message_id
        self._args['allow_sending_without_reply'] = allow_sending_without_reply
        self._args['reply_markup'] = reply_markup

    def result(self) -> "Message":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class sendChatAction(DefaultMethod):

    def __init__(
        self,
        action: "String",
                chat_id: "Integer" | "String",
    ):
        self._method = "sendChatAction"
        self._res_type = "Boolean"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['action'] = action

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class getUserProfilePhotos(DefaultMethod):

    def __init__(
        self,
        user_id: "Integer",
        offset: "Integer" = None,
        limit: "Integer" = None,
    ):
        self._method = "getUserProfilePhotos"
        self._res_type = "UserProfilePhotos"
        self._args = {}
        self._args['user_id'] = user_id
        self._args['offset'] = offset
        self._args['limit'] = limit

    def result(self) -> "UserProfilePhotos":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class getFile(DefaultMethod):

    def __init__(
        self,
        file_id: "String",
    ):
        self._method = "getFile"
        self._res_type = "File"
        self._args = {}
        self._args['file_id'] = file_id

    def result(self) -> "File":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class banChatMember(DefaultMethod):

    def __init__(
        self,
        user_id: "Integer",
        chat_id: "Integer" | "String",
        until_date: "Integer" = None,
        revoke_messages: "Boolean" = None,
    ):
        self._method = "banChatMember"
        self._res_type = "Boolean"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['user_id'] = user_id
        self._args['until_date'] = until_date
        self._args['revoke_messages'] = revoke_messages

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class unbanChatMember(DefaultMethod):

    def __init__(
        self,
        user_id: "Integer",
        chat_id: "Integer" | "String",
        only_if_banned: "Boolean" = None,
    ):
        self._method = "unbanChatMember"
        self._res_type = "Boolean"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['user_id'] = user_id
        self._args['only_if_banned'] = only_if_banned

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class restrictChatMember(DefaultMethod):

    def __init__(
        self,
        permissions: "ChatPermissions",
        user_id: "Integer",
        chat_id: "Integer" | "String",
        until_date: "Integer" = None,
    ):
        self._method = "restrictChatMember"
        self._res_type = "Boolean"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['user_id'] = user_id
        self._args['permissions'] = permissions
        self._args['until_date'] = until_date

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class promoteChatMember(DefaultMethod):

    def __init__(
        self,
        user_id: "Integer",
        chat_id: "Integer" | "String",
        is_anonymous: "Boolean" = None,
        can_manage_chat: "Boolean" = None,
        can_post_messages: "Boolean" = None,
        can_edit_messages: "Boolean" = None,
        can_delete_messages: "Boolean" = None,
        can_manage_video_chats: "Boolean" = None,
        can_restrict_members: "Boolean" = None,
        can_promote_members: "Boolean" = None,
        can_change_info: "Boolean" = None,
        can_invite_users: "Boolean" = None,
        can_pin_messages: "Boolean" = None,
    ):
        self._method = "promoteChatMember"
        self._res_type = "Boolean"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['user_id'] = user_id
        self._args['is_anonymous'] = is_anonymous
        self._args['can_manage_chat'] = can_manage_chat
        self._args['can_post_messages'] = can_post_messages
        self._args['can_edit_messages'] = can_edit_messages
        self._args['can_delete_messages'] = can_delete_messages
        self._args['can_manage_video_chats'] = can_manage_video_chats
        self._args['can_restrict_members'] = can_restrict_members
        self._args['can_promote_members'] = can_promote_members
        self._args['can_change_info'] = can_change_info
        self._args['can_invite_users'] = can_invite_users
        self._args['can_pin_messages'] = can_pin_messages

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class setChatAdministratorCustomTitle(DefaultMethod):

    def __init__(
        self,
        custom_title: "String",
        user_id: "Integer",
        chat_id: "Integer" | "String",
    ):
        self._method = "setChatAdministratorCustomTitle"
        self._res_type = "Boolean"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['user_id'] = user_id
        self._args['custom_title'] = custom_title

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class banChatSenderChat(DefaultMethod):

    def __init__(
        self,
        sender_chat_id: "Integer",
        chat_id: "Integer" | "String",
    ):
        self._method = "banChatSenderChat"
        self._res_type = "Boolean"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['sender_chat_id'] = sender_chat_id

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class unbanChatSenderChat(DefaultMethod):

    def __init__(
        self,
        sender_chat_id: "Integer",
        chat_id: "Integer" | "String",
    ):
        self._method = "unbanChatSenderChat"
        self._res_type = "Boolean"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['sender_chat_id'] = sender_chat_id

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class setChatPermissions(DefaultMethod):

    def __init__(
        self,
        permissions: "ChatPermissions",
        chat_id: "Integer" | "String",
    ):
        self._method = "setChatPermissions"
        self._res_type = "Boolean"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['permissions'] = permissions

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class exportChatInviteLink(DefaultMethod):

    def __init__(
        self,
        chat_id: "Integer" | "String",
    ):
        self._method = "exportChatInviteLink"
        self._res_type = "String"
        self._args = {}
        self._args['chat_id'] = chat_id

    def result(self) -> "String":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class createChatInviteLink(DefaultMethod):

    def __init__(
        self,
        chat_id: "Integer" | "String",
        name: "String" = None,
        expire_date: "Integer" = None,
        member_limit: "Integer" = None,
        creates_join_request: "Boolean" = None,
    ):
        self._method = "createChatInviteLink"
        self._res_type = "ChatInviteLink"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['name'] = name
        self._args['expire_date'] = expire_date
        self._args['member_limit'] = member_limit
        self._args['creates_join_request'] = creates_join_request

    def result(self) -> "ChatInviteLink":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class editChatInviteLink(DefaultMethod):

    def __init__(
        self,
        invite_link: "String",
        chat_id: "Integer" | "String",
        name: "String" = None,
        expire_date: "Integer" = None,
        member_limit: "Integer" = None,
        creates_join_request: "Boolean" = None,
    ):
        self._method = "editChatInviteLink"
        self._res_type = "ChatInviteLink"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['invite_link'] = invite_link
        self._args['name'] = name
        self._args['expire_date'] = expire_date
        self._args['member_limit'] = member_limit
        self._args['creates_join_request'] = creates_join_request

    def result(self) -> "ChatInviteLink":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class revokeChatInviteLink(DefaultMethod):

    def __init__(
        self,
        invite_link: "String",
        chat_id: "Integer" | "String",
    ):
        self._method = "revokeChatInviteLink"
        self._res_type = "ChatInviteLink"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['invite_link'] = invite_link

    def result(self) -> "ChatInviteLink":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class approveChatJoinRequest(DefaultMethod):

    def __init__(
        self,
        user_id: "Integer",
        chat_id: "Integer" | "String",
    ):
        self._method = "approveChatJoinRequest"
        self._res_type = "Boolean"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['user_id'] = user_id

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class declineChatJoinRequest(DefaultMethod):

    def __init__(
        self,
        user_id: "Integer",
        chat_id: "Integer" | "String",
    ):
        self._method = "declineChatJoinRequest"
        self._res_type = "Boolean"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['user_id'] = user_id

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class setChatPhoto(DefaultMethod):

    def __init__(
        self,
        photo: "InputFile",
        chat_id: "Integer" | "String",
    ):
        self._method = "setChatPhoto"
        self._res_type = "Boolean"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['photo'] = photo

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class deleteChatPhoto(DefaultMethod):

    def __init__(
        self,
        chat_id: "Integer" | "String",
    ):
        self._method = "deleteChatPhoto"
        self._res_type = "Boolean"
        self._args = {}
        self._args['chat_id'] = chat_id

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class setChatTitle(DefaultMethod):

    def __init__(
        self,
        title: "String",
        chat_id: "Integer" | "String",
    ):
        self._method = "setChatTitle"
        self._res_type = "Boolean"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['title'] = title

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class setChatDescription(DefaultMethod):

    def __init__(
        self,
        chat_id: "Integer" | "String",
        description: "String" = None,
    ):
        self._method = "setChatDescription"
        self._res_type = "Boolean"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['description'] = description

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class pinChatMessage(DefaultMethod):

    def __init__(
        self,
        message_id: "Integer",
        chat_id: "Integer" | "String",
        disable_notification: "Boolean" = None,
    ):
        self._method = "pinChatMessage"
        self._res_type = "Boolean"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['message_id'] = message_id
        self._args['disable_notification'] = disable_notification

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class unpinChatMessage(DefaultMethod):

    def __init__(
        self,
        chat_id: "Integer" | "String",
        message_id: "Integer" = None,
    ):
        self._method = "unpinChatMessage"
        self._res_type = "Boolean"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['message_id'] = message_id

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class unpinAllChatMessages(DefaultMethod):

    def __init__(
        self,
        chat_id: "Integer" | "String",
    ):
        self._method = "unpinAllChatMessages"
        self._res_type = "Boolean"
        self._args = {}
        self._args['chat_id'] = chat_id

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class leaveChat(DefaultMethod):

    def __init__(
        self,
        chat_id: "Integer" | "String",
    ):
        self._method = "leaveChat"
        self._res_type = "Boolean"
        self._args = {}
        self._args['chat_id'] = chat_id

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class getChat(DefaultMethod):

    def __init__(
        self,
        chat_id: "Integer" | "String",
    ):
        self._method = "getChat"
        self._res_type = "Chat"
        self._args = {}
        self._args['chat_id'] = chat_id

    def result(self) -> "Chat":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class getChatAdministrators(DefaultMethod):

    def __init__(
        self,
        chat_id: "Integer" | "String",
    ):
        self._method = "getChatAdministrators"
        self._res_type = "List[ChatMember]"
        self._args = {}
        self._args['chat_id'] = chat_id

    def result(self) -> "List[ChatMember]":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class getChatMemberCount(DefaultMethod):

    def __init__(
        self,
        chat_id: "Integer" | "String",
    ):
        self._method = "getChatMemberCount"
        self._res_type = "Integer"
        self._args = {}
        self._args['chat_id'] = chat_id

    def result(self) -> "Integer":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class getChatMember(DefaultMethod):

    def __init__(
        self,
        user_id: "Integer",
        chat_id: "Integer" | "String",
    ):
        self._method = "getChatMember"
        self._res_type = "ChatMember"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['user_id'] = user_id

    def result(self) -> "ChatMember":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class setChatStickerSet(DefaultMethod):

    def __init__(
        self,
        sticker_set_name: "String",
        chat_id: "Integer" | "String",
    ):
        self._method = "setChatStickerSet"
        self._res_type = "Boolean"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['sticker_set_name'] = sticker_set_name

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class deleteChatStickerSet(DefaultMethod):

    def __init__(
        self,
        chat_id: "Integer" | "String",
    ):
        self._method = "deleteChatStickerSet"
        self._res_type = "Boolean"
        self._args = {}
        self._args['chat_id'] = chat_id

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class answerCallbackQuery(DefaultMethod):

    def __init__(
        self,
        callback_query_id: "String",
        text: "String" = None,
        show_alert: "Boolean" = None,
        url: "String" = None,
        cache_time: "Integer" = None,
    ):
        self._method = "answerCallbackQuery"
        self._res_type = "Boolean"
        self._args = {}
        self._args['callback_query_id'] = callback_query_id
        self._args['text'] = text
        self._args['show_alert'] = show_alert
        self._args['url'] = url
        self._args['cache_time'] = cache_time

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class setMyCommands(DefaultMethod):

    def __init__(
        self,
        commands: "List[BotCommand]",
        scope: "BotCommandScope" = None,
        language_code: "String" = None,
    ):
        self._method = "setMyCommands"
        self._res_type = "Boolean"
        self._args = {}
        self._args['commands'] = commands
        self._args['scope'] = scope
        self._args['language_code'] = language_code

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class deleteMyCommands(DefaultMethod):

    def __init__(
        self,
        scope: "BotCommandScope" = None,
        language_code: "String" = None,
    ):
        self._method = "deleteMyCommands"
        self._res_type = "Boolean"
        self._args = {}
        self._args['scope'] = scope
        self._args['language_code'] = language_code

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class getMyCommands(DefaultMethod):

    def __init__(
        self,
        scope: "BotCommandScope" = None,
        language_code: "String" = None,
    ):
        self._method = "getMyCommands"
        self._res_type = "List[BotCommand]"
        self._args = {}
        self._args['scope'] = scope
        self._args['language_code'] = language_code

    def result(self) -> "List[BotCommand]":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class setChatMenuButton(DefaultMethod):

    def __init__(
        self,
        chat_id: "Integer" = None,
        menu_button: "MenuButton" = None,
    ):
        self._method = "setChatMenuButton"
        self._res_type = "Boolean"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['menu_button'] = menu_button

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class getChatMenuButton(DefaultMethod):

    def __init__(
        self,
        chat_id: "Integer" = None,
    ):
        self._method = "getChatMenuButton"
        self._res_type = "MenuButton"
        self._args = {}
        self._args['chat_id'] = chat_id

    def result(self) -> "MenuButton":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class setMyDefaultAdministratorRights(DefaultMethod):

    def __init__(
        self,
        rights: "ChatAdministratorRights" = None,
                for_channels: "Boolean" = None,
    ):
        self._method = "setMyDefaultAdministratorRights"
        self._res_type = "Boolean"
        self._args = {}
        self._args['rights'] = rights
        self._args['for_channels'] = for_channels

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class getMyDefaultAdministratorRights(DefaultMethod):

    def __init__(
        self,
        for_channels: "Boolean" = None,
    ):
        self._method = "getMyDefaultAdministratorRights"
        self._res_type = "ChatAdministratorRights"
        self._args = {}
        self._args['for_channels'] = for_channels

    def result(self) -> "ChatAdministratorRights":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class editMessageText(DefaultMethod):

    def __init__(
        self,
        text: "String",
        chat_id: "Integer" | "String" = None,
        message_id: "Integer" = None,
        inline_message_id: "String" = None,
        parse_mode: "String" = None,
        entities: "List[MessageEntity]" = None,
        disable_web_page_preview: "Boolean" = None,
        reply_markup: "InlineKeyboardMarkup" = None,
    ):
        self._method = "editMessageText"
        self._res_type = "Message"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['message_id'] = message_id
        self._args['inline_message_id'] = inline_message_id
        self._args['text'] = text
        self._args['parse_mode'] = parse_mode
        self._args['entities'] = entities
        self._args['disable_web_page_preview'] = disable_web_page_preview
        self._args['reply_markup'] = reply_markup

    def result(self) -> "Message":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class editMessageCaption(DefaultMethod):

    def __init__(
        self,
        chat_id: "Integer" | "String" = None,
        message_id: "Integer" = None,
        inline_message_id: "String" = None,
        caption: "String" = None,
        parse_mode: "String" = None,
        caption_entities: "List[MessageEntity]" = None,
        reply_markup: "InlineKeyboardMarkup" = None,
    ):
        self._method = "editMessageCaption"
        self._res_type = "Message"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['message_id'] = message_id
        self._args['inline_message_id'] = inline_message_id
        self._args['caption'] = caption
        self._args['parse_mode'] = parse_mode
        self._args['caption_entities'] = caption_entities
        self._args['reply_markup'] = reply_markup

    def result(self) -> "Message":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class editMessageMedia(DefaultMethod):

    def __init__(
        self,
        media: "InputMedia",
        chat_id: "Integer" | "String" = None,
        message_id: "Integer" = None,
        inline_message_id: "String" = None,
        reply_markup: "InlineKeyboardMarkup" = None,
    ):
        self._method = "editMessageMedia"
        self._res_type = "Message"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['message_id'] = message_id
        self._args['inline_message_id'] = inline_message_id
        self._args['media'] = media
        self._args['reply_markup'] = reply_markup

    def result(self) -> "Message":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class editMessageReplyMarkup(DefaultMethod):

    def __init__(
        self,
        chat_id: "Integer" | "String" = None,
        message_id: "Integer" = None,
        inline_message_id: "String" = None,
        reply_markup: "InlineKeyboardMarkup" = None,
    ):
        self._method = "editMessageReplyMarkup"
        self._res_type = "Message"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['message_id'] = message_id
        self._args['inline_message_id'] = inline_message_id
        self._args['reply_markup'] = reply_markup

    def result(self) -> "Message":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class stopPoll(DefaultMethod):

    def __init__(
        self,
        message_id: "Integer",
        chat_id: "Integer" | "String",
        reply_markup: "InlineKeyboardMarkup" = None,
    ):
        self._method = "stopPoll"
        self._res_type = "Poll"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['message_id'] = message_id
        self._args['reply_markup'] = reply_markup

    def result(self) -> "Poll":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class deleteMessage(DefaultMethod):

    def __init__(
        self,
        message_id: "Integer",
        chat_id: "Integer" | "String",
    ):
        self._method = "deleteMessage"
        self._res_type = "Boolean"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['message_id'] = message_id

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class sendSticker(DefaultMethod):

    def __init__(
        self,
        sticker: "InputFile" | "String",
        chat_id: "Integer" | "String",
        disable_notification: "Boolean" = None,
        protect_content: "Boolean" = None,
        reply_to_message_id: "Integer" = None,
        allow_sending_without_reply: "Boolean" = None,
        reply_markup: "InlineKeyboardMarkup" | "ReplyKeyboardMarkup" | "ReplyKeyboardRemove" | "ForceReply" = None,
    ):
        self._method = "sendSticker"
        self._res_type = "Message"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['sticker'] = sticker
        self._args['disable_notification'] = disable_notification
        self._args['protect_content'] = protect_content
        self._args['reply_to_message_id'] = reply_to_message_id
        self._args['allow_sending_without_reply'] = allow_sending_without_reply
        self._args['reply_markup'] = reply_markup

    def result(self) -> "Message":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class getStickerSet(DefaultMethod):

    def __init__(
        self,
        name: "String",
    ):
        self._method = "getStickerSet"
        self._res_type = "StickerSet"
        self._args = {}
        self._args['name'] = name

    def result(self) -> "StickerSet":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class uploadStickerFile(DefaultMethod):

    def __init__(
        self,
        png_sticker: "InputFile",
        user_id: "Integer",
    ):
        self._method = "uploadStickerFile"
        self._res_type = "File"
        self._args = {}
        self._args['user_id'] = user_id
        self._args['png_sticker'] = png_sticker

    def result(self) -> "File":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class createNewStickerSet(DefaultMethod):

    def __init__(
        self,
        emojis: "String",
                title: "String",
                name: "String",
                user_id: "Integer",
                png_sticker: "InputFile" | "String" = None,
                tgs_sticker: "InputFile" = None,
                webm_sticker: "InputFile" = None,
                contains_masks: "Boolean" = None,
                mask_position: "MaskPosition" = None,
    ):
        self._method = "createNewStickerSet"
        self._res_type = "Boolean"
        self._args = {}
        self._args['user_id'] = user_id
        self._args['name'] = name
        self._args['title'] = title
        self._args['png_sticker'] = png_sticker
        self._args['tgs_sticker'] = tgs_sticker
        self._args['webm_sticker'] = webm_sticker
        self._args['emojis'] = emojis
        self._args['contains_masks'] = contains_masks
        self._args['mask_position'] = mask_position

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class addStickerToSet(DefaultMethod):

    def __init__(
        self,
        emojis: "String",
                name: "String",
                user_id: "Integer",
                png_sticker: "InputFile" | "String" = None,
                tgs_sticker: "InputFile" = None,
                webm_sticker: "InputFile" = None,
                mask_position: "MaskPosition" = None,
    ):
        self._method = "addStickerToSet"
        self._res_type = "Boolean"
        self._args = {}
        self._args['user_id'] = user_id
        self._args['name'] = name
        self._args['png_sticker'] = png_sticker
        self._args['tgs_sticker'] = tgs_sticker
        self._args['webm_sticker'] = webm_sticker
        self._args['emojis'] = emojis
        self._args['mask_position'] = mask_position

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class setStickerPositionInSet(DefaultMethod):

    def __init__(
        self,
        position: "Integer",
        sticker: "String",
    ):
        self._method = "setStickerPositionInSet"
        self._res_type = "Boolean"
        self._args = {}
        self._args['sticker'] = sticker
        self._args['position'] = position

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class deleteStickerFromSet(DefaultMethod):

    def __init__(
        self,
        sticker: "String",
    ):
        self._method = "deleteStickerFromSet"
        self._res_type = "Boolean"
        self._args = {}
        self._args['sticker'] = sticker

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class setStickerSetThumb(DefaultMethod):

    def __init__(
        self,
        user_id: "Integer",
        name: "String",
        thumb: "InputFile" | "String" = None,
    ):
        self._method = "setStickerSetThumb"
        self._res_type = "Boolean"
        self._args = {}
        self._args['name'] = name
        self._args['user_id'] = user_id
        self._args['thumb'] = thumb

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class answerInlineQuery(DefaultMethod):

    def __init__(
        self,
        results: "List[InlineQueryResult]",
        inline_query_id: "String",
        cache_time: "Integer" = None,
        is_personal: "Boolean" = None,
        next_offset: "String" = None,
        switch_pm_text: "String" = None,
        switch_pm_parameter: "String" = None,
    ):
        self._method = "answerInlineQuery"
        self._res_type = "Boolean"
        self._args = {}
        self._args['inline_query_id'] = inline_query_id
        self._args['results'] = results
        self._args['cache_time'] = cache_time
        self._args['is_personal'] = is_personal
        self._args['next_offset'] = next_offset
        self._args['switch_pm_text'] = switch_pm_text
        self._args['switch_pm_parameter'] = switch_pm_parameter

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class answerWebAppQuery(DefaultMethod):

    def __init__(
        self,
        result: "InlineQueryResult",
                web_app_query_id: "String",
    ):
        self._method = "answerWebAppQuery"
        self._res_type = "SentWebAppMessage"
        self._args = {}
        self._args['web_app_query_id'] = web_app_query_id
        self._args['result'] = result

    def result(self) -> "SentWebAppMessage":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class sendInvoice(DefaultMethod):

    def __init__(
        self,
        prices: "List[LabeledPrice]",
                currency: "String",
                provider_token: "String",
                payload: "String",
                description: "String",
                title: "String",
                chat_id: "Integer" | "String",
                max_tip_amount: "Integer" = None,
                suggested_tip_amounts: "List[Integer]" = None,
                start_parameter: "String" = None,
                provider_data: "String" = None,
                photo_url: "String" = None,
                photo_size: "Integer" = None,
                photo_width: "Integer" = None,
                photo_height: "Integer" = None,
                need_name: "Boolean" = None,
                need_phone_number: "Boolean" = None,
                need_email: "Boolean" = None,
                need_shipping_address: "Boolean" = None,
                send_phone_number_to_provider: "Boolean" = None,
                send_email_to_provider: "Boolean" = None,
                is_flexible: "Boolean" = None,
                disable_notification: "Boolean" = None,
                protect_content: "Boolean" = None,
                reply_to_message_id: "Integer" = None,
                allow_sending_without_reply: "Boolean" = None,
                reply_markup: "InlineKeyboardMarkup" = None,
    ):
        self._method = "sendInvoice"
        self._res_type = "Message"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['title'] = title
        self._args['description'] = description
        self._args['payload'] = payload
        self._args['provider_token'] = provider_token
        self._args['currency'] = currency
        self._args['prices'] = prices
        self._args['max_tip_amount'] = max_tip_amount
        self._args['suggested_tip_amounts'] = suggested_tip_amounts
        self._args['start_parameter'] = start_parameter
        self._args['provider_data'] = provider_data
        self._args['photo_url'] = photo_url
        self._args['photo_size'] = photo_size
        self._args['photo_width'] = photo_width
        self._args['photo_height'] = photo_height
        self._args['need_name'] = need_name
        self._args['need_phone_number'] = need_phone_number
        self._args['need_email'] = need_email
        self._args['need_shipping_address'] = need_shipping_address
        self._args['send_phone_number_to_provider'] = send_phone_number_to_provider
        self._args['send_email_to_provider'] = send_email_to_provider
        self._args['is_flexible'] = is_flexible
        self._args['disable_notification'] = disable_notification
        self._args['protect_content'] = protect_content
        self._args['reply_to_message_id'] = reply_to_message_id
        self._args['allow_sending_without_reply'] = allow_sending_without_reply
        self._args['reply_markup'] = reply_markup

    def result(self) -> "Message":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class createInvoiceLink(DefaultMethod):

    def __init__(
        self,
        prices: "List[LabeledPrice]",
                currency: "String",
                provider_token: "String",
                payload: "String",
                description: "String",
                title: "String",
                max_tip_amount: "Integer" = None,
                suggested_tip_amounts: "List[Integer]" = None,
                provider_data: "String" = None,
                photo_url: "String" = None,
                photo_size: "Integer" = None,
                photo_width: "Integer" = None,
                photo_height: "Integer" = None,
                need_name: "Boolean" = None,
                need_phone_number: "Boolean" = None,
                need_email: "Boolean" = None,
                need_shipping_address: "Boolean" = None,
                send_phone_number_to_provider: "Boolean" = None,
                send_email_to_provider: "Boolean" = None,
                is_flexible: "Boolean" = None,
    ):
        self._method = "createInvoiceLink"
        self._res_type = "String"
        self._args = {}
        self._args['title'] = title
        self._args['description'] = description
        self._args['payload'] = payload
        self._args['provider_token'] = provider_token
        self._args['currency'] = currency
        self._args['prices'] = prices
        self._args['max_tip_amount'] = max_tip_amount
        self._args['suggested_tip_amounts'] = suggested_tip_amounts
        self._args['provider_data'] = provider_data
        self._args['photo_url'] = photo_url
        self._args['photo_size'] = photo_size
        self._args['photo_width'] = photo_width
        self._args['photo_height'] = photo_height
        self._args['need_name'] = need_name
        self._args['need_phone_number'] = need_phone_number
        self._args['need_email'] = need_email
        self._args['need_shipping_address'] = need_shipping_address
        self._args['send_phone_number_to_provider'] = send_phone_number_to_provider
        self._args['send_email_to_provider'] = send_email_to_provider
        self._args['is_flexible'] = is_flexible

    def result(self) -> "String":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class answerShippingQuery(DefaultMethod):

    def __init__(
        self,
        ok: "Boolean",
        shipping_query_id: "String",
        shipping_options: "List[ShippingOption]" = None,
        error_message: "String" = None,
    ):
        self._method = "answerShippingQuery"
        self._res_type = "Boolean"
        self._args = {}
        self._args['shipping_query_id'] = shipping_query_id
        self._args['ok'] = ok
        self._args['shipping_options'] = shipping_options
        self._args['error_message'] = error_message

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class answerPreCheckoutQuery(DefaultMethod):

    def __init__(
        self,
        ok: "Boolean",
        pre_checkout_query_id: "String",
        error_message: "String" = None,
    ):
        self._method = "answerPreCheckoutQuery"
        self._res_type = "Boolean"
        self._args = {}
        self._args['pre_checkout_query_id'] = pre_checkout_query_id
        self._args['ok'] = ok
        self._args['error_message'] = error_message

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class setPassportDataErrors(DefaultMethod):

    def __init__(
        self,
        errors: "List[PassportElementError]",
                user_id: "Integer",
    ):
        self._method = "setPassportDataErrors"
        self._res_type = "Boolean"
        self._args = {}
        self._args['user_id'] = user_id
        self._args['errors'] = errors

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class sendGame(DefaultMethod):

    def __init__(
        self,
        game_short_name: "String",
        chat_id: "Integer",
        disable_notification: "Boolean" = None,
        protect_content: "Boolean" = None,
        reply_to_message_id: "Integer" = None,
        allow_sending_without_reply: "Boolean" = None,
        reply_markup: "InlineKeyboardMarkup" = None,
    ):
        self._method = "sendGame"
        self._res_type = "Message"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['game_short_name'] = game_short_name
        self._args['disable_notification'] = disable_notification
        self._args['protect_content'] = protect_content
        self._args['reply_to_message_id'] = reply_to_message_id
        self._args['allow_sending_without_reply'] = allow_sending_without_reply
        self._args['reply_markup'] = reply_markup

    def result(self) -> "Message":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class setGameScore(DefaultMethod):

    def __init__(
        self,
        score: "Integer",
        user_id: "Integer",
        force: "Boolean" = None,
        disable_edit_message: "Boolean" = None,
        chat_id: "Integer" = None,
        message_id: "Integer" = None,
        inline_message_id: "String" = None,
    ):
        self._method = "setGameScore"
        self._res_type = "Message"
        self._args = {}
        self._args['user_id'] = user_id
        self._args['score'] = score
        self._args['force'] = force
        self._args['disable_edit_message'] = disable_edit_message
        self._args['chat_id'] = chat_id
        self._args['message_id'] = message_id
        self._args['inline_message_id'] = inline_message_id

    def result(self) -> "Message":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


class getGameHighScores(DefaultMethod):

    def __init__(
        self,
        user_id: "Integer",
        chat_id: "Integer" = None,
        message_id: "Integer" = None,
        inline_message_id: "String" = None,
    ):
        self._method = "getGameHighScores"
        self._res_type = "List[GameHighScore]"
        self._args = {}
        self._args['user_id'] = user_id
        self._args['chat_id'] = chat_id
        self._args['message_id'] = message_id
        self._args['inline_message_id'] = inline_message_id

    def result(self) -> "List[GameHighScore]":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res