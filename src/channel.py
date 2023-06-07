import os, json
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""
    API_KEY = os.getenv('YT_API_KEY')
    url = []

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.youtube = build('youtube', 'v3', developerKey=Channel.API_KEY)
        self.channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.title = self.channel['items'][0]['snippet']['title']
        self.video_count = self.channel['items'][0]["statistics"]["videoCount"]
        for channels_ in self.channel['items'][0]['snippet']['thumbnails']:
            Channel.url.append(self.channel['items'][0]['snippet']['thumbnails'][channels_]['url'])
        self.subscriber_Count = self.channel['items'][0]["statistics"]["subscriberCount"]
        self.description = self.channel['items'][0]['snippet']["description"]
        self.view_count = self.channel['items'][0]["statistics"]["viewCount"]

    def print_info(self) -> None:
        """Метод печати на экран """
        print(json.dumps(self.channel))

    @property
    def channel_id(self):
        """Метод вывода приватного атрибута __channel_id """
        return self.__channel_id

    @classmethod
    def get_service(cls, standart='UC-OVMPlMA3-YCIeg4z5z23A'):
        """Метод создания экземпляров класса"""
        return cls(standart).youtube

    # @staticmethod
    # def to_json(path, standart='UC-OVMPlMA3-YCIeg4z5z23A'):
    #     """сохранения имен атрибутов экземпляра , и их значеня в словарь"""
    #     """Сохранение значений атрибутов экземпляра класса в json"""
    #
    #     with open(path, 'w') as file:
    #         exz = Channel(standart)
    #         dict_ = {}
    #         for attr in exz.__dict__:
    #             print(attr)
    #             dict_[attr] = str(getattr(exz, attr))
    #             print(dict_)
    #         json.dump(dict_, fp=file)

    @staticmethod
    def to_json_two(path, standart='UC-OVMPlMA3-YCIeg4z5z23A'):
        # Или так правильно ?
        """Сохранение значений атрибутов экземпляра класса в json"""
        exz = Channel(standart)
        with open(path, 'w') as file:
            json.dump(exz.channel, fp=file)
