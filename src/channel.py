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
        self.playlists = self.youtube.playlists().list(channelId=channel_id,part='contentDetails,snippet',maxResults=50,).execute()
        #self.video_response = self.youtube.videos().list(part='contentDetails,statistics',id=','.join(video_ids)).execute()
    def print_info(self) -> None:
        """Метод печати на экран """
        print(json.dumps(self.channel))

    @property
    def channel_id(self):
        """Метод вывода приватного атрибута __channel_id """
        return self.__channel_id

    @classmethod
    def get_service(cls):
        """Метод создания экземпляров класса"""
        return build('youtube', 'v3', developerKey=Channel.API_KEY)

    @staticmethod
    def to_json(path, standart='UC-OVMPlMA3-YCIeg4z5z23A'):
        """Сохранение значений атрибутов экземпляра класса в json"""
        exz = Channel(standart)
        with open(path, 'w') as file:
            json.dump(exz.channel, fp=file)

    def __str__(self):
        """метод вывода пользователю"""
        return f"{self.title} (https://www.youtube.com/channel/{self.channel_id})"

    def __add__(self, other):
        """метод перезрузки операции сложения"""
        return int(self.subscriber_Count) + int(other.subscriber_Count)

    def __sub__(self, other):
        """метод перезрузки операции вычитания"""
        return int(self.subscriber_Count) - int(other.subscriber_Count)

    def __gt__(self, other):
        """метод перезрузки операции сравнения"""
        return int(self.subscriber_Count) > int(other.subscriber_Count)

    def __ge__(self, other):
        """метод перезрузки операции сравнения"""
        return int(self.subscriber_Count) >= int(other.subscriber_Count)

    def __lt__(self, other):
        """метод перезрузки операции сравнения"""
        return int(self.subscriber_Count) < int(other.subscriber_Count)

    def __le__(self, other):
        """метод перезрузки операции сравнения"""
        return int(self.subscriber_Count) <= int(other.subscriber_Count)

    def __eq__(self, other):
        """метод перезрузки операции сравнения"""
        return int(self.subscriber_Count) == int(other.subscriber_Count)